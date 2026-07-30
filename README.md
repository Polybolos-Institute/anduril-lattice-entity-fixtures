# anduril-lattice-entity-fixtures

Example Lattice **entity JSON** fixtures that publish cleanly (HTTP 200) against
[anduril-mock-lattice](https://github.com/Polybolos-Institute/anduril-mock-lattice)
and are shaped for live Sandboxes PUTs.

Door/docs only. No C2 / ROE / class map.
Built by [Polybolos Institute](https://www.polybolos.org).
**Independent sample - not an Anduril product.**

## Fixtures

| File | Intent |
|------|--------|
| `fixtures/minimal_track.json` | Minimum fields that usually accept |
| `fixtures/adsb_airplane.json` | ADS-B air track shape |
| `fixtures/mavlink_ownship.json` | Friendly UAV / ownship shape |

## Test

With sibling `mock-lattice` checkout (or installed package):

```bash
pip install pytest
pytest -q
```

## Related doors

- [anduril-mock-lattice](https://github.com/Polybolos-Institute/anduril-mock-lattice)
- [anduril-lattice-sandbox-dx](https://github.com/Polybolos-Institute/anduril-lattice-sandbox-dx)


## License

MIT - see [LICENSE](LICENSE).

## Contact

Polybolos Institute builds integrated C2 systems for contested operations.

For production deployment, integration guidance, and commercial licensing:

mark.brown@polybolos.org · https://www.polybolos.org
