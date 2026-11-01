"""Publication figure from reviewed counts; conditions are not independent bugs."""
import hashlib
import json
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[1]


def main():
    folder=ROOT/'paper/feedback_utility_study_v2'
    windows=json.loads((folder/'windows_review_v1.json').read_bytes())
    linux=json.loads((folder/'linux_review_v1.json').read_bytes())
    if windows['policy_summary']!=linux['policy_summary']:
        raise ValueError('Per-OS results differ; do not collapse them')
    summary=windows['policy_summary']
    policies=('exit_only','actual_API_process_origin_and_exit','always_unknown')
    categories=('Correct, supported','Wrong checkout verdict','Correct, foreign source','Unknown')
    colors=('#19766c','#c54b46','#d2a548','#8e9aa7')
    rows=[]
    for name in policies:
        r=summary[name]
        rows.append([r['correct_supported_decisions'],r['wrong_checkout_verdicts'],
                     r['unsupported_source_claims']-r['wrong_checkout_verdicts'],r['unknown']])
    fig,ax=plt.subplots(figsize=(8.1,3.6),layout='constrained')
    left=[0]*len(rows)
    for category,color,column in zip(categories,colors,zip(*rows)):
        bars=ax.barh(range(len(rows)),column,left=left,label=category,color=color,height=.55)
        for bar,value in zip(bars,column):
            if value:ax.text(bar.get_x()+value/2,bar.get_y()+bar.get_height()/2,str(value),ha='center',va='center',fontsize=10,color='white' if color in colors[:2] else '#17242c')
        left=[a+b for a,b in zip(left,column)]
    ax.set_yticks(range(3),['Exit / version / preflight','Actual API-process origin','Always unknown'])
    ax.invert_yaxis();ax.set_xlim(0,288);ax.set_xticks([0,72,144,216,288])
    ax.set_xlabel('Constructed conditions per operating system (288)')
    ax.set_title('Supported feedback retains useful decisions',loc='left',weight='bold',pad=14)
    ax.spines[['top','right','left']].set_visible(False);ax.tick_params(axis='y',length=0)
    ax.legend(loc='lower left',bbox_to_anchor=(0,-.47),ncols=2,frameon=False,fontsize=9)
    fig.text(.02,.02,'Windows and Linux have identical counts. Three library snapshots; injected faults; no model repairs.',fontsize=8,color='#46535e')
    destination=ROOT/'paper/figures/feedback_utility_windows_linux_20261009_v1'
    for extension in ('png','svg'):
        path=destination.with_suffix('.'+extension)
        if path.exists():raise FileExistsError('Preserve the frozen figure')
        fig.savefig(path,dpi=220,bbox_inches='tight')
    receipt=dict(policy_summary=summary,plotted_counts=rows,counts_per_OS_not_pooled=True,
        source_sha256={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in
                       (Path(__file__),folder/'windows_review_v1.json',folder/'linux_review_v1.json')},
        errors_are_constructed_conditions_not_natural_issue_prevalence=True)
    destination.with_suffix('.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':main()
