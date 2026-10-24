"""Compile reviewed vector boards and explicit prototype routes into an offline plugin."""
from pathlib import Path
import sys, json, xml.etree.ElementTree as ET, copy
sys.dont_write_bytecode = True

HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'redesign'))
import build_design as d
C=d.C
screens={}
def add(key,board,title,links=None):
    svg='\n'.join(board.p+['</svg>']) if isinstance(board,d.Board) else board
    screens[key]={'key':key,'name':title,'svg':svg,'links':links or []}
    return screens[key]
def link(s,x,y,w,h,label,to):s['links'].append(dict(x=x,y=y,w=w,h=h,label=label,to=to))
def action(b,s,x,y,label,to,w=180,primary=False):
    b.button(x,y,label,w,primary);link(s,x,y,w,42,label,to)
def base(name,title,active='Overview',role='Student'):
    b=d.shell(title,active,role,subtitle='Interactive demonstration · fictional data · no live account changes')
    s=add(name,b,title);s['role']=role
    return b,s
def finish(s,b):s['svg']='\n'.join(b.p+['</svg>'])
def panel(name,title,body,actions,active='Overview',role='Student'):
    b,s=base(name,title,active,role);b.rect(272,224,1128,430,C['white'],12,C['line'])
    b.heading(304,274,title,24)
    for i,line in enumerate(body):b.text(304,318+i*28,line,15,C['muted'])
    x=304
    for label,to in actions:
        action(b,s,x,550,label,to,220,x==304);x+=244
    finish(s,b);return s

for key,file,title,role in [('overview','01-overview.svg','Student overview','Student'),('records','02-academic-records.svg','Academic records','Student'),('achievements','03-achievements.svg','Achievements','Student'),('teacher','04-teacher-workspace.svg','Assigned students','Teacher'),('mobile','05-mobile-overview.svg','Mobile overview','Mobile')]:
    s=add(key,(HERE.parent/'redesign'/file).read_text(encoding='utf-8'),title);s['role']=role

# Entry and role selection are prototype-only; no real login credentials are requested.
b=d.Board('Choose a demo workspace');s=add('login',b,'Demo sign in')
b.rect(0,0,620,1024,C['ink']);b.rect(52,56,48,48,C['accent'],12);b.heading(66,90,'S',30,C['white'])
b.heading(52,330,'Your learning.',48,C['white']);b.heading(52,397,'A clearer picture.',48,C['white']);b.text(52,456,'Academic results, progress and achievement evidence.',19,'#C5D5DF');b.text(52,950,'Student Digital Profile · Interactive diploma prototype',14,'#C5D5DF')
b.heading(732,278,'Choose a demo workspace',32);b.text(732,321,'Explore the student and teacher journeys with fictional data.',16,C['muted'])
for i,(label,to) in enumerate([('Continue as student','overview'),('Continue as teacher','teacher'),('Review administration','admin'),('Open mobile prototype','mobile')]):action(b,s,732,370+i*78,label,to,490,i==0)
b.text(732,736,'These entries simulate roles. They do not authenticate a user.',13,C['muted']);finish(s,b)

panel('period','Choose semester',['Select a demonstration period.','The selected period changes the records and indicators together.'],[('Autumn 2026','overview'),('Spring 2027','empty')])
panel('empty','No results this semester',['Spring 2027 · Dana Sarsen','There are no graded courses for this period.','GPA is unavailable; this does not mean zero performance.'],[('Back to Autumn 2026','overview'),('Test request failure','error')])
panel('error','Results could not be loaded',['Your records have not been changed.','Retry returns to the academic records in this demonstration.'],[('Try again','records'),('Back to overview','overview')])
panel('profile','Your profile',['Dana Sarsen · DEMO-001','Software Engineering · SE-DEMO','This profile contains fictional academic data.'],[('Back to overview','overview'),('Sign out','login')])
panel('course','Software architecture',['SE 301 · Autumn 2026 · 5 credits','Recorded result: A · 4.00 points','Weighted GPA contribution: 5 × 4.00 = 20.00','Students can inspect results; teachers maintain assigned records.'],[('Back to records','records')],active='Academic records')
panel('course-db','Database systems',['CS 204 · Autumn 2026 · 5 credits','Recorded result: B · 3.00 points','Weighted GPA contribution: 5 × 3.00 = 15.00'],[('Back to records','records')],active='Academic records')
panel('course-research','Research methods',['RS 201 · Autumn 2026 · 3 credits','Recorded result: A · 4.00 points','Weighted GPA contribution: 3 × 4.00 = 12.00'],[('Back to records','records')],active='Academic records')
panel('certificate','Certificate evidence',['Database design workshop','Dana Sarsen · 12 October 2026','Sample evidence preview: participation in a relational modelling workshop.','Synthetic certificate only. No file is downloaded or sent.'],[('Back to achievements','achievements')],active='Achievements')
panel('research','Research presentation',['Academic achievement · 23 October 2026','Presented a student research poster on educational data visualization.','Synthetic evidence is available in this prototype.'],[('View evidence','research-evidence'),('Back to achievements','achievements')],active='Achievements')
panel('research-evidence','Research evidence',['Research presentation · 23 October 2026','Sample certificate for a fictional student research poster.'],[('Back to details','research')],active='Achievements')

