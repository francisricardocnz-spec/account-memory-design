#!/usr/bin/env python3
"""Offline document checks only. Not a memory service, legal audit or complete secret scanner."""
import json
import hashlib
import math
import os
import xml.etree.ElementTree as ET
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

from capacity_model import calculate

ROOT = Path(__file__).resolve().parents[1]
ALLOWED = {'.md', '.json', '.py', '.svg'}
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
    paths = []
    for directory, dirs, names in os.walk(ROOT):
        dirs[:] = [name for name in dirs if name not in {'.git', '__pycache__', '.venv'}]
        paths.extend(Path(directory) / name for name in names)
    paths.sort()
    for path in paths:
        rel = str(path.relative_to(ROOT))
        if path.suffix not in ALLOWED and rel not in {'.gitignore','requirements-dev.txt'}:
            findings.append({'file': rel, 'rule': 'unexpected_file_type'})
            continue
        text = path.read_text(encoding='utf-8')
        for label, pattern in PATTERNS.items():
            for match in re.finditer(pattern, text):
                findings.append({'file': rel, 'line': text.count('\n', 0, match.start()) + 1, 'rule': label})
        if path.suffix == '.svg':
            graphic = ET.fromstring(text)
            for element in graphic.iter():
                if element.tag.split('}')[-1] in {'script','foreignObject','image'}:
                    findings.append({'file':rel,'rule':'active_or_external_svg'})
                if any(key.split('}')[-1]=='href' and not value.startswith('#') for key,value in element.attrib.items()):
                    findings.append({'file':rel,'rule':'external_svg_reference'})
        if path.suffix == '.json':
            json.loads(text)
        if path.suffix != '.md':
            continue
        if len(re.findall(r'^```', text, re.M)) % 2:
            findings.append({'file': rel, 'rule': 'unbalanced_fence'})
        for block in re.findall(r'```json\n(.*?)\n```', text, re.S):
            json.loads(block)
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
    from cost_sensitivity import compare
    cost=compare(json.loads((ROOT/'examples/cost-scenario.json').read_text()))
    expected=['18672.0000','26592.0000','43632.0000','20976.0000','15464.40000']
    if [row['memory_increment_cost'] for row in cost['scenarios']]!=expected:
        findings.append({'file':'examples/cost-scenario.json','rule':'normalized_cost_arithmetic'})
    report_path=ROOT/'examples/contract-check-results.json'
    if report_path.is_file():
        report=json.loads(report_path.read_text())
        for artifact in report.get('artifact_hashes',[]):
            source=ROOT/artifact['path']
            if not source.is_file() or hashlib.sha256(source.read_bytes()).hexdigest()!=artifact['sha256']:
                findings.append({'file':artifact['path'],'rule':'stale_contract_check_evidence'})
    return {'passed': not findings, 'scope': 'offline_document_bundle_only', 'files_checked': len(paths), 'relative_links_checked': checked_links, 'registry_fields': len(fields), 'planned_product_cases': 32, 'product_tests_run': False, 'findings': findings}


if __name__ == '__main__':
    report = check()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    sys.exit(0 if report['passed'] else 1)
