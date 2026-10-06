/* Atlas of European Collectives — quiz scoring engine, v1.4.
   The region data and the clustering engine are copied verbatim from index.html (v1.4.0): every facet scaled to
   equal spread and given an equal voice, average linkage, commonwealths and sub-groups read off the computed tree.
   If the atlas data or method changes, copy R, SC and the engine block across again.
   Runs only on the server (Cloudflare Pages Functions), so the full result is shown after payment. */
import {RES_KEYS,RES_OPT,HERITAGES,STATE_NAME,personScores} from "./appropriation.js";

var R=[
["ISL","Iceland",42,38,20,"in","nordic","prot","germn","latin","EU","neither","boreal|PA"],
["NOR","Norway",45,33,22,"in","nordic","prot","germn","latin","EU","both","tbroad|PA"],
["SWE","Sweden",43,35,22,"in","nordic","prot","germn","latin","EU","both","tbroad|PA"],
["FIN","Finland",40,28,22,"in","nordic","prot","uralic","latin","EU","both","boreal|PA"],
["DEN","Denmark",42,38,20,"in","nordic","prot","germn","latin","EU","both","tbroad|PA"],
["EST","Estonia",45,28,27,"in","civil","prot","uralic","latin","EU","both","tbroad|PA"],
["LAT","Latvia",45,28,27,"in","civil","prot","baltic","latin","EU","both","tbroad|PA"],
["LIT","Lithuania",45,28,27,"in","civil","cath","baltic","latin","EU","both","tbroad|PA"],
["RUS","Russia",42,28,22,"front","civil","orth","slave","cyr","EU","baroque","tbroad|PA"],
["BLR","Belarus",45,30,25,"front","civil","orth","slave","cyr","EU","baroque","tbroad|PA"],
["POL","Poland",45,32,23,"in","civil","cath","slavw","latin","EU","both","tbroad|PA"],
["IRL","Ireland",42,42,16,"in","common","cath","germw","latin","EU","gothic","tbroad|PA"],
["ULS","Ulster",42,42,16,"in","common","split","germw","latin","EU","gothic","tbroad|PA"],
["SCO","Scotland",42,40,18,"in","mixed","prot","germw","latin","EU","both","tbroad|PA"],
["ENG","England and Wales",38,45,17,"in","common","prot","germw","latin","EU","both","tbroad|PA"],
["NLD","Netherlands",38,45,17,"in","civil","prot","germw","latin","EU","both","tbroad|PA"],
["BEL","Belgium",36,47,17,"in","civil","cath","multi","latin","EU","both","tbroad|PA"],
["LUX","Luxembourg",35,48,17,"in","civil","cath","multi","latin","EU","both","tbroad|PA"],
["NGR","North Germany",38,45,17,"in","civil","prot","germw","latin","EU","both","tbroad|PA"],
["RHI","Rhineland",35,48,17,"in","civil","cath","germw","latin","EU","both","tbroad|PA"],
["SWA","Swabia",35,48,17,"in","civil","split","germw","latin","EU","both","tbroad|PA"],
["BAV","Bavaria",35,48,17,"in","civil","cath","germw","latin","EU","both","tbroad|PA"],
["BOH","Bohemia",38,45,17,"in","civil","cath","slavw","latin","EU","both","tbroad|PA"],
["SLK","Slovakia",40,40,20,"in","civil","cath","slavw","latin","EU","both","tbroad|PA"],
["GAL","Galicia (Ukraine)",42,34,24,"front","civil","greek","slave","cyr","EU","both","tbroad|PA"],
["UKR","Ukraine",42,34,24,"out","civil","orth","slave","cyr","EU","baroque","tbroad|PA"],
["FRA","France",32,52,16,"in","civil","cath","romance","latin","EU","both","tbroad|PA"],
["SUI","Switzerland",33,50,17,"in","civil","split","multi","latin","EU","both","tbroad|PA"],
["AUT","Austria",33,50,17,"in","civil","cath","germw","latin","EU","both","tbroad|PA"],
["HUN","Hungary",35,48,17,"in","civil","cath","uralic","latin","EU","both","tbroad|PA"],
["ROM","Romania",30,55,15,"front","civil","orth","romance","latin","EU","baroque","tbroad|PA"],
["MOL","Moldova",32,52,16,"out","civil","orth","romance","latin","EU","neither","tbroad|PA"],
["POR","Portugal",23,60,17,"in","civil","cath","romance","latin","EU","both","med|PA"],
["ESP","Spain",25,58,17,"in","civil","cath","romance","latin","EU","both","med|PA"],
["NIT","North Italy",25,60,15,"in","civil","cath","romance","latin","EU","both","tbroad|PA"],
["MEZ","Mezzogiorno",15,70,15,"in","civil","cath","romance","latin","EU","both","med|PA"],
["SAR","Sardinia",8,82,10,"in","civil","cath","romance","latin","EU","both","med|PA"],
["SLO","Slovenia",35,48,17,"in","civil","cath","slavs","latin","EU","both","tbroad|PA"],
["CRO","Croatia",35,48,17,"in","civil","cath","slavs","latin","EU","both","tbroad|PA"],
["BOS","Bosnia",33,52,15,"front","civil","split","slavs","digraph","EU","neither","tbroad|PA"],
["SRB","Serbia",32,52,16,"out","civil","orth","slavs","digraph","EU","baroque","tbroad|PA"],
["MNE","Montenegro",33,52,15,"out","civil","orth","slavs","digraph","EU","neither","med|PA"],
["MAC","Macedonia",25,60,15,"out","civil","orth","slavs","cyr","EU","neither","tbroad|PA"],
["ALB","Albania",25,60,15,"out","civil","islam","albanian","latin","EU","neither","med|PA"],
["BUL","Bulgaria",25,60,15,"out","civil","orth","slavs","cyr","EU","neither","tbroad|PA"],
["GRE","Greece",18,68,14,"out","civil","orth","hellenic","greek","EU","neither","med|PA"],
["USA","United States",38,45,17,"in","common","prot","germw","latin","NA","revival","tbroad|NA"],
["CAN","English Canada",40,44,16,"in","common","prot","germw","latin","NA","revival","tbroad|NA"],
["QUE","Québec",32,52,16,"in","mixed","cath","romance","latin","NA","baroque","tbroad|NA"],
["AUS","Australia",40,44,16,"in","common","split","germw","latin","OC","revival","tbroad|AA"],
["NZL","New Zealand",40,44,16,"in","common","prot","germw","latin","OC","revival","tbroad|AA"],
["ISR","Israel",10,80,10,"front","mixed","jew","semitic","hebrew","IL","neither","med|PA"],
["IBA","Ibero-America",25,58,17,"in","civil","cath","romance","latin","X","baroque","tmoist|NT"],
["ASH","Ashkenazim",10,78,12,"out","halakh","jew","germw","hebrew","X","neither","tbroad|PA"]
];
var I={code:0,name:1,st:2,ef:3,hg:4,chr:5,leg:6,con:7,lang:8,scr:9,grp:10,art:11,gd:12};
var SC={
 lang:{germn:["#2E4C7A","North Germanic","N. Germanic"],
  germw:["#5B88C2","West Germanic","W. Germanic"],
  romance:["#A63D2B","Romance","Romance"],
  slavw:["#C8912E","West Slavic","W. Slavic"],
  slave:["#8A5A1E","East Slavic","E. Slavic"],
  slavs:["#E0BC72","South Slavic","S. Slavic"],
  baltic:["#6B4472","Baltic","Baltic"],
  uralic:["#47786A","Uralic","Uralic"],
  hellenic:["#3E7F8C","Hellenic","Hellenic"],
  albanian:["#B5577E","Albanian","Albanian"],
  semitic:["#7D8F3A","Semitic","Semitic"],
  multi:["#8A8578","Multilingual","Multilingual"]},
 scr:{latin:["#2E4C7A","Latin alphabet","Latin"],
  cyr:["#A63D2B","Cyrillic","Cyrillic"],
  digraph:["#D38A6A","Cyrillic and Latin both","Both"],
  greek:["#3E7F8C","Greek alphabet","Greek"],
  hebrew:["#6B4472","Hebrew letters","Hebrew"]},
 gd:{"tbroad|PA":["#6E9A55","Temperate broadleaf and mixed forest, Palearctic","Broadleaf<br>Palearctic"],
  "tbroad|NA":["#A9C790","Temperate broadleaf and mixed forest, Nearctic","Broadleaf<br>Nearctic"],
  "tbroad|AA":["#C9DBB2","Temperate broadleaf and mixed forest, Australasian","Broadleaf<br>Australasian"],
  "boreal|PA":["#4F7390","Boreal forest and taiga, Palearctic","Boreal<br>Palearctic"],
  "med|PA":["#C98A4B","Mediterranean forest, woodland and scrub, Palearctic","Mediterr.<br>Palearctic"],
  "tmoist|NT":["#2C5E46","Tropical and subtropical moist forest, Neotropical","Trop. moist<br>Neotropical"]},
 art:{both:["#5B3A6E","Gothic and Baroque both took root","Both"],
  gothic:["#9A78B0","Gothic took root; Baroque did not","Gothic"],
  baroque:["#C9913D","Baroque took root without a medieval Gothic","Baroque"],
  revival:["#8FB0C4","No medieval Gothic; arrived as nineteenth-century revival","Revival only"],
  neither:["#E7B09A","Neither took root","Neither"]},
 chr:{"in":["#47786A","Inside the transmission","Inside"],
  front:["#A3BBA5","Contested frontier","Frontier"],
  out:["#E7B09A","Outside","Outside"]},
 leg:{common:["#A63D2B","Common law","Common"],
  civil:["#2E4C7A","Romano-Germanic civil law","Civil"],
  nordic:["#47786A","Nordic family","Nordic"],
  mixed:["#6B4472","Mixed","Mixed"],
  halakh:["#3E3A33","Halakha","Halakhic"]},
 con:{cath:["#8C3A2A","Christian: Latin Catholic","Catholic"],prot:["#35597F","Christian: Protestant","Protestant"],
  orth:["#C89328","Christian: Orthodox","Orthodox"],greek:["#6B4472","Christian: Greek Catholic","Greek Cath."],
  islam:["#3F7F5E","Muslim","Muslim"],
  split:["#8A8578","Confessionally split","Split"],jew:["#3E3A33","Judaism","Judaism"]}
};