for key,tag,rows in [('certificates','Certificates',[('Database design workshop','12 October 2026','certificate')]),('academic','Academic achievements',[('Research presentation','23 October 2026','research')])]:
    b,s=base(key,tag,'Achievements');b.rect(272,224,1128,300,C['white'],12,C['line']);b.pill(296,248,tag,180)
    for i,(name,date,target) in enumerate(rows):b.heading(296,325+i*80,name,22);b.text(296,355+i*80,date,14,C['muted']);action(b,s,1150,310+i*80,'View details',target)
    action(b,s,296,450,'Clear filter','achievements');finish(s,b)

for key,filled,error in [('add',False,False),('add-error',False,True),('add-filled',True,False)]:
    b,s=base(key,'Add achievement','Achievements');b.rect(272,224,738,658,C['white'],12,C['line']);b.heading(300,267,'Achievement details',22)
    for i,(label,value) in enumerate([('Title','Team project showcase'),('Category','Academic achievement'),('Date','23 October 2026'),('Description','Presented a student software project.')]):
        y=302+i*100;b.text(300,y,label,13,C['ink'],600);b.rect(300,y+14,682,48,C['bg'],8,C['red'] if error and i==0 else C['line']);b.text(316,y+44,value if filled else 'Click to use the sample value',15,C['ink'] if filled else C['muted']);link(s,300,y+14,682,48,'Fill '+label,'add-filled')
    if error:b.text(300,701,'A title is required. Use the sample values to continue.',13,C['red'])
    b.text(300,735,'Evidence: sample-project.pdf' if filled else 'Evidence: no sample selected',13,C['muted']);action(b,s,300,760,'Choose sample file','add-filled',220)
    action(b,s,300,822,'Save achievement','saved' if filled else 'add-error',220,True);action(b,s,544,822,'Cancel','discard',150)
    b.rect(1034,224,366,248,C['soft'],12);b.heading(1058,268,'Prototype form',20);b.text(1058,307,'Fields use preset sample values.',14,C['muted']);b.text(1058,337,'No real data or files are submitted.',14,C['muted']);b.text(1058,367,'Use Save to test the next state.',14,C['muted']);finish(s,b)
panel('discard','Discard unsaved changes?',['The sample form has not been saved.','Keep editing or return to the achievement list.'],[('Keep editing','add-filled'),('Discard changes','achievements')],active='Achievements')
panel('saved','Achievement saved',['Team project showcase','Academic achievement · 23 October 2026','Your sample entry is now shown in the saved-list state.'],[('View saved list','achievements-saved')],active='Achievements')
b,s=base('achievements-saved','Your achievements','Achievements');b.rect(272,224,1128,350,C['white'],12,C['line'])
for i,(title,target) in enumerate([('Database design workshop','certificate'),('Research presentation','research'),('Team project showcase','new-detail')]):
    y=258+i*96;b.heading(296,y+24,title,20);b.text(296,y+49,'Evidence attached · synthetic entry',13,C['muted']);action(b,s,1180,y+10,'View details',target,190)
action(b,s,272,604,'Add achievement','add',220,True);finish(s,b)
panel('new-detail','Team project showcase',['Academic achievement · 23 October 2026','Presented a student software project.','Sample evidence: sample-project.pdf'],[('Back to saved list','achievements-saved'),('Remove sample entry','delete-confirm')],active='Achievements')
panel('delete-confirm','Remove this sample entry?',['Team project showcase will be removed from the demonstration list.','This does not delete any real file or student record.'],[('Keep entry','new-detail'),('Remove entry','achievements')],active='Achievements')

