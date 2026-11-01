"""Publication figure from the two frozen host control receipts (Matplotlib)."""
import argparse
import json
from pathlib import Path


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--receipt-one', type=Path, required=True)
    p.add_argument('--receipt-two', type=Path, required=True)
    p.add_argument('--output-prefix', type=Path, required=True)
    a = p.parse_args()
    receipts = [json.loads(path.read_bytes()) for path in (a.receipt_one, a.receipt_two)]
    for receipt in receipts:
        if receipt['status'] != 'completed' or receipt['completed_conditions'] != 16:
            raise ValueError('Figure requires both complete frozen repetitions')
    first, second = [r['policy_summary'] for r in receipts]
    if first != second:
        raise ValueError('Repetition outcomes differ; do not plot them as identical')

    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.ticker import MultipleLocator

    names = ['exit_only', 'version_and_exit', 'preflight_origin_and_exit',
             'test_process_origin_and_exit', 'always_unknown']
    labels = ['Exit only', 'Matching version + exit', 'Preflight origin + exit',
              'Test-process origin + exit', 'Always unknown']
    supported = [first[n]['decisions'] - first[n]['unsupported_source_claims'] for n in names]
    unsupported = [first[n]['unsupported_source_claims'] for n in names]
    unknown = [first[n]['unknown'] for n in names]
    wrong = [first[n]['wrong_checkout_verdicts'] for n in names]
    if any(s + u + k != 16 for s, u, k in zip(supported, unsupported, unknown)):
        raise ValueError('Decision categories do not cover all conditions')
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
                         'svg.fonttype': 'none', 'pdf.fonttype': 42})
    fig, (left, right) = plt.subplots(1, 2, figsize=(10.5, 4.5), sharey=True,
                                    gridspec_kw={'width_ratios': [2, 1]})
    y = list(range(len(names)))
    left.barh(y, supported, color='#3274A1', label='Supported decision')
    left.barh(y, unsupported, left=supported, color='#C67C30', label='Unsupported source claim')
    left.barh(y, unknown, left=[s+u for s, u in zip(supported, unsupported)],
              color='#D9DEE3', label='Unknown')
    left.set_yticks(y, labels)
    left.invert_yaxis()
    left.set_xlim(0, 16)
    left.set_xlabel('Conditions per repetition (n = 16)')
    left.set_title('Decision coverage and source support', loc='left', fontsize=11)
    for i, (s, u, k) in enumerate(zip(supported, unsupported, unknown)):
        for start, value, color in ((0, s, 'white'), (s, u, 'white'), (s+u, k, '#26323E')):
            if value:
                left.text(start+value/2, i, str(value), ha='center', va='center', color=color)
    right.barh(y, wrong, color='#A74343')
    right.set_xlim(0, 5)
    right.set_xlabel('Wrong verdicts per 16 conditions')
    right.set_title('Checkout verdict errors', loc='left', fontsize=11)
    for i, value in enumerate(wrong):
        right.text(value+0.12, i, str(value), ha='left', va='center')
    for ax in (left, right):
        ax.xaxis.set_major_locator(MultipleLocator(4 if ax is left else 1))
        ax.spines[['top', 'right']].set_visible(False)
        ax.tick_params(axis='y', length=0)
        ax.set_axisbelow(True)
        ax.grid(axis='x', color='#E5E8EC', linewidth=0.7)
    fig.suptitle('A successful preflight does not bind a later test process', x=0.03,
                 ha='left', fontsize=13, fontweight='bold')
    handles, legend_labels = left.get_legend_handles_labels()
    fig.legend(handles, legend_labels, loc='lower left', bbox_to_anchor=(0.025, 0.06),
               ncol=3, frameon=False, fontsize=9)
    fig.text(0.03, 0.02, 'Two fresh Windows repetitions give identical counts. '
             'One synthetic package, two layouts; no model repair experiment.', fontsize=9)
    fig.subplots_adjust(left=0.265, right=0.97, top=0.80, bottom=0.23, wspace=0.28)
    a.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    for suffix in ('.png', '.svg', '.pdf'):
        target = a.output_prefix.with_suffix(suffix)
        if target.exists():
            raise FileExistsError(target)
        fig.savefig(target, dpi=220, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
