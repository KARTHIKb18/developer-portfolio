"""Builds an ATS-friendly, single-column resume as DOCX and PDF."""
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

OUT_DIR = Path(__file__).parent
OUT_NAME = "Karthik_B_Software_Engineer_Resume_2026"

FONT = "Calibri"
ACCENT = RGBColor(0x1F, 0x4E, 0x79)
DARK = RGBColor(0x1A, 0x1A, 0x1A)
MUTED = RGBColor(0x55, 0x55, 0x55)

PAGE_W, PAGE_H = Inches(8.27), Inches(11.69)  # A4
MARGIN_X, MARGIN_Y = Inches(0.6), Inches(0.5)
TEXT_W = PAGE_W - 2 * MARGIN_X

# ---------------------------------------------------------------- content
NAME = "KARTHIK B"
HEADLINE = ("Software Engineer | Python & AI Applications | "
            "Custom Application Development | Forensic Technology")
LOCATION = "Bengaluru, India"
PHONE = "+91 9663490402"
EMAIL = "karthikb2418@gmail.com"
LINKEDIN_URL = "https://www.linkedin.com/in/karthik-18k/"
LINKEDIN_TEXT = "LinkedIn"
PORTFOLIO_URL = "https://karthikb18.github.io/developer-portfolio/"
PORTFOLIO_TEXT = "Portfolio"

SUMMARY = (
    "Software Engineer with **5 years** of experience delivering **Python** applications, "
    "**AI-powered** solutions, REST API integrations and automation at scale. Associate Consultant at "
    "**KPMG Forensic Technology**, building custom **RelativityOne** apps and US FTech tools (**PODS**), "
    "SBX/RSMF parsing and data pipelines (**META**) and KPMG Digital Responder features (**KDR**). "
    "Strong in Python backend engineering, Azure automation, testing and production support, with a "
    "proven record of measurable performance and efficiency gains."
)

ACHIEVEMENTS = [
    "**~95% less manual effort** in attorney bar-license verification across nine U.S. states "
    "(ABL Verification App).",
    "**>50% faster performance** in Query Quick through an independently led backend redesign.",
    "**~7,000–8,000 secure-portal downloads automated** by the META SBX Download Tool, enabling "
    "same-day delivery.",
    "**100% accurate commissions in under 50% of allotted time** using BigQuery at FISDOM, "
    "fast-tracking a major partnership.",
]

SKILLS = [
    ("Languages", "Python 3, Python 2, SQL, JavaScript, TypeScript, Core Java, Shell Scripting"),
    ("Backend & Frameworks", "Flask, REST APIs, Pandas, Requests, Selenium, OpenCV, Tkinter, PyInstaller, "
                             "RelativityOne Apps"),
    ("Cloud & Integration", "Microsoft Azure (Functions, Logic Apps), GCP, BigQuery, Swagger/OpenAPI, "
                            "OAuth, Postman"),
    ("AI & GenAI", "AI Summarization & Translation, Prompt Engineering, Token Optimization, "
                   "KPMG Workbench APIs"),
    ("Data Formats", "CSV, Excel, DBF, HTML, JSON, XML"),
    ("Testing & Quality", "Pytest, Selenium, Functional, Regression, API, UI & End-to-End Testing, "
                          "Debugging, Logging"),
    ("Engineering Practices", "Git/GitHub, Code Reviews, CI/CD, Release Support, "
                              "Copilot-Assisted Development, Documentation"),
]

