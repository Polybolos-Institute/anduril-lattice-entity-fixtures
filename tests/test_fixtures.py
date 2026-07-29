"""Publish fixture JSON against anduril-mock-lattice (or skip if unavailable)."""

from __future__ import annotations

import json
import os
import threading
import time
import urllib.error
import urllib.request
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "fixtures"


def _load_mock():
    try:
        import sys

        parents = Path(__file__).resolve().parents[2]
        for name in ("mock-lattice", "anduril-mock-lattice"):
            mock_root = parents / name
            if mock_root.is_dir():
                sys.path.insert(0, str(mock_root))
                break
        from mock_lattice import STATE, start_background

        return STATE, start_background
    except Exception:
        return None, None


@pytest.fixture(scope="module")
def mock_base():
    STATE, start_background = _load_mock()
    if STATE is None:
        pytest.skip("anduril-mock-lattice not available as sibling package")
    STATE.reset()
    httpd, _ = start_background(host="127.0.0.1", port=0)
    host, port = httpd.server_address[:2]
    base = f"http://{host}:{port}"
    yield base
    httpd.shutdown()
    httpd.server_close()
    STATE.reset()


def _oauth(base: str) -> str:
    form = (
        "grant_type=client_credentials&client_id=test-client-id"
        "&client_secret=test-client-secret"
    ).encode()
    req = urllib.request.Request(
        f"{base}/api/v1/oauth/token",
        data=form,
        method="POST",
        headers={
            "Content-Type": "application/x-www-form-urlencoded",
            "Anduril-Sandbox-Authorization": "Bearer test-sandbox-token",
        },
    )
    with urllib.request.urlopen(req, timeout=5) as resp:
        body = json.loads(resp.read().decode())
    return body["access_token"]


def _put(base: str, token: str, entity: dict) -> int:
    data = json.dumps(entity).encode()
    req = urllib.request.Request(
        f"{base}/api/v1/entities",
        data=data,
        method="PUT",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "Anduril-Sandbox-Authorization": "Bearer test-sandbox-token",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.status
    except urllib.error.HTTPError as e:
        return e.code


@pytest.mark.parametrize(
    "name",
    ["minimal_track.json", "adsb_airplane.json", "mavlink_ownship.json"],
)
def test_fixture_fields(name):
    entity = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    assert entity.get("entityId")
    assert entity.get("isLive") is True
    assert "location" in entity
    assert "ontology" in entity
    assert "provenance" in entity


@pytest.mark.parametrize(
    "name",
    ["minimal_track.json", "adsb_airplane.json", "mavlink_ownship.json"],
)
def test_fixture_put_against_mock(mock_base, name):
    entity = json.loads((FIXTURES / name).read_text(encoding="utf-8"))
    token = _oauth(mock_base)
    status = _put(mock_base, token, entity)
    assert 200 <= status < 300
