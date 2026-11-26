# Expanded instrument coding (v3). Fixed rule, applied to every region:
#   list the instruments of the region's own traditional, folk, dance-band and liturgical-ensemble practice, as named in its
#   national music references (sources below), one entry per instrument, up to 20; count a family of near-identical
#   instruments once (e.g. the tamburica family); leave out instruments that come in only through a genre's band line-up
#   (the rock drum kit, the jazz saxophone) unless the region's own tradition uses them, because the genre half already
#   carries genre instrumentation; leave out instruments developed here but not played here (those are landmarks).
# Developed-and-played instruments ("dt") stay in music_data.py and are not repeated here.
# Families: str strings, ww woodwinds, br brass, fr free reeds, kb keyboards, pc percussion, el electric & electronic.
# Sources are region-level references where each entry can be checked; entries were coded from them and from general
# organology, and a sample was checked on the web (see research/README.md).

EXP = {
"ISL": [["Langspil","str"],["Fiðla","str"],["Harmonika","fr"],["Lúðrasveit brass","br"]],
"NOR": [["Fiddle","str"],["Langeleik","str"],["Munnharpe","pc"],["Seljefløyte","ww"],["Bukkehorn (prillarhorn)","br"],["Birch lur","br"],["Torader","fr"],["Trekkspill","fr"]],
"SWE": [["Fiddle","str"],["Hummel","str"],["Psalmodikon","str"],["Säckpipa","ww"],["Spilåpipa","ww"],["Härjedalspipa","ww"],["Näverlur","br"],["Kohorn","br"],["Mungiga","pc"],["Dragspel","fr"]],
"FIN": [["Kantele","str"],["Jouhikko","str"],["Fiddle","str"],["Pajupilli","ww"],["Mänkeri","ww"],["Tuohitorvi","br"],["Harmonikka","fr"],["Sámi drum","pc"],["Munniharppu","pc"]],
"DEN": [["Fiddle","str"],["Double bass","str"],["Hummel","str"],["Clarinet (spillemand bands)","ww"],["Transverse flute","ww"],["Sækkepibe","ww"],["Accordion","fr"]],
"EST": [["Kannel","str"],["Hiiu kannel","str"],["Fiddle","str"],["Torupill","ww"],["Vilepill","ww"],["Sarvepill","ww"],["Karjapasun","br"],["Lõõtspill","fr"],["Parmupill","pc"],["Trumm","pc"]],
"LAT": [["Kokle","str"],["Ģīga","str"],["Fiddle","str"],["Dūdas","ww"],["Stabule","ww"],["Ragi","br"],["Ermoņikas","fr"],["Trīdeksnis","pc"],["Bungas","pc"],["Vargāns","pc"]],
"LIT": [["Kanklės","str"],["Smuikas","str"],["Skudučiai","ww"],["Birbynė","ww"],["Lamzdeliai","ww"],["Daudytė","br"],["Ragai","br"],["Bandonija","fr"],["Armonika","fr"],["Būgnas","pc"],["Tabalas","pc"]],
"RUS": [["Domra","str"],["Gusli","str"],["Gudok","str"],["Seven-string guitar","str"],["Zhaleika","ww"],["Svirel","ww"],["Kugikly","ww"],["Volynka","ww"],["Rozhok","br"],["Lozhki","pc"],["Treshchotka","pc"],["Buben","pc"]],
"BLR": [["Tsymbaly","str"],["Lira","str"],["Skrypka","str"],["Basetlia","str"],["Duda","ww"],["Zhaleika","ww"],["Dudka","ww"],["Rozhok","br"],["Garmonik","fr"],["Buben","pc"]],
"POL": [["Suka biłgorajska","str"],["Złóbcoki","str"],["Skrzypce","str"],["Basy","str"],["Cymbały","str"],["Dudy","ww"],["Kozioł","ww"],["Koza","ww"],["Fujarka","ww"],["Trombita","br"],["Ligawka","br"],["Harmonia pedałowa","fr"],["Bębenek","pc"],["Burczybas","pc"]],
"IRL": [["Fiddle","str"],["Tenor banjo","str"],["Irish bouzouki","str"],["Tin whistle","ww"],["Wooden flute","ww"],["Concertina","fr"],["Button accordion","fr"],["Bodhrán","pc"],["Bones","pc"]],
"ULS": [["Fiddle","str"],["Harp","str"],["Fife","ww"],["Flute band","ww"],["Pipe-band bagpipe","ww"],["Uilleann pipes","ww"],["Accordion band","fr"],["Side drum","pc"],["Bodhrán","pc"]],
"SCO": [["Clàrsach","str"],["Fiddle","str"],["Border pipes","ww"],["Scottish smallpipes","ww"],["Tin whistle","ww"],["Button accordion","fr"],["Pipe-band snare drum","pc"],["Pipe-band bass drum","pc"],["Bodhrán","pc"],["Trump","pc"]],
"ENG": [["Fiddle","str"],["Welsh triple harp","str"],["Crwth","str"],["Northumbrian smallpipes","ww"],["Tin whistle","ww"],["Pipe and tabor","ww"],["Pibgorn","ww"],["Serpent (west gallery)","br"],["Brass-band cornet","br"],["Tenor horn","br"],["Euphonium","br"],["Melodeon","fr"],["Handbells","pc"],["Tower bells","pc"]],
"NLD": [["Hommel","str"],["Fiddle","str"],["Doedelzak","ww"],["Midwinterhoorn","br"],["Fanfare brass","br"],["Accordion","fr"],["Street organ","kb"],["Rommelpot","pc"]],
"BEL": [["Draailier","str"],["Fiddle","str"],["Doedelzak","ww"],["Fanfare brass","br"],["Accordion","fr"],["Decap dance organ","kb"],["Carillon","pc"],["Rommelpot","pc"]],
"LUX": [["Fiddle","str"],["Péckvillchen","ww"],["Wind band (Harmonie)","br"],["Accordion","fr"],["Harmonie drum","pc"]],
"NGR": [["Fiddle","str"],["Thuringian Waldzither","str"],["Hackbrett","str"],["Spielmannszug fife","ww"],["Schalmei band","ww"],["Posaunenchor","br"],["Accordion","fr"],["Spielmannszug drum","pc"],["Glockenspiel lyra","pc"]],
"RHI": [["Fiddle","str"],["Zither","str"],["Mandolin orchestra","str"],["Spielmannszug fife","ww"],["Schalmei band","ww"],["Carnival brass","br"],["Accordion","fr"],["Bandoneon club","fr"],["Barrel organ","kb"],["Carnival drum","pc"]],
"SWA": [["Fiddle","str"],["Zither","str"],["Hackbrett","str"],["Blasmusik clarinet","ww"],["Blasmusik brass","br"],["Harmonica clubs","fr"],["Accordion orchestra","fr"],["Black Forest orchestrion","kb"],["Fasnet bells","pc"]],
"BAV": [["Concert zither","str"],["Hackbrett","str"],["Volksharfe","str"],["Fiddle","str"],["Guitar","str"],["Flügelhorn","br"],["Blasmusik tuba","br"],["Allgäu alphorn","br"],["Ziach","fr"],["Blasmusik drum","pc"]],
"BOH": [["Fiddle","str"],["Basa","str"],["Cimbál","str"],["Dudy","ww"],["Moravian clarinet","ww"],["Píšťala","ww"],["Flugelhorn","br"],["Heligonka","fr"],["Bass drum","pc"]],
"SLK": [["Husle","str"],["Basa","str"],["Cimbal","str"],["Fujara","ww"],["Koncovka","ww"],["Gajdy","ww"],["Píšťala","ww"],["Dvojačka","ww"],["Fanfára","br"],["Heligónka","fr"],["Drumbľa","pc"],["Ozembuch","pc"]],
"GAL": [["Tsymbaly","str"],["Skrypka","str"],["Sopilka","ww"],["Floyara","ww"],["Dvodentsivka","ww"],["Koza","ww"],["Trembita","br"],["Drymba","pc"],["Bubon","pc"]],
"UKR": [["Bandura","str"],["Kobza","str"],["Torban","str"],["Lira","str"],["Tsymbaly","str"],["Skrypka","str"],["Basolia","str"],["Sopilka","ww"],["Telenka","ww"],["Duda","ww"],["Bayan","fr"],["Bubon","pc"],["Buhai","pc"]],
"FRA": [["Hurdy-gurdy","str"],["Violon","str"],["Épinette des Vosges","str"],["Cabrette and musette","ww"],["Biniou and bombarde","ww"],["Galoubet","ww"],["Txistu","ww"],["Fifre","ww"],["Trompe de chasse","br"],["Fanfare brass","br"],["Musette accordion","fr"],["Tambourin provençal","pc"]],
"SUI": [["Hackbrett","str"],["Halszither","str"],["Fiddle","str"],["Ländler double bass","str"],["Ländler clarinet","ww"],["Fasnacht piccolo","ww"],["Alphorn","br"],["Büchel","br"],["Basel drum","pc"],["Talerschwingen","pc"],["Trümpi","pc"]],
"AUT": [["Zither","str"],["Hackbrett","str"],["Tyrolean harp","str"],["Fiddle","str"],["Schrammel G-clarinet","ww"],["Schwegel","ww"],["Flügelhorn","br"],["Blasmusik tuba","br"],["Steirische Harmonika","fr"],["Maultrommel","pc"]],
"HUN": [["Tekerőlant","str"],["Citera","str"],["Hegedű","str"],["Kontra","str"],["Bőgő","str"],["Ütőgardon","str"],["Tambura","str"],["Duda","ww"],["Furulya","ww"],["Doromb","pc"],["Köcsögduda","pc"]],
"ROM": [["Cobza","str"],["Țambal","str"],["Vioară","str"],["Contrabas","str"],["Nai","ww"],["Fluier","ww"],["Caval","ww"],["Cimpoi","ww"],["Taragot","ww"],["Bucium","br"],["Acordeon","fr"],["Drâmbă","pc"],["Tobă","pc"]],
"MOL": [["Cobza","str"],["Țambal","str"],["Vioară","str"],["Contrabas","str"],["Nai","ww"],["Fluier","ww"],["Caval","ww"],["Cimpoi","ww"],["Bucium","br"],["Acordeon","fr"],["Tobă","pc"]],
"POR": [["Viola braguesa","str"],["Viola campaniça","str"],["Viola da terra","str"],["Bandolim","str"],["Gaita-de-fole","ww"],["Pífaro","ww"],["Concertina","fr"],["Acordeão","fr"],["Adufe","pc"],["Bombo","pc"],["Ferrinhos","pc"],["Reque-reque","pc"]],
"ESP": [["Bandurria","str"],["Laúd","str"],["Zanfona","str"],["Timple","str"],["Gaita gallega","ww"],["Dulzaina","ww"],["Gralla","ww"],["Tenora","ww"],["Tible","ww"],["Flabiol","ww"],["Txistu","ww"],["Alboka","ww"],["Trikitixa","fr"],["Castanets","pc"],["Pandereta","pc"],["Txalaparta","pc"],["Cajón flamenco","pc"]],
"NIT": [["Lombard mandolin","str"],["Mandola","str"],["Piva","ww"],["Baghet","ww"],["Piffero","ww"],["Müsa","ww"],["Ocarina","ww"],["Banda brass","br"],["Organetto","fr"],["Tamburello","pc"]],
"MEZ": [["Chitarra battente","str"],["Lira calabrese","str"],["Zampogna","ww"],["Ciaramella","ww"],["Friscalettu","ww"],["Organetto","fr"],["Tammorra","pc"],["Tamburello","pc"],["Putipù","pc"],["Triccheballacche","pc"],["Marranzanu","pc"]],
"SAR": [["Chitarra sarda","str"],["Launeddas","ww"],["Sulittu","ww"],["Benas","ww"],["Organetto","fr"],["Tumbarinu","pc"],["Trunfa","pc"]],
"SLO": [["Citre","str"],["Cimbalom","str"],["Fiddle","str"],["Bass","str"],["Guitar","str"],["Clarinet","ww"],["Trstenke","ww"],["Žvegla","ww"],["Oberkrainer trumpet","br"],["Frajtonarica","fr"],["Lončeni bas","pc"]],
"CRO": [["Lijerica","str"],["Gusle","str"],["Sopile","ww"],["Mišnice","ww"],["Dvojnice","ww"],["Diple","ww"],["Harmonika","fr"],["Bubanj","pc"]],
"BOS": [["Šargija","str"],["Saz","str"],["Gusle","str"],["Violin","str"],["Frula","ww"],["Dvojnice","ww"],["Diple","ww"],["Harmonika","fr"],["Def","pc"],["Tapan","pc"]],
"SRB": [["Gusle","str"],["Violin","str"],["Tamburica","str"],["Frula","ww"],["Dvojnice","ww"],["Kaval","ww"],["Gajde","ww"],["Zurla","ww"],["Truba","br"],["Harmonika","fr"],["Tapan","pc"],["Darabuka","pc"]],
"MNE": [["Gusle","str"],["Diple","ww"],["Frula","ww"],["Harmonika","fr"],["Drum","pc"]],
"MAC": [["Tambura","str"],["Kemane","str"],["Ut","str"],["Violin","str"],["Kaval","ww"],["Gajda","ww"],["Zurla","ww"],["Šupelka","ww"],["Čalgija clarinet","ww"],["Brass-band trumpet","br"],["Accordion","fr"],["Tapan","pc"],["Tarabuka","pc"],["Def","pc"]],
"ALB": [["Çifteli","str"],["Lahuta","str"],["Sharki","str"],["Llautë","str"],["Violin","str"],["Zurna","ww"],["Gajde","ww"],["Fyell","ww"],["Kavall","ww"],["Klarinet","ww"],["Accordion","fr"],["Lodër","pc"],["Def","pc"]],
"BUL": [["Gadulka","str"],["Tambura","str"],["Kaval","ww"],["Gaida","ww"],["Duduk","ww"],["Svirka","ww"],["Dvoyanka","ww"],["Wedding-band clarinet","ww"],["Wedding-band saxophone","ww"],["Accordion","fr"],["Tapan","pc"],["Tarambuka","pc"]],
"GRE": [["Cretan lyra","str"],["Politiki lyra","str"],["Laouto","str"],["Santouri","str"],["Baglamas","str"],["Tzouras","str"],["Kanonaki","str"],["Outi","str"],["Violi","str"],["Klarino","ww"],["Tsampouna","ww"],["Gaida","ww"],["Zournas","ww"],["Floyera","ww"],["Daouli","pc"],["Toubeleki","pc"]],
"USA": [["Old-time fiddle","str"],["Bluegrass mandolin","str"],["Upright bass","str"],["Appalachian dulcimer","str"],["Jazz clarinet","ww"],["Jazz saxophone","ww"],["Jazz trumpet","br"],["Jazz trombone","br"],["Jug","br"],["Blues harmonica","fr"],["Cajun accordion","fr"],["Washboard","pc"]],
"CAN": [["Cape Breton fiddle","str"],["Guitar","str"],["Highland pipes","ww"],["Tin whistle","ww"],["Newfoundland accordion","fr"],["Cape Breton piano","kb"],["Ugly stick","pc"],["Bodhrán","pc"]],
"QUE": [["Violon","str"],["Guitare","str"],["Accordéon","fr"],["Ruine-babines","fr"],["Guimbarde","pc"],["Cuillères","pc"],["Podorythmie","pc"],["Os","pc"]],
"AUS": [["Fiddle","str"],["Tea-chest bass","str"],["Gum leaf","ww"],["Tin whistle","ww"],["Didgeridoo","br"],["Button accordion","fr"],["Concertina","fr"],["Clapsticks","pc"],["Lagerphone","pc"],["Bones","pc"]],
"NZL": [["Guitar","str"],["Ukulele","str"],["Kōauau","ww"],["Pūtōrino","ww"],["Pūkāea","br"],["Pūtātara","br"],["Pahū","pc"]],
"ISR": [["Oud","str"],["Kanun","str"],["Bouzouki","str"],["Violin","str"],["Halil","ww"],["Shofar","br"],["Accordion","fr"],["Darbuka","pc"],["Tof","pc"]],
"IBA": [["Cuatro","str"],["Tres","str"],["Cavaquinho","str"],["Llanera harp","str"],["Berimbau","str"],["Quena","ww"],["Siku","ww"],["Mariachi trumpet","br"],["Bandoneon (tango)","fr"],["Vallenato accordion","fr"],["Güiro","pc"],["Maracas","pc"],["Congas and bongos","pc"],["Pandeiro","pc"],["Surdo","pc"],["Bombo legüero","pc"]],
"ASH": [["Klezmer fiddle","str"],["Tsimbl","str"],["Klezmer bass","str"],["Klezmer clarinet","ww"],["Fleyt","ww"],["Klezmer trumpet","br"],["Shofar","br"],["Accordion","fr"],["Poyk","pc"]],
}