EXPERIENCE = [
    {
        "company": "KPMG Global Services - Forensic Technology Services",
        "meta": "Bengaluru, India | 2025 – Present",
        "roles": [("Associate Consultant – Custom Application Development, Automation & Forensic Technology", "")],
        "bullets": [
            "Engineer Python automation, **AI-powered applications**, REST API integrations, data-processing "
            "solutions and custom **RelativityOne** apps across the **PODS**, **KDR** and **META** programs.",
            "Co-developed the **ABL Verification Standalone App** spanning **nine U.S. states**, cutting manual "
            "bar-license verification effort by **~95%** via a CSV-driven workflow with consolidated outputs, "
            "logging and automation controls.",
            "Independently re-architected the **Query Quick** backend for a documented **>50% performance boost**; "
            "drove UI/functional enhancements and production rollout in RelativityOne.",
            "Built **AI Summarizer** and **AI Translator** RelativityOne cards: prompt workflows, API integration, "
            "field-value persistence, output re-use, token optimization and multilingual support; drove testing "
            "and defect resolution.",
            "Delivered the **META SBX Download Tool** against an urgent deadline, automating **~7,000–8,000 "
            "secure-portal downloads** and enabling **same-day dataset delivery**.",
            "Powered **META Switchboard** with high-volume **SBX/RSMF parsing** and data-processing support, "
            "keeping priority-matter deliveries accurate and on track.",
            "Strengthened **KDR Case Management** and **Data Collector** through Data Transfer Object (DTO) fixes, "
            "Python Swagger/OpenAPI comparison automation, test suites, API alignment and Azure automation; "
            "resolved production issues and drove end-to-end testing and release readiness.",
            "Independently led **STR application** delivery end to end, covering requirements clarification, "
            "documentation, API research and integration, UI/UX, bulk workflows, test-data creation and "
            "functional validation.",
            "Modernized **Saved Search** with UI, filter and API enhancements, refining features through "
            "stakeholder feedback and QA for a smoother review experience.",
            "Supported META matters (**OPAL, LEVI, NHTSA, Crush AI, Instagram, Threads**) with parser fixes, "
            "data processing, historical validation, regression QC and output verification.",
            "Elevated team engineering standards through GitHub repo management, PR/code-review guidance, "
            "deployment support, knowledge transfer and reusable documentation.",
        ],
        "stack": "Python, Flask, REST APIs, RelativityOne, Microsoft Azure (Functions, Logic Apps), "
                 "Swagger/OpenAPI, KPMG Workbench AI APIs, Tkinter, PyInstaller, Pytest, Git/GitHub",
    },
    {
        "company": "FISDOM",
        "meta": "Bengaluru, India",
        "roles": [("SDET – L1 | Python Backend & Automation", "Jan 2022 – 2025")],
        "bullets": [
            "Automated the end-to-end **commission process** using Python frameworks and data-driven workflows.",
            "Owned company-wide **partner-commission calculations** on **BigQuery**, delivering **100% accuracy** "
            "in **under 50% of the allotted time** and fast-tracking a major partnership with direct revenue impact.",
            "Built automated pipelines to download and process files from multiple **fintech and stock-exchange "
            "platforms** using **Selenium**, **Flask** and Python.",
            "Created bulk **DBF, CSV and Excel** processing tools adopted across the organization, "
            "streamlining team workflows.",
            "Developed robust **testing tools** that raised product quality and efficiency and closed critical "
            "development gaps.",
        ],
        "stack": "Python 3, Python 2, JavaScript, SQL, Selenium, Flask, Pandas, OpenCV, Requests, "
                 "Google Cloud Platform (GCP), BigQuery",
    },
]

PROJECTS = [
    ("ABL Verification Standalone App", "Python, Tkinter, PyInstaller",
     "Nine-state bar-license verification with **~95%** less effort."),
    ("Query Quick", "Python, RelativityOne",
     "Saved-search analytics app; backend redesign achieved **>50%** faster performance."),
    ("AI Summarizer & Translator Cards", "AI/API Integration, RelativityOne",
     "AI-powered review components with prompt/API integration, stored outputs, token optimization "
     "and multilingual support."),
    ("KDR Case Management & Data Collector", "Python, Azure, Swagger/OpenAPI",
     "API alignment, automation, testing, defect resolution and release readiness."),
    ("META SBX Download Tool & Switchboard", "Python, Automation",
     "Secure-portal download automation plus high-volume parsing and data processing for priority matters."),
    ("STR Application & Saved Search Modernization", "RelativityOne, REST APIs",
     "End-to-end custom development: requirements, API integration, UI/UX, bulk workflows, QA "
     "and stakeholder-driven refinements."),
]

RECOGNITION = [
    "**Mega Star Award, KPMG** (June 2026): recognized for contributions during the assessment period.",
    "Appreciated by stakeholders for dependable META processing continuity and thorough KDR "
    "application validation.",
]

CERTIFICATIONS = [
    ("KPMG Badges", "KPMG Workbench – Developer Knowledge; AIQ Copilot Studio Maker; Copilot Studio Pro Maker"),
    ("Courses", "Java, JavaScript, HTML5 & CSS3 (JSpiders); Python Programming (Udemy, MIT); "
                "AWS Fundamentals (AWS)"),
    ("Workshops", "Unity Game Development (GITAM); Ethical Hacking (NITK)"),
    ("Continuous Learning", "GitHub & Microsoft Copilot; hands-on AI-assisted development, Azure, "
                            "RelativityOne and APIs"),
]

