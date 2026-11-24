import json,re,random,sys
import os
HERE=os.path.dirname(os.path.abspath(__file__)); EV=f'{HERE}/evidence'; ROOT=os.path.abspath(os.path.join(HERE,'..','..'))
R=random.Random(7)
def build(b):
    C=[]
    ads=json.load(open(f'{EV}/{b}/ads.json'))
    for i,a in enumerate(ads):
        C.append(dict(split='H' if i%4==3 else 'T',channel='ad',headline=a['headline'],body=a['body'],cta=a['cta']))
    ig=json.load(open(f'{EV}/{b}/ig.json'))
    for i,t in enumerate(ig['own']):
        C.append(dict(split='H' if i%4==3 else 'T',channel='social',headline='',body=t,cta=''))
    P=[p for p in json.load(open(f'{EV}/{b}/products.json')) if p['body'] and len(p['body'].split())>=15]
    seen=set();U=[]
    for p in P:
        k=p['body'][:80]
        if k in seen: continue
        seen.add(k);U.append(p)
    R.shuffle(U)
    for i,p in enumerate(U[:36]):
        C.append(dict(split='H' if i%3==2 else 'T',channel='pdp',headline=p['title'],body=p['body'],cta=''))
    json.dump(C,open(f'{ROOT}/harness/retail-{b}/realcopy_corpus.json','w'),indent=1,ensure_ascii=False)
    from collections import Counter
    print(b,len(C),Counter((c['split'],c['channel']) for c in C))
for b in ['mml','edikted','topo']: build(b)