/* ---------- Clustering engine: the exact distances, scaling, voices and clustering set out under Methodology ---------- */
var FAC=["chr","bio","gd","lang","scr","art","leg","con"];
var BIRTH={bio:1,gd:1};
var LFAM={germn:"G",germw:"G",slavw:"S",slave:"S",slavs:"S",romance:"R",baltic:"B",uralic:"U",hellenic:"H",albanian:"A",semitic:"X",multi:"M"};
var BFAM={tbroad:"T",tconif:"T",boreal:"C",tundra:"C",med:"D",desert:"D",tgrass:"D",tmoist:"X"};
var ARTD={"both|gothic":.5,"both|baroque":.5,"both|revival":.6,"both|neither":1,"gothic|baroque":.7,"gothic|revival":.5,"gothic|neither":.5,"baroque|revival":.6,"baroque|neither":.5,"revival|neither":.6};
var HALF={chr:["in|front","front|out"],scr:["latin|digraph","cyr|digraph"],con:["cath|greek","orth|greek","split|cath","split|prot","split|orth","split|islam"],leg:["mixed|common","mixed|civil","nordic|civil","nordic|common"]};
function dCat(f,a,b,strict){if(a===b)return 0;if(strict)return 1;
 if(f==="gd"){var A=a.split("|"),B=b.split("|");var db=A[0]===B[0]?0:(BFAM[A[0]]===BFAM[B[0]]?.5:1);return .75*db+.25*(A[1]===B[1]?0:1)}
 if(f==="art"){var v=ARTD[a+"|"+b];return v!==undefined?v:ARTD[b+"|"+a]}
 if(f==="lang"){if(a==="multi"||b==="multi")return .5;return LFAM[a]===LFAM[b]?.5:1}
 if(f==="con"&&((a==="cath"&&b==="prot")||(a==="prot"&&b==="cath")))return .6;
 var h=HALF[f]||[];return (h.indexOf(a+"|"+b)>=0||h.indexOf(b+"|"+a)>=0)?.5:1}
