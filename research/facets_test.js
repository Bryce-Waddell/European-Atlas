/* Inclusion test for the two music facets. With the atlas open, load /research/facets.js (window.FACDATA), set
   window.HSREL to the instrument facet's reliability (from the two coders), then load this file. Result: window.FACTEST.
   Uses the atlas's own treeD, spreads, redundancy discount and clustering, and restores the page's state. */
(function(){
var FD=window.FACDATA;
function run(){
 var n=R.length,P=LA.P;
 TREES.hstyp=FD.tree;var T=TREES.hstyp,H={root:1};Object.keys(T).forEach(function(k){H[k]=T[k][1]});TREEH.hstyp=H;
 function sq(){var M=[];for(var k=0;k<n;k++)M.push(new Float64Array(n));return M}
 function vec(M){return P.map(function(p){return M[p[0]][p[1]]})}
 /* instruments: a region's present types, each an equal share, compared on the Hornbostel–Sachs tree */
 function hsComp(c){var o={},k=0,t;for(t in c)if(c[t])k++;for(t in c)if(c[t])o[t]=1/k;return o}
 var HSM=sq(),CTM=sq();
 P.forEach(function(p){var a=R[p[0]][0],b=R[p[1]][0];
  HSM[p[0]][p[1]]=HSM[p[1]][p[0]]=treeD("hstyp",hsComp(FD.hs[a]),hsComp(FD.hs[b]));
  /* song style: the mean gap over Lomax's scales both regions have, each scale 0–1 on its codes, as the atlas's indicator facets */
  var A=FD.ct[a],B=FD.ct[b],v=NaN;if(A&&B){var s=0,m=0;for(var j=0;j<A.profile.length;j++){var x=A.profile[j],y=B.profile[j];if(x!=null&&y!=null){s+=Math.abs(x-y);m++}}v=m?s/m:NaN}
  CTM[p[0]][p[1]]=CTM[p[1]][p[0]]=v});
 function withFacets(extra,rel){var keys=Object.keys(extra),F=FAC.slice().concat(keys),dd=Object.assign({},LA.d,extra),V={},S={},C={},RED={},t=0;
  F.forEach(function(f){V[f]=vec(dd[f]);S[f]=LA.sdev(V[f])});
  F.forEach(function(f){C[f]={};F.forEach(function(g){var c=LA.corr(V[f],V[g]);if(rel&&f!==g){var q=(rel[f]||1)*(rel[g]||1);c=Math.max(-1,Math.min(1,c/Math.sqrt(q)))}C[f][g]=c})});
  F.forEach(function(f){var u=1;F.forEach(function(g){if(g!==f)u+=Math.max(0,C[f][g])});RED[f]=1/u;t+=RED[f]});
  F.forEach(function(f){RED[f]/=t});
  var w={},tw=0;F.forEach(function(f){w[f]=RED[f]/S[f];tw+=w[f]});F.forEach(function(f){w[f]/=tw});
  keys.forEach(function(k){FAC.push(k)});var lab;try{lab=part3(w,dd)}finally{FAC.splice(13)}
  var moved=[];R.forEach(function(d,i){if(lab[i]!==REF3[i])moved.push(d[0])});
  var top={},voice={};keys.forEach(function(k){top[k]=F.filter(function(g){return g!==k}).map(function(g){return [g,+LA.corr(V[k],V[g]).toFixed(2)]}).sort(function(a,b){return b[1]-a[1]}).slice(0,3);voice[k]=+(100*RED[k]).toFixed(1)});
  var rank=F.slice().sort(function(a,b){return RED[b]-RED[a]});
  return {voicePct:voice,ranks:keys.map(function(k){return rank.indexOf(k)+1}),of:F.length,sameThree:LA.same(REF3,lab),ari:+LA.ari(REF3,lab).toFixed(3),moved:moved,closest:top}}
 var seed=13;function rnd(){seed=16807*seed%2147483647;return seed/2147483647}
 function mantel(A,B,reps){var a=vec(A),b=vec(B),ok=a.map(function(x,i){return x===x&&b[i]===b[i]}),r0=LA.corr(a,b),idx=R.map(function(_,k){return k}),ge=0;
  for(var q=0;q<reps;q++){for(var i=n-1;i>0;i--){var j=Math.floor(rnd()*(i+1)),t=idx[i];idx[i]=idx[j];idx[j]=t}
   var bb=P.map(function(p){return B[idx[p[0]]][idx[p[1]]]});if(LA.corr(a,bb)>=r0)ge++}
  return {r:+r0.toFixed(3),p:+((ge+1)/(reps+1)).toFixed(4)}}
 var rel={ins:window.HSREL||null,song:FD.ct_rel.median},out={reliability:rel};
 out.agree=mantel(HSM,CTM,999);
 out.insAlone=withFacets({ins:HSM});out.songAlone=withFacets({song:CTM});
 out.both=withFacets({ins:HSM,song:CTM});
 out.bothCorrected=withFacets({ins:HSM,song:CTM},rel.ins?rel:{song:rel.song});
 out.nearest={};["ENG","USA","AUT","SRB","IBA","GRE","FIN","POR","IRL","HUN","ESP","RUS"].forEach(function(c){var i=LA.IDX[c];
  out.nearest[c]={ins:R.map(function(d,j){return [d[0],j===i?9:HSM[i][j]]}).sort(function(x,y){return x[1]-y[1]}).slice(0,4).map(function(x){return x[0]}),
   song:R.map(function(d,j){var v=CTM[i][j];return [d[0],j===i||v!==v?9:v]}).sort(function(x,y){return x[1]-y[1]}).slice(0,4).map(function(x){return x[0]})}});
 window.FACMAT={ins:HSM,song:CTM};
 delete TREES.hstyp;delete TREEH.hstyp;window.FACTEST=out}
try{run()}catch(e){window.FACTEST={error:String(e&&e.stack||e)}}
})();
