"""Generate editable SVG review boards. No real student information is used."""
from pathlib import Path
from html import escape
import json

OUT = Path(__file__).parent
C = dict(bg='#F2F5F8', white='#FFFFFF', ink='#142C42', muted='#526779', accent='#176887', soft='#E8F2F6', line='#D9E2EA', green='#216B52', red='#A73732')

class Board:
    def __init__(self, title, width=1440, height=1024):
        self.width, self.height = width, height
        self.p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{escape(title)}">', f'<title>{escape(title)}</title>']
        self.rect(0, 0, width, height, C['bg'])
    def rect(self,x,y,w,h,fill=C['white'],r=0,stroke=None):
        self.p.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}"'+(f' stroke="{stroke}"' if stroke else '')+'/>')
    def text(self,x,y,s,size=14,color=None,weight=400,family='IBM Plex Sans, Segoe UI, sans-serif'):
        self.p.append(f'<text x="{x}" y="{y}" fill="{color or C["ink"]}" font-family="{family}" font-size="{size}" font-weight="{weight}">{escape(str(s))}</text>')
    def heading(self,x,y,s,size=26,color=None):
        self.text(x,y,s,size,color,650,'Manrope, Segoe UI, sans-serif')
    def line(self,x1,y1,x2,y2,color=None):
        self.p.append(f'<path d="M{x1} {y1} L{x2} {y2}" stroke="{color or C["line"]}" fill="none"/>')
    def circle(self,x,y,r,fill):
        self.p.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}"/>')
    def pill(self,x,y,s,w=100,fill=None,color=None):
        self.rect(x,y,w,28,fill or C['soft'],14)
        self.text(x+12,y+19,s,12,color or C['accent'],600)
    def button(self,x,y,s,w=150,primary=False):
        self.rect(x,y,w,42,C['accent'] if primary else C['white'],8,None if primary else C['line'])
        self.text(x+16,y+27,s,14,C['white'] if primary else C['ink'],600)
    def icon(self,x,y,kind,color=None):
        paths={
            'grid':'M2 2h7v7H2z M13 2h7v7h-7z M2 13h7v7H2z M13 13h7v7h-7z',
            'book':'M4 2h14v18H4z M8 7h6 M8 11h6 M8 15h4',
            'award':'M11 2a6 6 0 1 0 0 12a6 6 0 1 0 0-12 M7 13l-2 8 6-3 6 3-2-8',
            'person':'M11 2a4 4 0 1 0 0 8a4 4 0 1 0 0-8 M3 21v-3a8 8 0 0 1 16 0v3',
            'arrow':'M4 11h14 M13 6l5 5-5 5',
            'check':'M4 11l5 5L19 5',
        }
        self.p.append(f'<path transform="translate({x} {y})" d="{paths[kind]}" stroke="{color or C["muted"]}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>')
    def save(self,name):
        (OUT/name).write_text('\n'.join(self.p+['</svg>']),encoding='utf-8')

def shell(title,active='Overview',role='Student',subtitle='Your academic progress, with the detail behind every number.'):
    b=Board(title)
    b.rect(0,0,232,1024)
    b.line(232,0,232,1024)
    b.rect(28,30,38,38,C['accent'],10); b.text(36,55,'S',25,C['white'],700)
    b.heading(78,47,'Student',19); b.text(78,66,'digital profile',12,C['muted'])
    b.text(28,128,'WORKSPACE',10,C['muted'],600)
    nav=[('Overview','grid'),('Academic records','book'),('Achievements','award')] if role=='Student' else [('Assigned students','person'),('Academic results','book')]
    for i,(label,icon) in enumerate(nav):
        y=151+i*54
        if label==active: b.rect(16,y,200,44,C['soft'],8); b.rect(16,y+10,3,24,C['accent'],1)
        b.icon(30,y+11,icon,C['accent'] if label==active else C['muted'])
        b.text(64,y+28,label,14,C['accent'] if label==active else C['muted'],600 if label==active else 400)
    b.rect(20,744,192,118,C['bg'],10)
    b.text(36,770,'A record you can understand',12,C['ink'],600)
    b.text(36,794,'Every indicator connects',12,C['muted'])
    b.text(36,813,'back to your course results.',12,C['muted'])
    b.text(36,842,'Demonstration workspace',11,C['accent'])
    b.line(20,912,212,912); b.circle(44,950,18,C['soft']); b.text(33,955,'DS' if role=='Student' else 'TD',12,C['accent'],600)
    b.text(74,947,'Dana Sarsen' if role=='Student' else 'Teacher Demo',13,C['ink'],600); b.text(74,966,role+' account',11,C['muted'])
    b.rect(233,0,1207,80); b.line(232,80,1440,80)
    b.text(272,47,'Workspace',13,C['muted']); b.text(354,47,'/',13,C['muted']); b.text(375,47,active,13,C['ink'],500)
    b.pill(1120,26,'Synthetic data',113); b.circle(1372,40,18,C['soft']); b.text(1361,45,'DS' if role=='Student' else 'TD',12,C['accent'],600)
    b.text(272,122,'ACADEMIC YEAR 2026–2027',11,C['accent'],600)
    b.heading(272,163,title,30); b.text(272,191,subtitle,14,C['muted'])
    b.button(1190,130,'Autumn 2026  ∨',210)
    b.text(272,994,'Student Digital Profile  /  SDP-7 · Design revision 02',11,C['muted'])
    b.text(1130,994,'Fictional records · No live data',11,C['muted'])
    return b