var LA=(function(){var n=R.length,IDX={};R.forEach(function(d,i){IDX[d[0]]=i});
 var P=[],i,j;for(i=0;i<n;i++)for(j=i+1;j<n;j++)P.push([i,j]);
 function mean(a){var s=0;for(var k=0;k<a.length;k++)s+=a[k];return s/a.length}
 function sdev(a){var m=mean(a),s=0;for(var k=0;k<a.length;k++)s+=(a[k]-m)*(a[k]-m);return Math.sqrt(s/a.length)}
 function corr(a,b){var ma=mean(a),mb=mean(b),x=0,y=0,z=0;for(var k=0;k<a.length;k++){x+=(a[k]-ma)*(b[k]-mb);y+=(a[k]-ma)*(a[k]-ma);z+=(b[k]-mb)*(b[k]-mb)}return x/Math.sqrt(y*z)}
 function sq(){var M=[];for(var k=0;k<n;k++)M.push(new Float64Array(n));return M}
 /* biological: centred log-ratio, Euclidean (Aitchison) distance; shares may be passed in to test measurement noise */
 function bioD(sh){var clr=sh.map(function(x){var l=x.map(Math.log),m=(l[0]+l[1]+l[2])/3;return l.map(function(v){return v-m})}),M=sq(),mx=0,mp=null;
  P.forEach(function(p){var a=clr[p[0]],b=clr[p[1]],v=Math.hypot(a[0]-b[0],a[1]-b[1],a[2]-b[2]);M[p[0]][p[1]]=M[p[1]][p[0]]=v;if(v>mx){mx=v;mp=p}});
  P.forEach(function(p){M[p[0]][p[1]]/=mx;M[p[1]][p[0]]/=mx});return {M:M,mx:mx,mp:mp}}
 var SH=R.map(function(d){return [d[I.st],d[I.ef],d[I.hg]]});
 function facetD(strict,bio){var d={};FAC.forEach(function(f){if(f==="bio"){d.bio=bio.M;return}d[f]=sq();
   P.forEach(function(p){var v=dCat(f,R[p[0]][I[f]],R[p[1]][I[f]],strict&&f!=="gd"?1:0);if(strict&&f==="gd")v=v>0?1:0;d[f][p[0]][p[1]]=d[f][p[1]][p[0]]=v})});return d}
 var B0=bioD(SH),d=facetD(false,B0);
 function vecs(dd){var V={};FAC.forEach(function(f){V[f]=P.map(function(p){return dd[f][p[0]][p[1]]})});return V}
 function spreads(V){var S={};FAC.forEach(function(f){S[f]=sdev(V[f])});return S}
 var V=vecs(d),S=spreads(V);
 var C={};FAC.forEach(function(f){C[f]={};FAC.forEach(function(g){C[f][g]=corr(V[f],V[g])})});
 /* voices: the share of influence each facet is meant to have before the facets' agreement is counted */
 var EQ={},TR={},CONS={},RED={},t1=0,t2=0;
 FAC.forEach(function(f){EQ[f]=1/8;TR[f]=BIRTH[f]?0:1/6;var s=0,u=1;FAC.forEach(function(g){if(g!==f){s+=C[f][g];u+=Math.max(0,C[f][g])}});CONS[f]=Math.max(0,s/7);RED[f]=1/u;t1+=CONS[f];t2+=RED[f]});
 FAC.forEach(function(f){CONS[f]/=t1;RED[f]/=t2});
 /* coefficients actually applied: voice divided by the facet's spread, renormalised to sum to one */
 function coef(W,S2){S2=S2||S;var o={},t=0;FAC.forEach(function(f){o[f]=W[f]/S2[f];t+=o[f]});FAC.forEach(function(f){o[f]/=t});return o}
 var OM=coef(EQ);
 function D(a,b,w,dd){w=w||OM;dd=dd||d;var s=0;for(var k=0;k<FAC.length;k++)s+=w[FAC[k]]*dd[FAC[k]][a][b];return s}
 function matrix(w,dd){var M=sq();P.forEach(function(p){M[p[0]][p[1]]=M[p[1]][p[0]]=D(p[0],p[1],w,dd)});return M}
 /* hierarchical clustering. Average linkage: the distance between two groups is the mean over all their cross pairs,
    updated after each merge by the Lance–Williams rule. Complete linkage: the largest cross pair. */
 function cluster(M,idx,link){idx=idx||R.map(function(_,k){return k});var N=2*n,Dm=new Float64Array(N*N),cl=idx.map(function(k){return {m:[k],leaf:k,h:0,id:k}}),merges=[],nid=n,a,b;
  for(a=0;a<cl.length;a++)for(b=a+1;b<cl.length;b++){var x=cl[a].id,y=cl[b].id;Dm[x*N+y]=Dm[y*N+x]=M[x][y]}
  while(cl.length>1){var bi=0,bj=1,bd=1e9;
   for(a=0;a<cl.length;a++){var ra=cl[a].id*N;for(b=a+1;b<cl.length;b++){var v=Dm[ra+cl[b].id];if(v<bd-1e-12){bd=v;bi=a;bj=b}}}
   var A=cl[bi],B=cl[bj],node={m:A.m.concat(B.m),l:A,r:B,h:bd,id:nid++},na=A.m.length,nb=B.m.length;
   for(a=0;a<cl.length;a++){if(a===bi||a===bj)continue;var K=cl[a].id,da=Dm[K*N+A.id],db=Dm[K*N+B.id],u=link==="complete"?Math.max(da,db):(na*da+nb*db)/(na+nb);Dm[K*N+node.id]=Dm[node.id*N+K]=u}
   merges.push(node);cl[bi]=node;cl.splice(bj,1)}
  return {root:cl[0],merges:merges,size:idx.length}}
 /* cut a tree into k groups: undo the last k−1 merges */
 function cut(T,k){var out=[T.root];while(out.length<k){var hi=-1,hk=-1;out.forEach(function(g,gi){if(g.l&&g.h>hi){hi=g.h;hk=gi}});if(hk<0)break;var g=out[hk];out.splice(hk,1,g.l,g.r)}return out}
 function labels(groups){var l={};groups.forEach(function(g,gi){g.m.forEach(function(k){l[k]=gi})});return l}
 function same(A,B,idx){idx=idx||R.map(function(_,k){return k});for(var a=0;a<idx.length;a++)for(var b=a+1;b<idx.length;b++){var x=idx[a],y=idx[b];if((A[x]===A[y])!==(B[x]===B[y]))return false}return true}
 function ari(A,B,idx){idx=idx||R.map(function(_,k){return k});var t={},ra={},rb={};idx.forEach(function(k){var q=A[k]+"_"+B[k];t[q]=(t[q]||0)+1;ra[A[k]]=(ra[A[k]]||0)+1;rb[B[k]]=(rb[B[k]]||0)+1});
  function c2(x){return x*(x-1)/2}var sij=0,sa=0,sb=0;Object.keys(t).forEach(function(q){sij+=c2(t[q])});Object.keys(ra).forEach(function(q){sa+=c2(ra[q])});Object.keys(rb).forEach(function(q){sb+=c2(rb[q])});
  var N=c2(idx.length),e=sa*sb/N,mx=(sa+sb)/2;return mx===e?1:(sij-e)/(mx-e)}
 function silhouette(M,lab,idx){idx=idx||R.map(function(_,k){return k});var per={},tot=0;
  idx.forEach(function(i){var g={};idx.forEach(function(j){if(j===i)return;(g[lab[j]]=g[lab[j]]||[]).push(M[i][j])});var own=g[lab[i]];if(!own){per[i]=0;return}
   var a=mean(own),b=1e9;Object.keys(g).forEach(function(q){if(+q!==lab[i]){var v=mean(g[q]);if(v<b)b=v}});per[i]=(b-a)/Math.max(a,b);tot+=per[i]});
  return {avg:tot/idx.length,per:per}}
 /* cophenetic correlation: how faithfully the tree's merge heights reproduce the distances */
 function coph(T,M){var H=sq();(function walk(nd){if(!nd.l)return;walk(nd.l);walk(nd.r);nd.l.m.forEach(function(x){nd.r.m.forEach(function(y){H[x][y]=H[y][x]=nd.h})})})(T.root);
  return corr(P.map(function(p){return M[p[0]][p[1]]}),P.map(function(p){return H[p[0]][p[1]]}))}
 /* effective influence: each facet's share of the variance of the combined distance */
 function influence(w){var Dv=P.map(function(p){return D(p[0],p[1],w)}),mD=mean(Dv),vD=0,out={};Dv.forEach(function(x){vD+=(x-mD)*(x-mD)});
  FAC.forEach(function(f){var m=mean(V[f]),c=0;for(var k=0;k<P.length;k++)c+=w[f]*(V[f][k]-m)*(Dv[k]-mD);out[f]=c/vD});return out}
 function jaccard(a,b){var s={},x=0;a.forEach(function(k){s[k]=1});b.forEach(function(k){if(s[k])x++});return x/(a.length+b.length-x)}
 return {n:n,IDX:IDX,P:P,mA:B0.mx,mP:B0.mp,SH:SH,bioD:bioD,facetD:facetD,d:d,V:V,S:S,C:C,spreads:spreads,vecs:vecs,
  EQ:EQ,TR:TR,CONS:CONS,RED:RED,W:EQ,coef:coef,OM:OM,D:D,matrix:matrix,cluster:cluster,cut:cut,labels:labels,same:same,ari:ari,
  silhouette:silhouette,coph:coph,influence:influence,jaccard:jaccard,mean:mean,sdev:sdev}
})();


