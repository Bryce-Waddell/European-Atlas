# Music facets for the Atlas: draft dataset for review (not yet in the clustering).
# Run: py -I research/music_data.py  -> writes research/music.json
# Roles: "d" = developed (invented or decisively engineered in the region, dated);
#        "t" = traditional (an emblematic instrument of the region's own music).
# German regions assumed by modern Land: NGR = north and east incl. Berlin, Saxony, Thuringia;
#   RHI = North Rhine-Westphalia, Rhineland-Palatinate, Saarland, Hesse; SWA = Baden-Württemberg; BAV = Bavaria.
# Italy assumed: NIT = north and centre to Lazio; MEZ = the south; SAR = Sardinia.
import json, os

IFAM = {  # instrument families, the broad ones developed across the globe
 "str": "Strings", "ww": "Woodwinds", "br": "Brass", "fr": "Free reeds",
 "kb": "Keyboards", "pc": "Percussion", "el": "Electric & electronic"}
GFAM = {
 "art": "Art music", "cho": "Choral & sacred", "folk": "Folk & dance", "song": "Popular song",
 "jazz": "Jazz & blues", "rock": "Rock & metal", "elec": "Electronic & dance", "hip": "Hip hop, soul & R&B"}

# genre: (family, core instrumentation by family, where and when it formed)
G = {
 "Gregorian chant": ("cho", [], "Carolingian Francia, 8th-9th c."),
 "Byzantine chant": ("cho", [], "Constantinople, from the 4th c."),
 "Znamenny chant": ("cho", [], "Muscovy, 11th-17th c."),
 "Partes singing": ("cho", [], "Kyiv and western Ukraine, 17th c."),
 "Franco-Flemish polyphony": ("cho", [], "Low Countries and northern France, 15th-16th c."),
 "Lutheran chorale": ("cho", ["kb"], "Wittenberg, 1524"),
 "Anglican choral music": ("cho", ["kb"], "England, 16th c."),
 "Change ringing": ("cho", ["pc"], "England, 17th c."),
 "Spirituals and gospel": ("cho", ["kb"], "United States, 19th-20th c."),
 "Song-festival choral tradition": ("cho", [], "Estonia 1869, Latvia 1873, Lithuania 1924"),
 "Klapa": ("cho", [], "Dalmatia, 19th c."),
 "Holy minimalism (tintinnabuli)": ("art", ["str", "kb"], "Tallinn, Arvo Pärt, 1976"),
 "Madrigal": ("art", [], "Italy, 16th c."),
 "Opera": ("art", ["str", "ww", "br", "kb"], "Florence, 1597-1600"),
 "Oratorio": ("art", ["str", "kb"], "Rome, c. 1600"),
 "Concerto and sonata": ("art", ["str", "kb"], "Venice and Bologna, 17th c."),
 "Opera buffa": ("art", ["str", "ww"], "Naples, early 18th c."),
 "Ballet and tragédie en musique": ("art", ["str", "ww"], "French court, 17th c."),
 "Classical symphony": ("art", ["str", "ww", "br", "pc"], "Mannheim, Vienna and Milan, 18th c."),
 "Lied": ("art", ["kb"], "Vienna, early 19th c."),
 "Grand opéra": ("art", ["str", "ww", "br", "pc"], "Paris, 1828"),
 "Operetta": ("art", ["str", "ww", "br"], "Paris 1850s, Vienna 1870s"),
 "Zarzuela": ("art", ["str", "ww"], "Madrid, 17th c."),
 "Twelve-tone music": ("art", ["str", "ww", "kb"], "Vienna, 1921"),
 "Musique concrète": ("elec", ["el"], "Paris, 1948"),
 "Elektronische Musik": ("elec", ["el"], "Cologne WDR studio, 1951"),
 "Minimalism": ("art", ["kb", "pc", "str"], "United States, 1960s"),
 "Ballad opera and music hall": ("song", ["str", "kb"], "London, 1728; music hall 1850s"),
 "Brass band": ("folk", ["br", "pc"], "Northern England, 19th c."),
 "Musical theatre": ("song", ["str", "br", "ww", "kb"], "London and New York, 19th-20th c."),
 "Jazz": ("jazz", ["br", "ww", "pc", "kb", "str"], "New Orleans, c. 1900-1917"),
 "Blues": ("jazz", ["str", "fr"], "Mississippi Delta, c. 1900"),
 "Ragtime": ("jazz", ["kb"], "Missouri, 1890s"),
 "Gypsy jazz": ("jazz", ["str"], "Paris, 1934"),
 "Bossa nova": ("jazz", ["str", "pc", "kb"], "Rio de Janeiro, 1958"),
 "Latin jazz": ("jazz", ["br", "ww", "pc", "kb"], "New York and Havana, 1940s"),
 "Country": ("song", ["str"], "Appalachia and Nashville, 1920s"),
 "Bluegrass": ("folk", ["str"], "Kentucky, 1940s"),
 "Cajun and zydeco": ("folk", ["fr", "str"], "Louisiana, 19th-20th c."),
 "Rock and roll": ("rock", ["el", "pc", "kb"], "United States, 1950s"),
 "British beat and rock": ("rock", ["el", "pc"], "Liverpool and London, 1960s"),
 "Heavy metal": ("rock", ["el", "pc"], "Birmingham, 1968-70"),
 "Punk": ("rock", ["el", "pc"], "New York and London, 1974-77"),
 "Progressive rock": ("rock", ["el", "kb", "pc"], "England, late 1960s"),
 "Krautrock": ("rock", ["el", "pc"], "Cologne, Düsseldorf and Berlin, 1968-74"),
 "Celtic rock": ("rock", ["el", "ww", "str"], "Dublin and Scotland, early 1970s"),
 "Black metal": ("rock", ["el", "pc"], "Norway, early 1990s"),
 "Melodic death metal": ("rock", ["el", "pc"], "Gothenburg, early 1990s"),
 "Grunge": ("rock", ["el", "pc"], "Seattle, late 1980s"),
 "Pub rock (Oz rock)": ("rock", ["el", "pc"], "Australia, 1970s"),
 "Dunedin sound": ("rock", ["el", "pc"], "Dunedin, 1980s"),
 "Soul, funk and R&B": ("hip", ["el", "br", "pc", "kb"], "United States, 1940s-60s"),
 "Hip hop": ("hip", ["el", "pc"], "The Bronx, 1973"),
 "Grime": ("hip", ["el"], "London, early 2000s"),
 "Reggaeton": ("hip", ["el", "pc"], "Panama and Puerto Rico, 1990s"),
 "Disco": ("elec", ["el", "pc", "str"], "New York and Philadelphia, 1970s"),
 "House": ("elec", ["el"], "Chicago, 1984"),
 "Techno": ("elec", ["el"], "Detroit 1985-88; Berlin after 1989"),
 "Synth-pop": ("elec", ["el"], "England, late 1970s"),
 "Italo disco": ("elec", ["el"], "Northern Italy, late 1970s"),
 "EBM and new beat": ("elec", ["el"], "Belgium, 1980s"),
 "Trance": ("elec", ["el"], "Frankfurt, early 1990s"),
 "Gabber": ("elec", ["el"], "Rotterdam, early 1990s"),
 "Drum and bass": ("elec", ["el"], "London, early 1990s"),
 "French house": ("elec", ["el"], "Paris, mid-1990s"),
 "Chanson": ("song", ["str", "fr", "kb"], "Paris, 19th-20th c."),
 "Bal-musette": ("song", ["fr"], "Paris, 1880s-1930s"),
 "Chanson québécoise": ("song", ["str"], "Québec, 1960s"),
 "Schlager": ("song", ["br", "str", "kb"], "Germany, 1920s-50s"),
 "Schrammelmusik and Wienerlied": ("song", ["str", "fr"], "Vienna, 1878"),
 "Fado": ("song", ["str"], "Lisbon, 1820s"),
 "Rebetiko and laïko": ("song", ["str"], "Piraeus and Athens, 1920s-50s"),
 "Entechno": ("song", ["str", "kb"], "Greece, 1960s"),
 "Tango": ("song", ["fr", "str", "kb"], "Buenos Aires and Montevideo, 1880s"),
 "Samba": ("song", ["pc", "str"], "Rio de Janeiro, 1910s"),
 "Son, bolero and salsa": ("song", ["pc", "str", "br"], "Cuba 1880s-1920s; salsa New York 1960s"),
 "Cumbia": ("folk", ["pc", "ww", "fr"], "Colombian Caribbean coast"),
 "Mariachi": ("folk", ["str", "br"], "Jalisco, 19th c."),
 "Neapolitan song": ("song", ["str"], "Naples, 19th c."),
 "Canzone d'autore": ("song", ["str", "kb"], "Genoa, 1960s"),
 "Sevdalinka": ("song", ["str", "fr"], "Bosnia, Ottoman period"),
 "Turbo-folk": ("song", ["el", "fr"], "Serbia, 1980s-90s"),
 "Chalga": ("song", ["el", "ww"], "Bulgaria, 1990s"),
 "Manele": ("song", ["el", "fr"], "Romania, 1990s"),
 "Magyar nóta": ("song", ["str"], "Hungary, 19th c."),
 "Russian romance and bard song": ("song", ["str"], "Russia, 19th c.; bard song 1950s-60s"),
 "Finnish tango": ("song", ["fr", "str"], "Finland, 1940s-60s"),
 "Disco polo": ("song", ["el"], "Poland, 1990s"),
 "Levenslied": ("song", ["fr", "kb"], "Netherlands, 20th c."),
 "Yiddish theatre song": ("song", ["str", "ww"], "Iași 1876, then New York"),
 "Mizrahi music": ("song", ["str", "el"], "Israel, 1970s"),
 "Songs of the Land of Israel": ("song", ["str", "fr"], "Mandatory Palestine and Israel, 1920s-60s"),
 "Klezmer": ("folk", ["ww", "str", "fr", "br"], "Ashkenazi eastern Europe, 16th-19th c."),
 "Hasidic nigun and hazzanut": ("cho", [], "Ashkenazi eastern Europe, 18th c."),
}

