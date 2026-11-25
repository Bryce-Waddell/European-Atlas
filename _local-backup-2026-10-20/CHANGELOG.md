# Changelog

All notable changes to the Atlas of European Collectives.
Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [SemVer](https://semver.org/).
MAJOR = the findings change; MINOR = a facet, region or section is added; PATCH = corrections, wording, styling.

## [1.4.1] - 2026-10-06
### Changed
- Type: self-hosted EB Garamond (reading text and data) and Cinzel (titles, labels, controls) from `fonts/`; Google Fonts removed, so the pages load no third-party resources. The Fraktur dialectic sets its own name in UnifrakturMaguntia.
- Mobile: Plates I and III put the facet switch above the map (pinned while you scroll the plate) and the region card directly under it; a tap on the map brings the card into view. Insets sit three across. Wide maps open centred on Europe.
- Mobile: the matrix and correlation table keep their row names pinned while scrolling sideways; the facet tables in Methodology and Plate III stack into rows instead of squeezing five columns.
- Mobile: larger touch targets for facet tabs, region chips, menu links and compare controls; the open menu no longer spills into a second column.
- Content Security Policy: fonts from this site only.

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