/* ---------- The commonwealths and sub-groups, read off the tree this page computes ---------- */
var CWN=["Latin Commonwealth","Byzantine Commonwealth","Hebraic Commonwealth"];
var CWB={"Latin Commonwealth":"#2F6B5E","Byzantine Commonwealth":"#9C6A1E","Hebraic Commonwealth":"#5A4A8A"};
var CWANCH=[["FRA",0],["RUS",1],["ISR",2]];
var SUBDEF=[["ENG","Atlantic and Central core","#2F6B5E"],["ESP","Southern Romance and the New World","#7FAE9C"],
 ["RUS","Rus' lands","#9C6A1E"],["SRB","Danubian and South Slav","#C9912E"],["ALB","Albania","#D9A441"],["GRE","Greece","#B07A3C"],
 ["ISR","Israel","#5A4A8A"],["ASH","Ashkenazi diaspora","#8E7FBE"]];
var M0=LA.matrix(LA.OM),TREE=LA.cluster(M0),G3=LA.cut(TREE,3),G8=LA.cut(TREE,8),REF3=LA.labels(G3);
var CWG={};G3.forEach(function(g,gi){var nm=null;CWANCH.forEach(function(a){if(!nm&&g.m.indexOf(LA.IDX[a[0]])>=0)nm=CWN[a[1]]});CWG[gi]=nm||("Group "+(gi+1))});
var CW={},CWU={},SUBKEY={};
(function(){var used={};
 SUBDEF.forEach(function(s,si){G8.forEach(function(g,gi){if(used[gi]||g.m.indexOf(LA.IDX[s[0]])<0)return;used[gi]=1;var key="S"+si;SUBKEY[gi]=key;
  CW[key]=[CWG[REF3[g.m[0]]],s[1],s[2]];g.m.forEach(function(k){CWU[R[k][0]]=key})})});
 G8.forEach(function(g,gi){if(used[gi])return;var key="X"+gi;SUBKEY[gi]=key;CW[key]=[CWG[REF3[g.m[0]]],"Sub-group "+(gi+1),"#8A8578"];g.m.forEach(function(k){CWU[R[k][0]]=key})})})();


