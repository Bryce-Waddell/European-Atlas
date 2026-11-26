# v2 of the music facet data (method: research/MUSIC-METHOD.md). Builds on music_data.py.
# Run: py -I research/music_v2.py  -> rewrites research/music.json and writes research/music_shares.json
import json, os, runpy
HERE = os.path.dirname(os.path.abspath(__file__))
base = runpy.run_path(os.path.join(HERE, "music_data.py"))
R, G, IFAM, GFAM, credit, gen, out = base["R"], base["G"], base["IFAM"], base["GFAM"], base["credit"], base["gen"], base["out"]

# Practice versus event: an instrument counts in the distance only if the region plays it in its own music
# ("t", or "dt" = developed here and played here). An invention the region did not take up ("d") is a landmark only.
LANDMARK_ONLY = {
 "Russian horn band", "Theremin", "ANS synthesizer", "Bronze-Age lur", "Keyed bugle", "Saxophone",
 "Valve for brass", "Tuba", "German concertina", "Mouth organ (Aura)", "Trautonium", "Dresden pedal timpani",
 "Bandoneon", "Heckelphone", "WDR electronic studio", "Harmonica (mass-made)", "Clavinet and Pianet", "Hohner accordion",
 "Boehm flute", "Fortepiano action", "Oboe", "Ophicleide and cornet", "Saxhorn family", "Harmonium",
 "Double-escapement piano action", "Double-action pedal harp", "Ondes Martenot", "Viennese piano action",
 "English grand action", "Tin whistle (mass-made)", "Mellotron", "Ferranti Mark 1 music", "Vihuela", "Piano",
 "Hydraulis", "Electronic sackbut", "Fairlight CMI", "CSIRAC music", "Vox and Marshall amplifiers"}
# v3: the expanded coding replaces each region's traditional entries; developed entries ("d") stay
import importlib.util
_sp = importlib.util.spec_from_file_location("mi", os.path.join(HERE, "music_instruments.py")); _mi = importlib.util.module_from_spec(_sp); _sp.loader.exec_module(_mi)
EXP, SOURCES = _mi.EXP, _mi.SOURCES
assert sorted(EXP) == sorted(R), set(R) ^ set(EXP)
for r in R:
    ins, gs = R[r]
    keep = [i for i in ins if i[2] == "d"]
    have = {i[0].lower() for i in keep}
    add = [[n, f, "t", ""] for n, f in EXP[r] if n.lower() not in have]
    for n, f, *_ in add: assert f in IFAM, (r, n, f)
    R[r] = (keep + add, gs)
names = {i[0] for v in R.values() for i in v[0]}
missing = LANDMARK_ONLY - names
assert not missing, missing

