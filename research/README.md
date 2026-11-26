# Music research files

- `music_data.py`: the coding, one entry per region: instruments (name, family, role, note) and the genres formed there; genre families and each genre's core instrumentation.
- `music_v2.py`: practice versus invention (`LANDMARK_ONLY`), the dated and located landmarks for Plate VI, and the shrunk family shares. Run `py -I research/music_v2.py` to rebuild `music.json` and `music_shares.json`.
- `music_shares.js`: the same shares wrapped as a script, because the page's CSP blocks fetch.
- `music_test.js`: the inclusion test. With the atlas open, load `music_shares.js` and then `music_test.js`; read `window.MUSTEST`. It adds music to the atlas's own pipeline (spread, redundancy-discounted voice, clustering), then removes it again.

To put the landmarks on the page after a change, re-run `music_v2.py` and the Plate VI insertion (the `MUSIC=` block in `index.html`).

- `music_instruments.py`: the expanded coding (v3), one list per region under a fixed rule, with region-level sources.
- `music_types.py`: the Hornbostel–Sachs type tree and the rules that place each instrument on it.
- `music_test_results.json`: the numbers quoted on the page.

Spot-checked on the web (all confirmed): Péckvillchen (Luxembourg), lončeni bas (Slovenia), prillarhorn (Norway; merged with bukkehorn), the Schrammel G-clarinet (Vienna), the Thuringian Waldzither. Not yet done: a second coder on a random third of the regions.

## The two facets (2026-11-20): facets_build.py, facets_test.js

- **Instruments (Hornbostel–Sachs checklist):** 33 types, present or absent per region. Coder A derived from the instrument lists; coder B (a blind agent, `hs_coder_b.json`) coded a seeded random 18 regions directly from the checklist. Cells: 84% raw agreement, Krippendorff's α 0.64 (0.66 without the organ, where B applied a liturgical rule). Distance reliability between coders: r = 0.39. B marks more types present (median 14 against 9), so A's lists under-report: the two coders did not use the same method, and the test should be repeated with two blind checklist coders for all regions.
- **Song style (Cantometrics, Lomax; Wood et al. 2022):** 817 songs, 47 regions (missing ISL, LUX, AUT, MOL, SLO, GAL, NZL), majority-tradition societies only (map in facets_build.py), each region the mean of its songs on Lomax's 37 scales, shrunk by two songs toward the pooled profile. Split-half reliability 0.65 (0.54–0.73).
- **Re-run with two blind checklist coders (same method):** coder A2 (`hs_coder_a2.json`, all 54) against coder B (18). Cells: 91% raw agreement, Krippendorff's α 0.82. Distances: r = 0.68 (`hs_reliability.json`). The facet now uses A2. Added alone: 7.6% of the voice (5th of 14), the three commonwealths unchanged; nearest neighbours, e.g. Ireland with Ulster, the US, Scotland and New Zealand; Finland with Norway, Sweden and Estonia; Ibero-America with the Mezzogiorno, Portugal and Spain. With song style as well, reliability-corrected: 6.5% and 7.1% of the voice, Slovenia and Croatia move (adjusted Rand 0.86). The facets still do not agree with each other (r = 0.01).
- **Earlier run (superseded), neither meets the 0.7 rule.** If added anyway: instruments alone 11.9% of the voice (the largest), the three commonwealths unchanged; song style alone 8.1%, Slovenia, Croatia and Ibero-America move; both together, only Greece moves (adjusted Rand 0.976). The two facets do not agree with each other (r = 0.04, Mantel p = 0.29).
- Cantometrics data: research/cantometrics/, downloaded from github.com/theglobaljukebox/cantometrics (cite Lomax 1968; Wood et al. 2022, PLOS ONE 17(11): e0275469).

## Results, v3 coding (2026-11-20)

| Test | Result |
|---|---|
| Split-half reliability, instruments (types) | 0.24 (α = 1), 0.26 (α = 3) |
| Split-half reliability, genres | 0.50, 0.69 |
| Split-half reliability, music combined | 0.46, 0.65 (the rule is 0.7) |
| Agreement of the two halves | r = 0.09, Mantel p = 0.14 |
| One facet, α = 3, reliability-corrected | 13.3% of the voice; three commonwealths unchanged |
| Two facets | 24.4% of the voice; adjusted Rand 0.29 |

## Results, v1 coding (superseded)

| Test | Result |
|---|---|
| Agreement of the two halves (Mantel, 999 permutations) | r = 0.17, p = 0.02 |
| Split-half reliability, instruments | about 0.2 |
| Split-half reliability, genres | 0.5 (α = 1) to 0.7 (α = 3) |
| One facet: voice, three commonwealths | 17.5%; Ibero-America moves (α = 1), none move (α = 3) |
| Two facets: combined voice, three commonwealths | 27.4%; adjusted Rand 0.26 |

Conditions for entry are in the atlas under Methodology, "Music: the method, and why it waits".
