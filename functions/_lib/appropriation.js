/* Atlas of European Collectives — appropriation: is a heritage still being handed down?
   Shared by the Pages Functions and by tools/appropriation.mjs. Pure JavaScript, no platform APIs.

   Each consenting respondent answers fourteen research questions. For each of three heritages —
   their rite (faith), their tongue (everyday language) and their law — they score 0, 1 or 2 on:
     T  transmission   is it being handed on?
     O  offices        do they take part in staffing it?
     C  contest        do they argue over the thing itself?
   and the three scores give a state:
     taken-over  T = 2 and O + C >= 2     handed on, and served or fought over as itself
     kit         T = 0 and O + C <= 1     neither handed on nor taken up as a task
     inhabited   otherwise                 background: what one does
   This is the atlas's old Layer B rule adapted to a person. The old rule (T = 2, O >= 1, C >= 1, O + C >= 3) was written
   for whole regions, where "offices" meant a church or a bar staffed from within; asked of one lay person it would
   almost never be met, since few people both hold an office and argue over the thing itself.
   Region figures are aggregates of individuals, so they describe the people who answered, not institutions. */

export var RES_KEYS=["live","age","raised","last","pass","rofc","rcon","lc","lp","tofc","tcon","lown","lofc","lcon"];
export var RES_OPT={
  age:["18-29","30-49","50-64","65+"],
  raised:["cath","prot","orth","greek","split","jew","islam","x"],
  last:["w","m","y","l","n"],          /* past week, past month, past year, longer ago, never */
  pass:["y","p","n","na"],             /* yes, partly, no, not applicable */
  rofc:["r","o","n"],                  /* regularly, occasionally, no */
  rcon:["o","s","n"],                  /* often, sometimes, never */
  lc:["y","p","n"],
  lp:["y","p","n","na"],
  tofc:["r","o","n"],
  tcon:["o","s","n"],
  lown:["y","p","n"],                  /* own, partly, imposed */
  lofc:["w","s","n"],                  /* works with it, studies or studied it, no */
  lcon:["o","s","n"]
};
export var STATES=["take","inh","kit"];
export var STATE_NAME={take:"Taken-over",inh:"Inhabited",kit:"Kit",none:"None received"};
export var HERITAGES=[["rite","Rite"],["tongue","Tongue"],["law","Law"]];

export function stateOf(T,O,C){if(T===2&&O+C>=2)return "take";if(T===0&&O+C<=1)return "kit";return "inh"}

/* One respondent's heritage scores. r: research answers keyed by RES_KEYS; con: the faith they have taken up ("x" = none). */
export function personScores(r,con){
  var three={r:2,o:1,n:0},often={o:2,s:1,n:0},yn={y:2,p:1,n:0};
  /* rite */
  var rite;
  if(con==="x"&&r.raised==="x")rite={T:0,O:0,C:often[r.rcon],none:true};
  else{var T;
    if(con==="x")T=0;                                   /* raised in a faith, let it go */
    else{var p={w:2,m:2,y:1,l:0,n:0}[r.last],pass=r.pass==="na"?null:yn[r.pass];
      T=pass===null?p:(p===2&&pass===2?2:(p===0&&pass===0?0:1))}
    rite={T:T,O:con==="x"?0:three[r.rofc],C:often[r.rcon]}}
  /* tongue: everyday language; transmission from what they speak, or would speak, to children */
  var tT=r.lp==="na"?(r.lc==="y"?2:1):yn[r.lp];
  var tongue={T:tT,O:three[r.tofc],C:often[r.tcon]};
  /* law */
  var law={T:yn[r.lown],O:{w:2,s:1,n:0}[r.lofc],C:often[r.lcon]};
  [rite,tongue,law].forEach(function(h){h.state=stateOf(h.T,h.O,h.C)});
  if(rite.none)rite.state="none";
  return {rite:rite,tongue:tongue,law:law};
}

/* ---------- aggregation ---------- */
function wilson(k,n){if(!n)return [0,0];var z=1.96,p=k/n,d=1+z*z/n,c=(p+z*z/(2*n))/d,h=z*Math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d;return [Math.max(0,c-h),Math.min(1,c+h)]}
function r3(x){return Math.round(1000*x)/1000}

/* Quality filter. Keeps consenting adults, drops speeders, keeps only the latest answer from each browser. */
export function cleanRows(rows,opt){opt=opt||{};var minDur=opt.minDuration===undefined?60:opt.minDuration;
  var kept=rows.filter(function(x){return x.age&&RES_OPT.age.indexOf(x.age)>=0&&(x.duration_s===null||x.duration_s===undefined||+x.duration_s>=minDur)});
  var latest={};kept.forEach(function(x){var k=x.client||x.id;if(!latest[k]||String(x.day)+x.id>String(latest[k].day)+latest[k].id)latest[k]=x});
  return Object.keys(latest).map(function(k){return latest[k]})}

