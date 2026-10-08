import fs from 'node:fs';import * as T from 'three';
import {cfg,vesselPose,radiusAt,calibratedCycle} from '../src/workbench/calibration.mjs';
import {makeModel,disposeModel} from '../src/workbench/geometry.mjs';
const r=cfg.reference;
function envelope(c){const ps=[vesselPose(0,c),vesselPose(Math.PI/12,c)];let penetrations=0,minGap=Infinity;
 for(const [a,b] of [[0,1],[1,0]])for(let iz=0;iz<=60;iz++)for(let j=0;j<48;j++){
  const z=-r.height/2+iz*r.height/60,rr=radiusAt(z)/Math.cos(Math.PI/12),v=new T.Vector3(rr*Math.cos(j*Math.PI/24),rr*Math.sin(j*Math.PI/24),z).applyQuaternion(ps[a].quaternion).add(ps[a].position).sub(ps[b].position).applyQuaternion(ps[b].quaternion.clone().invert());
  if(Math.abs(v.z)<r.height/2){const gap=Math.hypot(v.x,v.y)-radiusAt(v.z)/Math.cos(Math.PI/12);minGap=Math.min(minGap,gap);if(gap<-.001)penetrations++}
 }
 return {penetratingEnvelopeSamples:penetrations,minEnvelopeGap:Number(minGap.toFixed(5)),sampling:'61 longitudinal x 48 circumferential, both directions; conservative filled-cone envelope, not exact contact proof'};
}
const trials=[];for(const pitchDeg of [100,105,110,115,120,125])for(const yawDeg of [20,32,45,60,75]){const c={...cfg.production,pitchDeg,yawDeg};trials.push({pitchDeg,yawDeg,...envelope(c)})}
const model=makeModel(),rim=model.children.filter(m=>m.userData.family==='COMP-KRUEMMLINGE'),nails=model.children.filter(m=>m.userData.nailPath&&m.userData.slot===0),paths=[];
for(const m of nails){const a=new T.Vector3(...m.userData.nailPath.start).applyMatrix4(m.matrixWorld),b=new T.Vector3(...m.userData.nailPath.end).applyMatrix4(m.matrixWorld),d=b.clone().sub(a),len=d.length(),hits=new T.Raycaster(a,d.normalize(),0,len).intersectObjects(rim);paths.push({id:m.name,length:len,holeMapping:m.userData.nailPath.holes,rimHits:hits.map(h=>({id:h.object.name,distance:h.distance})),start:a.toArray(),end:b.toArray()})}
const cycle=Array.from({length:180},(_,i)=>({degree:i*2,...calibratedCycle(i*Math.PI/90)}));
const report={schema:'ks-calibration-audit/v1',candidate:cfg.production,envelope:envelope(cfg.production),trials,nailPaths:paths,cycle,limits:['No structural proof','Reference dimensions are photo estimates','AABB alone is not used as collision proof','Nail insertion and withdrawal require explicit swept tests and field confirmation']};
fs.writeFileSync('state/reconstruction-loop/ITER-001/geometry-audit.json',JSON.stringify(report,null,2));
console.log(JSON.stringify({envelope:report.envelope,best:trials.sort((a,b)=>a.penetratingEnvelopeSamples-b.penetratingEnvelopeSamples||b.minEnvelopeGap-a.minEnvelopeGap).slice(0,8),paths,discharge:cycle.filter(x=>x.discharging).map(x=>[x.degree,x.inTrough])},null,2));disposeModel(model);
