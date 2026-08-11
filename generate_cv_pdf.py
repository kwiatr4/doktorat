from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable
from reportlab.lib.units import mm
from reportlab.lib import colors

CONTENT = '''
KRZYSZTOF WIATR
Wrocław, Poland
794 009 133 | kwiatr4@st.swps.edu.pl

RESEARCH PROFILE
Psychology graduate and engineer in Management and Production Engineering, developing expertise at the intersection of experimental research, behavioral and physiological data analysis, artificial intelligence, and computational technologies. Experienced in designing and conducting experiments, working with eye-tracking data, analyzing experimental data, designing human–AI interactions, and working with data from wearable devices.

Co-founder of a research and technology project applying AI, physiological and behavioral data to the detection and monitoring of depressive symptoms. Interested in further developing expertise in neuroscience, precision phenotyping, biomedical and behavioral data analysis, and computational methods applied to human health research. Planning to pursue a PhD and continue an academic research career.

RESEARCH EXPERIENCE

Research Internship — Eye-Tracking Research
SWPS University | Michał Król, PhD, DSc | 11.2025 – present

- conducting research procedures and working with eye-tracking equipment for recording eye movements;
- acquisition and processing of raw eye-tracking data;
- using GitHub Copilot to support data processing and automate the extraction of information on fixations and saccades;
- preparing data for further statistical analysis and contributing to the interpretation of research findings;
- working with behavioral and eye-tracking data.

Research on Verbal Mimicry in Human–AI Interaction
SWPS University | Jakub Kuś, PhD | 10.2024 – present

- design and implementation of an experimental study forming the basis of my Master's thesis;
- design of a digital experimental environment using vibe coding;
- development of two versions of a conversational script conducting natural conversations with participants, with or without verbal mimicry;
- preparation, collection, and analysis of quantitative data using Jamovi;
- presentation of the study concept at the Digital Mindscape Conference 2024 and research findings at the 19th Congress of the Polish Society of Social Psychology;
- preparation of research materials for submission to a scientific journal.

Research Internship — AI and Creativity
SWPS University | Jarosław Orzechowski, PhD, DSc, Prof. | 12.2023 – 01.2025

- co-development of methodology and design and implementation of a computer-based laboratory experiment;
- operationalization of variables and selection of appropriate research tools;
- preparation of participant instructions and research materials;
- investigation of creative problem-solving using association-based tasks, Dixit cards, and interactions with ChatGPT;
- preparation and organization of research data and materials for evaluation by independent expert judges.

Research on Mimicry and Blood Donation
SWPS University | Wojciech Kulesza, PhD, DSc, Prof. | 10.2023 – 05.2024

- co-development of research methodology and implementation of the research procedure;
- conducting field research;
- data collection and organization.

Research Assistant — Social Lab
SWPS University | Jakub Kuś, PhD | 06–07.2023

- participation in a study investigating diffusion of responsibility in online environments;
- operation of a simulated social networking platform used as an experimental environment;
- management of experimental data and events in a relational MySQL database using phpMyAdmin;
- controlling experimental conditions and working directly with research participants.

RESEARCH & TECHNOLOGY PROJECTS

MentaliCare AI
Co-founder | 01.2023 – present

R&D project using AI, physiological and behavioral data, and wearable devices to detect and monitor depressive symptoms.

- co-development of the research concept and methodology;
- designing an approach for analyzing data including HRV, heart rate, sleep, activity, skin temperature, and circadian rhythms;
- development of concepts for integrating data from multiple sources and applying interpretable AI models.

Real Action
Co-founder | Application Design | 11.2024 – 07.2025

- design of an application supporting reduction of problematic social media use;
- participation in NeuroHack organized by Łukasiewicz–PORT;
- completion of InQUBE Academy.

SKILLS
Research & Methodology: experimental research design · variable operationalization · research procedure design · research tool selection · data preparation · data analysis and interpretation · participant research

Data Analysis: Jamovi · SPSS · quantitative data analysis · preparation and structuring of experimental data

Eye-Tracking: data acquisition and preprocessing · fixation analysis · saccade analysis · data structuring

Programming & Technology: Python (basic) · MySQL · GitHub Copilot · vibe coding · AI-assisted data processing · human–AI interaction design

EDUCATION

SWPS University, Wrocław
Master's Degree in Psychology — Clinical Psychology
2026

Wrocław University of Economics and Business
Bachelor of Engineering in Management and Production Engineering
2019

ACADEMIC & ORGANIZATIONAL ACTIVITIES

HumanTech Wrocław / Digital Mindscape
Co-founder and Chair | 04.2023 – 04.2026

- development of an interdisciplinary initiative combining psychology, technology, and AI;
- organization of academic and technology-focused conferences and events;
- organization of workshops on Python, AI, and statistical analysis.

CONFERENCES & PUBLICATIONS
19th Congress of the Polish Society of Social Psychology — oral presentation, 09.2024

Digital Mindscape Conference — conceptual research poster, 05.2024

Manuscript in preparation: The Impact of Verbal Mimicry on Motivation and Perception of Interactions with Artificial Intelligence

LANGUAGES
Polish — native | English — communicative proficiency in spoken and written communication
'''

