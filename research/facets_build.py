# Build the two music facets from the coding and the published data.
#   Instruments (Hornbostel–Sachs): a present/absent checklist of instrument types per region (coder A, from the
#     instrument coding in music_data.py + music_instruments.py, typed by music_types.py).
#   Song style (Cantometrics): Lomax's 37 performance-style scales, averaged over each region's majority-tradition songs.
# Run: py -I research/facets_build.py  -> research/facets.json and research/facets.js (window.FACDATA)
import csv, json, os, random, importlib.util, statistics
HERE = os.path.dirname(os.path.abspath(__file__))
def load(name):
    sp = importlib.util.spec_from_file_location(name, os.path.join(HERE, name + ".py")); m = importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
mt = load("music_types")
TYPES = [k for k, v in mt.TREE.items() if v[1] == 0]

# ---------------------------------------------------------------- instruments: coder A checklist
mus = json.load(open(os.path.join(HERE, "music.json"), encoding="utf-8"))
LANDMARK_ONLY = load("music_v2").LANDMARK_ONLY if False else None  # roles in music.json already mark landmark-only as "d"
HS = {}
for r, v in mus["regions"].items():
    have = set()
    for i in v["instruments"]:
        if i["role"] == "d": continue          # invented here, not played here: not part of the tradition
        t = mt.type_of(i["name"]); assert t in TYPES, (r, i["name"], t)
        have.add(t)
    HS[r] = {t: int(t in have) for t in TYPES}

# ---------------------------------------------------------------- song style: Cantometrics
CT_DIR = os.path.join(HERE, "cantometrics")
soc = {s["society_id"]: s for s in csv.DictReader(open(os.path.join(CT_DIR, "societies.csv"), encoding="utf-8"))}
codes = list(csv.DictReader(open(os.path.join(CT_DIR, "codes.csv"), encoding="utf-8-sig")))
K = {}
for c in codes:
    K[c["var_id"]] = max(K.get(c["var_id"], 0), int(c["code"]))
LINES = ["line_%d" % i for i in range(1, 38) if ("line_%d" % i) in K]
# Rule: each region takes the songs of its majority tradition, as Lomax's societies sample it. Indigenous nations of the
# settler states, national minorities, immigrant enclaves and multi-country samples are left out; in the United States
# both the Anglo-American and the African-American traditions are the majority tradition and both are kept.
MAP = {
 "NOR": ["Norwegian"], "SWE": ["Swedish"], "FIN": ["Finnish", "Karelia"], "DEN": ["Danish"],
 "EST": ["Estonian"], "LAT": ["Latvian"], "LIT": ["Žemaitija", "Lithuanian Folk"],
 "RUS": ["Vladimir", "Urals", "Smolenskaya", "St. Petersburg 19th c", "Vologda", "Kirovskaya", "Bryanskaya", "Perm", "Samara", "Kursk", "Stavropol"],
 "BLR": ["Belarus"], "POL": ["Danzig", "C Polish Folk"], "UKR": ["Ukrainian"],
 "IRL": ["Aran Islands", "Donegal", "Galway", "Cork", "Dublin", "Leitrim"], "ULS": ["Ulster"],
 "SCO": ["Perthshire", "Orkney", "Shetlands", "Barra", "Aberdeen", "Lowland Scotland", "South Uist"],
 "ENG": ["Norfolk", "Newcastle", "Suffolk", "Bristol", "S W England", "Sussex", "Durham Pitmen", "Wales"],
 "NLD": ["Nederlanders"], "BEL": ["Walloon"],
 "NGR": ["Lower Saxony", "Schleswig-Holstein", "Urban E Germans"], "RHI": ["Rhine-Westphalia", "Palatine"],
 "SWA": ["Baden-Württemberg"], "BAV": ["Bayern (Bavarians)", "Deggendorf", "Bavaria Munich High Germany"],
 "BOH": ["Bohemian", "Moravian"], "SLK": ["Carpathian Slovakia", "Slovakia"],
 "FRA": ["Vendée", "Paris", "Normandy", "Auvergne", "Berry", "Brittany", "French Basques", "Haute Corse", "Lothringen"],
 "SUI": ["Alpine Swiss"], "HUN": ["Tolna", "Magyar"],
 "ROM": ["Crişana", "Maramureș", "Banat", "Bucharest", "Hunedoara", "Arges", "Oltenia", "Cluj"],
 "POR": ["Lisbon", "Douro", "Algarve", "Tras-Os-Montes"],
 "ESP": ["Ibiza", "Cantabria", "Granada", "Segovia", "Mallorca", "Leon", "Cadiz", "Valencia", "Murcia", "Extremadura", "La Mancha", "Oropesa", "Aragon", "Seville", "Galicia", "Spanish Basques", "Asturias"],
 "NIT": ["Umbria-Marche", "Emilia-Romagna", "Trentino Alto Adige", "Chioggia", "Genoa", "Piemonte", "N Liguria", "Friuli"],
 "MEZ": ["Letino", "Caggiano", "Montepertuso", "Vibo Valentia", "Trapani", "Lucania", "Feroleto Antico", "Capri", "Catania", "Bagheria", "Enna", "Salento S Puglia", "Canicattì", "Gargano", "Naples & Coast"],
 "SAR": ["Barbagia", "Cagliari"],
 "CRO": ["Croatian", "Croatian Istria", "Slavonia", "N Croatia"], "BOS": ["Bosnia"],
 "SRB": ["Kumane", "Kruševica", "Vasilj", "Serbia"], "MNE": ["Montenegro"], "MAC": ["Slavic Macedonian"], "ALB": ["Ghegs"],
 "BUL": ["Dobrudzha", "N Bulgaria", "Pirin", "Rhodope", "Sofia District"],
 "GRE": ["Greek Orthodox Monastics", "Naxos", "Kalamata", "Greek Epirus", "Crete", "Inner Mani"],
 "USA": ["N European American Lumberjack", "Harlem 1900s", "Harlem 1920s", "Lake Charles, LA", "Dust Bowl", "New York S Black", "C & N Florida", "Chattanooga", "Cajun", "Piedmont Black", "Piedmont White", "Alabama Black", "Alabama White", "Shreveport Black", "Ozark", "Texas Black", "Texas White", "Hampton Roads", "Georgia Sea Islands", "Nashville", "New Orleans Creole", "Hill Country Black", "Memphis Black", "MS Delta Black", "Appalachia", "New Mexico Folk"],
 "CAN": ["Newfoundlander", "Black Nova Scotians", "Ottawa Valley Anglo-Canadians", "Canadian Mennonites", "Nova Scotia"],
 "QUE": ["French Canadians"], "AUS": ["Anglo Australians"], "ISR": ["Israeli Jews"], "ASH": ["Ashkenazi New York Jews"],
 "IBA": ["Rio", "São Paulo", "Salvador", "Piaui", "Uruguay Folk", "Chileno", "Tucuman Gaucho", "Llanero", "Costeño", "Valledupar", "Havana Folk", "Afro-Cuban", "Jalisco", "Veracruz", "Durango", "Hidalgo", "San Luis Potosí", "Guerrero", "Michoacan", "Arequipa", "Nueva Esparta", "San Andrés", "Pacific/ Chocó"],
}
byname = {}
for sid, s in soc.items(): byname.setdefault(s["society"].strip(), []).append(sid)
SID = {}
for r, names in MAP.items():
    ids = []
    for nm in names:
        assert nm in byname, (r, nm)
        ids += byname[nm]
    SID[r] = ids
