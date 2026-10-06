/* GET /api/result?session_id=cs_...  ->  the scored result, only once Stripe reports the session paid.
   If the respondent also gave research answers, the result includes how others in their region hold the same heritages,
   once at least 30 people there have answered. */
import { parseAnswers, score } from "../_lib/atlas.js";
import { aggregate } from "../_lib/appropriation.js";
import { json, stripe, ID_RE } from "../_lib/http.js";

export async function onRequestGet({ request, env }) {
  if (!env.STRIPE_SECRET_KEY) return json({ error: "Payments are not set up yet." }, 503);

  const id = new URL(request.url).searchParams.get("session_id") || "";
  if (!/^cs_(test|live)_[A-Za-z0-9]{10,200}$/.test(id)) return json({ error: "Invalid result link." }, 400);

  const s = await stripe(env, "GET", "checkout/sessions/" + encodeURIComponent(id));
  if (s.status === 404) return json({ error: "Result not found." }, 404);
  if (!s.ok) return json({ error: "Could not check payment. Please refresh." }, 502);
  if (s.data.payment_status !== "paid") return json({ error: "Payment has not completed." }, 402);

  const meta = s.data.metadata || {};
  const a = parseAnswers(meta.a);
  if (!a) return json({ error: "Answers could not be read." }, 500);
  const out = score(a);

  if (env.DB) {
    try {
      if (ID_RE.test(meta.rid || "")) await env.DB.prepare("UPDATE responses SET paid = 1 WHERE id = ?").bind(meta.rid).run();
      if (a.research && a.research.live !== "x") {
        const q = await env.DB.prepare("SELECT * FROM responses WHERE live = ?").bind(a.research.live).all();
        const agg = aggregate(q.results || [], { by: "live" });
        const rows = agg.rows.filter((r) => r.reliability !== "insufficient");
        if (rows.length) out.region = { code: a.research.live, n: rows[0].n, rows };
      }
    } catch (e) { console.log("d1 result error", String(e)); }
  }
  return json(out);
}
