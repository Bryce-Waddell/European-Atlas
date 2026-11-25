# Changelog

All notable changes to the Atlas of European Collectives.
Format: [Keep a Changelog](https://keepachangelog.com/). Versioning: [SemVer](https://semver.org/).
MAJOR = the findings change; MINOR = a facet, region or section is added; PATCH = corrections, wording, styling.

## [2.1.0] - 2026-11-20
### Added
- Facet families. The thirteen facets are grouped by what they are about: Birthright (Biological, Geographic descent); Word & learning (Language, Script, Learning); Faith & festival (Confession, Festive calendar); Law & society (Legal family, Civic trust, Individualism); Household (Family & kinship, Foodways); and Art (Architecture). The families order the Plate I and Plate III facet pickers, the Category explanations menu, the Methodology facet table and the category explanations themselves, and each explanation names its family. The grouping is not a weighting: every facet keeps its voice and no result changes.
- A "Skip to content" link and a main landmark.
- Plate III: "How the facets agree with one another". A tree of the thirteen facets by the agreement of their distances, with the groups it forms (the church facets; ancestry, land, food and language; trust and individualism) and a permutation test showing that the subject families are not statistical groups (p ≈ 0.23). All recomputed in the browser.
- A spec card on every facet's explanation: status, kind, source, coverage, voice, the three facets it agrees with most, and its reliability: for facets with several parts, how far the parts agree (Family & kinship 0.14, Foodways 0.27, Learning 0.34, Festive calendar 0.66, all computed live); for the rest, untested.
- Methodology: "How reliable each facet is", a table of the same figures for all thirteen scored facets and the two music measures.
- Art › Music, measured but not scored. On Plate I the map can be coloured by either of two music measures: the instrument types a region plays (33 Hornbostel–Sachs types, two blind coders, α 0.82 on cells, 0.68 on distances) or how its songs are sung (Lomax's 37 Cantometrics scales, 817 songs from the Global Jukebox, 47 regions, split-half 0.65). Each colour is the region's place on the first axis of a classical scaling of that measure's distances. Over the map, 156 dated markers show where instruments were first built and genres first took shape, with a timeline and filters; each region's card lists its instrument types, its song sample and what began there. The Music explanation gives both measures' spec cards and why neither is yet scored.
- Music explanation: the Hornbostel–Sachs tree, drawn live to the distances the instrument measure uses (two types are as far apart as the point where their branches meet: 0.25 within a manner of sounding, 0.5 within a class, 1 across classes), with every type's count of regions and examples from different regions. "Highlight a region" lights that region's branches; "By where it's from" re-sorts the same instruments by country so that the families scatter. On Plate I, a region's instrument types are grouped by class in the same colours, with a link to its branches on the tree. The tree replaces the paragraph that described the classification in words.
- Methodology: "Rules for adding a facet", seven conditions fixed before any new facet's results are seen: sourced, covered, coded by a fixed rule, a reliability of at least 0.7 with a second coder, Heidegger's test, a voice corrected for unreliability, and tested both ways.
- Philosophy: "Nietzsche: the European man and the abolition of nations", the full text of *Human, All Too Human* I §475 (Kaufmann's translation, with the scanning errors of the source copy corrected), set as a block quote after the closing line.
- Philosophy: "Nietzsche: on pity", the passage from *The Antichrist* §7 that the law of natural selection is thwarted by pity, set as a block quote after §475.
### Changed
- The Art facet is renamed Architecture, the first facet in the Art family. What it codes is unchanged: whether the Gothic-to-Baroque building tradition took root.
- Body text 16 px (was 15.5), map hints 14 px (was 13.5).
- Heading levels no longer skip: the Plate I, III and IV sidebar headings, the Methodology subsections and the commonwealth cards' "What sets it apart" move up one level, styled as before.
- On phones the facet rail scrolls to the chosen facet again now that the buttons sit in families.
- Footer version brought up to date.

## [2.0.10] - 2026-11-01
### Removed
- Plate I no longer shows the selected facet's notes (what it measures, Boundary, Groups and Splits) beside or under the map. Before a region is chosen the card says only: "Choose a facet to recolour the map, then tap a region to see all its facets." On phones this gives the map more of the screen. The facets are still explained in full under Category explanations.

## [2.0.9] - 2026-11-01
### Changed
- Phones and other narrow or portrait screens: Plates I, III and IV are each one screen high, so the map, its controls and the region card are all in view at once. The legend sits on top, with arrows to step through the facets; the map fills the middle; the facet buttons (Plate III: views, orders and steps) run in a single sideways-scrolling row under it; and the region card is a sheet along the bottom. Before a region is chosen the sheet shows what the facet measures.
- The insets (North America, Oceania, Israel) are pages of the same map, chosen from buttons on the map; Ibero-America and the Ashkenazim sit beside them. Choosing a region on another page turns to it.
- The map can be zoomed by pinching, double-tapping or the + and − buttons, and dragged when zoomed; ⟲ shows the whole map again.
- The region card opens with the facet on the map first. Its name is a menu of every region, "More" pulls the card up, and flicking it sideways steps to the next facet, so one region can be read facet by facet while the map recolours. Tapping a facet in the card shows it on the map, on every screen size.
- Choosing a region scrolls the plate fully into view if part of it is off screen, and the plates settle into place when scrolled near.
- Plate II: on phones the matrix is a grid of colours that fits the screen, with the facet names upright and pinned at the top while scrolling; tapping a square shows its value beneath, a region code its name, a heading sorts. "Full table" brings back the table.
- Plate V: on phones, tapping a facet shows both regions' full values, which the narrow table hides.
### Unchanged
- Wider screens, including the open iPhone Duo, are identical to 2.0.8.

## [2.0.8] - 2026-11-01
### Changed
- Language, on the region cards (Plate I) and in Plate V: each region now names its languages instead of only their branches. The first line gives the main language and its branch (for example "Mostly German (West Germanic)"); the next lists every first language counted, with its share from the same census or survey (Austria: German 88.6, Turkish 2.3, Serbian 2.2, Croatian 1.6 per cent); the last gives the branch shares the facet scores. Regions counted as a single official language show just that language. Spain, Poland, Croatia, Slovenia and Bosnia now show their published shares (Spanish, Catalan, Galician and Basque; Polish and Silesian; and so on), all within the branch already scored; Ibero-America is split into Spanish and Portuguese by the populations of its seven countries. Scores are unchanged.

## [2.0.7] - 2026-10-27
### Changed
- Philosophy: the critique is restructured around four Strauss–Howe lodestones (unrepresented government; the Civil War and slavery; the Second World War, the Holocaust and the Holodomor; supplantation). The penance paragraph now describes the lodestones hardened into civilizational dogmas of perpetual penance; the global market and the universal moral code fold into supplantation, alongside automation, atomization and falling fertility; the section closes with a call to take up the inheritances the plates measure.

## [2.0.6] - 2026-10-27
### Changed
- Dates are given as BC and AD throughout, in place of BCE and CE.
- The alphabet tree in Script now stands in the main text, after "Where the alphabets came from", instead of inside the "More" dropdown.
- Both radial trees (Language and Script): the points are larger and each has a wide invisible target, names can be pointed at too, and the drawing is fitted to its frame so the tree fills it. Hovering, tapping or tabbing to a point opens a card, and its line back to the root and all its descendants light up while the rest fades. The card places itself where it hides least of that lineage. Tapping again or tapping elsewhere closes it; Escape closes it from the keyboard.
### Added
- Each point now carries a second fact beside its date. Language tree: the first written record and today's speakers (rounded first-language counts). Script tree: the number of letters and the earliest surviving text; adopting regions also give when they adopted the script.
### Fixed
- "Hover or tap a node for its date" did nothing on phones and little on desktops: the dates sat in SVG title tooltips, which touch screens never show and desktops show only after a delay over a 6-pixel dot. Most leaves had no date to show.

## [2.0.5] - 2026-10-26
### Fixed
- The top bar now meets the top edge of the screen in Safari on the open iPhone Duo. With Safari's toolbar collapsed, the bar hung about an inch down with the page showing through above it, because it was placed below the screen's top safe area; it now starts at the top and extends its background up through that area. The page no longer shifts when that area changes size.
### Removed
- The 2.0.4 pinning of the bar to the visible area, which did not address the cause. The ?vv readout stays.

## [2.0.4] - 2026-10-26
### Fixed
- The top bar no longer slides off the top in Safari on the open iPhone Duo when scrolling down. Safari can move the visible area below the top of the page's layout while its toolbar collapses; the bar now follows the visible area.
### Added
- Adding ?vv to the address shows a small readout of the viewport measurements, for diagnosing layout on a device.

## [2.0.3] - 2026-10-26
### Fixed
- The top bar stays at the top while scrolling in Safari on the iPhone Duo. It is now fixed to the screen instead of sticky, and the page is offset by the bar's measured height, so nothing else moves.

## [2.0.2] - 2026-10-26
### Changed
- Layout for the iPhone Duo and other foldables. Open (about 890 by 626, landscape), each map plate sits beside its facet buttons, legend and region card, as on a desktop, and the map is sized to fit the screen height; folding or unfolding mid-visit moves the legend to match. Folded (about 466 by 678) and in Split View (about 445 wide), the phone layout stays, with a smaller crest on short screens and the pinned legend capped at a third of the screen.
- iOS: no automatic text enlargement in landscape; the burger menu, side panel and dropdowns size to the visible screen (dynamic viewport units); content and the top bar keep clear of side safe-area insets.
- Unchanged: data, scores and findings, and the layout on ordinary phones, tablets and wide desktops. A desktop window 840 to 999 px wide now also gets the side-by-side plates.

## [2.0.1] - 2026-10-25
### Changed
- Philosophy: the opening paragraph rewritten on Aristotle's order of inquiry, the "that" (to hoti) before the "why" (to dioti).

## [2.0.0] - 2026-10-25
### Changed
- Slovakia's cousin-marriage figure enters the family facet: 0.2 per cent, from Bittles's Europe table (all Czechoslovakia, 1961-64; Stevenson et al. 1966), the survey behind Czechia's. 25 of 54 regions now have a figure.
- Findings that move: the exact three-way split recurs in 88 of 300 moderate re-weightings (was 90); commonwealth stability 0.84 to 0.97 (was 0.83 to 0.97), Latin Roman West 0.92, Byzantine East 0.84; six facet pairs now agree at r ≥ 0.5, adding Script with Family & kinship; effective number of independent facets 6.7 (was 6.8). Family & kinship at its own best cut puts Slovakia with the regions east of the Hajnal line, so its intensive third band is the western Balkans and Israel.
- Unchanged: the three commonwealths and their membership, the cophenetic correlation (0.84) and the shuffled-data test (p < 0.005).

## [1.7.14] - 2026-10-25
### Added
- The evidence that cousin marriage is rare in the north-western and central European countries without a national survey: church law, measured neighbours, Finland's first-cousin counts (Ignatius 1995) and genomic runs of homozygosity (McQuillan et al. 2008), and the all-Czechoslovakia survey that covers Slovakia (Stevenson et al. 1966). No value is imputed and no calculation changes; the south-east and the East Slavic countries are stated as unknown.
### Changed
- Plate I region card: each facet's headline on its own line with the detail beneath, grouped into ancestry and setting and the transmitted facets, the facet on the map marked, the commonwealth shown with its colour, and a close button.

## [1.7.13] - 2026-10-25
### Changed
- Family and kinship: a plain-language account of how the score is worked out, with live worked examples and a region-by-region table of cousin-marriage figures and their scores, stating which regions have none and how little the measure moves distances inside Europe.
- Plate II family cells always show the cousin-marriage share, or n/a where there is no figure; region cards say when the figure is missing.

## [1.7.12] - 2026-10-23
### Changed
- Philosophy: the paragraph on a universal moral code is rewritten to argue against the idea itself, without generalizing about or naming any group.

## [1.7.11] - 2026-10-21
### Changed
- Blackletter retired from the last two places it remained: the footer lockup and the link-preview image now set the title in Grenze Gotisch, like the page title.
- The link-preview image shows the brass compass in place of the crest.

## [1.7.10] - 2026-10-20
### Changed
- Favicons and app icons become a brass compass: a deep-blue dial, a red-and-ivory needle and a brass bezel, detailed with a gold rose, degree ticks and N, E, S, W at the large sizes and simplified for browser tabs. The mark beside the site name in the top bar matches.

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