# region-level references where entries can be checked (titles of standard entries, not page-by-page citations)
NAT = {"ISL":"Iceland","NOR":"Norway","SWE":"Sweden","FIN":"Finland","DEN":"Denmark","EST":"Estonia","LAT":"Latvia","LIT":"Lithuania",
 "RUS":"Russia","BLR":"Belarus","POL":"Poland","IRL":"Ireland","ULS":"Northern Ireland","SCO":"Scotland","ENG":"England; Music of Wales",
 "NLD":"the Netherlands","BEL":"Belgium","LUX":"Luxembourg","NGR":"Germany","RHI":"Germany","SWA":"Germany","BAV":"Germany; Bavarian folk music",
 "BOH":"the Czech Republic","SLK":"Slovakia","GAL":"Ukraine; Hutsul music","UKR":"Ukraine","FRA":"France","SUI":"Switzerland","AUT":"Austria",
 "HUN":"Hungary","ROM":"Romania","MOL":"Moldova","POR":"Portugal","ESP":"Spain","NIT":"Italy","MEZ":"Italy; Music of Sicily","SAR":"Sardinia",
 "SLO":"Slovenia","CRO":"Croatia","BOS":"Bosnia and Herzegovina","SRB":"Serbia","MNE":"Montenegro","MAC":"North Macedonia","ALB":"Albania",
 "BUL":"Bulgaria","GRE":"Greece","USA":"the United States","CAN":"Canada; Music of Nova Scotia; Music of Newfoundland and Labrador",
 "QUE":"Quebec","AUS":"Australia","NZL":"New Zealand; Taonga pūoro","ISR":"Israel","IBA":"Latin America; Music of Mexico; Music of Brazil; Music of Argentina","ASH":"Klezmer"}
SOURCES = {r: ["Wikipedia, 'Music of %s' and its instrument entries" % NAT[r], "Encyclopaedia Britannica, the music entries for the country",
               "MIMO (Musical Instrument Museums Online), Hornbostel–Sachs records"] for r in NAT}
SOURCES["ASH"] = ["Wikipedia, 'Klezmer' and 'Jewish music'", "Encyclopaedia Britannica, 'klezmer music'", "MIMO, Hornbostel–Sachs records"]
