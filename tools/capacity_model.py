#!/usr/bin/env python3
"""Recalculate a synthetic capacity scenario. No network or database access."""
import json
import math
import sys
from pathlib import Path


def calculate(scenario):
    keys = ['dau', 'turns_per_dau', 'memory_requests_per_turn', 'peak_to_average',
            'main_model_calls_per_turn', 'mean_model_occupancy_seconds', 'memory_owners',
            'mean_items_per_owner', 'effective_bytes_per_item', 'history_multiplier',
            'index_overhead', 'online_copies', 'backup_equivalent_copies']
    for key in keys:
        value = scenario[key]
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise ValueError('Expected a finite nonnegative number: ' + key)
    turns = scenario['dau'] * scenario['turns_per_dau']
    items = scenario['memory_owners'] * scenario['mean_items_per_owner']
    logical = items * scenario['effective_bytes_per_item']
    primary = logical * scenario['history_multiplier'] * (1 + scenario['index_overhead'])
    return {
        'status': 'formula_only_not_load_test',
        'turns_per_day': turns,
        'memory_peak_qps': turns * scenario['memory_requests_per_turn'] / 86400 * scenario['peak_to_average'],
        'model_peak_concurrency': turns * scenario['main_model_calls_per_turn'] / 86400 * scenario['peak_to_average'] * scenario['mean_model_occupancy_seconds'],
        'current_memory_items': items,
        'current_logical_bytes': logical,
        'primary_modeled_bytes': primary,
        'modeled_bytes_with_copies': primary * (scenario['online_copies'] + scenario['backup_equivalent_copies']),
        'currency_cost': None,
        'price_basis': 'not_configured',
    }


if __name__ == '__main__':
    default = Path(__file__).resolve().parents[1] / 'examples/capacity-scenario.json'
    scenario_path = Path(sys.argv[1]) if len(sys.argv) > 1 else default
    result = calculate(json.loads(scenario_path.read_text(encoding='utf-8')))
    print(json.dumps(result, ensure_ascii=False, indent=2, allow_nan=False))
