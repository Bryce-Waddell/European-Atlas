/* Small helpers shared by the quiz API. Stripe is called over its REST API with fetch, so no SDK or build step is needed. */
export function json(body, status = 200) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "private, no-store",
      "X-Content-Type-Options": "nosniff",
    },
  });
}

export function text(body, type = "text/csv; charset=utf-8", filename) {
  const headers = { "Content-Type": type, "Cache-Control": "private, no-store", "X-Content-Type-Options": "nosniff" };
  if (filename) headers["Content-Disposition"] = 'attachment; filename="' + filename + '"';
  return new Response(body, { headers });
}

export async function stripe(env, method, path, params) {
  const init = {
    method,
    headers: { Authorization: "Bearer " + env.STRIPE_SECRET_KEY },
  };
  if (params) {
    init.headers["Content-Type"] = "application/x-www-form-urlencoded";
    init.body = new URLSearchParams(params).toString();
  }
  const res = await fetch("https://api.stripe.com/v1/" + path, init);
  const data = await res.json().catch(() => ({}));
  return { ok: res.ok, status: res.status, data };
}

/* Requests that change data must come from this site. */
export function sameOrigin(request) {
  const from = request.headers.get("Origin");
  return !from || from === new URL(request.url).origin;
}

export async function sha256hex(s) {
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(s));
  return [...new Uint8Array(buf)].map((b) => b.toString(16).padStart(2, "0")).join("");
}

/* Admin endpoints: Authorization: Bearer <ADMIN_TOKEN>. Compared by hash so the comparison takes the same time whatever the input. */
export async function isAdmin(request, env) {
  if (!env.ADMIN_TOKEN || env.ADMIN_TOKEN.length < 24) return false;
  const got = (request.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "");
  return (await sha256hex(got)) === (await sha256hex(env.ADMIN_TOKEN));
}

export const ID_RE = /^[0-9a-f-]{36}$/;
