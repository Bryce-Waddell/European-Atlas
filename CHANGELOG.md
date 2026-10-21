# Changelog

All notable changes to the Atlas of European Collectives.
Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [SemVer](https://semver.org/).
MAJOR = the findings change; MINOR = a facet, region or section is added; PATCH = corrections, wording, styling.

## [1.7.9] - 2026-10-20
### Changed
- The motto ribbon is removed from the crest, on the page and in the link-preview image.

## [1.7.8] - 2026-10-20
### Changed
- The full crest replaces the shield mark: the imperial eagle on its gold shield in a night sky, with an orbit, a rocket rising toward a red planet, and the motto Per aspera ad astra. Larger on every screen; on phones it stacks above the title at up to 300 px. Link-preview image redrawn around it.

## [1.7.7] - 2026-10-20
### Changed
- The page title is set in Grenze Gotisch, a blackletter–roman hybrid that reads at a glance; blackletter (UnifrakturMaguntia) stays only in the footer lockup and the link-preview image. Font self-hosted.

## [1.7.6] - 2026-10-20
### Changed
- The method and frame references move from the page footer to a References list at the end of Methodology; the footer's Sources line points there.

## [1.7.5] - 2026-10-20
### Changed
- The version history moves out of the page footer into this file; the footer keeps a one-line version stamp linking here.

## [1.7.4] - 2026-10-20
### Changed
- Latin Christian Commonwealth identity: shield-and-orbit crest, cross-potent favicon and app icons, new link-preview image.
- Palette of parchment, cardinal, gold leaf and royal blue; blackletter title, EB Garamond headings, Libre Baskerville body; fonts self-hosted.
- Celestial ornaments: night-sky menu bar, starred section rules, an arcade of stars under the title, a starfield in dark mode.
- Clearer hover, selection and focus states on tabs and controls; the menu marks the section being read.

## [1.7.3] - 2026-10-15
### Changed
- Biological facet: the hunter-gatherer component dated to its post-glacial spread, about 14,000 years ago, rather than the first arrival of modern humans.
### Added
- A new contrast, Share is not contribution, from Reich's 2026 range-expansion hypothesis and the Bronze Age Iberian Y chromosomes.

## [1.7.2] - 2026-10-12
### Changed
- The abstract opens with Fichte.
- The page leads with the plates, with Methodology and the category cards after the conclusion.
- Details collapsed behind toggles; each finding told once.

## [1.7.1] - 2026-10-12
### Changed
- The commonwealths named for their inheritances: Latin Roman West, Byzantine East, Hebraic Jews.

## [1.7.0] - 2026-10-12
### Changed
- Script a facet of its own again, compared on the alphabets' family tree.
- Shorter legends.
### Added
- The other standard linkage rules, and a prediction test net of nearness, added to the stability tests.

## [1.6.0] - 2026-10-09
### Changed
- Every facet measured or documented.
- The Latin Roman facet split into Family & kinship, Learning and Civic trust, with Roman-law contract folded into Legal family.
- Language and confession as measured shares on family trees.
- Commonwealths renamed Western, Eastern and Hebraic.
### Added
- Individualism.
- Statutory holidays in the calendar.
- Plate III: each facet alone, and the result assembled facet by facet.

## [1.5.0] - 2026-10-09
### Changed
- Script folded into Confession.
- Voices discounted for redundancy.
### Added
- Foodways and Festive calendar.
- Buildings on the Art plate.

## [1.4.0] - 2026-10-02
### Changed
- Plate III method: every facet scaled to equal spread and given an equal voice; v1.3's agreement-based weights kept only as a robustness check. The three commonwealths are unchanged; the Latin sub-groups change.
- Methodology: live robustness battery (15 tests) and a section on methodological risks.
- The quiz scores with the v1.4 method, and its commonwealths and sub-groups are read off the same tree as the atlas.
- Content Security Policy no longer pins scripts to a SHA-256 hash; one policy in `_headers` covers every page.
### Added
- The Peoplehood Quiz (`quiz.html`), with $5 result unlock through Stripe Checkout.
- Opt-in research questions measuring how respondents hold their rite, tongue and law, with a free reading for participants and self-service withdrawal.
- Research database (Cloudflare D1, `db/schema.sql`), admin export (`/api/data`), public aggregate summary (`/api/appropriation`) and offline analysis (`tools/appropriation.mjs`).
### Removed
- Plate IV (Layer B: appropriation, coded by hand). Plate V, compare two regions, is now Plate IV.

## [1.0.1] - 2026-09-25
### Added
- Selected insight comparing Ukraine and Russia: seven facets agree, one splits, and not in the expected direction.
- Dialectic on the Kyiv-Mohyla Academy of 1632 under the Latin juridical inheritance.
### Removed
- "Suggest an edit" section and its nav tab.
### Changed
- Recomputed the Content Security Policy script hash.

## [1.0.0] - 2026-09-25
### Added
- Eight facets: Latin Roman, Ancestry, Phenotype, Language, Script, Art, Legal family, Confession.
- Fifty-four regions, drawn as cultural regions rather than states where the two differ.
- Plate I, the facet map, with Anglosphere and Israel insets; Plate II, the sortable matrix; Plate III, the three commonwealths.
- Abstract, Methodology, Category explanations with Dialectics per facet, Selected insights, Conclusion.
- Radial clade trees for Language and Script.
- Site branding, favicon and app-icon set, link-preview metadata.
- Content Security Policy locking the page to its own hashed script.
