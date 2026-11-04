#!/usr/bin/env python3
"""Synthetic normalized-unit cost arithmetic only; not a bill, quote or load test."""
import copy
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def number(value):
    if isinstance(value, bool):
        raise ValueError('Boolean is not a model quantity')
    result = Decimal(str(value))
    if not result.is_finite() or result < 0:
        raise ValueError('Expected finite nonnegative quantity')
    return result

def estimate(config):
    v = {k:number(x) for k,x in config['parameters'].items()}
    price = {k:number(x) for k,x in config['prices'].items() if k!='unit'}
    for field in ['memory_input_fraction','memory_cache_fraction','extra_calls_per_turn']:
        if v[field] > 1:
            raise ValueError('Fraction outside zero to one')
    turns = v['dau'] * v['turns_per_dau'] * v['days']
    main_calls = turns * v['main_calls_per_turn']
    memory_input = main_calls * v['memory_input_fraction'] * v['memory_input_tokens']
    cached = memory_input * v['memory_cache_fraction']
    million = Decimal(1000000)
    memory_input_cost = ((memory_input-cached)*price['uncached_input_per_million']+cached*price['cached_input_per_million'])/million
    proposal_cost = turns*v['proposal_output_tokens_per_turn']*price['output_per_million']/million
    extra_cost = turns*v['extra_calls_per_turn']*(v['extra_input_tokens']*price['uncached_input_per_million']+v['extra_output_tokens']*price['output_per_million'])/million
    baseline = main_calls*(v['baseline_input_tokens']*price['uncached_input_per_million']+v['baseline_output_tokens']*price['output_per_million'])/million
    result = {'monthly_user_turns':turns,'monthly_main_model_calls':main_calls,'monthly_memory_input_tokens':memory_input,'memory_input_cost':memory_input_cost,'proposal_output_cost':proposal_cost,'extra_memory_call_cost':extra_cost,'memory_increment_cost':memory_input_cost+proposal_cost+extra_cost,'baseline_main_model_cost':baseline,'combined_modeled_cost':baseline+memory_input_cost+proposal_cost+extra_cost}
    return {'unit':config['prices']['unit'],'infrastructure_cost':'not_modeled','real_provider_price':'not_used',**{k:format(value,'f') for k,value in result.items()}}

def compare(config):
    scenarios = [('baseline',{}),('memory_input_plus_500',{'memory_input_tokens':config['parameters']['memory_input_tokens']+500}),('proposal_output_mean_300',{'proposal_output_tokens_per_turn':300}),('extra_calls_ten_percent',{'extra_calls_per_turn':0.1}),('memory_input_cache_thirty_percent',{'memory_cache_fraction':0.3})]
    output=[]
    base=estimate(config)
    for name,changes in scenarios:
        candidate=copy.deepcopy(config);candidate['parameters'].update(changes);row=estimate(candidate)
        row['scenario']=name;row['memory_increment_difference']=format(Decimal(row['memory_increment_cost'])-Decimal(base['memory_increment_cost']),'f');output.append(row)
    return {'synthetic':True,'scope':'normalized_formula_only','scenarios':output}

if __name__=='__main__':
    print(json.dumps(compare(json.loads((ROOT/'examples/cost-scenario.json').read_text())),ensure_ascii=False,indent=2))
