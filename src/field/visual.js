const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
export function renderGuide(guide){
 const base=document.getElementById('field-app').dataset.base,src=base+guide.visual_asset;
 return `<figure class="task-guide"><div class="guide-canvas"><a href="${esc(src)}" target="_blank" rel="noopener" aria-label="${esc(guide.title)} vergrößern"><img src="${esc(src)}" alt="${esc(guide.title)} · ${guide.visual_kind==='current-photo-overlay'?'Originalfoto mit Aufnahmepunkten':'technische Projektion der Rekonstruktion'}"/></a></div><figcaption><strong>${esc(guide.title)}</strong><p>${esc(guide.note)}</p><ul>${guide.labels.map(label=>`<li>${esc(label)}</li>`).join('')}</ul><a href="${base}drawings/${guide.sheet}.svg" target="_blank" rel="noopener">Technisches Blatt vergrößern</a></figcaption></figure>`;
}
