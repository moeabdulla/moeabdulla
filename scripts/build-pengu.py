"""The original Pengu Focus mascot, animated using its existing articulated groups."""
import re
from artwork import ROOT,THEMES,text,document,save
original=(ROOT/'assets/source/pengu.svg').read_text()
inner=original[original.index('>')+1:original.rindex('</svg>')]
CSS='''
#left-eye,#right-eye{opacity:0}
#left-eye-curved,#right-eye-curved{opacity:1}
@media(prefers-reduced-motion:no-preference){
#motion-left-arm{transform-origin:425.51px 638.5px;animation:wave 7s ease-in-out infinite}
#motion-head{transform-origin:508.91px 461.82px;animation:nod 7s ease-in-out infinite}
#left-eye,#right-eye{transform-box:fill-box;transform-origin:center;animation:blink 6s linear infinite,eyes-open 7s step-end infinite}
#left-eye-curved,#right-eye-curved{animation:eyes-smile 7s step-end infinite}
.focus-ring{animation:focus 14s linear infinite}
}
@keyframes wave{0%,15%,75%,100%{transform:rotate(0deg) translate(0,0)}26%,44%,62%{transform:rotate(81deg) translate(-4.4px,46.7px)}35%,53%{transform:rotate(73deg) translate(-4.4px,46.7px)}}
@keyframes nod{0%,100%{transform:rotate(0deg)}35%,60%{transform:rotate(-3deg)}}
@keyframes eyes-open{0%,20%{opacity:1}21%,74%{opacity:0}75%,100%{opacity:1}}
@keyframes eyes-smile{0%,20%{opacity:0}21%,74%{opacity:1}75%,100%{opacity:0}}
@keyframes blink{0%,43%,47%,100%{transform:scaleY(1)}45%{transform:scaleY(.08)}}
@keyframes focus{0%{stroke-dashoffset:1}90%,100%{stroke-dashoffset:0}}
'''
for theme,c in THEMES.items():
    green='#123d36';ink='#f1f5e8';mint='#c9ddce';gold='#d8b260'
    local={**c,'paper':green}
    body=text('A LITTLE PERSONALITY / MY INDEPENDENT FOCUS APP',40,36,14,mint,tracking=.45)
    body+=text('Built solo.',38,119,69,ink,tracking=-1.7)
    body+=text('With personality.',42,210,82,ink,serif=True,tracking=-1)
    body+=text('Pengu Focus / sessions, friends & earned cosmetics',43,254,20,mint)
    body+=f'<circle cx="649" cy="141" r="51" fill="none" stroke="#315d4d" stroke-width="5"/><circle class="focus-ring" pathLength="1" cx="649" cy="141" r="51" fill="none" stroke="{gold}" stroke-width="5" stroke-dasharray="1" stroke-dashoffset=".15" transform="rotate(-90 649 141)" stroke-linecap="round"/>'
    body+=f'<path d="M649 113v29l18 11" fill="none" stroke="{gold}" stroke-width="4" stroke-linecap="round"/>'
    body+=f'<svg class="pengu-wave" x="731" y="43" width="181" height="219" viewBox="0 0 556 631" overflow="visible">{inner}</svg>'
    for x,y,s in [(714,76,1),(904,45,.6),(704,244,.6)]:body+=f'<path class="spark" d="M{x} {y-7*s}q0 {7*s} {-7*s} {7*s}q{7*s} 0 {7*s} {7*s}q0 {-7*s} {7*s} {-7*s}q{-7*s} 0 {-7*s} {-7*s}z" fill="{gold}"/>'
    save('pengu',theme,document('Pengu Focus — built solo, with personality','The original Pengu Focus character waves with smiling eyes and blinks beside a moving focus timer. Designed, built and released independently by Mohammed Abdulla.',body,local,285,CSS))
