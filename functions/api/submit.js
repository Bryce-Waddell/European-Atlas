/* POST /api/submit  { a, consent: true, client, duration }  ->  { inheritance, rid?, token? }
   Scores the research answers and, if the respondent consented and the database is connected, stores them.
   Nothing is stored without consent, and nothing is stored for anyone under 18 (the quiz never sends it). */
import { parseAnswers, inheritance, rowOf, ROW_COLS, VERSION } from "../_lib/atlas.js";
import { json, sameOrigin, sha256hex } from "../_lib/http.js";

export async function onRequestPost({ request, env }) {
  if (!sameOrigin(request)) return json({ error: "Forbidden" }, 403);
  let body;
  try { body = await request.json(); } catch { return json({ error: "Bad request" }, 400); }
  const a = parseAnswers(body && body.a);
  if (!a || !a.research) return json({ error: "Some answers are missing." }, 400);

  const out = { inheritance: inheritance(a) };
  if (body.consent !== true || !env.DB) return json(out);

  const id = crypto.randomUUID(), token = crypto.randomUUID();
  const client = typeof body.client === "string" && /^[0-9a-f]{16,64}$/.test(body.client) ? body.client : null;
  const duration = Number.isFinite(body.duration) ? Math.max(0, Math.min(86400, Math.round(body.duration))) : null;
  const row = rowOf(a);
  const cols = ["id", "day", "client", "version", "duration_s", "del_hash", "code"].concat(ROW_COLS);
  const vals = [id, new Date().toISOString().slice(0, 10), client, VERSION, duration, await sha256hex(token), body.a]
    .concat(ROW_COLS.map((c) => row[c]));
  try {
    await env.DB.prepare("INSERT INTO responses (" + cols.join(",") + ") VALUES (" + cols.map(() => "?").join(",") + ")").bind(...vals).run();
  } catch (e) {
    console.log("d1 insert error", String(e));
    return json(out);
  }
  out.rid = id; out.token = token;
  return json(out);
}