/* Post-stratification weights by age band within each group. targets: {group: {"18-29":share,...}} */
function weightsFor(list,targets){var w=list.map(function(){return 1});if(!targets)return w;
  var cnt={};list.forEach(function(x){cnt[x.age]=(cnt[x.age]||0)+1});var n=list.length;
  return list.map(function(x){var t=targets[x.age];if(!t||!cnt[x.age])return 1;return t/(cnt[x.age]/n)})}

/* rows: database rows (one per respondent). by: column to group by ("live", "peoplehood", "cw" or "subgroup").
   Returns one record per group and heritage with n, effective n, mean T/O/C with 95% intervals,
   the share in each state with 95% intervals, the plurality state, and a reliability flag. */
export function aggregate(rows,opt){opt=opt||{};var by=opt.by||"live",targets=opt.targets||null,minN=opt.minN||30;
  /* scores are recomputed from the raw answers, so a change to the scoring rules applies to every stored response */
  var clean=cleanRows(rows,opt).map(function(x){var s=personScores(x,x.con),o=Object.assign({},x);
    HERITAGES.forEach(function(h){var k=h[0];o[k+"_T"]=s[k].T;o[k+"_O"]=s[k].O;o[k+"_C"]=s[k].C;o[k+"_state"]=s[k].state});return o}),groups={};
  clean.forEach(function(x){var g=x[by];if(!g||g==="x")return;(groups[g]=groups[g]||[]).push(x)});
  var out=[];
  Object.keys(groups).sort().forEach(function(g){var L=groups[g],w=weightsFor(L,targets&&targets[g]),W=w.reduce(function(a,b){return a+b},0),W2=w.reduce(function(a,b){return a+b*b},0),neff=W*W/W2;
    var paid=L.reduce(function(a,x,i){return a+(+x.paid?w[i]:0)},0)/W;
    var monthly=L.reduce(function(a,x,i){return a+((x.last==="w"||x.last==="m")?w[i]:0)},0)/W;
    HERITAGES.forEach(function(h){var key=h[0],rec={group:g,heritage:key,n:L.length,n_eff:Math.round(neff*10)/10,paid_share:r3(paid),monthly_practice:r3(monthly)};
      ["T","O","C"].forEach(function(s){var col=key+"_"+s,m=0;L.forEach(function(x,i){m+=w[i]*(+x[col])});m/=W;var v=0;L.forEach(function(x,i){v+=w[i]*Math.pow(+x[col]-m,2)});v/=W;
        var se=Math.sqrt(v/Math.max(1,neff));rec[s+"_mean"]=r3(m);rec[s+"_lo"]=r3(Math.max(0,m-1.96*se));rec[s+"_hi"]=r3(Math.min(2,m+1.96*se))});
      var counts={take:0,inh:0,kit:0,none:0};L.forEach(function(x,i){var st=x[key+"_state"];counts[st]=(counts[st]||0)+w[i]});
      var best=null;STATES.concat(["none"]).forEach(function(st){var p=counts[st]/W,ci=wilson(p*neff,neff);rec[st+"_share"]=r3(p);rec[st+"_lo"]=r3(ci[0]);rec[st+"_hi"]=r3(ci[1]);if(!best||counts[st]>counts[best])best=st});
      rec.plurality=best;
      /* a plurality counts as clear only if its interval does not overlap the runner-up's */
      var ranked=STATES.concat(["none"]).slice().sort(function(a,b){return counts[b]-counts[a]});
      rec.clear=rec[ranked[0]+"_lo"]>rec[ranked[1]+"_hi"];
      rec.reliability=L.length<minN?"insufficient":(neff<100?"provisional":"reportable");
      out.push(rec)})});
  return {rows:out,respondents:clean.length,dropped:rows.length-clean.length,by:by,weighted:!!targets};
}

/* Optional benchmark: compare the sample's monthly-practice share with a published survey figure for the same region,
   to show how far this self-selected sample over- or under-states practice. bench: {group: share} */
export function calibrate(agg,bench){if(!bench)return [];var seen={};
  return agg.rows.filter(function(r){if(seen[r.group]||bench[r.group]===undefined)return false;seen[r.group]=1;return true})
    .map(function(r){return {group:r.group,sample_monthly:r.monthly_practice,benchmark_monthly:bench[r.group],ratio:bench[r.group]?r3(r.monthly_practice/bench[r.group]):null,n:r.n}})}

export function toCSV(objs){if(!objs.length)return "";var cols=Object.keys(objs[0]);
  function q(v){if(v===null||v===undefined)return "";var s=String(v);return /[",\n]/.test(s)?'"'+s.replace(/"/g,'""')+'"':s}
  return cols.join(",")+"\n"+objs.map(function(o){return cols.map(function(c){return q(o[c])}).join(",")}).join("\n")+"\n"}
