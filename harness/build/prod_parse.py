import json,re,sys,html as H,collections
b=sys.argv[1]
d=json.load(open(f'/home/claude/brands/{b}/ev/products_raw.txt'))['body']['html']
m=re.search(r'(\{"products":.*\})',d,re.S)
j=json.loads(H.unescape(re.sub(r'<[^>]+>','',m.group(1))) if '<' in m.group(1) else m.group(1))
P=[]
for p in j['products']:
    vs=p.get('variants',[])
    prices=[float(v['price']) for v in vs if v.get('price')]
    cmp=[float(v['compare_at_price']) for v in vs if v.get('compare_at_price')]
    body=H.unescape(re.sub(r'<[^>]+>',' ',p.get('body_html') or '')); body=re.sub(r'\s+',' ',body).strip()
    opts={o['name']:o['values'] for o in p.get('options',[])}
    P.append(dict(title=p['title'],type=p.get('product_type'),tags=p.get('tags'),price=min(prices) if prices else None,compare=max(cmp) if cmp else None,body=body,options=opts,created=p.get('created_at','')[:10]))
json.dump(P,open(f'/home/claude/brands/{b}/ev/products.json','w'),indent=1,ensure_ascii=False)
print(b,'products',len(P),'types',collections.Counter(x['type'] for x in P).most_common(12))
pr=[x['price'] for x in P if x['price']]; print(' price min/median/max',min(pr),sorted(pr)[len(pr)//2],max(pr),'| with compare_at',sum(1 for x in P if x['compare'] and x['compare']>x['price']))
bl=[len(x['body'].split()) for x in P if x['body']]; print(' desc words median',sorted(bl)[len(bl)//2] if bl else 0,'n',len(bl))
for x in P[:3]: print('  -',x['title'],'|',x['type'],'|',x['price'],x['compare'],'|',x['body'][:260])
