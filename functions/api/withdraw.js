/* POST /api/withdraw  { rid, token }  ->  { deleted: 0 | 1 }
   Deletes a respondent's row. Only the browser that submitted it holds the token. */
import { json, sameOrigin, sha256hex, ID_RE } from "../_lib/http.js";

export async function onRequestPost({ request, env }) {
  if (!sameOrigin(request)) return json({ error: "Forbidden" }, 403);
  if (!env.DB) return json({ error: "Research data is not set up." }, 503);
  let body;
  try { body = await request.json(); } catch { return json({ error: "Bad request" }, 400); }
  if (!body || !ID_RE.test(body.rid || "") || !ID_RE.test(body.token || "")) return json({ error: "Bad request" }, 400);
  const r = await env.DB.prepare("DELETE FROM responses WHERE id = ? AND del_hash = ?").bind(body.rid, await sha256hex(body.token)).run();
  return json({ deleted: (r.meta && r.meta.changes) || 0 });
}