styles = getSampleStyleSheet()

def add_section(title, content_parts):
    parts = []
    parts.append(Paragraph(title, styles['Heading2']))
    for part in content_parts:
        parts.append(Paragraph(part, styles['BodyText']))
    return parts

story = []
style_title = ParagraphStyle(
    name='Title',
    parent=styles['Title'],
    fontName='Helvetica-Bold',
    fontSize=18,
    leading=22,
    spaceAfter=8,
    alignment=1,
)
style_body = ParagraphStyle(
    name='Body',
    parent=styles['BodyText'],
    fontName='Helvetica',
    fontSize=9.5,
    leading=12,
    spaceAfter=3,
)
style_sub = ParagraphStyle(
    name='Sub',
    parent=styles['BodyText'],
    fontName='Helvetica-Bold',
    fontSize=10,
    leading=12,
    spaceAfter=4,
)
style_h2 = ParagraphStyle(
    name='H2',
    parent=styles['Heading2'],
    fontName='Helvetica-Bold',
    fontSize=11,
    leading=13,
    spaceBefore=10,
    spaceAfter=6,
    textColor=colors.black,
)

# Split into lines while preserving content ordering.
lines = [line.rstrip() for line in CONTENT.strip().splitlines()]
# Some headings are single-line labels; keep raw text and format by simple rules.
current_paragraph = []
for line in lines:
    if not line.strip():
        if current_paragraph:
            story.append(Paragraph(' '.join(current_paragraph).strip(), style_body))
            current_paragraph = []
        story.append(Spacer(1, 4))
        continue

    if line.startswith(' ') or line.startswith('\t'):
        continue

    if line.endswith(':') and len(line) < 80:
        story.append(Paragraph(line, style_h2))
        continue

    if line.isupper() and len(line) < 80:
        # section headings in all caps or title-like forms
        story.append(Paragraph(line, style_h2))
        continue

    if line in {'KRZYSZTOF WIATR', 'Wrocław, Poland', '794 009 133 | kwiatr4@st.swps.edu.pl'}:
        if line == 'KRZYSZTOF WIATR':
            story.append(Paragraph(line, style_title))
        else:
            story.append(Paragraph(line, style_body))
        continue

    if line.startswith('- '):
        if current_paragraph:
            story.append(Paragraph(' '.join(current_paragraph).strip(), style_body))
            current_paragraph = []
        story.append(Paragraph(line[2:], style_body))
        continue

    if line.startswith('Research ') or line.startswith('SWPS ') or line.startswith('Wrocław ') or line.startswith('HumanTech ') or line.startswith('Digital ') or line.startswith('Polish ') or line.startswith('Master') or line.startswith('Bachelor') or line.startswith('Manuscript') or line.startswith('MentaliCare') or line.startswith('Real Action'):
        story.append(Paragraph(line, style_sub if ('|' in line or '—' in line) else style_body))
        continue

    current_paragraph.append(line)

if current_paragraph:
    story.append(Paragraph(' '.join(current_paragraph).strip(), style_body))

pdf = SimpleDocTemplate(
    'CV_Krzysztof_Wiatr_ENG.pdf',
    pagesize=A4,
    leftMargin=18*mm,
    rightMargin=18*mm,
    topMargin=14*mm,
    bottomMargin=14*mm,
)
pdf.build(story)
print('PDF generated: CV_Krzysztof_Wiatr_ENG.pdf')