# region: (instruments [name, family, role, note], genres [names; a genre named by several regions is split between them])
R = {
"ISL": ([["Langspil", "str", "t", "bowed box zither"], ["Fiðla", "str", "t", "bowed zither"]],
        ["Rímur and tvísöngur"]),
"NOR": ([["Hardanger fiddle", "str", "d", "Hardanger, earliest dated 1651"], ["Langeleik", "str", "t", ""], ["Seljefløyte", "ww", "t", "willow overtone flute"], ["Bukkehorn and birch lur", "br", "t", "lip-vibrated horns"]],
        ["Slått and kveding", "Black metal"]),
"SWE": ([["Nyckelharpa", "str", "d", "keyed fiddle, medieval Uppland"], ["Swedish bagpipe", "ww", "t", ""], ["Hummel", "str", "t", ""], ["Birch lur", "br", "t", ""]],
        ["Polska", "Melodic death metal"]),
"FIN": ([["Kantele", "str", "t", "box zither"], ["Jouhikko", "str", "t", "bowed lyre"], ["Accordion (harmonikka)", "fr", "t", ""]],
        ["Runo song", "Finnish tango"]),
"DEN": ([["Bronze-Age lur", "br", "d", "Nordic Bronze Age, most finds in Denmark"], ["Fiddle", "str", "t", ""], ["Accordion", "fr", "t", ""], ["Clarinet (spillemand bands)", "ww", "t", ""]],
        ["Danish fiddle dance"]),
"EST": ([["Kannel", "str", "t", ""], ["Torupill", "ww", "t", "bagpipe"], ["Hiiu kannel", "str", "t", "bowed lyre"]],
        ["Regilaul", "Song-festival choral tradition", "Holy minimalism (tintinnabuli)"]),
"LAT": ([["Kokle", "str", "t", ""], ["Dūdas", "ww", "t", "bagpipe"], ["Trīdeksnis", "pc", "t", "rattle staff"]],
        ["Dainas", "Song-festival choral tradition"]),
"LIT": ([["Kanklės", "str", "t", ""], ["Skudučiai", "ww", "t", "panpipes"], ["Birbynė", "ww", "t", "reed pipe"], ["Daudytė", "br", "t", "wooden trumpet"]],
        ["Sutartinės", "Song-festival choral tradition"]),
"RUS": ([["Balalaika (concert form)", "str", "d", "Vasily Andreyev, 1880s"], ["Domra and gusli", "str", "t", ""], ["Garmon", "fr", "d", "Tula, 1830s"], ["Bayan", "fr", "d", "Pyotr Sterligov, 1907"], ["Russian horn band", "br", "d", "St Petersburg, 1751"], ["Theremin", "el", "d", "Léon Theremin, Petrograd, 1920"], ["ANS synthesizer", "el", "d", "Yevgeny Murzin, Moscow, 1958"], ["Zhaleika", "ww", "t", "hornpipe"], ["Lozhki", "pc", "t", "spoons"]],
        ["Znamenny chant", "Russian romance and bard song", "Chastushka"]),
"BLR": ([["Tsymbaly", "str", "t", "hammered dulcimer"], ["Duda", "ww", "t", "bagpipe"], ["Lira", "str", "t", "hurdy-gurdy"], ["Zhaleika", "ww", "t", ""]],
        ["Belarusian calendar songs"]),
"POL": ([["Suka biłgorajska", "str", "t", "fiddle played with the fingernail"], ["Dudy and kozioł", "ww", "t", "bagpipes"], ["Basy", "str", "t", "folk bass"], ["Cymbały", "str", "t", ""]],
        ["Mazurka", "Polonaise", "Krakowiak and oberek", "Disco polo"]),
"IRL": ([["Gaelic harp", "str", "d", "wire-strung, medieval"], ["Uilleann pipes", "ww", "d", "bellows-blown, early 18th c."], ["Keyed bugle", "br", "d", "Joseph Haliday, Cavan Militia, patent 1810; rights sold to a Dublin maker"], ["Bodhrán", "pc", "t", ""], ["Fiddle", "str", "t", ""], ["Concertina", "fr", "t", "Clare"]],
        ["Sean-nós", "Irish dance music", "Celtic rock"]),
"ULS": ([["Lambeg drum", "pc", "d", "Ulster, 18th-19th c."], ["Fife", "ww", "t", ""], ["Fiddle", "str", "t", ""], ["Accordion band", "fr", "t", ""]],
        ["Marching-band music", "Ulster song"]),
"SCO": ([["Great Highland bagpipe", "ww", "d", "Highlands, 15th-18th c."], ["Clàrsach", "str", "t", "harp"], ["Fiddle", "str", "t", ""], ["Border pipes", "ww", "t", ""]],
        ["Pibroch", "Strathspey and reel", "Celtic rock"]),
"ENG": ([["English concertina", "fr", "d", "Charles Wheatstone, London, 1829"], ["Tin whistle (mass-made)", "ww", "d", "Robert Clarke, Manchester, 1843"], ["English grand action", "kb", "d", "Backers and Broadwood, London, 1770s"], ["Handbells", "pc", "t", ""], ["Welsh triple harp and crwth", "str", "t", "Wales"], ["Northumbrian smallpipes", "ww", "t", ""], ["Vox and Marshall amplifiers", "el", "d", "Dartford 1958, London 1962"], ["Mellotron", "el", "d", "Birmingham, 1963"], ["Ferranti Mark 1 music", "el", "d", "Manchester, 1951"]],
        ["Anglican choral music", "Change ringing", "Ballad opera and music hall", "Brass band", "Musical theatre", "British beat and rock", "Heavy metal", "Punk", "Progressive rock", "Synth-pop", "Drum and bass", "Grime"]),
"NLD": ([["Tuned carillon", "pc", "d", "Hemony brothers, Zutphen, 1644"], ["Street organ", "kb", "t", ""], ["Accordion", "fr", "t", ""]],
        ["Franco-Flemish polyphony", "Levenslied", "Gabber"]),
"BEL": ([["Saxophone", "ww", "d", "Adolphe Sax, Brussels, c. 1840 (patented Paris 1846)"], ["Carillon", "pc", "t", "Mechelen school"], ["Accordion", "fr", "t", ""], ["Doedelzak", "ww", "t", "Flemish bagpipe"], ["Draailier", "str", "t", "hurdy-gurdy"]],
        ["Franco-Flemish polyphony", "EBM and new beat"]),
"LUX": ([["Wind band (Harmonie)", "br", "t", ""], ["Fiddle", "str", "t", ""]],
        ["Echternach procession music"]),
"NGR": ([["Valve for brass", "br", "d", "Stölzel and Blühmel, Silesia and Berlin, 1814-18"], ["Tuba", "br", "d", "Wieprecht and Moritz, Berlin, 1835"], ["German concertina", "fr", "d", "Carl Friedrich Uhlig, Chemnitz, 1834"], ["Mouth organ (Aura)", "fr", "d", "Christian Buschmann, Berlin, 1821"], ["Baroque organ", "kb", "d", "Schnitger (Hamburg) and Silbermann (Saxony)"], ["Markneukirchen violins", "str", "t", "Vogtland"], ["Posaunenchor", "br", "t", "Protestant church brass choir"], ["Trautonium", "el", "d", "Friedrich Trautwein, Berlin, 1930"], ["Dresden pedal timpani", "pc", "d", "Carl Pittrich, 1881"]],
        ["Lutheran chorale", "Schlager", "Krautrock", "Techno"]),
"RHI": ([["Bandoneon", "fr", "d", "Krefeld, 1840s; Heinrich Band named it, invention disputed"], ["Heckelphone", "ww", "d", "Heckel, Biebrich, 1904"], ["WDR electronic studio", "el", "d", "Cologne, 1951"], ["Schalmei band", "ww", "t", "Rhineland and Ruhr"], ["Carnival brass", "br", "t", "Cologne and Mainz Karneval"], ["Accordion", "fr", "t", ""]],
        ["Elektronische Musik", "Krautrock", "Trance"]),
"SWA": ([["Harmonica (mass-made)", "fr", "d", "Matthias Hohner, Trossingen, 1857"], ["Clavinet and Pianet", "el", "d", "Hohner, Trossingen, 1960s"], ["Hohner accordion", "fr", "d", "Trossingen"], ["Black Forest orchestrion", "kb", "t", "mechanical organ, 19th c."], ["Blasmusik", "br", "t", "brass band"], ["Harmonica clubs", "fr", "t", "Swabia"]],
        ["Classical symphony", "Swabian folk song"]),
"BAV": ([["Clarinet", "ww", "d", "J. C. Denner, Nuremberg, c. 1700"], ["Boehm flute", "ww", "d", "Theobald Boehm, Munich, 1832-47"], ["Fortepiano action", "kb", "d", "J. A. Stein, Augsburg, 1770s"], ["Concert zither", "str", "t", ""], ["Blasmusik", "br", "t", "brass band"]],
        ["Ländler and Schuhplattler", "Yodel"]),
"BOH": ([["Červený chromatic brass", "br", "d", "Hradec Králové, from 1842"], ["Czech bagpipe (dudy)", "ww", "t", ""], ["Cimbál", "str", "t", "Moravia"]],
        ["Polka", "Dechovka (brass-band music)"]),
"SLK": ([["Fujara", "ww", "t", "overtone flute"], ["Koncovka", "ww", "t", ""], ["Gajdy", "ww", "t", "bagpipe"], ["Cimbal", "str", "t", ""]],
        ["Slovak folk song"]),
"GAL": ([["Trembita", "br", "t", "Hutsul alphorn"], ["Tsymbaly", "str", "t", ""], ["Sopilka", "ww", "t", ""], ["Drymba", "pc", "t", "jaw harp"]],
        ["Kolomyika", "Partes singing"]),
"UKR": ([["Bandura", "str", "t", ""], ["Kobza", "str", "t", ""], ["Lira", "str", "t", "hurdy-gurdy"], ["Sopilka", "ww", "t", ""], ["Buhai", "pc", "t", "friction drum"]],
        ["Duma", "Hopak", "Partes singing"]),
"FRA": ([["Oboe", "ww", "d", "French court, c. 1657"], ["Ophicleide and cornet", "br", "d", "Halary, Paris, 1817-28"], ["Saxhorn family", "br", "d", "Adolphe Sax, Paris, 1845"], ["Harmonium", "fr", "d", "Alexandre Debain, Paris, 1840"], ["Double-escapement piano action", "kb", "d", "Sébastien Érard, 1821"], ["Double-action pedal harp", "str", "d", "Érard, 1810"], ["Ondes Martenot", "el", "d", "Maurice Martenot, Paris, 1928"], ["Hurdy-gurdy", "str", "t", ""], ["Cabrette and musette", "ww", "t", "bagpipes"], ["Musette accordion", "fr", "t", ""], ["Biniou and bombarde", "ww", "t", "Brittany"]],
        ["Gregorian chant", "Franco-Flemish polyphony", "Ballet and tragédie en musique", "Grand opéra", "Operetta", "Chanson", "Bal-musette", "Gypsy jazz", "Musique concrète", "French house"]),
"SUI": ([["Alphorn", "br", "t", ""], ["Schwyzerörgeli", "fr", "d", "central Switzerland, 1880s"], ["Hackbrett", "str", "t", "Appenzell"], ["Basel drum", "pc", "t", ""]],
        ["Yodel", "Ländlermusik"]),
"AUT": ([["Accordion", "fr", "d", "Cyrill Demian, Vienna, patent 1829"], ["Viennese piano action", "kb", "d", "Stein and Streicher, Vienna"], ["Vienna horn", "br", "d", "Leopold Uhlmann, Vienna, 1830"], ["Contraguitar", "str", "d", "Vienna, 19th c."], ["Steirische Harmonika", "fr", "t", ""], ["Zither", "str", "t", ""]],
        ["Classical symphony", "Lied", "Operetta", "Viennese waltz", "Schrammelmusik and Wienerlied", "Twelve-tone music", "Yodel"]),
"HUN": ([["Concert cimbalom", "str", "d", "Vencel József Schunda, Budapest, 1874"], ["Modern tárogató", "ww", "d", "Schunda, 1890s"], ["Tekerőlant", "str", "t", "hurdy-gurdy"], ["Duda", "ww", "t", "bagpipe"], ["Citera", "str", "t", "zither"]],
        ["Verbunkos", "Csárdás", "Magyar nóta"]),
"ROM": ([["Nai", "ww", "t", "panpipes"], ["Cobza", "str", "t", "lute"], ["Țambal", "str", "t", "cimbalom"], ["Bucium", "br", "t", "alphorn"], ["Cimpoi", "ww", "t", "bagpipe"], ["Taragot", "ww", "t", ""]],
        ["Doina", "Hora", "Lăutărească music", "Manele"]),
"MOL": ([["Nai", "ww", "t", ""], ["Cobza", "str", "t", ""], ["Țambal", "str", "t", ""], ["Fluier", "ww", "t", ""], ["Cimpoi", "ww", "t", ""]],
        ["Doina", "Hora", "Lăutărească music"]),
"POR": ([["Portuguese guitar", "str", "d", "from the English guitar, 19th c."], ["Cavaquinho (ancestor of the ukulele)", "str", "d", "Minho; to Hawaii from Madeira, 1879"], ["Viola braguesa", "str", "t", ""], ["Adufe", "pc", "t", "frame drum"], ["Gaita-de-fole", "ww", "t", "bagpipe"]],
        ["Fado", "Cante alentejano"]),
"ESP": ([["Vihuela", "str", "d", "16th c."], ["Modern classical guitar", "str", "d", "Antonio de Torres, Seville and Almería, 1850s"], ["Castanets", "pc", "t", ""], ["Gaita gallega", "ww", "t", "bagpipe"], ["Txalaparta", "pc", "t", "Basque"], ["Bandurria", "str", "t", ""]],
        ["Mozarabic chant", "Zarzuela", "Flamenco", "Jota", "Sardana"]),
"NIT": ([["Violin family", "str", "d", "Andrea Amati, Cremona, c. 1550"], ["Piano", "kb", "d", "Bartolomeo Cristofori, Florence, c. 1700"], ["Castelfidardo accordion", "fr", "d", "Paolo Soprani, 1863"], ["Mandolin (Lombard)", "str", "t", ""]],
        ["Madrigal", "Opera", "Oratorio", "Concerto and sonata", "Classical symphony", "Canzone d'autore", "Italo disco"]),
"MEZ": ([["Neapolitan mandolin", "str", "d", "Vinaccia family, Naples, 18th c."], ["Zampogna", "ww", "t", "bagpipe"], ["Ciaramella", "ww", "t", "shawm"], ["Tammorra", "pc", "t", "frame drum"]],
        ["Opera buffa", "Neapolitan song", "Tarantella and pizzica"]),
"SAR": ([["Launeddas", "ww", "t", "triple clarinet"], ["Organetto", "fr", "t", ""], ["Tumbarinu", "pc", "t", "drum"]],
        ["Canto a tenore", "Ballu tundu", "Cantu a chiterra"]),
"SLO": ([["Diatonic accordion (frajtonarica)", "fr", "t", ""], ["Cimbalom", "str", "t", "Prekmurje"], ["Trstenke", "ww", "t", "panpipes"], ["Brass", "br", "t", ""]],
        ["Oberkrainer polka", "Slovene folk song"]),
"CRO": ([["Tamburica ensemble", "str", "d", "Pajo Kolarić, Osijek, 1847"], ["Lijerica", "str", "t", "bowed, Dubrovnik"], ["Sopile", "ww", "t", "shawm, Istria"]],
        ["Klapa", "Ojkanje and Istrian two-part singing", "Tamburica music"]),
"BOS": ([["Šargija and saz", "str", "t", "long-neck lutes"], ["Gusle", "str", "t", "bowed, epic"], ["Def", "pc", "t", "frame drum"]],
        ["Sevdalinka", "Ganga", "Gusle epic"]),
"SRB": ([["Gusle", "str", "t", ""], ["Frula", "ww", "t", "flute"], ["Gajde", "ww", "t", "bagpipe"], ["Truba", "br", "t", "brass band"], ["Tapan", "pc", "t", "drum"]],
        ["Kolo", "Guča brass", "Gusle epic", "Turbo-folk"]),
"MNE": ([["Gusle", "str", "t", ""], ["Diple", "ww", "t", "double pipe"]],
        ["Gusle epic", "Oro"]),
"MAC": ([["Kaval", "ww", "t", ""], ["Gajda", "ww", "t", ""], ["Zurla", "ww", "t", "shawm"], ["Tapan", "pc", "t", ""], ["Tambura", "str", "t", ""]],
        ["Oro and teškoto", "Čalgija", "Romani brass"]),
"ALB": ([["Çifteli", "str", "t", "two-string lute"], ["Lahuta", "str", "t", "bowed, epic"], ["Zurna", "ww", "t", ""], ["Def", "pc", "t", ""]],
        ["Iso-polyphony", "Epic of the frontier warriors", "Albanian urban song"]),
"BUL": ([["Gadulka", "str", "t", "bowed"], ["Kaval", "ww", "t", ""], ["Gaida", "ww", "t", "bagpipe"], ["Tambura", "str", "t", ""], ["Tapan", "pc", "t", ""]],
        ["Shop diaphony", "Horo and rachenitsa", "Wedding music", "Chalga"]),
"GRE": ([["Bouzouki (four-course)", "str", "d", "Manolis Chiotis, 1950s"], ["Cretan lyra", "str", "t", "bowed"], ["Laouto and santouri", "str", "t", ""], ["Klarino", "ww", "t", "clarinet"], ["Tsampouna", "ww", "t", "bagpipe"], ["Daouli", "pc", "t", "drum"], ["Hydraulis", "kb", "d", "Ctesibius, Alexandria, 3rd c. BC: the first organ"]],
        ["Byzantine chant", "Rebetiko and laïko", "Entechno", "Syrtos and kalamatianos"]),
"USA": ([["Five-string banjo", "str", "d", "from West African antecedents, 1830s"], ["Steel and resonator guitar", "str", "d", "Hawaii 1889; Los Angeles 1927"], ["Electric guitar and bass", "el", "d", "Rickenbacker 1932, Fender 1950-51, Gibson 1952"], ["Hammond organ", "el", "d", "Chicago, 1935"], ["Moog and Buchla synthesizers", "el", "d", "New York and San Francisco, 1963-64"], ["Drum kit", "pc", "d", "New Orleans and Chicago, 1900s; Ludwig pedal 1909"], ["Vibraphone", "pc", "d", "Leedy, Indianapolis, 1921"], ["Sousaphone", "br", "d", "Philadelphia, 1893"], ["Iron-framed overstrung piano", "kb", "d", "Babcock 1825; Steinway 1859"], ["Autoharp", "str", "d", "Philadelphia, 1882"], ["Blues harmonica", "fr", "t", "the German mouth organ, taken up in the Delta"]],
        ["Spirituals and gospel", "Minimalism", "Musical theatre", "Jazz", "Blues", "Ragtime", "Latin jazz", "Country", "Bluegrass", "Cajun and zydeco", "Rock and roll", "Punk", "Grunge", "Soul, funk and R&B", "Hip hop", "Disco", "House", "Techno", "Son, bolero and salsa"]),
"CAN": ([["Electronic sackbut", "el", "d", "Hugh Le Caine, Ottawa, 1945-48"], ["Fiddle", "str", "t", "Cape Breton"], ["Button accordion", "fr", "t", "Newfoundland"]],
        ["Cape Breton fiddling", "Newfoundland song"]),
"QUE": ([["Violon (fiddle)", "str", "t", ""], ["Button accordion", "fr", "t", ""], ["Cuillères and podorythmie", "pc", "t", "spoons and foot percussion"]],
        ["Québécois reels and chanson à répondre", "Chanson québécoise"]),
"AUS": ([["Fairlight CMI", "el", "d", "Sydney, 1979: the first commercial sampler"], ["CSIRAC music", "el", "d", "Sydney, 1951"], ["Didgeridoo", "br", "t", "Arnhem Land; Aboriginal, lip-vibrated"], ["Lagerphone", "pc", "t", "bush band"]],
        ["Bush ballad", "Pub rock (Oz rock)"]),
"NZL": ([["Taonga pūoro", "ww", "t", "Māori flutes and trumpets"], ["Guitar", "str", "t", ""]],
        ["Kapa haka", "Dunedin sound"]),
"ISR": ([["Shofar", "br", "t", "ritual ram's horn"], ["Oud", "str", "t", ""], ["Darbuka", "pc", "t", ""]],
        ["Songs of the Land of Israel", "Mizrahi music", "Israeli folk dance"]),
"IBA": ([["Charango", "str", "d", "Andes, 18th c."], ["Marimba", "pc", "d", "Guatemala and Chiapas, from African antecedents"], ["Cajón", "pc", "d", "Peru, 18th-19th c."], ["Mariachi vihuela and guitarrón", "str", "d", "Mexico"], ["Quena and siku", "ww", "t", "Andean flutes and panpipes"], ["Berimbau and pandeiro", "pc", "t", "Brazil"], ["Bandoneon (tango)", "fr", "t", "from Krefeld to the Río de la Plata"]],
        ["Tango", "Samba", "Bossa nova", "Son, bolero and salsa", "Latin jazz", "Cumbia", "Mariachi", "Reggaeton"]),
"ASH": ([["Klezmer clarinet and fiddle", "ww", "t", ""], ["Tsimbl", "str", "t", "hammered dulcimer"], ["Shofar", "br", "t", ""]],
        ["Klezmer", "Hasidic nigun and hazzanut", "Yiddish theatre song"]),
}