# Landmarks: name, kind (i instrument, g genre), family, unit credited, lat, lon, year, date as written, note.
# Only events with a documented place and date are pinned.
LM = [
 ["Hardanger fiddle", "i", "str", "NOR", 60.32, 6.65, 1651, "1651", "Jaastad fiddle, the oldest dated"],
 ["Nyckelharpa", "i", "str", "SWE", 57.60, 18.60, 1350, "c. 1350", "earliest depiction, Källunge church, Gotland"],
 ["Bronze-Age lurs", "i", "br", "DEN", 55.85, 12.25, -800, "c. 800 BC", "Brudevælte pair, North Zealand"],
 ["Russian horn band", "i", "br", "RUS", 59.94, 30.31, 1751, "1751", "J. A. Maresch, St Petersburg"],
 ["Garmon", "i", "fr", "RUS", 54.19, 37.62, 1830, "1830s", "Tula workshops"],
 ["Concert balalaika", "i", "str", "RUS", 59.94, 30.31, 1887, "1880s", "Vasily Andreyev, St Petersburg"],
 ["Theremin", "i", "el", "RUS", 59.95, 30.33, 1920, "1920", "Léon Theremin, Petrograd"],
 ["ANS synthesizer", "i", "el", "RUS", 55.75, 37.62, 1958, "1958", "Yevgeny Murzin, Moscow"],
 ["Keyed bugle", "i", "br", "IRL", 53.35, -6.26, 1810, "1810", "Joseph Haliday's patent; rights sold to a Dublin maker"],
 ["Lambeg drum", "i", "pc", "ULS", 54.53, -6.07, 1870, "late 19th c.", "named for Lambeg, Co. Antrim"],
 ["English concertina", "i", "fr", "ENG", 51.51, -0.13, 1829, "1829", "Charles Wheatstone, London"],
 ["Mass-made tin whistle", "i", "ww", "ENG", 53.48, -2.24, 1843, "1843", "Robert Clarke, Manchester"],
 ["English grand action", "i", "kb", "ENG", 51.51, -0.14, 1772, "1770s", "Backers and Broadwood, London"],
 ["Computer music", "i", "el", "ENG", 53.47, -2.23, 1951, "1951", "Ferranti Mark 1, Manchester"],
 ["Vox AC30 amplifier", "i", "el", "ENG", 51.44, 0.22, 1958, "1958", "Dartford"],
 ["Marshall amplifier", "i", "el", "ENG", 51.51, -0.33, 1962, "1962", "Hanwell, London"],
 ["Mellotron", "i", "el", "ENG", 52.48, -1.89, 1963, "1963", "Birmingham"],
 ["Tuned carillon", "i", "pc", "NLD", 52.14, 6.20, 1644, "1644", "Hemony brothers, Zutphen"],
 ["Saxophone", "i", "ww", "BEL", 50.85, 4.35, 1840, "c. 1840", "Adolphe Sax, Brussels; patented in Paris 1846"],
 ["Schnitger organ", "i", "kb", "NGR", 53.55, 9.99, 1693, "1693", "Arp Schnitger, St Jacobi, Hamburg"],
 ["Silbermann organ", "i", "kb", "NGR", 50.92, 13.34, 1714, "1714", "Gottfried Silbermann, Freiberg Cathedral"],
 ["Valve for brass", "i", "br", "NGR", 52.52, 13.40, 1818, "1818", "Stölzel and Blühmel's patent, Berlin"],
 ["Mouth organ (Aura)", "i", "fr", "NGR", 52.52, 13.38, 1821, "1821", "Christian Buschmann, Berlin"],
 ["German concertina", "i", "fr", "NGR", 50.83, 12.92, 1834, "1834", "Carl Friedrich Uhlig, Chemnitz"],
 ["Tuba", "i", "br", "NGR", 52.51, 13.39, 1835, "1835", "Wieprecht and Moritz, Berlin"],
 ["Dresden pedal timpani", "i", "pc", "NGR", 51.05, 13.74, 1881, "1881", "Carl Pittrich, Dresden"],
 ["Trautonium", "i", "el", "NGR", 52.53, 13.41, 1930, "1930", "Friedrich Trautwein, Berlin"],
 ["Bandoneon", "i", "fr", "RHI", 51.33, 6.56, 1847, "1840s", "Krefeld; Heinrich Band named it, invention disputed"],
 ["Heckelphone", "i", "ww", "RHI", 50.04, 8.24, 1904, "1904", "Heckel, Biebrich"],
 ["WDR electronic studio", "i", "el", "RHI", 50.94, 6.96, 1951, "1951", "Cologne"],
 ["Mass-made harmonica", "i", "fr", "SWA", 48.07, 8.63, 1857, "1857", "Matthias Hohner, Trossingen"],
 ["Clavinet", "i", "el", "SWA", 48.08, 8.64, 1964, "1964", "Hohner, Trossingen"],
 ["Clarinet", "i", "ww", "BAV", 49.45, 11.08, 1700, "c. 1700", "J. C. Denner, Nuremberg"],
 ["Stein fortepiano action", "i", "kb", "BAV", 48.37, 10.90, 1777, "by 1777", "J. A. Stein, Augsburg"],
 ["Boehm flute", "i", "ww", "BAV", 48.14, 11.58, 1847, "1832–47", "Theobald Boehm, Munich"],
 ["Červený chromatic brass", "i", "br", "BOH", 50.21, 15.83, 1842, "from 1842", "Hradec Králové"],
 ["Oboe", "i", "ww", "FRA", 48.80, 2.13, 1657, "c. 1657", "French court; Hotteterre and Philidor"],
 ["Double-action pedal harp", "i", "str", "FRA", 51.50, -0.12, 1810, "1810", "Sébastien Érard, patented in London"],
 ["Ophicleide", "i", "br", "FRA", 48.86, 2.35, 1817, "1817", "Halary, Paris"],
 ["Double-escapement piano action", "i", "kb", "FRA", 48.87, 2.34, 1821, "1821", "Sébastien Érard, Paris"],
 ["Cornet à pistons", "i", "br", "FRA", 48.85, 2.36, 1828, "c. 1828", "Halary, Paris"],
 ["Harmonium", "i", "fr", "FRA", 48.86, 2.33, 1840, "1840", "Alexandre Debain, Paris"],
 ["Saxhorn family", "i", "br", "FRA", 48.87, 2.36, 1845, "1845", "Adolphe Sax, Paris"],
 ["Ondes Martenot", "i", "el", "FRA", 48.85, 2.34, 1928, "1928", "Maurice Martenot, Paris"],
 ["Schwyzerörgeli", "i", "fr", "SUI", 47.01, 8.65, 1885, "1880s", "Ibach, Schwyz"],
 ["Viennese piano action", "i", "kb", "AUT", 48.20, 16.36, 1794, "1794", "Streicher, Vienna"],
 ["Accordion", "i", "fr", "AUT", 48.20, 16.35, 1829, "1829", "Cyrill Demian's patent, Vienna"],
 ["Vienna horn", "i", "br", "AUT", 48.21, 16.38, 1830, "c. 1830", "Leopold Uhlmann, Vienna"],
 ["Concert cimbalom", "i", "str", "HUN", 47.50, 19.04, 1874, "1874", "Vencel József Schunda, Budapest"],
 ["Modern tárogató", "i", "ww", "HUN", 47.49, 19.05, 1895, "1890s", "Schunda, Budapest"],
 ["Violin", "i", "str", "NIT", 45.13, 10.02, 1550, "c. 1550", "Andrea Amati, Cremona"],
 ["Piano", "i", "kb", "NIT", 43.77, 11.26, 1700, "c. 1700", "Bartolomeo Cristofori, Florence"],
 ["Castelfidardo accordion", "i", "fr", "NIT", 43.46, 13.55, 1863, "1863", "Paolo Soprani"],
 ["Neapolitan mandolin", "i", "str", "MEZ", 40.85, 14.27, 1750, "18th c.", "Vinaccia family, Naples"],
 ["Tamburica ensemble", "i", "str", "CRO", 45.55, 18.69, 1847, "1847", "Pajo Kolarić, Osijek"],
 ["Hydraulis", "i", "kb", "GRE", 31.20, 29.92, -250, "3rd c. BC", "Ctesibius, Alexandria: the first organ"],
 ["Four-course bouzouki", "i", "str", "GRE", 37.98, 23.73, 1955, "1950s", "Manolis Chiotis, Athens"],
 ["Modern classical guitar", "i", "str", "ESP", 37.39, -5.98, 1856, "1850s", "Antonio de Torres, Seville"],
 ["Iron-framed piano", "i", "kb", "USA", 42.36, -71.06, 1825, "1825", "Alpheus Babcock, Boston"],
 ["Overstrung grand", "i", "kb", "USA", 40.71, -74.01, 1859, "1859", "Steinway, New York"],
 ["Autoharp", "i", "str", "USA", 39.95, -75.16, 1882, "1882", "Charles Zimmermann, Philadelphia"],
 ["Sousaphone", "i", "br", "USA", 39.96, -75.17, 1893, "1893", "J. W. Pepper, Philadelphia"],
 ["Bass-drum pedal", "i", "pc", "USA", 41.88, -87.63, 1909, "1909", "Ludwig, Chicago"],
 ["Vibraphone", "i", "pc", "USA", 39.77, -86.16, 1921, "1921", "Leedy, Indianapolis"],
 ["Resonator guitar", "i", "str", "USA", 34.05, -118.24, 1927, "1927", "Dopyera brothers, Los Angeles"],
 ["Electric guitar", "i", "el", "USA", 34.06, -118.25, 1932, "1932", "Rickenbacker 'Frying Pan', Los Angeles"],
 ["Hammond organ", "i", "el", "USA", 41.89, -87.62, 1935, "1935", "Chicago"],
 ["Solid-body guitar and electric bass", "i", "el", "USA", 33.87, -117.92, 1950, "1950–51", "Fender, Fullerton"],
 ["Buchla synthesizer", "i", "el", "USA", 37.77, -122.42, 1963, "1963", "San Francisco"],
 ["Moog synthesizer", "i", "el", "USA", 42.54, -76.66, 1964, "1964", "Trumansburg, New York"],
 ["Electronic sackbut", "i", "el", "CAN", 45.42, -75.70, 1948, "1945–48", "Hugh Le Caine, Ottawa"],
 ["CSIRAC music", "i", "el", "AUS", -33.87, 151.20, 1951, "1951", "Sydney"],
 ["Fairlight CMI sampler", "i", "el", "AUS", -33.88, 151.21, 1979, "1979", "Sydney"],
 ["Byzantine chant", "g", "cho", "GRE", 41.01, 28.98, 400, "from the 4th c.", "Constantinople"],
 ["Gregorian chant", "g", "cho", "FRA", 49.12, 6.18, 754, "8th c.", "Roman chant taken up at Metz under Chrodegang"],
 ["Franco-Flemish polyphony", "g", "cho", "FRA", 50.18, 3.23, 1450, "15th c.", "Cambrai, Dufay's cathedral"],
 ["Lutheran chorale", "g", "cho", "NGR", 51.87, 12.65, 1524, "1524", "Wittenberg, the first Lutheran hymnals"],
 ["Madrigal", "g", "art", "NIT", 41.90, 12.50, 1530, "1530", "first book of madrigals, Rome"],
 ["Anglican choral music", "g", "cho", "ENG", 51.50, -0.14, 1549, "1549", "Book of Common Prayer; Chapel Royal"],
 ["Ballet de cour", "g", "art", "FRA", 48.86, 2.34, 1581, "1581", "Ballet comique de la reine, Paris"],
 ["Sonata", "g", "art", "NIT", 45.44, 12.32, 1597, "1597", "Giovanni Gabrieli, Venice"],
 ["Opera", "g", "art", "NIT", 43.77, 11.25, 1598, "1598–1600", "Florentine Camerata: Dafne, Euridice"],
 ["Oratorio", "g", "art", "NIT", 41.90, 12.48, 1600, "1600", "Cavalieri, Rome"],
 ["Partes singing", "g", "cho", "GAL", 49.84, 24.03, 1620, "17th c.", "Lviv brotherhoods"],
 ["Zarzuela", "g", "art", "ESP", 40.42, -3.70, 1657, "1657", "Madrid, the Zarzuela palace"],
 ["Change ringing", "g", "cho", "ENG", 52.21, 0.12, 1668, "1668", "Tintinnalogia, Cambridge"],
 ["Opera buffa", "g", "art", "MEZ", 40.84, 14.25, 1710, "early 18th c.", "Naples"],
 ["Ballad opera", "g", "song", "ENG", 51.52, -0.12, 1728, "1728", "The Beggar's Opera, London"],
 ["Hasidic nigun", "g", "cho", "ASH", 49.44, 27.42, 1740, "1740s", "Medzhybizh, the Baal Shem Tov's court"],
 ["Classical symphony", "g", "art", "SWA", 49.49, 8.47, 1745, "1740s", "Mannheim court orchestra"],
 ["Lied", "g", "art", "AUT", 48.21, 16.37, 1814, "1814", "Schubert, Gretchen am Spinnrade, Vienna"],
 ["Viennese waltz", "g", "folk", "AUT", 48.20, 16.37, 1825, "1820s", "Lanner and Strauss I, Vienna"],
 ["Grand opéra", "g", "art", "FRA", 48.87, 2.33, 1828, "1828", "La muette de Portici, Paris"],
 ["Fado", "g", "song", "POR", 38.72, -9.14, 1830, "1820s–40s", "Lisbon"],
 ["Polka", "g", "folk", "BOH", 50.08, 14.43, 1835, "1830s", "Bohemia, then Prague's ballrooms"],
 ["Neapolitan song", "g", "song", "MEZ", 40.85, 14.26, 1839, "1839", "Te voglio bene assaje, Naples"],
 ["Flamenco", "g", "folk", "ESP", 37.39, -5.99, 1847, "from 1847", "first cafés cantantes, Seville"],
 ["Sardana", "g", "folk", "ESP", 42.27, 2.96, 1850, "1850s", "Pep Ventura, Figueres"],
 ["Music hall", "g", "song", "ENG", 51.50, -0.11, 1852, "1852", "Canterbury Hall, Lambeth"],
 ["Operetta", "g", "art", "FRA", 48.87, 2.35, 1858, "1858", "Orphée aux enfers, Paris"],
 ["Song festival", "g", "cho", "EST", 58.38, 26.72, 1869, "1869", "Tartu"],
 ["Song festival", "g", "cho", "LAT", 56.95, 24.11, 1873, "1873", "Riga"],
 ["Viennese operetta", "g", "art", "AUT", 48.20, 16.36, 1874, "1874", "Die Fledermaus, Vienna"],
 ["Yiddish theatre song", "g", "song", "ASH", 47.16, 27.59, 1876, "1876", "Avrom Goldfaden, Iași"],
 ["Schrammelmusik", "g", "song", "AUT", 48.22, 16.34, 1878, "1878", "Schrammel brothers, Vienna"],
 ["Chanson réaliste", "g", "song", "FRA", 48.88, 2.34, 1881, "1881", "Le Chat Noir, Montmartre"],
 ["Ragtime", "g", "jazz", "USA", 38.70, -93.23, 1899, "1899", "Maple Leaf Rag, Sedalia"],
 ["Blues", "g", "jazz", "USA", 34.20, -90.57, 1903, "1903", "W. C. Handy hears it in the Mississippi Delta"],
 ["Jazz", "g", "jazz", "USA", 29.95, -90.07, 1910, "c. 1900–1917", "New Orleans"],
 ["Twelve-tone music", "g", "art", "AUT", 48.19, 16.37, 1921, "1921", "Schoenberg, Vienna"],
 ["Rebetiko", "g", "song", "GRE", 37.94, 23.65, 1923, "1920s", "Piraeus, after the refugees from Smyrna"],
 ["Song festival", "g", "cho", "LIT", 54.90, 23.90, 1924, "1924", "Kaunas"],
 ["Schlager", "g", "song", "NGR", 52.51, 13.38, 1925, "1920s", "Berlin"],
 ["Country", "g", "song", "USA", 36.60, -82.19, 1927, "1927", "Bristol sessions, Tennessee–Virginia"],
 ["Cajun recording", "g", "folk", "USA", 30.22, -92.02, 1928, "1928", "Joe Falcon, Louisiana"],
 ["Gypsy jazz", "g", "jazz", "FRA", 48.86, 2.36, 1934, "1934", "Quintette du Hot Club de France, Paris"],
 ["Latin jazz", "g", "jazz", "USA", 40.80, -73.95, 1943, "1943", "Machito's Tanga, New York"],
 ["Bluegrass", "g", "folk", "USA", 36.16, -86.78, 1945, "1945", "Bill Monroe's band at the Grand Ole Opry, Nashville"],
 ["Musique concrète", "g", "elec", "FRA", 48.85, 2.29, 1948, "1948", "Pierre Schaeffer, Paris"],
 ["Elektronische Musik", "g", "elec", "RHI", 50.94, 6.95, 1951, "1951", "WDR studio, Cologne"],
 ["Rock and roll", "g", "rock", "USA", 35.14, -90.04, 1954, "1954", "Sun Records, Memphis"],
 ["Bard song", "g", "song", "RUS", 55.75, 37.60, 1957, "late 1950s", "Moscow"],
 ["Soul and the Motown sound", "g", "hip", "USA", 42.36, -83.08, 1959, "1959", "Motown, Detroit"],
 ["Canzone d'autore", "g", "song", "NIT", 44.41, 8.93, 1960, "1960s", "Genoa school"],
 ["Entechno", "g", "song", "GRE", 37.97, 23.72, 1960, "1960", "Theodorakis's Epitaphios, Athens"],
 ["Chanson québécoise", "g", "song", "QUE", 45.50, -73.57, 1960, "1960s", "Montreal's boîtes à chansons"],
 ["British beat", "g", "rock", "ENG", 53.41, -2.98, 1962, "1962", "Liverpool"],
 ["Minimalism", "g", "art", "USA", 37.77, -122.41, 1964, "1964", "Terry Riley's In C, San Francisco"],
 ["Salsa", "g", "song", "USA", 40.75, -73.99, 1964, "1960s", "Fania Records, New York"],
 ["Krautrock", "g", "rock", "RHI", 50.93, 6.96, 1968, "1968", "Can, Cologne"],
 ["Progressive rock", "g", "rock", "ENG", 51.52, -0.13, 1969, "1969", "London"],
 ["Heavy metal", "g", "rock", "ENG", 52.48, -1.90, 1970, "1970", "Black Sabbath, Birmingham"],
 ["Celtic rock", "g", "rock", "IRL", 53.34, -6.27, 1970, "1970", "Horslips, Dublin"],
 ["Hip hop", "g", "hip", "USA", 40.84, -73.86, 1973, "1973", "The Bronx"],
 ["Pub rock (Oz rock)", "g", "rock", "AUS", -33.86, 151.21, 1973, "1970s", "Sydney"],
 ["Punk", "g", "rock", "USA", 40.73, -73.99, 1974, "1974", "CBGB, New York"],
 ["Disco", "g", "elec", "USA", 40.74, -73.99, 1974, "1970s", "New York"],
 ["Punk", "g", "rock", "ENG", 51.51, -0.15, 1976, "1976", "London"],
 ["Mizrahi music", "g", "song", "ISR", 32.07, 34.78, 1975, "1970s", "Tel Aviv"],
 ["Holy minimalism", "g", "art", "EST", 59.44, 24.75, 1976, "1976", "Arvo Pärt, Tallinn"],
 ["Italo disco", "g", "elec", "NIT", 45.46, 9.19, 1978, "late 1970s", "Milan"],
 ["Synth-pop", "g", "elec", "ENG", 53.38, -1.47, 1978, "1978", "The Human League, Sheffield"],
 ["Dunedin sound", "g", "rock", "NZL", -45.87, 170.50, 1981, "1981", "Flying Nun bands, Dunedin"],
 ["EBM", "g", "elec", "BEL", 50.85, 4.36, 1981, "1981", "Front 242, Brussels"],
 ["House", "g", "elec", "USA", 41.88, -87.64, 1984, "1984", "Chicago"],
 ["Techno", "g", "elec", "USA", 42.33, -83.05, 1985, "1985–88", "Detroit"],
 ["Grunge", "g", "rock", "USA", 47.61, -122.33, 1986, "1986", "Seattle"],
 ["Disco polo", "g", "song", "POL", 53.13, 23.16, 1989, "late 1980s", "Podlasie, Białystok"],
 ["Turbo-folk", "g", "song", "SRB", 44.79, 20.45, 1990, "c. 1990", "Belgrade"],
 ["Techno in Berlin", "g", "elec", "NGR", 52.51, 13.42, 1991, "1991", "Tresor, Berlin"],
 ["Black metal", "g", "rock", "NOR", 59.91, 10.75, 1991, "early 1990s", "Oslo"],
 ["Trance", "g", "elec", "RHI", 50.11, 8.68, 1992, "early 1990s", "Frankfurt"],
 ["Gabber", "g", "elec", "NLD", 51.92, 4.48, 1992, "early 1990s", "Rotterdam"],
 ["Melodic death metal", "g", "rock", "SWE", 57.71, 11.97, 1993, "early 1990s", "Gothenburg"],
 ["Drum and bass", "g", "elec", "ENG", 51.53, -0.07, 1993, "early 1990s", "London"],
 ["French house", "g", "elec", "FRA", 48.86, 2.37, 1996, "mid-1990s", "Paris"],
 ["Grime", "g", "hip", "ENG", 51.53, -0.02, 2002, "early 2000s", "Bow, east London"],
]
OFFMAP = [
 ["Charango", "i", "str", "IBA", "18th c.", "Andes"], ["Marimba", "i", "pc", "IBA", "", "Guatemala and Chiapas, from African antecedents"],
 ["Cajón", "i", "pc", "IBA", "18th–19th c.", "Peru"], ["Tango", "g", "song", "IBA", "1880s", "Buenos Aires and Montevideo"],
 ["Samba", "g", "song", "IBA", "1917", "Pelo Telefone, Rio de Janeiro"], ["Bossa nova", "g", "jazz", "IBA", "1958", "Rio de Janeiro"],
 ["Son cubano", "g", "song", "IBA", "1910s", "eastern Cuba"], ["Reggaeton", "g", "hip", "IBA", "1990s", "Panama and Puerto Rico"],
 ["Steel guitar", "i", "str", "USA", "1889", "Joseph Kekuku, Hawaii"]]
