/* POST /api/checkout  { a: "<encoded answers>", rid? }  ->  { url: "<Stripe Checkout page>" }
   The answers ride along in the Checkout Session's metadata, so the result needs no database. */
import { parseAnswers, PRICE_CENTS } from "../_lib/atlas.js";
import { json, stripe, sameOrigin, ID_RE } from "../_lib/http.js";

export async function onRequestPost({ request, env }) {
  if (!env.STRIPE_SECRET_KEY) return json({ error: "Payments are not set up yet." }, 503);
  if (!sameOrigin(request)) return json({ error: "Forbidden" }, 403);
  const origin = new URL(request.url).origin;

  let body;
  try { body = await request.json(); } catch { return json({ error: "Bad request" }, 400); }
  const code = body && typeof body.a === "string" ? body.a : "";
  if (!parseAnswers(code)) return json({ error: "Some answers are missing. Please retake the quiz." }, 400);
  const rid = body && ID_RE.test(body.rid || "") ? body.rid : "";

  const params = {
    mode: "payment",
    submit_type: "pay",
    "line_items[0][quantity]": "1",
    "line_items[0][price_data][currency]": "usd",
    "line_items[0][price_data][unit_amount]": String(PRICE_CENTS),
    "line_items[0][price_data][product_data][name]": "Your peoplehood — Atlas of European Collectives",
    "line_items[0][price_data][product_data][description]": "Your commonwealth, peoplehood, defining facet and full eight-facet profile.",
    "metadata[a]": code,
    success_url: origin + "/quiz?session_id={CHECKOUT_SESSION_ID}",
    cancel_url: origin + "/quiz?canceled=1",
  };
  if (rid) params["metadata[rid]"] = rid;
  const s = await stripe(env, "POST", "checkout/sessions", params);
  if (!s.ok || !s.data.url) {
    console.log("stripe checkout error", s.status, JSON.stringify(s.data && s.data.error));
    return json({ error: "Could not start checkout. Please try again." }, 502);
  }
  return json({ url: s.data.url });
}