for key,person,result,error in [('grade','Dana Sarsen','A · 4.00',False),('grade-options','Dana Sarsen','Choose grade',False),('grade-invalid','Dana Sarsen','5.00',True),('grade-ready','Dana Sarsen','B · 3.00',False),('grade-arman','Arman Bek','Pending',False),('grade-amina','Amina Nur','B · 3.00',False)]:
    b,s=base(key,'Edit academic result','Academic results','Teacher');b.rect(272,224,790,470,C['white'],12,C['line']);b.heading(300,272,person,24);b.text(300,307,'Software architecture · Autumn 2026 · 5 credits',15,C['muted']);b.text(300,361,'Grade points',13,C['ink'],600);b.rect(300,380,734,52,C['bg'],8,C['red'] if error else C['line']);b.text(318,412,result,18);
    if person=='Dana Sarsen':link(s,300,380,734,52,'Choose demonstration grade','grade-options')
    if error:b.text(300,465,'Enter a grade from 0.00 to 4.00. No changes were saved.',14,C['red'])
    elif key=='grade-options':
        action(b,s,300,452,'Choose B · 3.00','grade-ready',220);action(b,s,544,452,'Test invalid 5.00','grade-invalid',220)
    else:b.text(300,465,'Click the grade field to explore valid and invalid states.' if person=='Dana Sarsen' else 'Read-only demonstration. Use Cancel to return to the assigned list.',14,C['muted'])
    # Only Dana has a mutable predefined result; other students remain inspect-only.
    if person=='Dana Sarsen':action(b,s,300,580,'Save result','grade-saved' if key=='grade-ready' else 'grade-invalid',220,True)
    action(b,s,544,580,'Cancel','teacher',150);finish(s,b)
panel('grade-saved','Academic result saved',['Dana Sarsen · Software architecture','New result: B · 3.00 points · 5 credits','Recalculated semester GPA: (15 + 15 + 12) / 13 = 3.23'],[('Back to assigned list','teacher-saved')],active='Assigned students',role='Teacher')
saved_teacher=copy.deepcopy(screens['teacher']);saved_teacher.update(key='teacher-saved',name='Assigned students · saved result');saved_teacher['svg']=saved_teacher['svg'].replace('A · 4.00','B · 3.00');saved_teacher['links']=[];screens['teacher-saved']=saved_teacher
panel('teacher-period','Teaching period',['Only the Autumn 2026 course assignment is available in this demo.','The assignment boundary is maintained when changing views.'],[('Autumn 2026','teacher')],active='Assigned students',role='Teacher')
panel('teacher-profile','Teacher account',['Teacher Demo','Assigned course: Software architecture · SE-DEMO','No student account credentials or personal records are exposed.'],[('Back to students','teacher'),('Sign out','login')],active='Assigned students',role='Teacher')
panel('admin','Accounts and assignments',['Dana Sarsen · Student · Own records','Teacher Demo · Teacher · Software architecture / SE-DEMO','Admin Demo · Administrator · Account configuration','Administrative mutations need agreed permissions and remain read-only.'],[('Review scope policy','admin-policy'),('Sign out','login')],role='Administrator')
panel('admin-policy','Administrative scope',['Account, role and assignment changes require an approved workflow.','This prototype does not grant administrator grade-editing permissions.','No production assignment or grading rule is modified.'],[('Back to accounts','admin'),('Sign out','login')],role='Administrator')

# Mobile destinations preserve mobile-sized navigation rather than jumping into desktop boards.
for key,title,lines in [('mobile-records','Academic records',['Software architecture · A · 5 credits','Database systems · B · 5 credits','Research methods · A · 3 credits','GPA: 47 / 13 = 3.62']),('mobile-achievements','Achievements',['Database design workshop','Certificate · 12 October 2026','Research presentation','Academic · 23 October 2026']),('mobile-profile','Student profile',['Dana Sarsen · DEMO-001','Software Engineering · SE-DEMO','Fictional demonstration account'])]:
    b=d.Board(title,390,844);s=add(key,b,title);s['role']='Mobile';b.heading(20,65,title,25)
    for i,line in enumerate(lines):b.rect(20,106+i*95,350,78,C['white'],10,C['line']);b.text(36,150+i*95,line,13)
    if key=='mobile-profile':action(b,s,20,560,'Sign out','login',180)
    b.rect(0,774,390,70)
    for x,label,to in [(20,'Overview','mobile'),(143,'Records','mobile-records'),(263,'Achievements','mobile-achievements')]:b.text(x,815,label,13,C['accent'],600);link(s,x-4,778,117,62,label,to)
    link(s,20,16,350,60,'Student profile','mobile-profile');finish(s,b)