/* ---------- Answers ---------- */
/* Encoded as  v2~chr1,chr2,chr3~gp1,gp2,gp3,gp4~birth~lang~scr~art~leg~con~RESEARCH
   ("x" = not known / none). RESEARCH is "-" if the respondent did not take part, otherwise fourteen
   comma-separated answers in the order of RES_KEYS. */
var BYC={};R.forEach(function(d){BYC[d[0]]=d});
var REGION_CODES=R.filter(function(d){return d[0]!=="ASH"}).map(function(d){return d[0]});
var OPT={
  chr:["in","front","out"],
  gp:R.map(function(d){return d[0]}).concat(["x"]),
  birth:REGION_CODES.concat(["x"]),
  lang:Object.keys(SC.lang).concat(["x"]),
  scr:Object.keys(SC.scr).concat(["x"]),
  art:Object.keys(SC.art),
  leg:Object.keys(SC.leg).concat(["x"]),
  con:Object.keys(SC.con).concat(["x"])
};
var RES_ALL=Object.assign({live:REGION_CODES.concat(["x"])},RES_OPT);
function parseAnswers(code){
  if(typeof code!=="string"||code.length>400)return null;
  var p=code.split("~");if(p.length!==10||p[0]!=="v2")return null;
  var chr=p[1].split(","),gp=p[2].split(",");
  if(chr.length!==3||gp.length!==4)return null;
  function ok(list,v){return list.indexOf(v)>=0}
  if(!chr.every(function(v){return ok(OPT.chr,v)}))return null;
  if(!gp.every(function(v){return ok(OPT.gp,v)}))return null;
  var keys=["birth","lang","scr","art","leg","con"],a={chr:chr,gp:gp,research:null};
  for(var k=0;k<keys.length;k++){if(!ok(OPT[keys[k]],p[k+3]))return null;a[keys[k]]=p[k+3]}
  /* Latin Roman and Art are always answered; require two more facets so a result means something */
  var extra=(gp.some(function(v){return v!=="x"})?1:0)+["birth","lang","scr","leg","con"].filter(function(key){return a[key]!=="x"}).length;
  if(extra<2)return null;
  if(p[9]!=="-"){var rv=p[9].split(",");if(rv.length!==RES_KEYS.length)return null;var r={};
    for(var j=0;j<RES_KEYS.length;j++){if(!ok(RES_ALL[RES_KEYS[j]],rv[j]))return null;r[RES_KEYS[j]]=rv[j]}
    a.research=r}
  return a;
}

