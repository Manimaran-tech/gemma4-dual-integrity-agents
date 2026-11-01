"""Missing-result sensitivity and paired bounds; never impute observed grades."""
import json
from pathlib import Path


def result(row, collection_errors_unknown=True):
    if row['status']=='unattempted': return None
    code=row.get('test_exit_code')
    repaired=row.get('verified_repair',row.get('verified_resolved'))
    if type(repaired) is not bool or type(code) is not int:
        raise ValueError('Completed scalar fields are malformed')
    if repaired:
        if code!=0 or row.get('patch_bytes',0)<=0:raise ValueError('Repair lacks positive independent evidence')
        return True
    if code<0 or (collection_errors_unknown and code==2):return None
    if code==0:raise ValueError('A nonrepair zero exit requires separately justified fixture classification')
    if code in (1,2):return False
    return None


def summarize(study, collection_errors_unknown=True):
    arms=study['arms']
    if len(arms)!=2 or len(set(arms))!=2:raise ValueError('Require two distinct declared arms')
    grouped={}; seen=set()
    counts={a:dict(assigned=0,completed=0,unattempted=0,verified_repairs=0,known_failed_verdicts=0,
                  unknown=0,collection_errors=0) for a in arms}
    for row in study['assignments']:
        key=(row['arm'],row['task_id'])
        if row['arm'] not in arms or key in seen:raise ValueError('Duplicate or undeclared assignment')
        if row['status'] not in ('unattempted','completed'):raise ValueError('Nonterminal assignment')
        seen.add(key);grouped.setdefault(row['task_id'],{})[row['arm']]=row
        c=counts[row['arm']];c['assigned']+=1;c[row['status']]+=1
        state=result(row,collection_errors_unknown)
        c['verified_repairs']+=state is True;c['known_failed_verdicts']+=state is False;c['unknown']+=state is None
        c['collection_errors']+=row.get('test_exit_code')==2
    if any(set(pair)!=set(arms) for pair in grouped.values()):raise ValueError('Missing planned paired assignment')
    both_known=discordant_a=discordant_b=0
    lower=upper=0
    for pair in grouped.values():
        a,b=[result(pair[arm],collection_errors_unknown) for arm in arms]
        both_known+=a is not None and b is not None
        discordant_a+=a is True and b is False;discordant_b+=b is True and a is False
        amin,amax=(int(a),int(a)) if a is not None else (0,1)
        bmin,bmax=(int(b),int(b)) if b is not None else (0,1)
        lower+=bmin-amax;upper+=bmax-amin
    n=len(grouped)
    for arm,c in counts.items():
        c['all_assigned_grade_fraction_bounds']=[c['verified_repairs']/c['assigned'],(c['verified_repairs']+c['unknown'])/c['assigned']]
        c['known_verdict_coverage']=(c['verified_repairs']+c['known_failed_verdicts'])/c['assigned']
    return dict(name=study['name'],arms=counts,paired_task_count=n,both_verifiers_known_pairs=both_known,
        known_discordant_first_only=discordant_a,known_discordant_second_only=discordant_b,
        second_minus_first_count_bounds=[lower,upper],second_minus_first_fraction_bounds=[lower/n,upper/n],
        bounds_are_not_confidence_intervals=True,collection_errors_treated_unknown=collection_errors_unknown,
        unknown_or_unattempted_outcomes_imputed=False,independent_random_sample=False,
        assumptions='Loose worst-case bounds permit either outcome for every unknown; empty/partial patches stay ungraded rather than being assigned test results.')


def compare(studies):
    if len({s['name'] for s in studies})!=len(studies):raise ValueError('Duplicate study')
    strict=[summarize(s,True) for s in studies]
    recorded=[summarize(s,False) for s in studies]
    return dict(scope='Recorded scalar sensitivity; no fresh model or grading, no pooling of reused tasks.',
        studies=strict,recorded_exit_nonnegative_convention=recorded,
        total_assigned=sum(c['assigned'] for s in strict for c in s['arms'].values()),
        total_completed=sum(c['completed'] for s in strict for c in s['arms'].values()),
        total_unattempted=sum(c['unattempted'] for s in strict for c in s['arms'].values()),
        new_population_accuracy_or_prize_claim=False)


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--data',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    a=p.parse_args();r=compare(json.loads(a.data.read_bytes())['studies'])
    a.output.open('x',encoding='utf-8').write(json.dumps(r,indent=2)+'\n')
    print(json.dumps({k:r[k] for k in ('total_assigned','total_completed','total_unattempted')}))
