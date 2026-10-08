// Technical projections are generated once by build-workbench.mjs from the shared mesh model.
import fs from 'node:fs';
const p=JSON.parse(fs.readFileSync('docs/field-kit/model-projections.json'));
if(p.schema!=='ks-technical-projections/v2'||p.sheets.length<8)throw Error('Technical reconstruction projections missing. Run prepare:workbench.');
console.log('Verified shared technical projection set:',p.sheets.length);
