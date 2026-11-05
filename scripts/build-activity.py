"""Render the actual GitHub contribution calendar snapshot, with an animated courier."""
import json
from datetime import date
from artwork import ROOT,THEMES,text,document,save
calendar=json.loads((ROOT/'data/activity.json').read_text())['data']['user']['contributionsCollection']['contributionCalendar']
weeks=calendar['weeks']
days=[day for w in weeks for day in w['contributionDays']]
CSS='''.tail{display:none}@media(prefers-reduced-motion:no-preference){.courier{animation:travel 18s linear infinite}.tail{display:inline}.scan{animation:scan 18s linear infinite}}\n'''
waypoints=[]
for i,w in enumerate(weeks):
    row=0 if i%2==0 else 6
    waypoints.append(f'{i/(len(weeks)-1)*100:.3f}%{{transform:translate({i*12}px,{row*12}px)}}')
CSS+='@keyframes travel{'+''.join(waypoints)+'}\n@keyframes scan{0%{transform:translateX(0)}100%{transform:translateX(624px)}}'
for theme,c in THEMES.items():
    palette= ['#e5e1d8','#efd0c8','#df998b','#ce6651','#a92d1d'] if theme=='light' else ['#34343b','#563a3c','#8a4b49','#c76357','#ed8a76']
    body=text('GITHUB / A YEAR OF BUILDING',40,35,14,c['muted'],tracking=1)
    body+=text(f'{calendar["totalContributions"]:,}',38,117,79,c['ink'],tracking=-2)
    body+=text('contributions',42,146,20,c['muted'])
    for col,w in enumerate(weeks):
        for row,day in enumerate(w['contributionDays']):
            level=['NONE','FIRST_QUARTILE','SECOND_QUARTILE','THIRD_QUARTILE','FOURTH_QUARTILE'].index(day['contributionLevel'])
            body+=f'<rect x="{285+col*12}" y="{63+row*12}" width="9" height="9" rx="2" fill="{palette[level]}"><title>{day["date"]}: {day["contributionCount"]} contributions</title></rect>'
    body+='<g transform="translate(289.5 67.5)">'
    for j in range(9,0,-1):
        size=8-j*.25
        body+=f'<g class="courier tail" style="animation-delay:{j*.075}s"><rect x="{-size/2}" y="{-size/2}" width="{size}" height="{size}" rx="2" fill="{c["red"]}" opacity="{.85-j*.065}"/></g>'
    body+=f'<g class="courier"><rect x="-5" y="-5" width="10" height="10" rx="3" fill="{c["red"]}" stroke="{c["paper"]}" stroke-width="1"/><circle cx="-1.8" cy="-1.5" r=".8" fill="{c["paper"]}"/><circle cx="1.8" cy="-1.5" r=".8" fill="{c["paper"]}"/></g></g>'
    body+=text(f'GitHub contribution calendar / {days[0]["date"]} to {days[-1]["date"]}',285,174,13,c['muted'])
    save('activity',theme,document('A year of contributions',f'{calendar["totalContributions"]} GitHub contributions from {days[0]["date"]} to {days[-1]["date"]}. An animated red courier traces the contribution grid. Snapshot, not a live count.',body,c,200,CSS))
