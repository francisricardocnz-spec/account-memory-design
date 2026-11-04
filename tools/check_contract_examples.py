#!/usr/bin/env python3
"""Offline shape/API example checks. No server, authority or database is exercised."""
import copy
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    raise SystemExit('Install optional requirements-dev.txt in a virtual environment first.')

ROOT = Path(__file__).resolve().parents[1]

def read(name):
    return json.loads((ROOT / name).read_text(encoding='utf-8'))

def pointer(document, fragment):
    current = document
    for token in fragment.lstrip('/').split('/') if fragment else []:
        current = current[token.replace('~1', '/').replace('~0', '~')]
    return current

def check_refs(document, path):
    count = 0
    def walk(node):
        nonlocal count
        if isinstance(node, dict):
            if '$ref' in node:
                target = node['$ref']
                filepart, _, fragment = target.partition('#')
                resolved = (path.parent / filepart).resolve() if filepart else path
                if not resolved.is_relative_to(ROOT) or not resolved.is_file():
                    raise ValueError('Reference leaves the public bundle or is missing')
                pointer(json.loads(resolved.read_text()), fragment)
                count += 1
            for item in node.values():
                walk(item)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk(document)
    return count

def run():
    if 'date-time' not in jsonschema.FormatChecker.checkers:
        raise SystemExit('date-time checker unavailable; install requirements-dev.txt including format extras.')
    schemas = {name: read('schemas/' + name + '.schema.json') for name in ['proposal', 'context-bundle', 'correction-receipt']}
    references = 0
    for name, schema in schemas.items():
        jsonschema.Draft202012Validator.check_schema(schema)
        references += check_refs(schema, ROOT / ('schemas/' + name + '.schema.json'))
    validators = {name: jsonschema.Draft202012Validator(schema, format_checker=jsonschema.FormatChecker()) for name, schema in schemas.items()}
    examples = {name: read('examples/' + name + '.json')['data'] for name in schemas}
    results = []
    def case(case_id, schema, instance, expected_valid, boundary=False):
        actual = validators[schema].is_valid(instance)
        results.append({'id': case_id, 'schema': schema, 'expected_shape_valid': expected_valid, 'observed_shape_valid': actual, 'passed': actual == expected_valid, 'runtime_check_still_required': boundary, 'product_test': False})
    def altered(name, mutate):
        value = copy.deepcopy(examples[name]); mutate(value); return value
    case('P01', 'proposal', examples['proposal'], True)
    case('P02', 'proposal', altered('proposal', lambda x: x.update(owner_account_id='example-account-other')), False)
    case('P03', 'proposal', altered('proposal', lambda x: x['claims'][0].update(lifecycle='active')), False)
    case('P04', 'proposal', altered('proposal', lambda x: x['claims'][0].update(field_id='arbitrary.path')), False)
    case('P05', 'proposal', altered('proposal', lambda x: x['claims'][0].update(field_id='trait.stable_pattern')), False)
    case('P06', 'proposal', altered('proposal', lambda x: x['claims'][0].update(value={'kind':'reference','ref':{'entity_type':'event','id':'example-event-a','revision':'1'}})), False)
    case('P07', 'proposal', altered('proposal', lambda x: x['claims'][0].update(epistemic_status='independently_verified')), False)
    case('P08', 'proposal', altered('proposal', lambda x: x['claims'][0].update(value={'kind':'text','text':'x'*1001})), False)
    case('P09', 'proposal', altered('proposal', lambda x: x.update(source_bindings=x['source_bindings']*33)), False)
    case('P10', 'proposal', altered('proposal', lambda x: x['claims'][0].update(value=None)), False)
    case('P11', 'proposal', altered('proposal', lambda x: x['claims'][0].update(value=None,missing_reason='unknown')), True)
    case('P12', 'proposal', altered('proposal', lambda x: x['claims'][0]['valid_time'].update(start='not-a-time')), False)
    case('P13', 'proposal', altered('proposal', lambda x: x['source_bindings'][0].update(quote='完全不同的虚构句')), True, True)
    case('P14', 'proposal', altered('proposal', lambda x: x['claims'][0].update(field_id='hypothesis.contextual_pattern',epistemic_status='inferred',support='insufficient')), True, True)
    case('C01', 'context-bundle', examples['context-bundle'], True)
    case('C02', 'context-bundle', altered('context-bundle', lambda x: x['segments'][1].update(kind='current_task')), False)
    case('C03', 'context-bundle', altered('context-bundle', lambda x: x['token_accounting'].update(total_input_tokens=9000)), True, True)
    case('C04', 'context-bundle', altered('context-bundle', lambda x: x['authority_versions'].update(consent_version='1')), True, True)
    case('R01', 'correction-receipt', examples['correction-receipt'], True)
    case('R02', 'correction-receipt', altered('correction-receipt', lambda x: x.update(independent_ledger_state='pending')), False)
    case('R03', 'correction-receipt', altered('correction-receipt', lambda x: x.update(state='committed')), False)
    case('R04', 'correction-receipt', altered('correction-receipt', lambda x: x.update(result_code='RESULT_UNKNOWN',state='committed')), False)
    api = read('api/openapi.json'); expected = read('api/operations.json')['operations']
    assert api['openapi'] == '3.1.1' and api['x-design-status'] == 'reference-not-production'
    actual = {(method.upper(),path):op for path, methods in api['paths'].items() for method,op in methods.items()}
    assert len(actual) == len(expected) == 9
    ids = []
    for operation in expected:
        item = actual[(operation['method'],operation['path'])]
        assert item['operationId'] == operation['operation_id']
        assert set(item['responses']) == set(operation['required_response_codes'])
        assert item['security'] == [{'BearerAuth': []}]
        ids.append(item['operationId'])
    assert len(set(ids)) == 9
    references += check_refs(api, ROOT / 'api/openapi.json')
    # Extract the local control schemas; they have no component refs.
    for name in ['ControlRequest', 'ControlReceipt']:
        jsonschema.Draft202012Validator.check_schema(api['components']['schemas'][name])
    control = api['components']['schemas']['ControlRequest']
    # EntityRef is embedded with a local component ref in only other operations; request item schema is inlined.
    cv = jsonschema.Draft202012Validator(control, format_checker=jsonschema.FormatChecker())
    control_cases = [
        ('O01', {'selector_kind':'account_memory','target_refs':[],'include_independent_quotes':True}, True),
        ('O02', {'selector_kind':'source_lineage','target_refs':[{'entity_type':'source','id':'example-source-a','revision':'1'}],'include_independent_quotes':False}, False),
        ('O03', {'selector_kind':'account_memory','target_refs':[{'entity_type':'source','id':'example-source-a','revision':'1'}],'include_independent_quotes':True}, False),
    ]
    for case_id, data, wanted in control_cases:
        observed = cv.is_valid(data)
        results.append({'id':case_id,'schema':'OpenAPI-ControlRequest','expected_shape_valid':wanted,'observed_shape_valid':observed,'passed':wanted==observed,'runtime_check_still_required':False,'product_test':False})
    receipt_validator = jsonschema.Draft202012Validator(api['components']['schemas']['ControlReceipt'])
    control_receipt = {'operation_id':'example-control-a','state':'committed','new_use_state':'blocked','independent_ledger_state':'pending','phase':'purging','external_copy_state':'unknown','all_physical_copies_deleted':False}
    for case_id, data, wanted in [
        ('O04', control_receipt, False),
        ('O05', dict(control_receipt,independent_ledger_state='durable',phase='completed',all_physical_copies_deleted=True), False),
    ]:
        observed=receipt_validator.is_valid(data)
        results.append({'id':case_id,'schema':'OpenAPI-ControlReceipt','expected_shape_valid':wanted,'observed_shape_valid':observed,'passed':wanted==observed,'runtime_check_still_required':False,'product_test':False})
    article=(ROOT/'docs/deep-dive/03-api-and-storage.md').read_text()
    import re
    confirmation_example=json.loads(re.findall(r'```json\n(.*?)\n```',article,re.S)[0])
    confirm_validator=jsonschema.Draft202012Validator(dict(api,**{'$ref':'#/components/schemas/ConfirmRequest'}),format_checker=jsonschema.FormatChecker())
    assert confirm_validator.is_valid(confirmation_example), 'Article JSON example diverges from API shape'
    return {'passed':all(x['passed'] for x in results),'scope':'public_contract_examples_only','schema_meta_checks':3,'api_manifest_operations':9,'resolved_local_references':references,'shape_case_count':len(results),'runtime_boundaries_demonstrated':sum(x['runtime_check_still_required'] for x in results),'product_tests_run':False,'results':results}

if __name__ == '__main__':
    result = run()
    print(json.dumps(result,ensure_ascii=False,indent=2))
    sys.exit(0 if result['passed'] else 1)
