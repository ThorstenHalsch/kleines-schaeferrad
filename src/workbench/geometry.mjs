import * as T from 'three';
import {mergeGeometries} from 'three/addons/utils/BufferGeometryUtils.js';
import armConfig from '../../data/arm-hypotheses.json' with {type:'json'};
import config from '../../data/hypothesis.parameters.json' with { type: 'json' };
export { config };
export const p = Object.fromEntries(Object.entries(config.parameters).map(([k,v])=>[k,v.value]));
export const views = {gesamt:[6,-7,5],land:[-9,0,0],wasser:[9,0,0],welle:[1,-7,3],kranz:[-8,0,0],kumpf:[-5,-4,3],schaufeln:[5,-5,3]};
export function makeModel(variant='A', explode=0, options={}) {
 const group=new T.Group(); group.name='hypothesis';
 const shape=options.armShape||'unknown',layers=options.armLayers||'staggered';
 const add=(id,family,geometry,position=[0,0,0],rotation=[0,0,0],stationary=false)=>{
  const material=new T.MeshStandardMaterial({color:stationary?0x738178:family.includes('KUMPF')||family==='COMP-KUEMPFE'?0xb68a44:0x377d79,transparent:true,opacity:stationary?.25:.58,roughness:1,side:T.DoubleSide});
  const mesh=new T.Mesh(geometry,material);mesh.position.set(...position);mesh.rotation.set(...rotation);mesh.userData={id,family,stationary,status:stationary?'context-hypothesis':'hypothesis',parameters:'data/hypothesis.parameters.json'};
  const edges=new T.LineSegments(new T.EdgesGeometry(geometry,25),new T.LineBasicMaterial({color:stationary?0x758477:0x1a4946,transparent:true,opacity:.8}));mesh.add(edges);group.add(mesh);return mesh;
 };
 add('HYP-SHAFT','COMP-SHAFT',new T.BoxGeometry(p.shaftLength,p.shaftWidth,p.shaftWidth));
 for(const [side,sign] of [['LAND',-1],['WATER',1]]) {
  const x=sign*(p.ringDistance/2+explode*.8);
  for(let i=0;i<p.armsPerPlane;i++) {
   const layer=layers==='coplanar'?0:(i-1)*p.armDepth*(layers==='reverse'?-1:1), pieces=[];
   for(const sign of [-1,1]) {
    const points=shape==='dogleg'?[[0,0,sign*.4],[armConfig.display_only.dogleg_offset*sign,0,sign*.85],[armConfig.display_only.dogleg_offset*sign,0,sign*p.innerRadius]]:[[0,0,sign*.4],[0,0,sign*p.innerRadius]];
    for(let j=1;j<points.length;j++) {const a=new T.Vector3(...points[j-1]),b=new T.Vector3(...points[j]),v=b.clone().sub(a),g=new T.BoxGeometry(p.armDepth,p.armWidth,v.length());g.applyQuaternion(new T.Quaternion().setFromUnitVectors(new T.Vector3(0,0,1),v.normalize()));const mid=a.clone().add(b).multiplyScalar(.5);g.translate(...mid.toArray());pieces.push(g)}
   }
   const geometry=mergeGeometries(pieces);pieces.forEach(g=>g.dispose());const mesh=add(`HIST-ARM-${side}-${i+1}-${i+4}`,'COMP-ARMS',geometry,[x+layer,0,0],[i*Math.PI/3,0,0]);mesh.userData.armShape=shape;mesh.userData.armLayers=layers;mesh.userData.hiddenCenterOmitted=true;mesh.material.wireframe=shape==='unknown';
  }
  const unknown=add(`UNKNOWN-JOINT-${side}`,'COMP-SHAFT',new T.SphereGeometry(armConfig.display_only.unknown_zone_radius,12,8),[x,0,0]);unknown.material.wireframe=true;unknown.userData.unknownZone=true;
  for(let i=0;i<p.segmentsPerPlane;i++) {
   const shape=new T.Shape(),a=i*Math.PI/3+.012,b=(i+1)*Math.PI/3-.012;
   shape.moveTo(-Math.sin(a)*p.outerRadius,Math.cos(a)*p.outerRadius);
   for(let j=1;j<=20;j++){const t=a+(b-a)*j/20;shape.lineTo(-Math.sin(t)*p.outerRadius,Math.cos(t)*p.outerRadius)}
   for(let j=20;j>=0;j--){const t=a+(b-a)*j/20;shape.lineTo(-Math.sin(t)*p.innerRadius,Math.cos(t)*p.innerRadius)}shape.closePath();
   const g=new T.ExtrudeGeometry(shape,{depth:p.rimWidth,bevelEnabled:false,steps:1});
   // Local shape XY maps to mechanical YZ; extrusion Z maps to X.
   g.applyMatrix4(new T.Matrix4().set(0,0,1,0, 1,0,0,0, 0,1,0,0, 0,0,0,1));g.translate(-p.rimWidth/2,0,0);
   const t=(a+b)/2;
   add(`HIST-KRU-${side}-${String(i+1).padStart(2,'0')}`,'COMP-KRUEMMLINGE',g,[x,-Math.sin(t)*explode*.25,Math.cos(t)*explode*.25]);
  }
 }
 for(let i=0;i<p.vesselCount;i++) {
  const a=i*Math.PI*2/p.vesselCount,r=p.outerRadius+.13+explode*.45;
  // Hollow open vessel; wall thickness is the only sourced A/B variation.
  const outer=p.vesselRadius,inner=outer-config.variants[variant].staveThickness;
  const points=[new T.Vector2(0,-p.vesselHeight/2),new T.Vector2(outer,-p.vesselHeight/2),new T.Vector2(outer,p.vesselHeight/2),new T.Vector2(inner,p.vesselHeight/2),new T.Vector2(inner,-p.vesselHeight/2+.025),new T.Vector2(0,-p.vesselHeight/2+.025)];
  const g=new T.LatheGeometry(points,12);g.rotateX(Math.PI/2);
  add(`EXPECTED-KUM-${String(i+1).padStart(2,'0')}`,'COMP-KUEMPFE',g,[-p.ringDistance/2-explode*1.2,-Math.sin(a)*r,Math.cos(a)*r],[a,0,0]);
 }
 for(let i=0;i<p.paddleCount;i++) {const a=(i+.5)*Math.PI*2/p.paddleCount,r=p.outerRadius+.15+explode*.45;add(`EXPECTED-PAD-${String(i+1).padStart(2,'0')}`,'COMP-PADDLES',new T.BoxGeometry(p.ringDistance,.09,.42),[explode*.2,-Math.sin(a)*r,Math.cos(a)*r],[a,0,0]);}
 for(const sign of [-1,1]){
  add(`HYP-BEARING-${sign}`,'COMP-BEARINGS',new T.BoxGeometry(.38,.55,.3),[sign*1.65,0,-.28],[0,0,0],true);
  add(`CTX-BEARING-STAND-${sign}`,'COMP-BEARING-STANDS',new T.BoxGeometry(.34,.42,2.35),[sign*1.65,0,-1.45],[0,0,0],true);
 }
 // Stationary timber context seen around the wheel. All dimensions and exact joints are display hypotheses.
 add('CTX-MAIN-BEAM-FRONT','COMP-FRAME-MAIN',new T.BoxGeometry(.28,5.25,.28),[.55,0,-.82],[0,0,0],true);
 add('CTX-MAIN-BEAM-REAR','COMP-FRAME-MAIN',new T.BoxGeometry(.28,4.65,.24),[-.95,0,-1.02],[0,0,0],true);
 for(const y of [-2.25,-.78,.78,2.25]) add(`CTX-POST-${y}`,'COMP-FRAME-MAIN',new T.BoxGeometry(.3,.3,2.45),[.55,y,-1.92],[0,0,0],true);
 add('CTX-LOWER-RAIL','COMP-FRAME-LOWER',new T.BoxGeometry(.28,4.7,.24),[.5,0,-2.55],[0,0,0],true);
 add('CTX-LOWER-RAIL-REAR','COMP-FRAME-LOWER',new T.BoxGeometry(.28,3.8,.22),[-.9,0,-2.35],[0,0,0],true);
 for(const [y,rot] of [[-1.55,.62],[1.55,-.62]]) add(`CTX-DIAG-${y}`,'COMP-FRAME-LOWER',new T.BoxGeometry(.22,2.25,.2),[.48,y,-1.72],[rot,0,0],true);
 add('CTX-SIDE-GUIDE-A','COMP-FRAME-SIDE',new T.BoxGeometry(1.8,.2,.22),[-.2,-2.6,-.65],[0,.12,0],true);
 add('CTX-SIDE-GUIDE-B','COMP-FRAME-SIDE',new T.BoxGeometry(1.8,.2,.22),[-.2,2.6,-.65],[0,-.12,0],true);
 add('HYP-TROUGH','COMP-TROUGH',new T.BoxGeometry(.55,2.4,.2),[-1.15,0,1.8],[0,0,0],true);
 group.updateMatrixWorld(true);return group;
}
export function matchesFamily(mesh, selected) {
 const f=mesh.userData.family;
 if(selected==='ALL')return true;
 if(['COMP-RIMS','COMP-RIM-LAND','COMP-RIM-WATER'].includes(selected))return f==='COMP-KRUEMMLINGE'&&(!selected.endsWith('LAND')||mesh.userData.id.includes('LAND'))&&(!selected.endsWith('WATER')||mesh.userData.id.includes('WATER'));
 if(['COMP-KUMPF-STAVES','COMP-KUMPF-BASE','COMP-KUMPF-HOOPS'].includes(selected))return f==='COMP-KUEMPFE';
 if(selected.startsWith('COMP-HUB-'))return f==='COMP-SHAFT'||f==='COMP-ARMS';
 return f===selected;
}
export function disposeModel(model){model.traverse(o=>{o.geometry?.dispose();if(o.material){for(const m of [].concat(o.material))m.dispose()}})}