DIFFUSE = ["Gaelic harp", "Uilleann pipes", "Great Highland bagpipe", "Vihuela", "Portuguese guitar", "Cavaquinho",
 "Five-string banjo", "Drum kit", "Znamenny chant", "Klapa", "Mazurka", "Polonaise", "Csárdás", "Verbunkos", "Doina",
 "Sevdalinka", "Klezmer", "Yodel", "Kolo", "Spirituals"]

ALPHA = 1.0  # Dirichlet pseudo-count: one instrument's (one genre's) worth of the pooled profile

_st = importlib.util.spec_from_file_location("mt", os.path.join(HERE, "music_types.py")); _mt = importlib.util.module_from_spec(_st); _st.loader.exec_module(_mt)
TYPES = {n for n, v in _mt.TREE.items() if v[1] == 0}
practice = {}
for r, (ins, gs) in R.items():
    ic = {}
    for i in ins:
        if i[2] == "d" and i[0] in LANDMARK_ONLY: continue
        ic[i[1]] = ic.get(i[1], 0) + 1
    gc = {}
    for g in gs: gc[gen(g)[0]] = gc.get(gen(g)[0], 0) + 1 / credit[g]
    tc = {}
    for i in ins:
        if i[2] == "d" and i[0] in LANDMARK_ONLY: continue
        ty = _mt.type_of(i[0]); assert ty in TYPES, (r, i[0], ty)
        tc[ty] = tc.get(ty, 0) + 1
    practice[r] = (ic, gc, tc)
