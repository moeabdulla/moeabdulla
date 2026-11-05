from artwork import THEMES,text,document,save
CSS='''@media(prefers-reduced-motion:no-preference){.file{animation:file 5s cubic-bezier(.3,.1,.2,1) infinite}.file.two{animation-delay:-3.3s}.file.three{animation-delay:-1.6s}.result{animation:result 5s ease-in-out infinite}}
@keyframes file{0%{transform:translateX(0);opacity:0}10%{opacity:1}80%{transform:translateX(240px);opacity:1}100%{transform:translateX(240px);opacity:0}}
@keyframes result{0%,25%,100%{opacity:.35}40%,85%{opacity:1}}'''
for theme,c in THEMES.items():
 body=text('FISHERIES AND OCEANS CANADA',40,36,14,c['muted'],tracking=.6)
 body+=text('Minutes',38,124,64,c['ink'],tracking=-2)+text('to seconds.',300,126,78,c['red'],serif=True,tracking=-1.5)
 body+=text('QGIS search + a nightly Azure-to-Oracle metadata pipeline.',42,183,22,c['muted'])
 body+=f'<g fill="none" stroke="{c["rule"]}" stroke-width="2"><rect x="680" y="64" width="49" height="68" rx="5"/><rect x="824" y="64" width="79" height="68" rx="6"/><path d="M743 97h68"/></g>'
 for cls in ['one','two','three']:body+=f'<g class="file {cls}"><rect x="664" y="89" width="10" height="15" rx="2" fill="{c["red"]}"/></g>'
 body+=f'<g class="result" stroke="{c["red"]}" stroke-width="3" stroke-linecap="round"><path d="M835 78h43M835 90h31M835 102h42M835 114h23"/></g>'
 save('dfo',theme,document('DFO — file searches reduced from minutes to seconds','Built a Python/PyQt search plugin for QGIS and a nightly Azure-to-Oracle metadata pipeline. Identical searches improved from minutes to seconds in comparison tests. Animated files and results are an illustration.',body,c,220,CSS))
