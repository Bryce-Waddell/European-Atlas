# Instrument types for the music facet (v3): each coded instrument is assigned one type on a three-level tree after
# Hornbostel–Sachs (1914; MIMO revision 2011): class (chordophone, aerophone, percussion, electrophone), then the way the
# sound is excited (bowed, plucked, struck; flute, reed, lip, free reed; membrane, idiophone), then the type.
# The broad families of the genre half and of the map legend stay as they are; types are only for the instrument distance.

TREE = {  # node: [parent, height]; a pair of pure types is as far apart as the height of the lowest node they share
 "CHORD": ["root", .5], "BOW": ["CHORD", .25], "PLUCK": ["CHORD", .25], "STRUCK": ["CHORD", .25],
 "AERO": ["root", .5], "FLUTE": ["AERO", .25], "REED": ["AERO", .25], "LIP": ["AERO", .25], "FREE": ["AERO", .25],
 "PERC": ["root", .5], "MEMB": ["PERC", .25], "IDIO": ["PERC", .25],
 "bowlute": ["BOW", 0], "bowlyre": ["BOW", 0], "bowzither": ["BOW", 0], "hurdy": ["BOW", 0],
 "longneck": ["PLUCK", 0], "shortneck": ["PLUCK", 0], "boxzither": ["PLUCK", 0], "harp": ["PLUCK", 0], "mbow": ["PLUCK", 0],
 "dulcimer": ["STRUCK", 0], "piano": ["STRUCK", 0],
 "flute": ["FLUTE", 0], "panpipe": ["FLUTE", 0], "doubleflute": ["FLUTE", 0],
 "reedpipe": ["REED", 0], "clarinet": ["REED", 0], "shawm": ["REED", 0], "bagpipe": ["REED", 0], "sax": ["REED", 0],
 "horn": ["LIP", 0], "brass": ["LIP", 0],
 "accordion": ["FREE", 0], "concertina": ["FREE", 0], "harmonica": ["FREE", 0], "organ": ["FREE", 0],
 "frame": ["MEMB", 0], "drum": ["MEMB", 0], "goblet": ["MEMB", 0], "friction": ["MEMB", 0],
 "jaw": ["IDIO", 0], "idio": ["IDIO", 0], "bells": ["IDIO", 0],
 "electric": ["root", 0],
}
# Pipe organs are aerophones, not free reeds; they sit with the free reeds here only because both are wind keyboards
# and the atlas has very few of them. Their count is small enough that the choice moves no distance noticeably.