def table(b,x,y,w=744,row_h=67):
    b.rect(x,y,w,44,C['bg'],6)
    for xx,s in [(x+18,'COURSE'),(x+w-240,'CREDITS'),(x+w-148,'GRADE'),(x+w-74,'POINTS')]:b.text(xx,y+28,s,10,C['muted'],600)
    data=[('SE 301','Software architecture','5','A','4.00'),('CS 204','Database systems','5','B','3.00'),('RS 201','Research methods','3','A','4.00')]
    for i,(code,title,credits,grade,points) in enumerate(data):
        yy=y+44+i*row_h
        b.text(x+18,yy+(20 if row_h<60 else 26),title,14,C['ink'],500);b.text(x+18,yy+(37 if row_h<60 else 45),code,11,C['muted'])
        b.text(x+w-221,yy+33,credits,14)
        b.pill(x+w-152,yy+15,grade,42)
        b.text(x+w-68,yy+33,points,14,C['ink'],500)
        b.line(x+16,yy+row_h,x+w-16,yy+row_h)

def chart(b,x,y,w=720,h=210):
    for value in range(5):
        yy=y+h-value*h/4
        b.text(x,yy+4,str(value)+'.0',10,C['muted']);b.line(x+38,yy,x+w,yy)
    values=[3.10,3.35,3.62]; xs=[x+74,x+w/2,x+w-38]; ys=[y+h-v*h/4 for v in values]
    path=' '.join(('M' if i==0 else 'L')+f'{xx} {yy}' for i,(xx,yy) in enumerate(zip(xs,ys)))
    b.p.append(f'<path d="{path} L{xs[-1]} {y+h} L{xs[0]} {y+h} Z" fill="{C["soft"]}"/>')
    b.p.append(f'<path d="{path}" stroke="{C["accent"]}" stroke-width="3" fill="none"/>')
    for xx,yy,v,label in zip(xs,ys,values,['Spring 2025','Autumn 2025','Autumn 2026']):
        b.circle(xx,yy,7,C['white']); b.circle(xx,yy,4,C['accent']); b.text(xx-16,yy-17,f'{v:.2f}',13,C['accent'],600);b.text(xx-36,y+h+25,label,11,C['muted'])