def pooled(idx, fams):
    tot = {k: 0.0 for k in fams}
    for r in R:
        c = practice[r][idx]; n = sum(c.values())
        for k in fams: tot[k] += (c.get(k, 0) / n if n else 0) / len(R)
    return tot
def shrink(c, prior, a=ALPHA):
    n = sum(c.values())
    return {k: (c.get(k, 0) + a * prior[k]) / (n + a) for k in prior}, n
PI_I, PI_G = pooled(0, IFAM), pooled(1, GFAM)
PI_T = pooled(2, {k: 1 for k in sorted(TYPES)})
mus = {}
for r in R:
    si, ni = shrink(practice[r][0], PI_I); sg, ng = shrink(practice[r][1], PI_G)
    mus[r] = {"i": {k: round(v, 4) for k, v in si.items()}, "g": {k: round(v, 4) for k, v in sg.items()},
              "ri": practice[r][0], "rt": practice[r][2], "rg": {k: round(v, 4) for k, v in practice[r][1].items()}, "ni": ni, "ng": round(ng, 2)}
for k in out["regions"]:
    out["regions"][k]["instruments"] = [{"name": i[0], "family": i[1], "role": i[2], "note": i[3]} for i in R[k][0]]
    out["regions"][k]["sources"] = SOURCES[k]
    out["regions"][k]["developed"] = sum(1 for i in R[k][0] if i[2] == "d")
    for i in out["regions"][k]["instruments"]:
        if i["role"] == "d" and i["name"] not in LANDMARK_ONLY: i["role"] = "dt"
    out["regions"][k]["instrument_shares"] = mus[k]["i"]; out["regions"][k]["genre_shares"] = mus[k]["g"]
out["method"] = {"alpha": ALPHA, "pooled_instruments": PI_I, "pooled_genres": PI_G}
out["landmarks"] = [dict(zip(["n", "k", "f", "u", "lat", "lon", "y", "d", "t"], l)) for l in LM]
out["offmap"] = [dict(zip(["n", "k", "f", "u", "d", "t"], l)) for l in OFFMAP]
out["diffuse"] = DIFFUSE
json.dump(out, open(os.path.join(HERE, "music.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump({"alpha": ALPHA, "PI": PI_I, "PG": PI_G, "PT": PI_T, "TTREE": _mt.TREE, "R": mus}, open(os.path.join(HERE, "music_shares.json"), "w", encoding="utf-8"), separators=(",", ":"))
print("played instruments per region: min", min(mus[r]["ni"] for r in R), "median", sorted(mus[r]["ni"] for r in R)[27], "max", max(mus[r]["ni"] for r in R), "total", sum(mus[r]["ni"] for r in R))
print("landmarks", len(LM), "instruments", sum(1 for l in LM if l[1] == "i"), "genres", sum(1 for l in LM if l[1] == "g"),
      "| thin (n<3 played instruments):", [r for r in R if mus[r]["ni"] < 3])
