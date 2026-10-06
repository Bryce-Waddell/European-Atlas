/* GET /api/data — the research data, for the atlas's author only.
   Authorization: Bearer <ADMIN_TOKEN>

   ?view=raw            every stored response, one row each (no withdrawal hashes)
   ?view=regions        appropriation by group: n, effective n, mean T/O/C with 95% intervals, state shares with 95% intervals
   ?view=calibration    sample monthly practice against the published benchmarks in _lib/targets.js
   &by=live|peoplehood|cw|subgroup   grouping for regions (default live: where respondents live now)
   &weighted=1          weight by age band to the targets in _lib/targets.js
   &min_duration=60     drop answers completed faster than this many seconds
   &format=csv|json     default csv */
import { aggregate, calibrate, toCSV } from "../_lib/appropriation.js";
import { AGE, BENCH } from "../_lib/targets.js";
import { json, text, isAdmin } from "../_lib/http.js";

const BY = ["live", "peoplehood", "cw", "subgroup"];

export async function onRequestGet({ request, env }) {
  if (!(await isAdmin(request, env))) return json({ error: "Not found" }, 404);
  if (!env.DB) return json({ error: "Research data is not set up." }, 503);
  const q = new URL(request.url).searchParams;
  const view = q.get("view") || "regions", format = q.get("format") || "csv";
  const by = BY.includes(q.get("by")) ? q.get("by") : "live";
  const minDuration = Math.max(0, parseInt(q.get("min_duration") || "60", 10) || 0);
  const res = await env.DB.prepare("SELECT * FROM responses ORDER BY day, id").all();
  const rows = (res.results || []).map((r) => { const o = Object.assign({}, r); delete o.del_hash; return o; });
  const stamp = new Date().toISOString().slice(0, 10);

  let out;
  if (view === "raw") out = rows;
  else {
    const agg = aggregate(rows, { by, minDuration, targets: q.get("weighted") === "1" && by === "live" ? AGE : null });
    if (view === "calibration") out = calibrate(agg, BENCH);
    else out = format === "json" ? agg : agg.rows;
  }
  if (format === "json") return json(out);
  return text(toCSV(Array.isArray(out) ? out : []), "text/csv; charset=utf-8", "atlas-" + view + "-" + by + "-" + stamp + ".csv");
}