def dashboard():
    b=shell('Your semester, at a glance')
    b.rect(272,224,1128,112,C['white'],12,C['line'])
    for i,(label,value,detail) in enumerate([('SEMESTER GPA','3.62','of 4.00 · +0.27 vs previous'),('EARNED CREDITS','13','13 graded credits this semester'),('COMPLETED COURSES','3','All current results are available')]):
        x=296+i*376
        if i:b.line(x-24,248,x-24,312)
        b.text(x,251,label,10,C['muted'],600);b.heading(x,294,value,34);b.text(x+100,290,detail,12,C['green'] if i==0 else C['muted'])
    b.rect(272,360,784,324,C['white'],12,C['line']); b.heading(296,397,'Academic trajectory',19);b.text(296,419,'Semester GPA · demonstration history · scale 0–4',12,C['muted']);chart(b,296,447,736,184)
    b.rect(1080,360,320,324,C['ink'],12);b.circle(1122,406,22,C['accent']);b.text(1111,411,'DS',14,C['white'],600)
    b.heading(1104,461,'Dana Sarsen',22,C['white']);b.text(1104,488,'Software Engineering',14,'#C5D5DF');b.text(1104,511,'DEMO-001  /  SE-DEMO',12,'#C5D5DF');b.line(1104,536,1376,536,'#375064')
    b.text(1104,567,'Your academic record',12,'#C5D5DF');b.text(1104,592,'Results, context and evidence.',15,C['white'],500);b.text(1104,649,'Current period · Autumn 2026',12,'#C5D5DF')
    b.rect(272,708,784,254,C['white'],12,C['line']);b.heading(296,745,'Results behind your GPA',19);b.text(889,744,'3 courses',12,C['muted']);table(b,288,761,752,49)
    b.rect(1080,708,320,254,C['white'],12,C['line']);b.heading(1104,746,'Achievement spotlight',18);b.icon(1104,774,'award',C['accent']);b.pill(1140,773,'Certificate',101)
    b.text(1104,827,'Database design workshop',15,C['ink'],600);b.text(1104,852,'12 October 2026',12,C['muted']);b.text(1104,881,'Evidence attached · sample file',12,C['muted']);b.line(1104,904,1376,904);b.text(1104,935,'Explore achievements',13,C['accent'],600);b.icon(1351,920,'arrow',C['accent'])
    b.save('01-overview.svg')

def records():
    b=shell('Academic records','Academic records',subtitle='A clear record of your courses, credits and results.')
    b.rect(272,224,1128,78,C['white'],12,C['line']);b.pill(296,249,'Autumn 2026',120);b.text(446,268,'3 graded courses',14,C['muted']);b.text(1104,270,'Semester GPA',13,C['muted']);b.heading(1280,273,'3.62',26)
    b.rect(272,326,1128,344,C['white'],12,C['line']);b.heading(296,365,'Course results',20);table(b,288,386,1096)
    b.rect(272,694,738,225,C['white'],12,C['line']);b.heading(296,734,'Understand the calculation',20);b.text(296,765,'Grade points are weighted by course credits.',14,C['muted']);b.rect(296,788,690,54,C['soft'],8);b.text(316,822,'(5 × 4.00 + 5 × 3.00 + 3 × 4.00) ÷ 13 = 3.62',20,C['accent'],500);b.text(296,884,'Test policy v1 · Final value rounded to two decimal places.',12,C['muted'])
    b.rect(1034,694,366,225,C['white'],12,C['line']);b.heading(1058,734,'What counts toward GPA?',18);b.text(1058,775,'Completed, graded courses count.',14,C['muted']);b.text(1058,805,'Pending results are excluded.',14,C['muted']);b.text(1058,835,'Missing results never mean zero.',14,C['muted']);b.pill(1058,866,'Demonstration policy',158)
    b.save('02-academic-records.svg')

def achievements():
    b=shell('Your achievements','Achievements',subtitle='Evidence of the work and learning beyond your grades.')
    b.rect(272,224,1128,62,C['white'],10,C['line']);b.text(296,262,'All achievements',14,C['accent'],600);b.text(469,262,'Certificates',14,C['muted']);b.text(600,262,'Academic',14,C['muted']);b.button(1198,234,'+ Add achievement',182,True)
    entries=[('Certificate','Database design workshop','Completed a practical workshop on','relational modelling and query design.','12 October 2026'),('Academic','Research presentation','Presented a student research poster','on educational data visualization.','23 October 2026')]
    for i,(tag,title,l1,l2,date) in enumerate(entries):
        x=272+i*576;b.rect(x,310,552,340,C['white'],12,C['line']);b.rect(x+24,334,58,58,C['soft'],12);b.icon(x+42,352,'award',C['accent']);b.pill(x+400,346,tag,124)
        b.heading(x+24,439,title,22);b.text(x+24,474,l1,14,C['muted']);b.text(x+24,497,l2,14,C['muted']);b.line(x+24,528,x+528,528);b.icon(x+24,550,'book');b.text(x+58,566,'sample-certificate.pdf',13,C['ink'],500);b.pill(x+370,546,'Evidence attached',157)
        b.text(x+24,620,date,12,C['muted']);b.text(x+420,620,'View details',13,C['accent'],600)
    b.rect(272,678,1128,146,C['soft'],12);b.heading(300,720,'A portfolio with context',20);b.text(300,752,'Add a clear title, date and supporting evidence so each achievement tells a useful story.',14,C['muted']);b.text(300,782,'This design shows two synthetic entries, including the saved-state example.',12,C['muted']);b.save('03-achievements.svg')

