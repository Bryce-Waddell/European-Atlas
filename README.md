# Atlas of European Collectives

A single-file static site. Eight facets, fifty-four regions, three commonwealths.

    index.html          the entire site: markup, styles, script, images (base64)
    quiz.html           the Peoplehood Quiz (free to take, $5 to see the result)
    functions/          Cloudflare Pages Functions: scoring, checkout, research data for the quiz
    db/schema.sql       the research database table (Cloudflare D1)
    tools/              offline analysis of the research data
    _headers            security headers for Netlify / Cloudflare Pages
    site.webmanifest    Android / Chrome install metadata
    favicon*, icon-*    icons for browsers, iOS, Android
    og-image.png        link-preview card for iMessage, Slack, LinkedIn

## Editing

Open `index.html` in a plain-text editor. **Not Notes or Word** — they convert straight quotes to curly ones and break the code.

The data lives in one array near the top of the `<script>`, one row per region:

    ["POL","Poland",45,32,23,"in","civil","cath","slavw","latin","EU","both","tbroad|PA"],

Order: code, name, steppe %, farmer %, forager %, Latin Roman, legal family, confession, language, script, map group, art, geographic descent (biome|realm). The same array is copied into `functions/_lib/atlas.js` for the quiz.

## Content Security Policy

The pages run their own inline script, so the policy allows `'unsafe-inline'` scripts from this site and nothing else: no scripts from other domains, no embedding in frames, no form posts elsewhere. Edit the script freely; there is no hash to update. The policy is set once in `_headers` for every page, and repeated in each page's meta tag for hosts that cannot send headers.

## Deploying

**Cloudflare Pages (recommended).** Connect this repo, build command empty, output directory `/`. `_headers` is applied automatically. Then in the dashboard enable Always Use HTTPS, HSTS, and Bot Fight Mode.

**Netlify.** Same; `_headers` works out of the box.

**GitHub Pages.** Works, but *cannot send custom headers* — the CSP meta tag still applies, but HSTS and X-Frame-Options will not. Put Cloudflare in front of it if you use Pages.

## The Peoplehood Quiz

Ten questions place the visitor on the atlas's eight facets, scored with the atlas's own method (v1.4): every facet scaled to the same spread and given an equal voice, the same category distances, then the commonwealth with the smallest mean distance and the nearest region inside it. Commonwealths and sub-groups are read off the same clustering tree the atlas draws. Taking the quiz is free; the full result costs $5.

After the ten, visitors are offered fourteen optional research questions on how they hold their faith, language and law (see *Research data* below). Those who take part see their own reading free, straight away.

How payment works:

1. The visitor answers; the page sends the encoded answers to `/api/checkout`.
2. That function creates a Stripe Checkout session for $5 and stores the answers in the session's metadata, so the result itself needs no database.
3. Stripe returns the visitor to `/quiz?session_id=…`. The page asks `/api/result`, which checks with Stripe that the session is paid, then scores the answers on the server and returns the result.

Scoring lives only in `functions/_lib/atlas.js`, so the result cannot be read out of the page. The region data and the clustering engine in that file are copies of the ones in `index.html` (v1.4.0); if you change the atlas data or method, copy them across too.

**This needs Cloudflare Pages.** GitHub Pages serves static files only and cannot run `functions/`.

Setup, once:

1. Create a Stripe account and finish activation (business details, bank account).
2. In Stripe → Developers → API keys, copy the **secret key**. Start with the test key (`sk_test_…`).
3. In Cloudflare → Workers & Pages → your project → Settings → Variables and Secrets, add `STRIPE_SECRET_KEY` as a **Secret** for Production (and Preview). Never commit it.
4. Redeploy. Take the quiz and pay with Stripe's test card `4242 4242 4242 4242`, any future date, any CVC.
5. When it works, replace the secret with the live key (`sk_live_…`) and redeploy.

To change the price, edit `PRICE_CENTS` at the bottom of `functions/_lib/atlas.js` and every "$5" in `quiz.html`.

Payments appear in the Stripe dashboard with the answers attached to each one; refunds are issued there.

## Research data: measuring appropriation

The atlas's old Layer B coded, by hand, whether each region's rite, tongue and law were still being handed down. The quiz now measures it from people instead. Each consenting respondent scores 0–2 on three things for each heritage — **transmission** (handing it on), **offices** (serving it) and **contest** (arguing over the thing itself) — which give a state: *taken over* (T = 2 and O + C ≥ 2), *inhabited*, or *kit* (T = 0 and O + C ≤ 1). Regions are reported as the share of their respondents in each state, with 95% intervals. The rules live in `functions/_lib/appropriation.js`, and every report recomputes them from the raw answers, so changing a rule applies to all past data.

