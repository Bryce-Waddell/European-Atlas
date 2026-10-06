-- Atlas of European Collectives — research responses (Cloudflare D1).
-- Create once:  npx wrangler d1 execute atlas-research --remote --file=db/schema.sql
-- One row per consenting adult respondent. No names, emails, IP addresses or payment details are stored.
CREATE TABLE IF NOT EXISTS responses (
  id          TEXT PRIMARY KEY,          -- random; shown to the respondent so they can withdraw
  day         TEXT NOT NULL,             -- date only, YYYY-MM-DD
  client      TEXT,                      -- random per-browser id, used only to keep the latest answer from each browser
  version     TEXT NOT NULL,             -- scoring version
  duration_s  INTEGER,                   -- seconds from first question to submission
  paid        INTEGER NOT NULL DEFAULT 0,
  del_hash    TEXT NOT NULL,             -- SHA-256 of the withdrawal token held by the respondent
  code        TEXT NOT NULL,             -- the full answer code
  -- Layer A answers
  chr0 TEXT, chr1 TEXT, chr2 TEXT, gp1 TEXT, gp2 TEXT, gp3 TEXT, gp4 TEXT, birth TEXT,
  lang TEXT, scr TEXT, art TEXT, leg TEXT, con TEXT,
  -- research answers
  live TEXT, age TEXT, raised TEXT, last TEXT, pass TEXT, rofc TEXT, rcon TEXT,
  lc TEXT, lp TEXT, tofc TEXT, tcon TEXT, lown TEXT, lofc TEXT, lcon TEXT,
  -- derived at submission
  cw TEXT, subgroup TEXT, peoplehood TEXT, match_pct INTEGER,
  rite_T INTEGER, rite_O INTEGER, rite_C INTEGER, rite_state TEXT,
  tongue_T INTEGER, tongue_O INTEGER, tongue_C INTEGER, tongue_state TEXT,
  law_T INTEGER, law_O INTEGER, law_C INTEGER, law_state TEXT
);
CREATE INDEX IF NOT EXISTS responses_live ON responses(live);
CREATE INDEX IF NOT EXISTS responses_peoplehood ON responses(peoplehood);
CREATE INDEX IF NOT EXISTS responses_client ON responses(client);