EDUCATION = {
    "degree": "Bachelor of Engineering – Computer Science and Engineering",
    "years": "2017 – 2021",
    "school": "Rajeev Institute of Technology, Hassan",
}

ACADEMIC_PROJECT = {
    "name": "Driver Drowsiness Detection using AI",
    "stack": "Python, OpenCV, TensorFlow, CNN, Flask, Tkinter",
    "text": "Designed, trained and evaluated a camera-based drowsiness-detection module, achieving a documented "
            "**80% accuracy**, and explored an IR-filter approach for low-light conditions.",
}

KEYWORDS = ("Software Engineer, Python, AI, REST API, Flask, Azure, Azure Functions, RelativityOne, "
            "Automation, Pytest, Selenium, BigQuery, Swagger, OpenAPI, Prompt Engineering, Forensic Technology")


# ---------------------------------------------------------------- helpers
def set_spacing(p, before=0, after=0, line=1.0):
    pf = p.paragraph_format
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line


def add_run(p, text, bold=False, italic=False, size=None, color=None):
    run = p.add_run(text)
    run.bold = bold
    run.italic = italic
    if size:
        run.font.size = Pt(size)
    if color is not None:
        run.font.color.rgb = color
    return run


def add_rich(p, text, size=None, color=None, base_bold=False):
    """Writes text where **segments** are bold."""
    for i, part in enumerate(text.split("**")):
        if part:
            add_run(p, part, bold=base_bold or i % 2 == 1, size=size, color=color)


def add_hyperlink(p, url, text, color=ACCENT):
    r_id = p.part.relate_to(url, RT.HYPERLINK, is_external=True)
    link = OxmlElement("w:hyperlink")
    link.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    clr = OxmlElement("w:color")
    clr.set(qn("w:val"), str(color))
    rpr.append(clr)
    u = OxmlElement("w:u")
    u.set(qn("w:val"), "single")
    rpr.append(u)
    run.append(rpr)
    t = OxmlElement("w:t")
    t.text = text
    t.set(qn("xml:space"), "preserve")
    run.append(t)
    link.append(run)
    p._p.append(link)


def bottom_border(p, color="1F4E79", size=8):
    ppr = p._p.get_or_add_pPr()
    bdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), str(size))
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), color)
    bdr.append(bottom)
    ppr.append(bdr)


def keep_with_next(p):
    p.paragraph_format.keep_with_next = True


def section(doc, title):
    p = doc.add_paragraph()
    set_spacing(p, before=10, after=4)
    add_run(p, title.upper(), bold=True, size=11.5, color=ACCENT)
    bottom_border(p)
    keep_with_next(p)
    return p


def bullet(doc, text, size=10, after=2.5):
    p = doc.add_paragraph(style="List Bullet")
    pf = p.paragraph_format
    pf.left_indent = Inches(0.2)
    pf.first_line_indent = Inches(-0.15)
    set_spacing(p, after=after, line=1.05)
    add_rich(p, text, size=size, color=DARK)
    return p


def label_line(doc, label, value, after=2):
    p = doc.add_paragraph()
    set_spacing(p, after=after, line=1.05)
    add_run(p, f"{label}: ", bold=True, size=10, color=ACCENT)
    add_rich(p, value, size=10, color=DARK)
    return p


def left_right(doc, left, right, left_size=11, before=4, after=0):
    p = doc.add_paragraph()
    set_spacing(p, before=before, after=after)
    p.paragraph_format.tab_stops.add_tab_stop(TEXT_W, WD_TAB_ALIGNMENT.RIGHT)
    add_run(p, left, bold=True, size=left_size, color=DARK)
    add_run(p, "\t" + right, italic=True, size=10, color=MUTED)
    keep_with_next(p)
    return p


