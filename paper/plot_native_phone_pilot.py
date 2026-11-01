"""One source-qualified episode: sampled PSS and actual tool observations."""
import argparse
import json
from pathlib import Path
from hashlib import sha256


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--native', type=Path, required=True)
    p.add_argument('--analysis', type=Path, required=True)
    p.add_argument('--output-prefix', type=Path, required=True)
    a = p.parse_args()
    analysis = json.loads(a.analysis.read_bytes())
    if not analysis['independent_grading_source_and_bytes_reviewed']:
        raise ValueError('Independent grading not source reviewed')
    transfers = {r['path']: r for r in json.loads((a.native/'transfers.json').read_bytes())}
    sources = {}
    for name in ('episode.json', 'memory_samples.jsonl', 'tool_results.jsonl'):
        path = a.native/name
        expected = transfers[name]
        actual = sha256(path.read_bytes()).hexdigest()
        if (not expected['content_verified'] or expected['remote_sha256'] != actual
                or expected['sha256'] != actual or path.stat().st_size != expected['bytes_received']):
            raise ValueError('Unverified device journal: ' + name)
        sources[name] = actual
    episode = json.loads((a.native/'episode.json').read_bytes())
    samples = [json.loads(s) for s in (a.native/'memory_samples.jsonl').read_text().splitlines()]
    tools = [json.loads(s) for s in (a.native/'tool_results.jsonl').read_text().splitlines()]
    start = episode['started_elapsed_ms']
    elapsed = (episode['finished_elapsed_ms'] - start)/1000
    if episode['samples'] != samples or any(s['elapsed_ms'] < start for s in samples):
        raise ValueError('Episode and journal observations differ')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family': 'DejaVu Sans', 'font.size': 10,
        'svg.fonttype': 'none', 'pdf.fonttype': 42})
    fig, (top, bottom) = plt.subplots(2, 1, figsize=(9, 5.3), sharex=True,
        gridspec_kw={'height_ratios': [3, 1]}, layout='constrained')
    top.plot([(s['elapsed_ms']-start)/1000 for s in samples],
        [s['whole_app_pss_mib']/1024 for s in samples], color='#28648B', linewidth=1.5)
    top.set_ylabel('Sampled whole-app PSS (GiB)')
    top.set_title('One native Gemma 4 E2B generation episode • FastAPI 14361', loc='left', fontsize=12)
    top.grid(axis='y', alpha=.2)
    top.text(.985, .06, '528 samples • Calculator present in 528/528\n'
        'No production edit • Independent native-patch grade: FAIL',
        transform=top.transAxes, ha='right', va='bottom', fontsize=9,
        bbox={'facecolor':'white','edgecolor':'#CDD4DA','alpha':.95,'pad':6})
    labels = {'repo_list': 'list', 'repo_read': 'read', 'repo_search': 'search'}
    for tool in tools:
        t = (tool['elapsed_ms']-start)/1000
        success = tool['success']
        bottom.scatter(t, 1 if success else 0, color='#358455' if success else '#B24745',
            marker='o' if success else 'x', s=45, linewidths=2)
        bottom.annotate(labels.get(tool['name'], tool['name']), (t, 1 if success else 0),
            xytext=(0, 8 if success else -16), textcoords='offset points', ha='center', fontsize=8)
    bottom.set_yticks([0, 1], ['Tool failure', 'Tool success'])
    bottom.set_ylim(-.65, 1.55)
    bottom.set_xlim(0, elapsed)
    bottom.set_xlabel('Seconds from native episode start (same monotonic clock)')
    fig.text(.01, -.055, 'Sampled memory is not exact peak or model-only memory. Foreground presence does not measure responsiveness.\n'
        'Setup transfer and shutdown memory are excluded; elapsed timing includes shutdown. One exposed case, no gain estimate.', fontsize=8)
    a.output_prefix.parent.mkdir(parents=True, exist_ok=True)
    outputs = {}
    for ext in ('png', 'svg', 'pdf'):
        target = a.output_prefix.with_suffix('.'+ext)
        if target.exists(): raise FileExistsError(target)
        fig.savefig(target, dpi=200, bbox_inches='tight')
        outputs[target.name] = sha256(target.read_bytes()).hexdigest()
    plt.close(fig)
    receipt = dict(scope='single_exposed_phone_episode_not_accuracy_or_gain', sources=sources,
        analysis_sha256=sha256(a.analysis.read_bytes()).hexdigest(), elapsed_seconds=elapsed,
        samples=len(samples), sampled_maximum_whole_app_PSS_MiB=max(s['whole_app_pss_mib'] for s in samples),
        tool_successes=sum(t['success'] for t in tools), tool_failures=sum(not t['success'] for t in tools),
        generated_token_count_measured=False, model_token_count_is_total_conversation=True, outputs=outputs)
    a.output_prefix.with_suffix('.json').open('x', encoding='utf-8').write(json.dumps(receipt, indent=2)+'\n')
    print(json.dumps(receipt))


if __name__ == '__main__': main()
