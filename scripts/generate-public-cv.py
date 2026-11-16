from pathlib import Path
import json
from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.lib import colors
import pypdfium2 as pdfium
w=Path(__file__).resolve().parents[1]
cv={'cv':{'name':'Jiale Chang','email':'changjiale@stu.njau.edu.cn','website':'https://changjiale444.github.io','summary':'Research interests: agent memory, multimodal intelligence, personalized AI agents, embodied intelligence, and graph-based memory modeling.','sections':{'education':[{'institution':'Xiamen University','area':'Computer Science and Technology · MAC Lab','degree':'Incoming M.S.','highlights':['Incoming student; enrollment date to be confirmed.']},{'institution':'Nanjing Agricultural University','area':'Data Science and Big Data Technology','degree':'B.S. (in progress)','highlights':['Undergraduate, Class of 2023.']}],'experience':[{'company':'Nanjing University','position':'Research collaboration','highlights':['Large-scale Intelligence and Knowledge Laboratory · Agent Memory']},{'company':'Nanjing Agricultural University','position':'Research experience','highlights':['Computational Agriculture and Systems Integration Laboratory · Hyperspectral analysis']},{'company':'Xiamen University — MAC Lab','position':'Research project','highlights':['Embodied Simulation & Workflow Navigation']}],'publications':[{'title':'ScrapMem: A Bio-inspired Framework for On-device Personalized Agent Memory via Optical Forgetting','authors':['Jiale Chang','Yuxiang Ren'],'journal':'ACM SIGKDD 2027 · Accepted','url':'https://arxiv.org/abs/2605.03804'},{'title':'On-Device Agent Memory: Forms, Lifecycle Management, and Personalization','journal':'Survey Preprint · 2026','url':'https://holmeshu.github.io/On-Device-Agent-Memory-Survey/'},{'title':'SPECGAN: Extracting Sensitive Bands from Plant Disease Spectra Based on Generative Adversarial Network','journal':'Spectrochimica Acta Part A · 2026','url':'https://doi.org/10.1016/j.saa.2026.127711'}],'awards':[{'name':x} for x in ['National Scholarship','First-class University Scholarship','National Third Prize, China Robotics and Artificial Intelligence Competition','National Silver Award, 2025 New Liberal Arts Practice Innovation Competition','Provincial Second Prize, Chinese Mathematics Competition','Provincial Second Prize, Lanqiao Cup Competition']]}}}
styles=getSampleStyleSheet();styles.add(ParagraphStyle(name='NameJ',fontName='Helvetica-Bold',fontSize=25,leading=30,textColor=colors.HexColor('#172033'),spaceAfter=12));styles.add(ParagraphStyle(name='SectionJ',fontName='Helvetica-Bold',fontSize=11,leading=16,textColor=colors.HexColor('#4776e6'),spaceBefore=10,spaceAfter=5));styles['BodyText'].fontSize=9;styles['BodyText'].leading=11
story=[Paragraph('Jiale Chang',styles['NameJ']),Paragraph('changjiale@stu.njau.edu.cn | github.com/changjiale444',styles['BodyText']),Spacer(1,9),Paragraph(cv['cv']['summary'],styles['BodyText'])]
for section,rows in cv['cv']['sections'].items():
 story.append(Paragraph(section.title(),styles['SectionJ']))
 for row in rows:
  title=row.get('institution') or row.get('company') or row.get('title') or row.get('name')
  story.append(Paragraph('<b>'+title+'</b>',styles['BodyText']))
  detail=row.get('degree','')+' '+row.get('area','') if section=='education' else row.get('position') or row.get('journal','')
  if detail: story.append(Paragraph(detail,styles['BodyText']))
  for h in row.get('highlights',[]):story.append(Paragraph(h,styles['BodyText']))
  story.append(Spacer(1,3))
SimpleDocTemplate(str(w/'public/assets/pdf/jiale-chang-cv.pdf'),rightMargin=43,leftMargin=43,topMargin=38,bottomMargin=38,title='Jiale Chang — Public Academic CV',author='Jiale Chang').build(story)
d=pdfium.PdfDocument(str(w/'public/assets/pdf/jiale-chang-cv.pdf'));print('Public CV pages:',len(d));d[0].render(scale=1.5).to_pil().save('/tmp/jiale-public-cv.png')
