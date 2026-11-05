"""Animated build-and-ship scene, entirely declarative SVG/CSS."""
from artwork import THEMES,text,document,save

CSS='''
.phrase{opacity:0}.phrase.one{opacity:1}
@media(prefers-reduced-motion:no-preference){
.code-line{animation:code 10s ease-in-out infinite;transform-box:fill-box;transform-origin:left}
.c2{animation-delay:-9s}.c3{animation-delay:-8s}.c4{animation-delay:-7s}
.cursor{animation:cursor 10s ease-in-out infinite}
.tap{transform-box:fill-box;transform-origin:center;animation:tap 10s ease-out infinite}
.success{animation:success 10s ease-in-out infinite}
.phrase{animation:phrase 15s step-end infinite}.phrase.two{animation-delay:-10s}.phrase.three{animation-delay:-5s}
.preview-tile{animation:tile 10s ease-in-out infinite;transform-box:fill-box;transform-origin:bottom}
.t2{animation-delay:-9.5s}.t3{animation-delay:-9s}
}
@keyframes code{0%,8%,100%{transform:scaleX(.1);opacity:.2}22%,83%{transform:scaleX(1);opacity:1}95%{transform:scaleX(.1);opacity:.2}}
@keyframes cursor{0%,10%,100%{transform:translate(0,0)}35%,44%{transform:translate(110px,57px)}53%,85%{transform:translate(175px,108px)}95%{transform:translate(0,0)}}
@keyframes tap{0%,40%,60%,100%{opacity:0;transform:scale(.4)}45%{opacity:.8;transform:scale(.4)}58%{opacity:0;transform:scale(2)}}
@keyframes success{0%,53%,100%{opacity:0}60%,88%{opacity:1}96%{opacity:0}}
@keyframes phrase{0%,32%{opacity:1}33%,100%{opacity:0}}
@keyframes tile{0%,16%,100%{transform:scaleY(.3);opacity:.4}35%,90%{transform:scaleY(1);opacity:1}}
'''
for theme,c in THEMES.items():
    soft='#fffdf9' if theme=='light' else '#2c2c33'
    body=text('FULL-STACK DEVELOPER / OTTAWA',40,37,14,c['muted'],tracking=.7)
    body+=text('Mohammed',38,133,88,c['ink'],tracking=-3.5)+text('Abdulla',130,247,130,c['ink'],serif=True,tracking=-2)
    body+=f'<path d="M43 171 C4 300 378 331 521 236" fill="none" stroke="{c["red"]}" stroke-width="3"/>'
    body+=f'<path d="M494 236 C552 260 583 281 644 282 H890" fill="none" stroke="{c["rule"]}" stroke-width="2"/><path class="flow" d="M494 236 C552 260 583 281 644 282 H890" fill="none" stroke="{c["red"]}" stroke-width="3"/>'
    body+=f'<g class="floating"><rect x="558" y="57" width="351" height="202" rx="10" fill="{soft}" stroke="{c["rule"]}"/><path d="M558 86H909" stroke="{c["rule"]}"/>'
    for x in [573,586,599]:body+=f'<circle cx="{x}" cy="72" r="3" fill="{c["red"]}" opacity=".7"/>'
    body+=text('build / preview',620,77,11,c['muted'])
    for i,(w,color) in enumerate([(99,c['red']),(124,c['ink']),(77,c['red']),(109,c['muted'])]):
        body+=f'<rect class="code-line c{i+1}" x="580" y="{115+i*25}" width="{w}" height="7" rx="3" fill="{color}" opacity=".8"/>'
    body+=f'<path d="M725 103V242" stroke="{c["rule"]}"/>'
    body+=f'<rect x="745" y="106" width="141" height="48" rx="6" fill="{c["red"]}" opacity=".14"/>'
    for i,h in enumerate([42,61,31]):body+=f'<rect class="preview-tile t{i+1}" x="{745+i*48}" y="{233-h}" width="35" height="{h}" rx="4" fill="{c["red"]}" opacity="{.4+i*.2}"/>'
    body+='</g>'
    body+=f'<g class="floating" style="animation-delay:-2s"><rect x="796" y="166" width="100" height="161" rx="17" fill="{c["ink"]}"/><rect x="802" y="173" width="88" height="147" rx="12" fill="{soft}"/><rect x="827" y="177" width="39" height="6" rx="3" fill="{c["ink"]}"/>'
    body+=f'<rect x="812" y="198" width="66" height="33" rx="5" fill="{c["red"]}" opacity=".25"/><path d="M813 243H870M813 253H860M813 263H868" stroke="{c["rule"]}" stroke-width="5" stroke-linecap="round"/>'
    body+=f'<g class="success"><circle cx="847" cy="290" r="15" fill="{c["red"]}"/><path d="m840 290 5 5 9-10" fill="none" stroke="{soft}" stroke-width="3" stroke-linecap="round"/></g></g>'
    body+=f'<circle class="tap" cx="759" cy="232" r="11" fill="none" stroke="{c["red"]}" stroke-width="2"/>'
    body+=f'<g class="cursor"><path d="M644 167v22l6-6 5 11 5-3-5-10h9z" fill="{c["red"]}" stroke="{soft}" stroke-width="1.5"/></g>'
    for cls,label in [('one','Web platforms.'),('two','Mobile apps.'),('three','Systems behind them.')]:body+=f'<g class="phrase {cls}">'+text(label,42,333,26,c['ink'])+'</g>'
    save('header',theme,document('Mohammed Abdulla — web, mobile and the systems behind them','A looping scene types code, builds a browser preview and ships a mobile app. Full-stack developer in Ottawa.',body,c,370,CSS))
