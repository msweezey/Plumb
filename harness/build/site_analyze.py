import json,re,sys,collections,html as H
b=sys.argv[1]
d=json.load(open(f'/home/claude/brands/{b}/ev/home_raw.txt')); h=d['body']['html']
open(f'/home/claude/brands/{b}/ev/home.html','w').write(h)
print('== ',b,'len',len(h))
t=re.search(r'<title>(.*?)</title>',h,re.S); print('TITLE:',H.unescape(t.group(1).strip()) if t else '')
m=re.search(r'<meta[^>]+name="description"[^>]+content="([^"]*)"',h); print('META:',H.unescape(m.group(1)) if m else '')
ff=collections.Counter(x.strip().strip('"\'') for x in re.findall(r'font-family\s*:\s*["\']?([A-Za-z][\w -]+)',h))
print('FONTS:',ff.most_common(10))
faces=set(re.findall(r'@font-face\s*{[^}]*font-family\s*:\s*["\']?([^;"\']+)',h)); print('FACES:',faces)
print('FONT FILES:',sorted(set(re.findall(r'[\w./-]+\.woff2',h)))[:12])
css="\n".join(re.findall(r'<style[^>]*>(.*?)</style>',h,re.S))+"\n".join(re.findall(r'style="([^"]*)"',h))
use=collections.defaultdict(collections.Counter)
for prop,val in re.findall(r'([\w-]+)\s*:\s*([^;}"]+)',css):
    for hx in re.findall(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b',val): use[hx.lower()][prop]+=1
vars_=re.findall(r'(--[\w-]*(?:color|colour|bg|text|accent|primary|secondary|brand|button)[\w-]*)\s*:\s*(#[0-9a-fA-F]{3,6}|rgb[^;]+)',css,re.I)
print('COLOR VARS:',collections.Counter(vars_).most_common(25))
print('HEX USE:',[(k,sum(v.values()),dict(v.most_common(3))) for k,v in sorted(use.items(),key=lambda x:-sum(x[1].values()))[:18]])
txt=re.sub(r'<script.*?</script>|<style.*?</style>','',h,flags=re.S)
heads=[H.unescape(re.sub(r'<[^>]+>','',x)).strip() for x in re.findall(r'<h[1-3][^>]*>(.*?)</h[1-3]>',txt,re.S)]
print('HEADINGS:',[x for x in dict.fromkeys(heads) if x][:30])
btn=[H.unescape(re.sub(r'<[^>]+>','',x)).strip() for x in re.findall(r'<(?:a|button)[^>]*class="[^"]*(?:btn|button)[^"]*"[^>]*>(.*?)</(?:a|button)>',txt,re.S)]
print('BUTTONS:',collections.Counter(x for x in btn if x and len(x)<40).most_common(15))
ann=re.findall(r'(?:announcement|promo|banner)[^>]*>(.*?)</',txt,re.S|re.I)
print('PROMO:',[H.unescape(re.sub(r'<[^>]+>','',x)).strip()[:120] for x in ann if re.sub(r'<[^>]+>','',x).strip()][:8])
prices=re.findall(r'\$\d+(?:\.\d\d)?',txt); print('PRICES sample:',collections.Counter(prices).most_common(15))
print('SHOPIFY:', 'Shopify' in h or 'cdn.shopify' in h)