songs = {}
for row in csv.DictReader(open(os.path.join(CT_DIR, "data.csv"), encoding="utf-8")):
    songs.setdefault(row["society_id"], []).append(row)
def decode(v, k):
    # stored as the sum of 2**code over the codes given; a multicoded song takes the mean of its codes, scaled 0-1
    try: v = int(v)
    except: return None
    cs = [c for c in range(1, k + 1) if v & (1 << c)]
    return (sum(cs) / len(cs) - 1) / (k - 1) if cs else None
def song_vec(row): return [decode(row[l], K[l]) for l in LINES]
CTsongs = {}
for r, ids in SID.items():
    vs = []
    for sid in ids:
        for row in songs.get(sid, []): vs.append((sid, song_vec(row)))
    CTsongs[r] = vs
# Europe-wide pooled mean per line (over regions, equal weight), the target of shrinkage
def mean_vec(vs):
    out = []
    for j in range(len(LINES)):
        x = [v[j] for v in vs if v[j] is not None]
        out.append(sum(x) / len(x) if x else None)
    return out
pooled = mean_vec([mean_vec([v for _, v in CTsongs[r]]) for r in CTsongs if CTsongs[r]])
ALPHA_CT = 2.0  # two songs' worth of the pooled profile
def profile(vs, a=ALPHA_CT):
    m = mean_vec(vs); n = len(vs)
    return [None if m[j] is None else (n * m[j] + a * pooled[j]) / (n + a) for j in range(len(LINES))]
CT = {r: {"songs": len(v), "societies": len({s for s, _ in v}), "names": MAP[r], "profile": [None if x is None else round(x, 4) for x in profile([w for _, w in v])]} for r, v in CTsongs.items() if v}

# ---------------------------------------------------------------- split-half reliability of the Cantometrics distances
def dist(p, q):
    s = n = 0
    for a, b in zip(p, q):
        if a is not None and b is not None: s += abs(a - b); n += 1
    return s / n if n else None
def corr(x, y):
    mx, my = sum(x) / len(x), sum(y) / len(y)
    sx = sum((a - mx) ** 2 for a in x) ** .5; sy = sum((b - my) ** 2 for b in y) ** .5
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)
random.seed(13)
rs = [r for r in CTsongs if len(CTsongs[r]) >= 2]
rel = []
for rep in range(60):
    A, B = {}, {}
    for r in rs:
        v = [w for _, w in CTsongs[r]]; random.shuffle(v); h = (len(v) + 1) // 2
        A[r], B[r] = profile(v[:h]), profile(v[h:])
    da, db = [], []
    for i in range(len(rs)):
        for j in range(i + 1, len(rs)):
            da.append(dist(A[rs[i]], A[rs[j]])); db.append(dist(B[rs[i]], B[rs[j]]))
    c = corr(da, db); rel.append(2 * c / (1 + c))
rel.sort()
CT_REL = {"median": round(rel[30], 2), "lo": round(rel[3], 2), "hi": round(rel[56], 2), "regions": len(rs)}

out = {"types": TYPES, "tree": mt.TREE, "hs": HS, "ct": CT, "ct_lines": LINES, "ct_rel": CT_REL, "ct_alpha": ALPHA_CT,
       "ct_line_names": {c["var_id"]: None for c in codes}}
json.dump(out, open(os.path.join(HERE, "facets.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
open(os.path.join(HERE, "facets.js"), "w", encoding="utf-8").write("window.FACDATA=" + json.dumps(out, ensure_ascii=False, separators=(",", ":")) + ";\n")
print("HS regions", len(HS), "types/region median", statistics.median(sum(v.values()) for v in HS.values()))
print("CT regions", len(CT), "songs", sum(c["songs"] for c in CT.values()), "missing", sorted(set(HS) - set(CT)))
print("CT split-half reliability", CT_REL)
print("thin CT (<3 songs):", sorted((r, c["songs"]) for r, c in CT.items() if c["songs"] < 3))
