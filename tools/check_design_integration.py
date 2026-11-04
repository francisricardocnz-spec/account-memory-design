#!/usr/bin/env python3
"""Check anonymous synthesis and concept compatibility; not original-source or product verification."""
import collections
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check():
    failures = []

    def require(condition, rule, item=None):
        if not condition:
            failures.append({'rule': rule, 'item': item})

    expected = {'README.md', 'UNIFIED-INTERPRETATION.md', 'FIELD-CROSSWALK.md', 'field-crosswalk.json'}
    actual = {str(p.relative_to(ROOT / 'references')) for p in (ROOT / 'references').rglob('*') if p.is_file()}
    require(actual == expected, 'synthesis_only_reference_directory')
    cross = json.loads((ROOT / 'references/field-crosswalk.json').read_text())
    require(cross['status'] == 'anonymous_design_crosswalk_not_runtime_adapter', 'design_status')
    require(cross['automatic_import_allowed'] is False and cross['source_scripts_run'] is False and cross['product_tests_run'] is False, 'no_import_or_runtime_claim')
    registry = cross['target_registry']
    require(registry['path'] == 'examples/field-registry.json', 'canonical_target_path')
    raw = (ROOT / registry['path']).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == registry['sha256'], 'target_fingerprint')
    target = json.loads(raw)
    fields = {x['field_id']: x for x in target['fields']}
    require(len(fields) == registry['field_count'] == 33, 'target_field_count')
    require(sum(x['enabled_initially'] for x in fields.values()) == registry['enabled_initially'] == 21 and registry['disabled_initially'] == 12, 'target_enabled_count')
    require(registry['version'] == target['registry_version'], 'target_version')
    rows = cross['items']
    require(len(rows) == cross['concept_count'] == 105 and len({x['concept_id'] for x in rows}) == 105, '105_unique_concepts')
    require([x['concept_index'] for x in rows] == list(range(1, 106)), 'concept_sequence')
    require(dict(collections.Counter(x['mapping_mode'] for x in rows)) == cross['mapping_mode_counts'], 'mode_counts')
    allowed_keys = {'concept_index', 'concept_id', 'concept_label', 'input_value_kinds', 'mapping_mode', 'target_claim_fields', 'target_objects', 'target_field_policies', 'review_stage', 'interpretation', 'automatic_import_allowed', 'adds_public_registry_field', 'implemented', 'manual_approval'}
    for row in rows:
        cid = row['concept_id']
        require(set(row) == allowed_keys, 'concept_schema', cid)
        require(row['automatic_import_allowed'] is False and row['adds_public_registry_field'] is False and row['implemented'] is False and row['manual_approval'] is None, 'design_only_row', cid)
        require(set(row['target_claim_fields']) == set(row['target_field_policies']), 'target_policy_keys', cid)
        for field in row['target_claim_fields']:
            require(field in fields and row['target_field_policies'][field] == fields.get(field), 'target_policy_matches_canonical', cid)
    md = (ROOT / 'references/FIELD-CROSSWALK.md').read_text()
    require(re.findall(r'^\| (\d+) \|', md, re.M) == [str(i) for i in range(1, 106)], '105_markdown_rows')
    for row in rows:
        require(('`' + row['concept_id'] + '`') in md, 'markdown_concept_id', row['concept_id'])
    chapter = (ROOT / 'docs/deep-dive/11-source-integration.md').read_text()
    require(len(re.findall(r'^## \d+\.', chapter, re.M)) == 10, 'integration_chapter_sections')
    return {'passed': not failures, 'scope': 'offline_anonymous_synthesis_and_concept_crosswalk_only', 'concepts_crosswalked': len(rows), 'target_fields': len(fields), 'target_enabled_initially': 21, 'target_disabled_initially': 12, 'original_materials_published': False, 'external_software_run': False, 'external_author_tests_run': False, 'product_tests_run': False, 'findings': failures}


if __name__ == '__main__':
    report = check()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report['passed'] else 1)
