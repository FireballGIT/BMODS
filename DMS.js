export const DMS = {
  fact(n){
    if(n<0 || !Number.isInteger(n)) throw Error();
    let r=1;
    for(let i=2;i<=n;i++) r*=i;
    return r;
  },

  convert(v,u){
    u=u.toLowerCase();
    if(u==="farenheit") return [(v-32)*5/9,"Celsius"];
    if(u==="celcius") return [(v*9/5)+32,"Fahrenheit"];
    if(u==="centimeters") return [v/2.54,"Inches"];
    if(u==="inches") return [v*2.54,"Centimeters"];
    return [null,"Error"];
  },

  mean(d){ return d.length?d.reduce((a,b)=>a+b)/d.length:0; },

  median(d){
    if(!d.length) return 0;
    d=[...d].sort((a,b)=>a-b);
    let m=Math.floor(d.length/2);
    return d.length%2?d[m]:(d[m-1]+d[m])/2;
  },

  mode(d){
    let c={},m=0,r=[];
    d.forEach(x=>{c[x]=(c[x]||0)+1;m=Math.max(m,c[x])});
    for(let k in c) if(c[k]==m) r.push(Number(k));
    return r;
  },

  standardDeviation(d){
    if(d.length<2) return 0;
    let avg=this.mean(d);
    let v=d.reduce((s,x)=>s+(x-avg)**2,0)/(d.length-1);
    return Math.sqrt(v);
  }
}
