/* GET /api/appropriation?by=live|peoplehood  ->  public summary of the research data.
   Only groups with at least 30 respondents are published, and only aggregates: no individual answers.
   Cached at the edge for an hour. */
import { aggregate } from "../_lib/appropriation.js";

export async function onRequestGet({ request, env }) {
  const headers = { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "public, max-age=3600", "X-Content-Type-Options": "nosniff" };
  if (!env.DB) return new Response(JSON.stringify({ error: "Research data is not set up." }), { status: 503, headers });
  const by = new URL(request.url).searchParams.get("by") === "peoplehood" ? "peoplehood" : "live";
  const res = await env.DB.prepare("SELECT client, id, day, duration_s, paid, age, last, " + by +
    ", con, raised, last, pass, rofc, rcon, lc, lp, tofc, tcon, lown, lofc, lcon FROM responses").all();
  const agg = aggregate(res.results || [], { by });
  const rows = agg.rows.filter((r) => r.reliability !== "insufficient").map((r) => { const o = Object.assign({}, r); delete o.paid_share; return o; });
  return new Response(JSON.stringify({ by, respondents: agg.respondents, groups: rows }), { headers });
}
