/* Music facet inclusion test (v3). With the atlas open: load /research/music_shares.js (sets window.MUSDATA), then this file.
   Uses the atlas's own treeD, spreads, redundancy discount and clustering, and restores the page's state afterwards.
   Result: window.MUSTEST. Everything is seeded, so a re-run gives the same numbers. */
(function(){
var MU=window.MUSDATA;
function run(){
 var n=R.length,P=LA.P,K;
 /* trees. Instruments: Hornbostel–Sachs types (research/music_types.py). Genres: three lines of descent. */
 TREES.ityp=MU.TTREE;
 TREES.gen={WRIT:["root",.5],art:["WRIT",0],cho:["WRIT",0],VERN:["root",.5],folk:["VERN",0],song:["VERN",0],AFAM:["root",.5],jazz:["AFAM",0],rock:["AFAM",0],elec:["AFAM",0],hip:["AFAM",0]};
 ["ityp","gen"].forEach(function(t){var T=TREES[t],H={root:1};Object.keys(T).forEach(function(k){H[k]=T[k][1]});TREEH[t]=H});
 var seed=13;function rnd(){seed=16807*seed%2147483647;return seed/2147483647}
 function sq(){var M=[];for(var k=0;k<n;k++)M.push(new Float64Array(n));return M}
 function vec(M){return P.map(function(p){return M[p[0]][p[1]]})}
 /* a region's items: one per instrument; genre credit split into whole and fractional items */
 function items(c){var o=[];for(var k in c){var w=c[k];while(w>1e-9){var u=Math.min(1,w);o.push([k,u]);w-=u}}return o}
 function comp(list,prior,a){var raw={},t=0;list.forEach(function(x){raw[x[0]]=(raw[x[0]]||0)+x[1];t+=x[1]});var o={};for(var k in prior)o[k]=((raw[k]||0)+a*prior[k])/(t+a);return o}
 function mat(lists,tree,prior,a){var M=sq(),C={};R.forEach(function(d){C[d[0]]=comp(lists[d[0]],prior,a)});
  P.forEach(function(p){var v=treeD(tree,C[R[p[0]][0]],C[R[p[1]][0]]);M[p[0]][p[1]]=M[p[1]][p[0]]=v});return M}
 function avg(A,B){var M=sq();P.forEach(function(p){M[p[0]][p[1]]=M[p[1]][p[0]]=(A[p[0]][p[1]]+B[p[0]][p[1]])/2});return M}
 function full(key){var o={};R.forEach(function(d){o[d[0]]=items(MU.R[d[0]][key])});return o}
 function halves(key){var A={},B={};R.forEach(function(d){var it=items(MU.R[d[0]][key]);for(var i=it.length-1;i>0;i--){var j=Math.floor(rnd()*(i+1)),t=it[i];it[i]=it[j];it[j]=t}var h=Math.ceil(it.length/2);A[d[0]]=it.slice(0,h);B[d[0]]=it.slice(h)});return [A,B]}
 /* split-half reliability, Spearman–Brown corrected, median and 90% range over 60 random splits */
 function reliability(a,reps){var I=[],G=[],M=[];for(var r=0;r<reps;r++){var hi=halves("rt"),hg=halves("rg");
   var i1=mat(hi[0],"ityp",MU.PT,a),i2=mat(hi[1],"ityp",MU.PT,a),g1=mat(hg[0],"gen",MU.PG,a),g2=mat(hg[1],"gen",MU.PG,a);
   [[I,i1,i2],[G,g1,g2],[M,avg(i1,g1),avg(i2,g2)]].forEach(function(x){var c=LA.corr(vec(x[1]),vec(x[2]));x[0].push(2*c/(1+c))})}
  function sum(v){v.sort(function(a,b){return a-b});return {median:+v[Math.floor(v.length/2)].toFixed(2),lo:+v[Math.floor(v.length*.05)].toFixed(2),hi:+v[Math.floor(v.length*.95)].toFixed(2)}}
  return {instruments:sum(I),genres:sum(G),music:sum(M)}}
 /* add facets to the atlas's pipeline. rel: reliability per added facet; if given, its correlations are disattenuated
    (r / √rel, Spearman 1904) before the redundancy discount, so that noise cannot earn voice */
 function withFacets(extra,rel){var keys=Object.keys(extra),F=FAC.slice().concat(keys),dd=Object.assign({},LA.d,extra),V={},S={},C={},RED={},t=0;
  F.forEach(function(f){V[f]=vec(dd[f]);S[f]=LA.sdev(V[f])});
  F.forEach(function(f){C[f]={};F.forEach(function(g){var c=LA.corr(V[f],V[g]);if(rel&&f!==g){var q=(rel[f]||1)*(rel[g]||1);c=Math.max(-1,Math.min(1,c/Math.sqrt(q)))}C[f][g]=c})});
  F.forEach(function(f){var u=1;F.forEach(function(g){if(g!==f)u+=Math.max(0,C[f][g])});RED[f]=1/u;t+=RED[f]});
  F.forEach(function(f){RED[f]/=t});
  var w={},tw=0;F.forEach(function(f){w[f]=RED[f]/S[f];tw+=w[f]});F.forEach(function(f){w[f]/=tw});
  keys.forEach(function(k){FAC.push(k)});var lab;try{lab=part3(w,dd)}finally{FAC.splice(13)}
  var moved=[];R.forEach(function(d,i){if(lab[i]!==REF3[i])moved.push(d[0])});
  var top={};keys.forEach(function(k){top[k]=F.filter(function(g){return g!==k}).map(function(g){return [g,+LA.corr(V[k],V[g]).toFixed(2)]}).sort(function(a,b){return b[1]-a[1]}).slice(0,3)});
  var voice={};keys.forEach(function(k){voice[k]=+(100*RED[k]).toFixed(1)});
  var rank=F.slice().sort(function(a,b){return RED[b]-RED[a]});
  return {voicePct:voice,sumVoicePct:+(100*keys.reduce(function(s,k){return s+RED[k]},0)).toFixed(1),rankOfFirst:rank.indexOf(keys[0])+1,of:F.length,
   sameThree:LA.same(REF3,lab),ari:+LA.ari(REF3,lab).toFixed(3),moved:moved,closest:top}}
 function mantel(A,B,reps){var a=vec(A),b=vec(B),r0=LA.corr(a,b),idx=R.map(function(_,k){return k}),ge=0;
  for(var q=0;q<reps;q++){for(var i=n-1;i>0;i--){var j=Math.floor(rnd()*(i+1)),t=idx[i];idx[i]=idx[j];idx[j]=t}
   var bb=P.map(function(p){return B[idx[p[0]]][idx[p[1]]]});if(LA.corr(a,bb)>=r0)ge++}
  return {r:+r0.toFixed(3),p:+((ge+1)/(reps+1)).toFixed(4)}}

 var out={},a=MU.alpha,FI=full("rt"),FG=full("rg");
 [1,3].forEach(function(al){out["reliability_alpha"+al]=reliability(al,60)});
 var I=mat(FI,"ityp",MU.PT,a),G=mat(FG,"gen",MU.PG,a),M=avg(I,G);
 out.halvesAgree=mantel(I,G,999);
 var rr=out["reliability_alpha"+a].music.median;
 out.oneFacet=withFacets({mus:M});
 out.oneFacetCorrected=withFacets({mus:M},{mus:rr});
 out.twoFacets=withFacets({ins:I,gen:G});
 out.instrumentsOnly=withFacets({ins:I});
 out.genresOnly=withFacets({gen:G});
 var M3=avg(mat(FI,"ityp",MU.PT,3),mat(FG,"gen",MU.PG,3));
 out.oneFacetAlpha3Corrected=withFacets({mus:M3},{mus:out.reliability_alpha3.music.median});
 out.nearest={};["ENG","USA","AUT","SRB","IBA","GRE","FIN","POR","IRL","HUN"].forEach(function(c){var i=LA.IDX[c];
  out.nearest[c]=R.map(function(d,j){return [d[0],j===i?9:M[i][j]]}).sort(function(x,y){return x[1]-y[1]}).slice(0,4).map(function(x){return x[0]+" "+x[1].toFixed(2)})});
 window.MUSMATRIX=M;
 delete TREES.ityp;delete TREES.gen;delete TREEH.ityp;delete TREEH.gen;
 window.MUSTEST=out;
}
try{run()}catch(e){window.MUSTEST={error:String(e&&e.stack||e)}}
})();
