/* Offline analysis of the research data.
   1. Download the raw export:  curl -H "Authorization: Bearer $ADMIN_TOKEN" "https://europeanatlas.net/api/data?view=raw&format=json" -o responses.json
   2. Run:                      node tools/appropriation.mjs responses.json [--by=live|peoplehood|cw|subgroup] [--weighted] [--min-duration=60]
   Writes appropriation-<by>.csv next to the input and prints a summary. Uses the same code as the site. */
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { aggregate, calibrate, toCSV } from "../functions/_lib/appropriation.js";
import { AGE, BENCH } from "../functions/_lib/targets.js";

const args = process.argv.slice(2);
const file = args.find((a) => !a.startsWith("--"));
if (!file) { console.error("Usage: node tools/appropriation.mjs responses.json [--by=live] [--weighted] [--min-duration=60]"); process.exit(1); }
const opt = Object.fromEntries(args.filter((a) => a.startsWith("--")).map((a) => { const [k, v] = a.slice(2).split("="); return [k, v === undefined ? true : v]; }));
const by = opt.by || "live";
let rows = JSON.parse(readFileSync(file, "utf8"));
if (!Array.isArray(rows)) rows = rows.results || [];
const agg = aggregate(rows, { by, targets: opt.weighted && by === "live" ? AGE : null, minDuration: opt["min-duration"] !== undefined ? +opt["min-duration"] : 60 });
const out = join(dirname(file), "appropriation-" + by + ".csv");
writeFileSync(out, toCSV(agg.rows));

console.log(`${rows.length} stored responses, ${agg.respondents} kept after quality filters (${agg.dropped} dropped), grouped by ${by}${agg.weighted ? ", age-weighted" : ""}.`);
const pad = (s, n) => String(s).padEnd(n);
console.log(pad("group", 12) + pad("heritage", 9) + pad("n", 6) + pad("T", 6) + pad("O", 6) + pad("C", 6) + pad("taken", 8) + pad("inhab.", 8) + pad("kit", 8) + "plurality");
for (const r of agg.rows) {
  const pc = (x) => Math.round(100 * x) + "%";
  console.log(pad(r.group, 12) + pad(r.heritage, 9) + pad(r.n, 6) + pad(r.T_mean, 6) + pad(r.O_mean, 6) + pad(r.C_mean, 6) +
    pad(pc(r.take_share), 8) + pad(pc(r.inh_share), 8) + pad(pc(r.kit_share), 8) + r.plurality + (r.clear ? "" : " (not clear)") + (r.reliability !== "reportable" ? " [" + r.reliability + "]" : ""));
}
const cal = calibrate(agg, BENCH);
if (cal.length) { console.log("\nCalibration against published monthly-practice figures:"); cal.forEach((c) => console.log(pad(c.group, 12) + "sample " + c.sample_monthly + "  benchmark " + c.benchmark_monthly + "  ratio " + c.ratio + "  (n=" + c.n + ")")); }
console.log("\nWrote " + out);
