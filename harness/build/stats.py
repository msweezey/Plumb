import json,re,sys,statistics as st
from collections import Counter
EMO=re.compile("[\U0001F300-\U0001FAFF☀-☄☆-➿‼]")
def syl(w):
    n=len(re.findall(r'[aeiouy]+',w.lower())); return max(1,n-(1 if w.lower().endswith('e') and n>1 else 0))
def fk(t):
    s=[x for x in re.split(r'[.!?]+',t) if x.strip()]; w=re.findall(r"[A-Za-z']+",t)
    return 0 if not s or not w else 0.39*len(w)/len(s)+11.8*sum(syl(x) for x in w)/len(w)-15.59
def stats(b):
    C=json.load(open(f'{b}/corpus.json'))
    T=[c for c in C if c['split']=='T']
    print('=====',b)
    for ch in ['ad','social','pdp']:
        r=[c for c in T if c['channel']==ch]
        if not r: continue
        e=[len(EMO.findall(c['headline']+' '+c['body'])) for c in r]; x=[c['body'].count('!') for c in r]
        caps=[sum(1 for w in re.findall(r"\b[A-Z]{3,}\b",c['headline']+' '+c['body']) if w not in('USA','US','GOTS','PFAS','RN','NYC','DC','EDC','MAP','TSA','YKK','UV','XL','XS','PFC','RFID','SPF','USB','GNO')) for c in r]
        g=[fk(c['body']) for c in r if len(re.split(r'[.!?]+',c['body']))>=3]
        wl=[len(c['body'].split()) for c in r]
        print(f" {ch:6} n={len(r)} emoji max={max(e)} share={sum(1 for i in e if i)/len(r):.0%} | ! max={max(x)} share={sum(1 for i in x if i)/len(r):.0%} | CAPSwords max={max(caps)} share={sum(1 for i in caps if i)/len(r):.0%} | FK med={st.median(g) if g else 0:.1f} max={max(g) if g else 0:.1f} | words med={st.median(wl):.0f} min={min(wl)} max={max(wl)}")
    ads=[c for c in C if c['channel']=='ad']
    tc=lambda h: all(w[0].isupper() for w in re.findall(r"[A-Za-z][\w'’-]*",h) if w.lower() not in('a','an','the','and','or','of','to','in','on','for','with','at','by'))
    print(' ad headlines: n',len(ads),'TitleCase',sum(1 for c in ads if c['headline'] and tc(c['headline']) and not c['headline'].isupper()),'ALLCAPS',sum(1 for c in ads if c['headline'].isupper()),'empty',sum(1 for c in ads if not c['headline']),'maxlen',max(len(c['headline']) for c in ads),'| CTAs',Counter(c['cta'] for c in ads).most_common(4))
    soc=[c for c in C if c['channel']=='social']
    print(' IG hashtags',[re.findall(r'#\w+',c['body']) for c in soc][:10])
    allt=' '.join(c['headline']+' '+c['body'] for c in C)
    print(' name forms',Counter(re.findall(r'\b(?:M\.M\.\s?LaFleur|MM\s?LaFleur|M\.M\.|edikted|EDIKTED|Edikted|Topo Designs|TOPO|Topo)\b',allt)).most_common(8))
    words=Counter(w.lower() for w in re.findall(r"[A-Za-z][a-z']{3,}",' '.join(c['headline']+' '+c['body'] for c in C if c['channel']!='pdp')))
    print(' top words',[w for w,_ in words.most_common(60) if w not in('this','that','with','your','from','have','they','what','their','them','will','into','more','just','about','were','when','been','every','here','there','than','these','also','which','would','after')][:40])
    pw=Counter(w.lower() for w in re.findall(r"[A-Za-z][a-z']{3,}",' '.join(c['body'] for c in C if c['channel']=='pdp')))
    print(' pdp words',[w for w,_ in pw.most_common(45) if w not in('this','that','with','your','from','have','they','what','their','them','will','into','more','just','about','were','when','been','every','here','there','than','these','also','which','would','after')][:35])
    ser=sum(1 for c in C if re.search(r"\w+, [\w' -]+, (?:and|or) ",c['body'])); nos=sum(1 for c in C if re.search(r"\w+, [\w' -]+ (?:and|or) ",c['body']) and not re.search(r"\w+, [\w' -]+, (?:and|or) ",c['body']))
    print(' serial comma with/without',ser,nos)
for b in sys.argv[1:]: stats(b)
