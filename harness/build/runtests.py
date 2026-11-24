import json,sys
import os; sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
from brandkit import check, layer
from configs import BRANDS
CHMAP={'web_meta':'web','pdp_module':'pdp_module'}
def run(asset,cfg):
    ch=CHMAP.get(asset['channel'],asset['channel'])
    f=check(asset['body'],ch,cfg,asset.get('headline',''),asset.get('cta',''))
    return [x for x in f if layer(x[0])=='brand'],[x for x in f if layer(x[0])=='compliance']
def fidelity(b,show=False):
    C=json.load(open(f'{ROOT}/harness/retail-{b}/realcopy_corpus.json')); cfg=BRANDS[b]; out={}
    for sp in 'TH':
        A=[c for c in C if c['split']==sp]; fails=[]; comp=0
        for a in A:
            br,co=run(a,cfg); comp+=bool(co)
            if br: fails.append((a['channel'],(a['headline']+' | '+a['body'])[:90].replace('\n',' '),br))
        out[sp]=dict(n=len(A),passed=len(A)-len(fails),rate=round((len(A)-len(fails))/len(A),3),compliance_flagged=comp,fails=fails)
        if show:
            print(f' {b} {sp}: {len(A)-len(fails)}/{len(A)} = {out[sp]["rate"]:.0%}  (compliance findings on {comp})')
            for f in fails: print('    ',f[0],f[2],'::',f[1])
    return out
def discrimination(show=False):
    M={}
    for tgt in BRANDS:
        for src in BRANDS:
            if src==tgt: continue
            A=[c for c in json.load(open(f'{ROOT}/harness/retail-{src}/realcopy_corpus.json')) if c['channel'] in('ad','social')]
            rej=sum(1 for a in A if run(a,BRANDS[tgt])[0])
            M[f'{src}->{tgt}']=(rej,len(A))
    if show:
        print('discrimination (rows = copy source, cols = brand rules; rejected/total)')
        ks=list(BRANDS); print('        '+''.join(f'{k:>12}' for k in ks))
        for s in ks: print(f'{s:8}'+''.join(f'{"—" if s==t else "%d/%d"%M[f"{s}->{t}"]:>12}' for t in ks))
    return M
if __name__=='__main__':
    bs=sys.argv[1:] or list(BRANDS)
    for b in bs: fidelity(b,True)
    discrimination(True)
