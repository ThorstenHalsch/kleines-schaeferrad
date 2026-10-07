const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const pt=(p)=>p.join(',');
function primitive(p){
 const cls=`guide-${p.style||'solid'}`;
 if(p.type==='circle')return `<circle class="${cls}" cx="${p.cx}" cy="${p.cy}" r="${p.r}"/>`;
 if(p.type==='rect')return `<rect class="${cls}" x="${p.x}" y="${p.y}" width="${p.w}" height="${p.h}"/>`;
 if(p.type==='line')return `<line class="${cls}" x1="${p.x1}" y1="${p.y1}" x2="${p.x2}" y2="${p.y2}"/>`;
 if(p.type==='polyline')return `<polyline class="${cls}" points="${p.points.map(pt).join(' ')}"/>`;
 if(p.type==='arc'){
  const r=Math.PI/180,a=p.a0*r,b=p.a1*r,x1=p.cx+Math.cos(a)*p.r,y1=p.cy+Math.sin(a)*p.r,x2=p.cx+Math.cos(b)*p.r,y2=p.cy+Math.sin(b)*p.r,large=Math.abs(p.a1-p.a0)>180?1:0;
  return `<path class="${cls}" d="M ${x1} ${y1} A ${p.r} ${p.r} 0 ${large} 1 ${x2} ${y2}"/>`;
 }
 if(p.type==='trapezoid')return `<polygon class="${cls}" points="${p.points.map(pt).join(' ')}"/>`;
 return '';
}
function callout(c,active){
 const cls=`guide-callout guide-${c.type} ${active?'is-active':''}`;
 if(c.type==='measure')return `<g class="${cls}"><line x1="${c.x1}" y1="${c.y1}" x2="${c.x2}" y2="${c.y2}"/><circle cx="${c.x1}" cy="${c.y1}" r="1.2"/><circle cx="${c.x2}" cy="${c.y2}" r="1.2"/><text x="${(c.x1+c.x2)/2}" y="${(c.y1+c.y2)/2-2}">${esc(c.id)}</text></g>`;
 if(c.type==='photo'){const right=c.x>80,tx=right?c.x-4:c.x+4,anchor=right?'end':'start';return `<g class="${cls}"><line x1="${c.x}" y1="${c.y}" x2="${c.tx}" y2="${c.ty}"/><rect x="${c.x-3}" y="${c.y-2.2}" width="6" height="4.4" rx=".7"/><circle cx="${c.x}" cy="${c.y}" r="1.1"/><text x="${tx}" y="${c.y-3}" text-anchor="${anchor}">${esc(c.id)}</text></g>`;}
 if(c.type==='scan'||c.type==='datum'){const right=c.x>80,tx=right?c.x-4:c.x+4,anchor=right?'end':'start';return `<g class="${cls}"><circle cx="${c.x}" cy="${c.y}" r="3"/><path d="M ${c.x-4} ${c.y} h 8 M ${c.x} ${c.y-4} v 8"/><text x="${tx}" y="${c.y-3}" text-anchor="${anchor}">${esc(c.id)}</text></g>`;}
 if(c.type==='unknown')return `<g class="${cls}"><circle cx="${c.x}" cy="${c.y}" r="4"/><text class="question-mark" x="${c.x}" y="${c.y+2}">?</text></g>`;
 return '';
}
export function renderGuide(guide,mode='overview'){
 const type=mode==='Fotos'?'photo':mode==='Messung'?'measure':mode==='Auftrag'?'overview':mode==='Erklärung / offen'?'unknown':'overview';
 const callouts=guide.callouts.map(c=>callout(c,type==='overview'||c.type===type||(type==='unknown'&&c.type==='unknown'))).join('');
 const legend=guide.callouts.map(c=>`<li class="${type==='overview'||c.type===type?'is-active':''}"><strong>${esc(c.id)}</strong> ${esc(c.label)}</li>`).join('');
 return `<figure class="task-guide"><div class="guide-canvas"><svg viewBox="0 0 100 100" role="img" aria-label="${esc(guide.title)}">${guide.primitives.map(primitive).join('')}${callouts}</svg></div><figcaption><strong>${esc(guide.title)}</strong><p>${esc(guide.note)}</p><ul>${legend}</ul></figcaption></figure>`;
}