# local genres not in G: folk song and dance of one region, no special instrumentation
FOLK_DEFAULT = ("folk", [], "")

def gen(name):
    return G.get(name, FOLK_DEFAULT)

credit = {}
for r, (_, gs) in R.items():
    for g in gs: credit[g] = credit.get(g, 0) + 1

out = {"instrument_families": IFAM, "genre_families": GFAM, "regions": {}, "genres": {}}
for name, (fam, ins, where) in G.items():
    out["genres"][name] = {"family": fam, "instrumentation": ins, "formed": where}
for r, (ins, gs) in R.items():
    ishare = {k: 0.0 for k in IFAM}
    for i in ins: ishare[i[1]] += 1 / len(ins)
    gshare = {k: 0.0 for k in GFAM}
    gw = {g: 1 / credit[g] for g in gs}
    tot = sum(gw.values())
    for g, w in gw.items(): gshare[gen(g)[0]] += w / tot
    # instrumentation carried by the region's genres: each genre's families, equal shares within it
    carried = {k: 0.0 for k in IFAM}; cn = 0
    for g, w in gw.items():
        fams = gen(g)[1]
        for f in fams: carried[f] += w / len(fams)
        if fams: cn += w
    if cn: carried = {k: v / cn for k, v in carried.items()}
    out["regions"][r] = {
        "instruments": [{"name": i[0], "family": i[1], "role": i[2], "note": i[3]} for i in ins],
        "genres": [{"name": g, "family": gen(g)[0], "credit": round(1 / credit[g], 3)} for g in gs],
        "instrument_shares": {k: round(v, 3) for k, v in ishare.items()},
        "genre_shares": {k: round(v, 3) for k, v in gshare.items()},
        "genre_instrumentation": {k: round(v, 3) for k, v in carried.items()} if cn else None,
        "developed": sum(1 for i in ins if i[2] == "d"),
    }
assert len(out["regions"]) == 54, len(out["regions"])
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "music.json")
json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("regions", len(out["regions"]), "genres", len(credit), "instruments", sum(len(v[0]) for v in R.values()),
      "developed", sum(v["developed"] for v in out["regions"].values()))
