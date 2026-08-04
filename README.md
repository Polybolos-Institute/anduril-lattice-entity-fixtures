# anduril-lattice-entity-fixtures

## Status & recognition (factual)

> Independent Polybolos Institute sample (not an Anduril product).  
> OASW(SO/LIC) Jul 2026 **Selected** (technically meritorious; under evaluation/consideration).  
> AFRL Apr 2026: RQ portfolio share (Col Rondeau) + Control Science Center exchange (Weintraub; “state of the art” / partnership / SBIR language in correspondence). Attributed dialogue.  
> TRL 5 Decision-C2 lineage · Lattice sandbox / interop sample · Inquiries: mark.brown@polybolos.org · CAGE 1AVY9 · UEI RUSHH9B2UQV3

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

This repository is the open foundation (MIT).

Polybolos Institute also maintains a proprietary catalog of additional capabilities that are not published here. Contact us to discuss production deployment and commercial licensing.

mark.brown@polybolos.org · https://www.polybolos.org
