#!/usr/bin/env python3
"""Offline document checks only. Not a memory service, legal audit or complete secret scanner."""
import json
import math
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from capacity_model import calculate

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'.md', '.json', '.py'}
PATTERNS = {
    'personal_home_path': r'/(?:Users|home)/[A-Za-z0-9._-]+/',
    'windows_home_path': r'[A-Za-z]:\\(?:Users|Documents and Settings)\\[^\\\s]+',
    'github_credential': r'(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{25,})',
    'provider_credential': r'sk-(?:proj-)?[A-Za-z0-9_-]{32,}',
    'private_key': r'-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----',
    'private_network': r'https?://(?:127\.0\.0\.1|localhost|10\.\d+\.\d+\.\d+|192\.168\.\d+\.\d+)(?=[:/\s])',
    'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b',
}


def check():
    findings = []
    checked_links = 0
    paths = sorted(f for f in ROOT.rglob('*') if f.is_file() and not any(part in {'.git', '__pycache__'} for part in f.relative_to(ROOT).parts))
    for path in paths:
        rel = str(path.relative_to(ROOT))
        if path.suffix not in ALLOWED and rel != '.gitignore':
            findings.append({'file': rel, 'rule': 'unexpected_file_type'})
            continue
        text = path.read_text(encoding='utf-8')
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, text):
                findings.append({'file': rel, 'line': text.count('\n', 0, match.start()) + 1, 'rule': label})
        if path.suffix == '.json':
            json.loads(text)
        if path.suffix != '.md':
            continue
        if len(re.findall(r'^```', text, re.M)) % 2:
            findings.append({'file': rel, 'rule': 'unbalanced_fence'})
        for link in re.findall(r'\]\(([^)]+)\)', text):
            if urlparse(link).scheme in {'https', 'http', 'mailto'}:
                continue
            target = unquote(link.split('#')[0]).strip('<>')
            if not target:
                continue
            checked_links += 1
            resolved = (path.parent / target).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                findings.append({'file': rel, 'rule': 'broken_or_outside_link'})
    registry = json.loads((ROOT / 'examples/field-registry.json').read_text())
    fields = registry['fields']
    if len(fields) != 33 or len({x['field_id'] for x in fields}) != 33 or sum(x['enabled_initially'] for x in fields) != 21:
        findings.append({'file': 'examples/field-registry.json', 'rule': 'registry_cardinality'})
    allowed_statuses = {'reported', 'observed', 'inferred', 'measured', 'independently_verified'}
    if not all(set(x['allowed_epistemic_status']) <= allowed_statuses and x['value_kind'] in {'text', 'category', 'boolean', 'measurement', 'reference'} for x in fields):
        findings.append({'file': 'examples/field-registry.json', 'rule': 'registry_types'})
    example = json.loads((ROOT / 'examples/memory-lifecycle.json').read_text())
    if example.get('synthetic') is not True or example['source']['locator']['end'] != len(example['source']['text']):
        findings.append({'file': 'examples/memory-lifecycle.json', 'rule': 'synthetic_source_coordinates'})
    acceptance = (ROOT / 'docs/06-acceptance.md').read_text()
    if re.findall(r'^\| (T\d\d) ', acceptance, re.M) != [f'T{i:02}' for i in range(1, 33)]:
        findings.append({'file': 'docs/06-acceptance.md', 'rule': 'acceptance_ids'})
    result = calculate(json.loads((ROOT / 'examples/capacity-scenario.json').read_text()))
    if not math.isclose(result['memory_peak_qps'], 115.74074074074075) or result['modeled_bytes_with_copies'] != 1020000000000:
        findings.append({'file': 'examples/capacity-scenario.json', 'rule': 'example_arithmetic'})
    return {'passed': not findings, 'scope': 'offline_document_bundle_only', 'files_checked': len(paths), 'relative_links_checked': checked_links, 'registry_fields': len(fields), 'planned_product_cases': 32, 'product_tests_run': False, 'findings': findings}


if __name__ == '__main__':
    report = check()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report['passed'] else 1)