def teacher():
    b=shell('Your assigned students','Assigned students','Teacher','Review course results within your teaching assignments.')
    b.rect(272,224,1128,84,C['white'],12,C['line']);b.text(296,252,'COURSE',10,C['muted'],600);b.text(296,283,'Software architecture',16,C['ink'],600);b.text(691,252,'GROUP',10,C['muted'],600);b.text(691,283,'SE-DEMO',16);b.pill(1180,252,'Assigned scope',160)
    b.rect(272,332,1128,366,C['white'],12,C['line']);b.heading(296,372,'Student results',20);b.text(1272,370,'3 students',12,C['muted']);b.rect(288,397,1096,44,C['bg'],6)
    for x,s in [(306,'STUDENT'),(700,'STUDENT ID'),(910,'RESULT'),(1110,'STATUS'),(1280,'ACTION')]:b.text(x,425,s,10,C['muted'],600)
    for i,(name,initial,ident,grade,status) in enumerate([('Dana Sarsen','DS','DEMO-001','A · 4.00','Recorded'),('Arman Bek','AB','DEMO-002','—','Pending'),('Amina Nur','AN','DEMO-003','B · 3.00','Recorded')]):
        y=441+i*70;b.circle(321,y+33,18,C['soft']);b.text(310,y+38,initial,12,C['accent'],600);b.text(356,y+39,name,15,C['ink'],500);b.text(700,y+39,ident,13,C['muted']);b.text(910,y+39,grade,14);b.pill(1100,y+20,status,102);b.text(1280,y+39,'Edit result',13,C['accent'],600);b.line(304,y+69,1370,y+69)
    b.rect(272,724,1128,138,C['soft'],12);b.heading(296,764,'Your assignment defines access',20);b.text(296,797,'Only results for students in your assigned course are shown. Grades are validated against the selected policy.',14,C['muted']);b.text(296,829,'Student portfolios and results in other courses are not exposed by this workspace.',13,C['muted']);b.save('04-teacher-workspace.svg')

def mobile():
    b=Board('Student overview · mobile',390,1100);b.rect(0,0,390,78);b.rect(20,21,34,34,C['accent'],9);b.text(29,45,'S',21,C['white'],700);b.heading(66,44,'Student profile',18);b.circle(352,38,18,C['soft']);b.text(341,43,'DS',12,C['accent'],600)
    b.text(20,111,'AUTUMN 2026',11,C['accent'],600);b.heading(20,148,'Your semester',28);b.text(20,176,'Dana Sarsen · Software Engineering',13,C['muted'])
    b.rect(20,201,350,155,C['ink'],14);b.text(40,230,'SEMESTER GPA',11,'#C5D5DF',600);b.heading(40,288,'3.62',48,C['white']);b.text(164,286,'/ 4.00',20,'#C5D5DF');b.text(40,329,'13 earned credits  ·  3 completed courses',13,'#C5D5DF')
    b.rect(20,376,350,250,C['white'],12,C['line']);b.heading(40,411,'Academic trajectory',18);chart(b,36,440,308,129)
    b.heading(20,669,'Course results',21)
    for i,(name,grade,credits) in enumerate([('Software architecture','A · 4.00','5 credits'),('Database systems','B · 3.00','5 credits'),('Research methods','A · 4.00','3 credits')]):
        y=690+i*98;b.rect(20,y,350,84,C['white'],10,C['line']);b.text(36,y+28,name,15,C['ink'],600);b.text(36,y+58,credits,12,C['muted']);b.pill(267,y+39,grade,86)
    b.text(20,1008,'Fictional data · Test grading policy v1',11,C['muted']);b.rect(0,1030,390,70);b.line(0,1030,390,1030)
    for x,icon,label in [(48,'grid','Overview'),(177,'book','Records'),(298,'award','Achievements')]:b.icon(x,1041,icon,C['accent'] if x==48 else C['muted']);b.text(x-10,1082,label,10,C['accent'] if x==48 else C['muted'])
    b.save('05-mobile-overview.svg')

if __name__=='__main__':
    dashboard();records();achievements();teacher();mobile()
    (OUT/'tokens.json').write_text(json.dumps(C,indent=2)+'\n',encoding='utf-8')
    print('Generated 5 editable SVG boards.')
