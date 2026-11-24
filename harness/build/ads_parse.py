import json,sys
b=sys.argv[1]
raw=open(f'/home/claude/brands/{b}/ev/meta_ads_raw.txt').read()
d=json.loads(raw); d=d['body'] if 'body' in d else json.loads(d[0]['text'])['body']
out=[];seen=set()
for a in d['results']:
    s=a['snapshot']; bd=s.get('body'); bd=bd.get('text') if isinstance(bd,dict) else bd
    cards=s.get('cards') or []
    if not bd and cards: bd=cards[0].get('body')
    t=s.get('title') or (cards[0].get('title') if cards else '') or ''
    k=(t,bd)
    if k in seen or '{{' in t: continue
    seen.add(k); out.append(dict(page=a.get('page_name'),headline=t,body=bd or '',cta=s.get('cta_text') or '',fmt=s.get('display_format'),ai=a.get('contains_digital_created_media')))
json.dump(out,open(f'/home/claude/brands/{b}/ev/ads.json','w'),indent=1,ensure_ascii=False)
print(b,'unique ads',len(out),'pages',set(x['page'] for x in out),'total in library',d.get('searchResultsCount'))
