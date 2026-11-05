"""Project cards use real portfolio captures with original SVG motion."""
import base64
from pathlib import Path
from artwork import ROOT, THEMES, text, document, save

def image(name):
    return 'data:image/webp;base64,'+base64.b64encode((ROOT/'assets/source'/name).read_bytes()).decode()

def browser(c, name, x, y, w, h, key):
    soft='#fffdf9' if c['paper']=='#f6f4ef' else '#303038'
    clip=f'<clipPath id="screen-{key}"><rect x="{x+5}" y="{y+27}" width="{w-10}" height="{h-32}" rx="2"/></clipPath>'
    art=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="9" fill="{soft}" stroke="{c["rule"]}"/>'
    for offset in [14,26,38]:art+=f'<circle cx="{x+offset}" cy="{y+13}" r="2.7" fill="{c["muted"]}"/>'
    art+=f'<image href="{image(name)}" x="{x+5}" y="{y+27}" width="{w-10}" height="{h-32}" preserveAspectRatio="xMidYMin slice" clip-path="url(#screen-{key})"/>'
    return clip,art

def phone(c,name,x,y,w,h,key):
    clip=f'<clipPath id="phone-{key}"><rect x="{x+5}" y="{y+5}" width="{w-10}" height="{h-10}" rx="17"/></clipPath>'
    art=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="22" fill="#25242a"/><image href="{image(name)}" x="{x+5}" y="{y+5}" width="{w-10}" height="{h-10}" preserveAspectRatio="xMidYMin slice" clip-path="url(#phone-{key})"/>'
    return clip,art

CSS='''@media(prefers-reduced-motion:no-preference){
.rear{animation:rear 8s ease-in-out infinite}.front{animation:front 8s ease-in-out infinite}
.card-cursor{animation:select 8s ease-in-out infinite}.click-ring{transform-box:fill-box;transform-origin:center;animation:click 8s ease-out infinite}
.matching-dot{animation:match-flow 2.5s ease-in-out infinite}
.star{transform-box:fill-box;transform-origin:center;animation:twinkle 4s ease-in-out infinite}
}
@keyframes rear{0%,100%{transform:translate(0,0) rotate(0deg)}50%{transform:translate(-7px,-7px) rotate(-1deg)}}
@keyframes front{0%,100%{transform:translate(0,0)}50%{transform:translate(5px,-9px)}}
@keyframes select{0%,100%{transform:translate(0,0)}35%,58%{transform:translate(23px,-32px)}75%{transform:translate(0,0)}}
@keyframes click{0%,37%,65%,100%{opacity:0;transform:scale(.3)}42%{opacity:1;transform:scale(.4)}62%{opacity:0;transform:scale(2)}}
@keyframes match-flow{0%,100%{transform:translateX(0);opacity:0}20%{opacity:1}80%{transform:translateX(13px);opacity:1}95%{transform:translateX(13px);opacity:0}}
@keyframes twinkle{0%,100%{opacity:.4;transform:scale(.7) rotate(0)}50%{opacity:1;transform:scale(1) rotate(20deg)}}'''

for theme,c in THEMES.items():
    body=text('CLIENT WORK / LEAD ENGINEER',40,37,14,c['muted'],tracking=.5)
    body+=text('Promote',38,109,62,c['ink'],tracking=-1.8)
    body+=text('100,000+',38,212,84,c['red'],tracking=-2)
    body+=text('registered users during my involvement',42,242,18,c['muted'])
    body+=text('Campaigns. Creators. Operations.',42,294,24,c['ink'])
    defs,rear=browser(c,'promote.webp',529,37,367,226,'rear')
    d,front=browser(c,'promote-campaigns.webp',492,132,368,174,'front');defs+=d
    body+=f'<g class="rear">{rear}</g><g class="front">{front}</g>'
    body+=f'<path class="card-cursor" d="M787 255v24l7-7 6 12 5-3-6-11h12z" fill="{c["red"]}" stroke="{c["paper"]}" stroke-width="2"/><circle class="click-ring" cx="815" cy="225" r="12" fill="none" stroke="{c["red"]}" stroke-width="2"/>'
    save('promote',theme,document('Promote — lead engineer, 100,000+ registered users during my involvement','Built campaign management, creator dashboards and admin tools, while coordinating delivery across three developers. Actual product captures, with sample data in the creator dashboard.',body,c,330,CSS,defs))

    body=text('CLIENT WORK / ORIGINAL APP BUILT SOLO',40,37,14,c['muted'],tracking=.4)
    body+=text('Shredder',38,109,62,c['ink'],tracking=-1.8)
    body+=text('60,000+',38,212,84,c['red'],tracking=-2)
    body+=text('registered users during my involvement',42,242,18,c['muted'])
    body+=text('Rider matching. Activity tracking.',42,294,24,c['ink'])
    defs,rear=phone(c,'shredder-second.webp',728,30,125,270,'shred-back')
    d,front=phone(c,'shredder.webp',559,44,137,284,'shred-front');defs+=d
    body+=f'<g class="rear">{rear}</g><g class="front">{front}</g><path d="M702 142H723M715 136L723 142L715 148" fill="none" stroke="{c["red"]}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/><circle class="matching-dot" cx="703" cy="142" r="2.8" fill="{c["red"]}"/>'
    save('shredder',theme,document('Shredder — original ski/snowboard app shipped solo, 60,000+ registered users during my involvement','Built the original matching and tracking app solo. Later returned for bug fixes and the Shreddy matching algorithm. Artwork represents the current product, which has since expanded.',body,c,350,CSS,defs))

    body=text('VOLUNTEER / WEB + MOBILE BUILT SOLO',40,37,14,c['muted'],tracking=.3)
    body+=text('Project IUoC',38,109,61,c['ink'],tracking=-1.5)
    body+=text('Free knowledge,',39,190,57,c['ink'],serif=True,tracking=-.4)
    body+=text('built for everyone.',39,250,57,c['ink'],serif=True,tracking=-.4)
    body+=text('A library. A reader. Everyday tools.',42,305,23,c['muted'])
    defs,rear=browser(c,'iuoc.webp',506,50,392,241,'iuoc-web')
    d,front=phone(c,'iuoc-reader.webp',773,141,95,197,'iuoc-phone');defs+=d
    body+=f'<g class="rear">{rear}</g><g class="front">{front}</g>'
    save('iuoc',theme,document('Project IUoC — free education website and mobile app, built independently as a volunteer','A searchable lecture library, Quran reader and everyday tools, backed by automated YouTube catalogue imports. Actual website and app captures.',body,c,360,CSS,defs))
