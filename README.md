# anduril-lattice-entity-fixtures

## Status & recognition (factual)

> Independent Polybolos Institute sample (not an Anduril product).  
> OASW(SO/LIC) Jul 2026 **Selected** (technically meritorious; under evaluation/consideration).  
> 1BCT/82nd Airborne Operation Epic Fury challenge (GoColosseum): **Submitted**.  
> AFRL Apr 2026: RQ portfolio share (Col Rondeau) + Control Science Center exchange (Weintraub; "state of the art" / partnership / SBIR language in correspondence). Attributed dialogue.  
> TRL 5 Decision-C2 lineage · Lattice sandbox / interop sample · Inquiries: mark.brown@polybolos.org · CAGE 1AVY9 · UEI RUSHH9B2UQV3

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