/* Turn answers into a profile coded exactly like a row of the atlas. null = facet not scored. */
function profileOf(a){
  var v={in:0,front:.5,out:1},m=(v[a.chr[0]]+v[a.chr[1]]+v[a.chr[2]])/3;
  var chr=m<1/3?"in":(m<=2/3?"front":"out");
  var known=a.gp.filter(function(u){return u!=="x"}).map(function(u){return BYC[u]});
  var bio=null;
  if(known.length){var s=[0,0,0];known.forEach(function(d){s[0]+=d[I.st];s[1]+=d[I.ef];s[2]+=d[I.hg]});
    bio=s.map(function(x){return Math.round(x/known.length)})}
  return {chr:chr,bio:bio,gd:a.birth==="x"?null:BYC[a.birth][I.gd],
    lang:a.lang==="x"?null:a.lang,scr:a.scr==="x"?null:a.scr,art:a.art,
    leg:a.leg==="x"?null:a.leg,con:a.con==="x"?null:a.con};
}

function clrOf(x){var l=x.map(Math.log),m=(l[0]+l[1]+l[2])/3;return l.map(function(v){return v-m})}
var CLR=LA.SH.map(clrOf);
function facetDist(prof,f,k){
  if(f==="bio"){var a=clrOf(prof.bio),b=CLR[k];return Math.min(1,Math.hypot(a[0]-b[0],a[1]-b[1],a[2]-b[2])/LA.mA)}
  return dCat(f,prof[f],R[k][I[f]]);
}
function cwOf(u){return CW[CWU[u]][0]}