# Explicit interaction map. No hotspot points to a missing screen.
for key,s in list(screens.items()):
    role=s.get('role')
    if role in ['Student','Teacher','Administrator']:
        nav=[('Overview','overview'),('Academic records','records'),('Achievements','achievements')] if role=='Student' else [('Assigned students','teacher'),('Academic results','teacher')] if role=='Teacher' else [('Accounts and assignments','admin'),('Scope policy','admin-policy')]
        for i,(label,to) in enumerate(nav):link(s,16,151+i*54,200,44,label,to)
        link(s,20,920,192,65,'Account and sign out','profile' if role=='Student' else 'teacher-profile' if role=='Teacher' else 'admin')
        link(s,1348,20,48,42,'Account','profile' if role=='Student' else 'teacher-profile' if role=='Teacher' else 'admin')
        if role!='Administrator':link(s,1190,130,210,42,'Choose semester','period' if role=='Student' else 'teacher-period')
    # Self destinations are selected/read-only controls, not navigation reactions.
    s['links']=[l for l in s['links'] if l['to']!=key]
    if role=='Administrator':
        s['svg']=s['svg'].replace('Assigned students','Accounts &amp; assignments').replace('Academic results','Scope policy')
        # Period selection is informational for this read-only admin workspace.
for key in ['overview','records']:
    s=screens[key]
    for i,target in enumerate(['course','course-db','course-research']):link(s,288,(805+i*49 if key=='overview' else 430+i*67),752 if key=='overview' else 1096,49 if key=='overview' else 67,'Open course result',target)
link(screens['overview'],1104,914,272,44,'Explore achievements','achievements')
for x,w,label,to in [(296,156,'All achievements','achievements'),(460,125,'Certificates','certificates'),(593,125,'Academic','academic'),(1198,182,'Add achievement','add')]:
    if to!='achievements':link(screens['achievements'],x,234,w,42,label,to)
for i,to in enumerate(['certificate','research']):
    link(screens['achievements'],272+i*576,310,552,340,'Open achievement',to)
for key in ['teacher','teacher-saved']:
    for i,to in enumerate(['grade','grade-arman','grade-amina']):link(screens[key],1264,452+i*70,110,46,'Edit or inspect result',to)
for x,label,to in [(20,'Overview','mobile'),(145,'Records','mobile-records'),(265,'Achievements','mobile-achievements')]:
    if to!='mobile':link(screens['mobile'],x,1030,120,70,label,to)
link(screens['mobile'],330,18,48,44,'Account','mobile-profile')

ET.register_namespace('','http://www.w3.org/2000/svg')
for s in screens.values():
    root=ET.fromstring(s['svg']);s['width']=int(root.attrib['width']);s['height']=int(root.attrib['height']);s['texts']=[]
    for text in list(root):
        if text.tag.endswith('}text'):
            s['texts'].append(dict(text=''.join(text.itertext()),x=float(text.attrib['x']),baseline=float(text.attrib['y']),size=float(text.attrib['font-size']),color=text.attrib['fill'],weight=int(text.attrib.get('font-weight',400)),family='Manrope' if 'Manrope' in text.attrib.get('font-family','') else 'IBM Plex Sans'))
            root.remove(text)
    s['vectorSvg']=ET.tostring(root,encoding='unicode')
    for l in s['links']:
        assert l['to'] in screens,(s['key'],l)
        assert 0<=l['x'] and 0<=l['y'] and l['x']+l['w']<=s['width'] and l['y']+l['h']<=s['height'],(s['key'],l)

payload={'version':'03','screens':list(screens.values()),'starts':{'Student journey':'login','Teacher journey':'teacher','Administration review':'admin','Mobile journey':'mobile'}}
(HERE/'prototype.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
runtime=(HERE/'runtime.js').read_text(encoding='utf-8')
(HERE/'code.js').write_text('const PROTOTYPE = '+json.dumps(payload,ensure_ascii=False)+';\n'+runtime,encoding='utf-8')
preview_data=[{k:s[k] for k in ['key','name','svg','links','width','height']} for s in screens.values()]
preview=(HERE/'preview-template.html').read_text(encoding='utf-8').replace('__SCREENS__',json.dumps(preview_data,ensure_ascii=False).replace('</','<\\/'))
(HERE/'preview.html').write_text(preview,encoding='utf-8')
print(f'Compiled {len(screens)} screens and {sum(len(s["links"]) for s in screens.values())} interactions.')
