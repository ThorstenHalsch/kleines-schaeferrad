"""Verify archived original bytes and structured evidence references; no mutations."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def read(path):
    return json.loads((ROOT / path).read_text())

manifest = read('evidence/manifest.json')
assert len(manifest['assets']) == 43
source_ids = {a['id'] for a in manifest['assets']} | {s['id'] for s in manifest['context_sources']}
assert len({a['sha256'] for a in manifest['assets']}) == 43
for a in manifest['assets']:
    data = (ROOT / a['archive']['path']).read_bytes()
    assert len(data) == a['bytes'], a['id']
    assert hashlib.sha256(data).hexdigest() == a['sha256'], a['id']
    assert hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() == a['git_blob_sha1'], a['id']
    check = a['prior_manifest_check']
    assert check.get('missing_from_prior_manifest') or (check['size_matches'] and check['sha256_matches'])
for d in manifest['derived_assets']:
    assert hashlib.sha256((ROOT / d['path']).read_bytes()).hexdigest() == d['sha256']
    assert set(d['parents']) <= source_ids
claims = read('data/geometry.claims.json')['claims']
claim_ids = {c['id'] for c in claims}
assert len(claim_ids) == len(claims)
for c in claims:
    assert c['evidence_class'] in {'measured','observed-current','historical-drawing','external-context','inferred','conflicting','unknown'}
    assert c['confidence'] in {'high','medium','low','unknown'}
    assert c['provenance'] and {p['source_id'] for p in c['provenance']} <= source_ids
    assert not c['as_built_eligible']
analyses = read('data/source-analyses.json')['sources']
assert len(analyses) == 43 and {s['source_id'] for s in analyses} == {a['id'] for a in manifest['assets']}
for s in analyses:
    assert set(s['claim_ids']) <= claim_ids
graph = read('data/assembly.graph.json')
nodes = {n['id'] for n in graph['nodes']}
for e in graph['relations']:
    assert e['from'] in nodes and e['to'] in nodes
    assert set(e['provenance']) <= source_ids and set(e['claim_ids']) <= claim_ids
for instance in graph['instances']:
    assert instance['family'] in nodes and set(instance['provenance']) <= source_ids
for component in read('data/components.json')['components']:
    assert set(component['claim_ids']) <= claim_ids
for conflict in read('data/conflicts.json')['conflicts']:
    assert set(conflict['claim_ids']) <= claim_ids
    assert conflict['conflict_claim'] in claim_ids and set(conflict['sources']) <= source_ids
    assert conflict['selected_as_built_value'] is None
print(f"Verified 43 original files, {len(manifest['derived_assets'])} derivatives, {len(claims)} claims and graph/conflict references")