# keyword rules, first match wins (lower-case substring of the instrument name)
RULES = [
 ("electric", ["electric guitar", "amplifier", "hammond", "moog", "buchla", "synth", "theremin", "trautonium", "ondes", "sackbut", "fairlight", "csirac", "computer", "wdr", "clavinet", "mellotron", "ans "]),
 ("hurdy", ["hurdy", "draailier", "tekerőlant", "zanfona", "lira"]),
 ("bowlyre", ["jouhikko", "hiiu kannel", "crwth"]),
 ("bowzither", ["langspil", "fiðla", "psalmodikon", "ģīga"]),
 ("bowlute", ["fiddle", "violin", "violon", "vioară", "skrypka", "skrzypce", "smuikas", "husle", "hegedű", "kontra", "violi", "gudok", "gadulka", "lyra", "gusle", "lahuta", "kemane", "lijerica", "nyckelharpa", "hardanger", "suka", "złóbcoki", "basy", "basetlia", "basolia", "bőgő", "basa", "contrabas", "double bass", "upright bass", "klezmer bass", "ländler double bass", "bass"]),
 ("mbow", ["berimbau"]),
 ("dulcimer", ["tsymbaly", "cymbały", "cimbal", "cimbál", "țambal", "hackbrett", "santouri", "tsimbl", "ütőgardon"]),
 ("piano", ["piano", "fortepiano", "grand action", "overstrung"]),
 ("harp", ["harp", "clàrsach", "harfe"]),
 ("boxzither", ["kantele", "kannel", "kokle", "kanklės", "gusli", "langeleik", "hummel", "zither", "citera", "citre", "épinette", "autoharp", "appalachian dulcimer", "kanun", "kanonaki"]),
 ("longneck", ["balalaika", "domra", "bouzouki", "baglamas", "tzouras", "saz", "šargija", "çifteli", "sharki", "tambura", "tamburica", "bisernica", "seven-string"]),
 ("shortneck", ["guitar", "guitare", "gitarre", "mandolin", "mandola", "bandolim", "cobza", "oud", "outi", "ut", "laouto", "llautë", "laúd", "bandurria", "cavaquinho", "ukulele", "charango", "banjo", "viola", "chitarra", "tres", "cuatro", "kobza", "bandura", "torban", "timple", "waldzither", "halszither", "guitarrón", "vihuela", "contraguitar", "tea-chest"]),
 ("bagpipe", ["bagpipe", "pipes", "gaida", "gajde", "gajda", "dudy", "duda", "torupill", "dūdas", "mänkeri", "säckpipa", "sækkepibe", "doedelzak", "piva", "baghet", "müsa", "zampogna", "gaita", "cimpoi", "tsampouna", "mišnice", "koza", "kozioł", "volynka", "cabrette", "biniou", "gajdy", "pipe-band"]),
 ("sax", ["saxophone"]),
 ("clarinet", ["clarinet", "klarino", "klarinet", "tárogató", "taragot", "launeddas"]),
 ("shawm", ["zurna", "zurla", "zournas", "sopile", "ciaramella", "bombarde", "dulzaina", "gralla", "tenora", "tible", "piffero", "schalmei", "duduk", "oboe", "heckelphone", "pibgorn"]),
 ("reedpipe", ["birbynė", "zhaleika", "sarvepill", "diple", "benas", "rozhok"]),
 ("panpipe", ["nai", "skudučiai", "kugikly", "siku", "trstenke"]),
 ("doubleflute", ["dvojnice", "dvojačka", "dvodentsivka", "dvoyanka"]),
 ("flute", ["flute", "whistle", "fife", "piccolo", "fujara", "koncovka", "kaval", "kavall", "caval", "frula", "fluier", "floyera", "svirel", "svirka", "sopilka", "telenka", "seljefløyte", "pajupilli", "fyell", "šupelka", "žvegla", "píšťala", "furulya", "flabiol", "txistu", "galoubet", "pipe and tabor", "halil", "quena", "kōauau", "pūtōrino", "lamzdeliai", "stabule", "vilepill", "spilåpipa", "härjedalspipa", "floyara", "fleyt", "sulittu", "friscalettu", "fujarka", "pífaro", "fifre", "gum leaf", "ocarina", "péckvillchen", "dudka", "alboka"]),
 ("horn", ["alphorn", "büchel", "trembita", "bucium", "lur", "bukkehorn", "ragai", "ragi", "daudytė", "ligawka", "trombita", "kohorn", "karjapasun", "tuohitorvi", "midwinterhoorn", "fanfára", "shofar", "pūkāea", "pūtātara", "didgeridoo", "trompe de chasse", "serpent", "jug", "näverlur", "bugle"]),
 ("brass", ["brass", "cornet", "flügelhorn", "flugelhorn", "tuba", "euphonium", "tenor horn", "truba", "trumpet", "posaunenchor", "fanfare", "harmonie", "banda", "lúðrasveit", "vienna horn", "červený", "sousaphone", "trombone", "valve", "ophicleide", "saxhorn"]),
 ("concertina", ["concertina", "bandonija", "bandoneon", "harmonia pedałowa"]),
 ("harmonica", ["harmonica", "mouth organ", "ruine-babines"]),
 ("organ", ["organ", "orchestrion", "harmonium", "hydraulis"]),
 ("accordion", ["accordion", "accordéon", "acordeon", "acordeão", "melodeon", "garmon", "bayan", "harmonika", "harmonikka", "steirische", "ziach", "heligonka", "heligónka", "frajtonarica", "trekkspill", "torader", "dragspel", "lõõtspill", "ermoņikas", "armonika", "garmonik", "organetto", "trikitixa", "schwyzerörgeli"]),
 ("friction", ["rommelpot", "putipù", "köcsögduda", "buhai", "lončeni bas", "burczybas"]),
 ("goblet", ["darbuka", "darabuka", "tarabuka", "tarambuka", "toubeleki"]),
 ("frame", ["bodhrán", "def", "adufe", "tammorra", "tamburello", "pandeiro", "tof", "buben", "pandereta", "sámi drum"]),
 ("drum", ["drum", "tapan", "daouli", "lodër", "bubanj", "bubon", "tobă", "trumm", "bungas", "būgnas", "bębenek", "lambeg", "tumbarinu", "bombo", "surdo", "tambourin", "poyk", "congas", "bass-drum pedal", "drum kit"]),
 ("jaw", ["munnharpe", "mungiga", "munniharppu", "parmupill", "vargāns", "drymba", "drumbľa", "doromb", "drâmbă", "maultrommel", "marranzanu", "trunfa", "trump", "guimbarde", "trümpi"]),
 ("bells", ["bell", "carillon", "glockenspiel", "vibraphone", "marimba"]),
 ("idio", ["tabalas", "trīdeksnis", "lozhki", "treshchotka", "cuillères", "os", "bones", "castanets", "ferrinhos", "reque-reque", "txalaparta", "talerschwingen", "ozembuch", "scetavajasse", "triccheballacche", "washboard", "ugly stick", "lagerphone", "clapsticks", "pahū", "maracas", "güiro", "podorythmie", "cajón"]),
]
EXACT = {"Bass": "bowlute", "Os": "idio", "Ut": "shortneck", "Lira": "hurdy", "Lira calabrese": "bowlute", "Tambura": "longneck",
         "Concert zither": "boxzither", "Zither": "boxzither", "Def": "frame", "Tapan": "drum", "Tof": "frame",
         "Dvojnice": "doubleflute", "Diple": "reedpipe", "Gaida": "bagpipe", "Klezmer bass": "bowlute", "Kaval": "flute",
         # resolved by hand where the keyword rules collide
         "Handbells": "bells", "Tower bells": "bells", "Fasnet bells": "bells", "Glockenspiel lyra": "bells", "Hommel": "boxzither",
         "Schwegel": "flute", "Bass drum": "drum", "Pipe-band bass drum": "drum", "Harmonie drum": "drum", "Pibgorn": "reedpipe",
         "Rozhok": "horn", "Seven-string guitar": "shortneck", "Organetto": "accordion", "Duduk": "flute", "Tea-chest bass": "mbow",
         "Thuringian Waldzither": "shortneck", "Halszither": "shortneck", "Alboka": "reedpipe", "Harmonia pedałowa": "organ"}

def type_of(name):
    if name in EXACT: return EXACT[name]
    n = name.lower()
    for t, keys in RULES:
        for k in keys:
            if (" " + k + " ") in (" " + n.replace("(", " ").replace(")", " ").replace(",", " ") + " ") or (len(k) > 4 and k in n):
                return t
    return None
