import * as T from 'three';
export const MECHANICAL_FRAME={origin:'shaft-axis / rim-midplane',shaftAxis:[1,0,0],up:[0,0,1],transverse:[0,1,0],sideAssignment:null};
export const TAU=Math.PI*2;
export const wrap=a=>(a%TAU+TAU)%TAU;
/** Periodic functional approximation, not CFD. Positive X rotation lifts on positive Y. */
export function vesselState(angle,{radius=2.25,waterLevel=-1.95,dischargeStart=5.85,dischargeEnd=6.20}={}){
 if(![angle,radius,waterLevel,dischargeStart,dischargeEnd].every(Number.isFinite)||radius<=0||dischargeStart<=Math.PI||dischargeEnd<=dischargeStart||dischargeEnd>TAU)throw new Error('Ungültige Betriebsparameter.');
 const a=wrap(angle),z=radius*Math.cos(a),immersed=z<waterLevel,capacity=Math.min(1,Math.max(0,(waterLevel+radius)/.18));
 let fill=0,state='leer';
 if(immersed){fill=Math.min(capacity,Math.max(0,(waterLevel-z)/.18));state=fill>0?'füllt sich':'leer'}
 else if(capacity>0&&a>Math.PI&&a<dischargeStart){fill=capacity;state='hebt Wasser'}
 else if(capacity>0&&a>=dischargeStart&&a<=dischargeEnd){fill=capacity*(1-(a-dischargeStart)/(dischargeEnd-dischargeStart));state='schüttet aus'}
 const mouth=new T.Vector3(0,0,1).applyMatrix4(new T.Matrix4().makeRotationY(.45).multiply(new T.Matrix4().makeRotationX(110*Math.PI/180))).applyAxisAngle(new T.Vector3(1,0,0),a);
 return {angle:a,y:-Math.sin(a)*radius,z,fill,immersed,state,mouthDirection:mouth.toArray(),discharging:state==='schüttet aus'&&fill>0};
}
const point=p=>Array.isArray(p)&&p.length===3&&p.every(Number.isFinite);
function points(ps,n,label){if(!Array.isArray(ps)||ps.length!==n||!ps.every(point))throw new Error(`${label}: ${n} endliche 3D-Punkte erforderlich.`);return ps.map(p=>new T.Vector3(...p))}
/** A/B set scale and primary axis; C sets plane. C, shaft endpoints and control validate the result. */
export function solveRegistration(source,target,axisSource,axisTarget,control){
 const sv=points(source,3,'Scanreferenzen'),tv=points(target,3,'Zielreferenzen'),as=points(axisSource,2,'Scanachse'),at=points(axisTarget,2,'Zielachse');
 if(!control||!Number.isFinite(control.measured)||control.measured<=0||!Number.isFinite(control.tolerance)||control.tolerance<=0)throw new Error('Kontrollmaß und Toleranz müssen positiv und endlich sein.');
 const cv=points(control.source,2,'Kontrollstrecke');if(cv[0].distanceTo(cv[1])<1e-8)throw new Error('Kontrollstrecke hat keine Länge.');
 const basis=ps=>{const [a,b,c]=ps,x=b.clone().sub(a),ac=c.clone().sub(a),cross=x.clone().cross(ac);if(x.length()<1e-8||ac.length()<1e-8||cross.length()/(x.length()*ac.length())<1e-6)throw new Error('Referenzpunkte sind gleich oder nahezu kollinear.');x.normalize();const z=cross.normalize(),y=z.clone().cross(x);return {origin:a,matrix:new T.Matrix4().makeBasis(x,y,z)}};
 for(const av of[as,at])if(av[0].distanceTo(av[1])<1e-8)throw new Error('Achspunkte müssen verschieden sein.');
 const s=basis(sv),t=basis(tv),scale=tv[0].distanceTo(tv[1])/sv[0].distanceTo(sv[1]);
 const matrix=new T.Matrix4().makeTranslation(...t.origin.toArray()).multiply(t.matrix).multiply(new T.Matrix4().makeScale(scale,scale,scale)).multiply(s.matrix.clone().invert()).multiply(new T.Matrix4().makeTranslation(...s.origin.clone().negate().toArray()));
 const residuals=sv.map((p,i)=>p.clone().applyMatrix4(matrix).distanceTo(tv[i])),rms=Math.sqrt(residuals.reduce((a,b)=>a+b*b,0)/3),sa=as.map(p=>p.applyMatrix4(matrix));
 const axisError=sa[1].clone().sub(sa[0]).angleTo(at[1].clone().sub(at[0]))*180/Math.PI,axisResiduals=sa.map((p,i)=>p.distanceTo(at[i])),axisPositionError=Math.max(...axisResiduals);
 const computed=cv[0].applyMatrix4(matrix).distanceTo(cv[1].applyMatrix4(matrix)),controlError=Math.abs(computed-control.measured),tolerance=control.tolerance;
 const passed=Math.max(...residuals)<=tolerance&&controlError<=tolerance&&axisPositionError<=tolerance&&axisError<=2;
 return {state:passed?'METRICALLY_CALIBRATED':'ROUGH_ALIGNED',matrix_row_major:matrix.clone().transpose().toArray(),scale,residuals,rms,axisResiduals,axisPositionError,axisErrorDeg:axisError,controlError,controlComputed:computed,tolerance,passed,adoption:'review-required'};
}