# ---------------------------------------------------------------- build
def build():
    doc = Document()

    sec = doc.sections[0]
    sec.page_width, sec.page_height = PAGE_W, PAGE_H
    sec.left_margin = sec.right_margin = MARGIN_X
    sec.top_margin = sec.bottom_margin = MARGIN_Y

    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(10)
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), FONT)
    normal.element.rPr.rFonts.set(qn("w:hAnsi"), FONT)
    normal.element.rPr.rFonts.set(qn("w:cs"), FONT)

    props = doc.core_properties
    props.title = "Karthik B - Software Engineer Resume"
    props.author = "Karthik B"
    props.subject = "Software Engineer | Python & AI Applications"
    props.keywords = KEYWORDS

    # Header (kept in body so ATS parsers read it)
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_spacing(p, after=1)
    add_run(p, NAME, bold=True, size=20, color=ACCENT)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_spacing(p, after=2)
    add_run(p, HEADLINE, bold=True, size=10.5, color=DARK)

    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_spacing(p, after=2)
    add_run(p, f"{LOCATION}  |  {PHONE}  |  ", size=10, color=DARK)
    add_hyperlink(p, f"mailto:{EMAIL}", EMAIL)
    add_run(p, "  |  ", size=10, color=DARK)
    add_hyperlink(p, LINKEDIN_URL, LINKEDIN_TEXT)
    add_run(p, "  |  ", size=10, color=DARK)
    add_hyperlink(p, PORTFOLIO_URL, PORTFOLIO_TEXT)

    section(doc, "Professional Summary")
    p = doc.add_paragraph()
    set_spacing(p, after=2, line=1.05)
    add_rich(p, SUMMARY, size=10, color=DARK)

    section(doc, "Key Achievements")
    for item in ACHIEVEMENTS:
        bullet(doc, item)

    section(doc, "Technical Skills")
    for label, value in SKILLS:
        label_line(doc, label, value)

    section(doc, "Professional Experience")
    for i, job in enumerate(EXPERIENCE):
        left_right(doc, job["company"], job["meta"], before=2 if i == 0 else 6)
        for title, dates in job["roles"]:
            p = doc.add_paragraph()
            set_spacing(p, after=2)
            p.paragraph_format.tab_stops.add_tab_stop(TEXT_W, WD_TAB_ALIGNMENT.RIGHT)
            add_run(p, title, bold=True, italic=True, size=10.5, color=ACCENT)
            if dates:
                add_run(p, "\t" + dates, italic=True, size=10, color=MUTED)
            keep_with_next(p)
        for j, b in enumerate(job["bullets"]):
            p = bullet(doc, b)
            # Keep short later jobs on one page; for the first job only bind the last bullet to its stack.
            if i > 0 or j == len(job["bullets"]) - 1:
                keep_with_next(p)
        p = doc.add_paragraph()
        set_spacing(p, before=2, after=1)
        add_run(p, "Tech Stack: ", bold=True, size=9.5, color=ACCENT)
        add_run(p, job["stack"], italic=True, size=9.5, color=MUTED)

    section(doc, "Key Projects - KPMG")
    for name, stack, desc in PROJECTS:
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.left_indent = Inches(0.2)
        p.paragraph_format.first_line_indent = Inches(-0.15)
        set_spacing(p, after=2.5, line=1.05)
        add_run(p, name, bold=True, size=10, color=DARK)
        add_run(p, f" ({stack}): ", italic=True, size=10, color=MUTED)
        add_rich(p, desc, size=10, color=DARK)

    section(doc, "Awards & Recognition")
    for item in RECOGNITION:
        bullet(doc, item)

    section(doc, "Certifications & Training")
    for label, value in CERTIFICATIONS:
        label_line(doc, label, value)

    section(doc, "Education")
    left_right(doc, EDUCATION["degree"], EDUCATION["years"], left_size=10.5, before=2)
    p = doc.add_paragraph()
    set_spacing(p, after=1)
    add_run(p, EDUCATION["school"], size=10, color=DARK)

    section(doc, "Academic Project")
    p = doc.add_paragraph()
    set_spacing(p, before=2, after=1)
    add_run(p, ACADEMIC_PROJECT["name"], bold=True, size=10.5, color=DARK)
    add_run(p, f"  |  {ACADEMIC_PROJECT['stack']}", italic=True, size=10, color=MUTED)
    keep_with_next(p)
    bullet(doc, ACADEMIC_PROJECT["text"])

    docx_path = OUT_DIR / f"{OUT_NAME}.docx"
    doc.save(docx_path)
    return docx_path


def to_pdf(docx_path):
    from docx2pdf import convert
    pdf_path = docx_path.with_suffix(".pdf")
    convert(str(docx_path), str(pdf_path))
    return pdf_path


if __name__ == "__main__":
    docx_file = build()
    pdf_file = to_pdf(docx_file)
    print(f"Created: {docx_file}\nCreated: {pdf_file}")