function score(a){
  var prof=profileOf(a);
  var used=FAC.filter(function(f){return prof[f]!==null});
  var wsum=used.reduce(function(s,f){return s+LA.OM[f]},0);
  var per=R.map(function(d,k){var o={};used.forEach(function(f){o[f]=facetDist(prof,f,k)});return o});
  var D=per.map(function(o){return used.reduce(function(s,f){return s+LA.OM[f]*o[f]},0)/wsum});

  /* commonwealth: smallest mean distance to its members (average linkage, as in Plate III) */
  var cws=CWN.map(function(name){var ks=[];R.forEach(function(d,k){if(cwOf(d[0])===name)ks.push(k)});
    var md=ks.reduce(function(s,k){return s+D[k]},0)/ks.length;return {name:name,members:ks,dist:md}});
  var ranked=cws.slice().sort(function(x,y){return x.dist-y.dist}),home=ranked[0];

  /* peoplehood: the nearest unit inside that commonwealth */
  var best=home.members.slice().sort(function(x,y){return D[x]-D[y]})[0],bd=R[best];

  /* defining facet: which facet does most to hold you inside your commonwealth rather than the others */
  var others=[];R.forEach(function(d,k){if(cwOf(d[0])!==home.name)others.push(k)});
  function mf(list,f){return list.reduce(function(s,k){return s+per[k][f]},0)/list.length}
  var pull=used.map(function(f){return {f:f,v:LA.OM[f]*(mf(others,f)-mf(home.members,f))/wsum}})
    .sort(function(x,y){return y.v-x.v});

  var near=R.map(function(d,k){return k}).sort(function(x,y){return D[x]-D[y]}).slice(0,5)
    .map(function(k){return {code:R[k][0],name:R[k][1],cw:cwOf(R[k][0]),sub:CW[CWU[R[k][0]]][1],match:Math.round(100*(1-D[k]))}});

  function lab(f,val){if(val===null)return null;if(f==="bio")return "steppe "+val[0]+" · farmer "+val[1]+" · forager "+val[2];return SC[f][val][1]}
  function unitVal(f){return f==="bio"?[bd[I.st],bd[I.ef],bd[I.hg]]:bd[I[f]]}
  var facets=FAC.map(function(f){var mine=prof[f];
    return {id:f,label:FACET_TEXT[f].label,kind:BIRTH[f]?"Birthright":"Transmitted",
      you:lab(f,mine),them:lab(f,unitVal(f)),
      dist:mine===null?null:Math.round(100*per[best][f])/100,
      coefficient:Math.round(1000*LA.OM[f]/wsum)/1000}});

  /* margin: how much nearer the home commonwealth is than the runner-up, as a share of the runner-up's distance */
  var margin=(ranked[1].dist-home.dist)/ranked[1].dist;
  var sk=CWU[bd[0]];
  var out={
    version:VERSION,
    commonwealth:{name:home.name,color:CWB[home.name],text:CW_TEXT[home.name],margin:Math.round(100*margin),runnerUp:ranked[1].name},
    subgroup:{key:sk,name:CW[sk][1],color:CW[sk][2],text:SUB_TEXT[CW[sk][1]]||""},
    peoplehood:{code:bd[0],name:bd[1],match:Math.round(100*(1-D[best])),
      tiedWith:home.members.filter(function(k){return k!==best&&Math.abs(D[k]-D[best])<1e-9}).map(function(k){return R[k][1]})},
    defining:{id:pull[0].f,label:FACET_TEXT[pull[0].f].label,text:FACET_TEXT[pull[0].f].text,runnerUp:pull[1]?FACET_TEXT[pull[1].f].label:null},
    commonwealths:cws.map(function(c){return {name:c.name,color:CWB[c.name],closeness:Math.round(100*(1-c.dist))}}),
    facets:facets,
    nearest:near,
    unscored:FAC.filter(function(f){return prof[f]===null}).map(function(f){return FACET_TEXT[f].label}),
    inheritance:a.research?inheritance(a):null
  };
  return out;
}

/* How the respondent holds their rite, tongue and law, from the research answers. Free to see once answered. */
function inheritance(a){var s=personScores(a.research,a.con);
  var names={rite:a.con!=="x"?SC.con[a.con][1]:(a.research.raised!=="x"?SC.con[a.research.raised][1]+" (raised, not kept)":"No faith received or taken up"),
    tongue:a.lang!=="x"?SC.lang[a.lang][1]:"Your everyday language",
    law:a.leg!=="x"?SC.leg[a.leg][1]:"The law you live under"};
  return HERITAGES.map(function(h){var x=s[h[0]];return {id:h[0],label:h[1],heritage:names[h[0]],T:x.T,O:x.O,C:x.C,state:x.state,stateName:STATE_NAME[x.state],text:STATE_TEXT[x.state]}});
}

/* A database row for one consenting respondent. */
function rowOf(a){var r=a.research,s=personScores(r,a.con),sc=score(a);
  return {chr0:a.chr[0],chr1:a.chr[1],chr2:a.chr[2],gp1:a.gp[0],gp2:a.gp[1],gp3:a.gp[2],gp4:a.gp[3],birth:a.birth,lang:a.lang,scr:a.scr,art:a.art,leg:a.leg,con:a.con,
    live:r.live,age:r.age,raised:r.raised,last:r.last,pass:r.pass,rofc:r.rofc,rcon:r.rcon,lc:r.lc,lp:r.lp,tofc:r.tofc,tcon:r.tcon,lown:r.lown,lofc:r.lofc,lcon:r.lcon,
    cw:sc.commonwealth.name,subgroup:sc.subgroup.name,peoplehood:sc.peoplehood.code,match_pct:sc.peoplehood.match,
    rite_T:s.rite.T,rite_O:s.rite.O,rite_C:s.rite.C,rite_state:s.rite.state,
    tongue_T:s.tongue.T,tongue_O:s.tongue.O,tongue_C:s.tongue.C,tongue_state:s.tongue.state,
    law_T:s.law.T,law_O:s.law.O,law_C:s.law.C,law_state:s.law.state}}
var ROW_COLS=["chr0","chr1","chr2","gp1","gp2","gp3","gp4","birth","lang","scr","art","leg","con","live","age","raised","last","pass","rofc","rcon","lc","lp","tofc","tcon","lown","lofc","lcon",
  "cw","subgroup","peoplehood","match_pct","rite_T","rite_O","rite_C","rite_state","tongue_T","tongue_O","tongue_C","tongue_state","law_T","law_O","law_C","law_state"];

