/* satin/silk drape renderer: draws smooth folds onto a canvas */
function drawSilk(cv,o){
 const W=cv.clientWidth||innerWidth,H=cv.clientHeight||innerHeight,sc=.5;
 const w=Math.max(2,Math.round(W*sc)),h=Math.max(2,Math.round(H*sc));cv.width=w;cv.height=h;
 const x=cv.getContext('2d'),img=x.createImageData(w,h),d=img.data;
 const hex=s=>[1,3,5].map(i=>parseInt(s.slice(i,i+2),16));
 const B=hex(o.base),S=hex(o.shadow),Hi=hex(o.hi||'#ffffff');
 let seed=o.seed||7;const rnd=()=>(seed=(seed*16807)%2147483647)/2147483647;
 const ang=(o.angle||-30)*Math.PI/180,waves=[];
 for(let i=0;i<(o.n||6);i++){const a=ang+(rnd()-.5)*.5,f=(.006+rnd()*.012)/sc*(o.freq||1);
  waves.push({kx:Math.cos(a)*f,ky:Math.sin(a)*f,amp:(1.4+rnd()*1.6)/(1+i*.35),ph:rnd()*6.28})}
 const warp={kx:.0021/sc,ky:.0033/sc,amp:28*sc};
 const L=[-.45,-.55,.7],ln=Math.hypot(...L);L[0]/=ln;L[1]/=ln;L[2]/=ln;
 const Hh=[L[0],L[1],L[2]+1],hn=Math.hypot(...Hh);Hh[0]/=hn;Hh[1]/=hn;Hh[2]/=hn;
 const str=o.strength||1,sp=o.spec||.26,ex=o.exp||16;
 for(let j=0;j<h;j++)for(let i=0;i<w;i++){
  const wx=i+Math.sin(j*warp.ky+1.3)*warp.amp,wy=j+Math.sin(i*warp.kx+.4)*warp.amp;
  let gx=0,gy=0;
  for(const v of waves){const c=Math.cos(v.kx*wx+v.ky*wy+v.ph)*v.amp;gx+=c*v.kx;gy+=c*v.ky}
  gx*=11*str;gy*=11*str;
  const nl=Math.hypot(gx,gy,1),nx=-gx/nl,ny=-gy/nl,nz=1/nl;
  const df=Math.max(0,nx*L[0]+ny*L[1]+nz*L[2]);
  const s=Math.pow(Math.max(0,nx*Hh[0]+ny*Hh[1]+nz*Hh[2]),ex)*sp;
  const t=Math.min(1,Math.max(0,.78+(df-L[2])*(o.gain||2.6))),k=(j*w+i)*4;
  for(let c=0;c<3;c++)d[k+c]=Math.min(255,S[c]+(B[c]-S[c])*t+Hi[c]*s);
  d[k+3]=255}
 x.putImageData(img,0,0)}