### Setup, once

1. Create the database: Cloudflare → Workers & Pages → D1 → *Create* → name it `atlas-research`.
2. Create the table: open the database's *Console* tab, paste the contents of `db/schema.sql`, run it.
3. Bind it: your Pages project → Settings → Bindings → *Add* → D1 database → variable name **`DB`**, database `atlas-research`. Do this for Production and Preview.
4. Add a secret for yourself: Settings → Variables and Secrets → **`ADMIN_TOKEN`**, type *Secret*, at least 24 random characters (a password manager's generator is ideal). Never commit it.
5. Redeploy. Without `DB` the quiz still works: participants see their reading, and nothing is stored.

### Getting the data out

    curl -H "Authorization: Bearer $ADMIN_TOKEN" "https://europeanatlas.net/api/data?view=regions" -o regions.csv

| Query | Returns |
|---|---|
| `view=regions` (default) | One row per region and heritage: n, effective n, mean T/O/C with 95% intervals, share taken over / inhabited / kit / none with 95% intervals, the plurality, whether it is clear, and a reliability flag |
| `view=raw` | Every stored response, one row each |
| `view=calibration` | The sample's monthly religious practice against published figures in `_lib/targets.js` |
| `by=live` / `peoplehood` / `cw` / `subgroup` | Group by where people live (default), by the peoplehood the quiz placed them in, by commonwealth or by sub-group |
| `weighted=1` | Weight respondents by age band to the population figures in `_lib/targets.js` |
| `min_duration=60` | Drop answers completed faster than this (default 60 seconds) |
| `format=json` | JSON instead of CSV |

For offline work, download the raw data and run the same code locally:

    curl -H "Authorization: Bearer $ADMIN_TOKEN" "https://europeanatlas.net/api/data?view=raw&format=json" -o responses.json
    node tools/appropriation.mjs responses.json --by=live --weighted

`/api/appropriation` is a public, cached summary — aggregates only, and only for groups of 30 or more — for the atlas page to read later.

**Reliability flags.** *Insufficient* under 30 respondents (not published); *provisional* under 100 effective respondents; *reportable* above. A plurality is *clear* only if its interval does not overlap the runner-up's.

### What the data can and cannot show

It is a self-selected sample of people who found an atlas about European peoplehood, so it will lean towards people who care about their inheritance and will overstate practice. Read it as a measure of *this audience*, compare regions with each other rather than with the truth, and fill in `BENCH` in `_lib/targets.js` with published survey figures (European Social Survey, Pew) so the calibration view shows by how much the sample overstates. Weighting by age fixes only the age skew. Offices and contest are measured as one person's involvement, not as whether a region's institutions are staffed.

### Your obligations

Faith is special-category data under the GDPR and sensitive data under several US state laws. The quiz asks for explicit, unticked-by-default consent, stores no names, emails, IP addresses or payment details, keeps only the day of submission, turns away under-18s before storing anything, lets each participant withdraw from their own browser, and publishes only aggregates of 30 or more. You are still the data controller: publish a short privacy notice with a contact address, and answer deletion requests. **Never commit exported data to this repository** — it is public; `.gitignore` blocks the usual file names.

## Security checklist

The HTML is hardened. These are the things that actually get static sites taken over:

- [ ] Two-factor authentication on GitHub, **with recovery codes saved offline**
- [ ] Two-factor authentication on the domain registrar and the host
- [ ] Registrar lock enabled on the domain
- [ ] DNSSEC enabled at the registrar
- [ ] Branch protection on `main`: require a pull request, block force-pushes and deletion
- [ ] Signed commits, so a stolen token cannot push work that looks like yours
- [ ] Review any GitHub Action you add; a malicious action can rewrite the site
- [ ] Keep no secrets in this repo — it is entirely public by design. The Stripe key and `ADMIN_TOKEN` live only in Cloudflare's encrypted variables
- [ ] Turn on a Cloudflare rate-limiting rule for `/api/submit` (for example, 10 requests per minute per IP) to blunt scripted submissions
- [ ] Two-factor authentication on Stripe

## Version

See `CHANGELOG.md`. Current: 1.4.0.