/* ---------- Copy ---------- */
var VERSION="1.4.0";
var FACET_TEXT={
  chr:{label:"Latin Roman",text:"The Latin juridical inheritance: marriage made by the consent of two people, self-governing corporations and chartered universities, and contracts a court will enforce. The atlas calls it co-apex with Confession, because clustering on all eight facets, with none given extra say, rediscovers exactly its boundary."},
  bio:{label:"Biological",text:"Ancient ancestral make-up: your share of Bronze-Age steppe, Neolithic farmer and hunter-gatherer descent, estimated from where your grandparents came from. A birthright facet: you did not choose it."},
  gd:{label:"Geographic descent",text:"The biome and realm you were born into. A birthright facet, and in the atlas the one that agrees with almost nothing else."},
  lang:{label:"Language",text:"The branch of the tongue you live in every day. Language cuts across every other facet and splits populations that nothing else separates."},
  scr:{label:"Script",text:"The alphabet you read in. The sharpest line on the map, almost exactly the 1054 schism, and the one facet you can read from a train window."},
  art:{label:"Art",text:"Whether the Gothic-to-Baroque building tradition is yours. Close to the Rome–Constantinople line, with its own exceptions."},
  leg:{label:"Legal family",text:"How the law you live under is made: judge-made precedent, a comprehensive code, the Nordic hybrid, a mixed system, or halakha."},
  con:{label:"Confession",text:"Which branch of faith you have taken up. In the atlas it is co-apex with the Latin Roman facet: a quarrel inside the inheritance in the west, a civilizational edge in the east."}
};
var CW_TEXT={
  "Latin Commonwealth":"Thirty-nine regions, from Iceland to Sardinia and across the oceans to Philadelphia, Sydney and Lima. What holds them together is not descent but a package received whole from the Latin church and Roman law: consent-made marriage, the self-governing corporation, the chartered university, the enforceable contract. The clustering finds this group by itself: it is exactly the set of regions inside the Latin Roman facet.",
  "Byzantine Commonwealth":"Thirteen regions, from Russia through the Balkans to Greece. Their inheritance came from Constantinople rather than Rome: the Orthodox rite, Cyrillic or Greek letters, and a tradition in which church and ruler act in symphony rather than as two rival jurisdictions. Five of the six frontier regions of the Latin package — Russia, Belarus, Galicia, Romania and Bosnia — fall to this side.",
  "Hebraic Commonwealth":"Two units, Israel and the Ashkenazi diaspora, which differ from every other region on script, confession, art and legal family at once. With every facet given an equal say, they are the first group the clustering splits away."
};
var SUB_TEXT={
  "Atlantic and Central core":"The broad heart of the Latin commonwealth: Scandinavia, the British Isles, the Low Countries, the German lands, France, North Italy, Switzerland, Austria, Bohemia, Slovakia, Poland, Hungary, the Baltics, Slovenia, Croatia and the Anglosphere overseas. The core itself is firm; its inner divisions are not. Give the agreeing facets more say and it splits into a Protestant North Sea group and a Catholic continent.",
  "Southern Romance and the New World":"Portugal, Spain, the Mezzogiorno, Sardinia, Québec and Ibero-America: Romance-speaking, Catholic and Baroque, born by the Mediterranean or in the New World. The least stable sub-group in the atlas: it appears when language and birthplace get their full say, and folds back into the Latin core when they do not.",
  "Rus' lands":"The Rus' lands: Russia, Belarus, Ukraine and Galicia. East Slavic, Cyrillic, Orthodox or Greek Catholic, and mostly Baroque without a medieval Gothic before it.",
  "Danubian and South Slav":"Romania, Moldova, Serbia, Bosnia, Montenegro, Macedonia and Bulgaria: the Byzantine rite or a confessional split, codified civil law, and Baroque without Gothic, or neither. Romania and Moldova sit on the seam with the Latin commonwealth and are the most movable regions in the atlas.",
  "Albania":"Albania: its own language, a Muslim plurality, and the Latin alphabet, outside the Latin juridical package. A branch of the Byzantine commonwealth that fits no other.",
  "Greece":"Greece: the Hellenic tongue and the Greek alphabet, Orthodox, Mediterranean. The source of the Byzantine inheritance rather than a receiver of it.",
  "Israel":"Israel: modern Hebrew, Hebrew letters, Judaism and a mixed legal system — a state that took over an older inheritance by decision, and the Latin package's frontier through its courts, universities and corporations.",
  "Ashkenazi diaspora":"The Ashkenazi diaspora: West Germanic speech descended from Yiddish, Hebrew letters, Judaism, and halakha with no state behind it."
};
var STATE_TEXT={
  take:"Handed on, and served or argued over as itself: a live possibility you have taken up.",
  inh:"Present in your life as background — what one does — but not, on your answers, both handed on and taken up as a task.",
  kit:"Kept, if at all, as heritage: neither handed on nor taken up as a task.",
  none:"You were not raised in a faith and have not taken one up, so there is no rite to hold."
};

export {R,OPT,LA,CW,CWU,CWN,parseAnswers,profileOf,score,inheritance,rowOf,ROW_COLS,VERSION};
export var PRICE_CENTS=500;
