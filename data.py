"""All portfolio content lives in this file. Edit it, then run:  python build.py

Content source: content/my_data.md. Nothing here should state more than that file does.
"""

# ---------------------------------------------------------------------------
# EDIT HERE: site settings and public links
# ---------------------------------------------------------------------------

# Public address of the deployed site, e.g. "https://karthik.example.com".
# Used for canonical links, the sitemap and social cards. Leave "" until you deploy.
SITE_URL = ""

# Leave a value "" to hide that button. No email address is published, by design.
CONTACT = {
    "linkedin": "https://www.linkedin.com/in/karthik-18k/",
    "github": "",
}

CONFIDENTIALITY_NOTE = (
    "Certain project details have been summarized or anonymized to protect "
    "confidential and proprietary information."
)

# ---------------------------------------------------------------------------
# Personal information
# ---------------------------------------------------------------------------

PERSON = {
    "name": "Karthik B",
    "initials": "KB",
    "title": "Associate Consultant",
    "role_line": "Custom Application Developer",
    "headline": "Associate Consultant | Custom Application Developer | Forensic Technology",
    "tagline": (
        "Building scalable enterprise applications, intelligent automation, and "
        "AI-enabled solutions that solve real operational challenges."
    ),
    "hero_blurb": (
        "Nearly five years across enterprise application development, workflow automation, "
        "AI-enabled solutions, data processing, testing, and production support."
    ),
    "description": (
        "Associate Consultant specializing in custom application development, Python automation, "
        "AI-enabled solutions, RelativityOne applications, API integration, and forensic technology."
    ),
    "keywords": [
        "Karthik B", "Associate Consultant", "Custom Application Developer", "Python developer",
        "Python automation", "RelativityOne", "REST API integration", "Azure Functions",
        "Forensic technology", "AI-enabled applications",
    ],
    "about": [
        "I am an Associate Consultant and custom application developer with nearly five years of "
        "experience building enterprise applications, process-automation tools, data-processing "
        "workflows, and AI-enabled solutions.",
        "I currently work within Forensic Technology, where I contribute to Python automation, REST API "
        "integrations, RelativityOne applications, Azure-based workflows, AI summarization and "
        "translation, application testing, deployment support, and production troubleshooting.",
        "Before moving into forensic technology, I worked in the fintech domain across Python backend "
        "development and software quality engineering. My work included automating commission "
        "processing, developing financial-data utilities, creating Selenium-based file-download "
        "workflows, processing high-volume datasets, and building tools for bulk DBF, CSV, and Excel "
        "operations.",
        "I enjoy solving operational problems that combine application development, automation, "
        "testing, data validation, user-experience improvement, and clear technical communication.",
    ],
    "resume_summary": (
        "Associate Consultant and custom application developer with nearly five years of experience "
        "in enterprise applications, Python automation, AI-enabled solutions, RelativityOne "
        "applications, REST API integration, Azure-based workflows, data processing, testing, and "
        "production support across forensic technology and fintech."
    ),
    "location": "Bengaluru, India",
    "focus_areas": [
        "Custom application development",
        "Python automation",
        "AI-enabled solutions",
        "RelativityOne applications",
        "REST API integration",
        "Azure automation",
        "Data processing",
        "Functional and API testing",
        "Deployment and production support",
        "Technical documentation",
        "Forensic technology",
        "Financial technology",
    ],
    "languages": ["Kannada", "English", "Hindi"],
    "stats": [
        ("Role", "Associate Consultant"),
        ("Based", "Bengaluru, India"),
        ("Experience", "Nearly 5 years"),
        ("Domains", "Forensic tech · Fintech · Legal tech"),
    ],
    "hero_phrases": [
        "Python automation",
        "AI-enabled applications",
        "RelativityOne applications",
        "Azure-based workflows",
        "REST API integrations",
    ],
    "hero_nodes": ["Python", "REST APIs", "Azure", "RelativityOne", "AI", "Data"],
}

# ---------------------------------------------------------------------------
# Impact at a glance
# qualifier: wording shown before the number. "from"/"to": numbers to count up.
# ---------------------------------------------------------------------------

IMPACT = [
    {
        "qualifier": "Approximately", "from": None, "to": 95, "suffix": "%",
        "label": "Reduction in manual effort",
        "context": "Attorney-license verification effort, through the ABL Verification Standalone Application.",
        "icon": "percent", "project": "abl-verification",
    },
    {
        "qualifier": "More than", "from": None, "to": 50, "suffix": "%",
        "label": "Performance improvement",
        "context": "Documented gain from the Query Quick backend redesign.",
        "icon": "gauge", "project": "query-quick",
    },
    {
        "qualifier": "Approximately", "from": 7000, "to": 8000, "suffix": " files",
        "label": "Secure downloads automated",
        "context": "Same-day dataset delivery through the META SBX Download Tool.",
        "icon": "download", "project": "meta-sbx-download",
    },
    {
        "qualifier": "Under", "from": None, "to": 50, "suffix": "%",
        "label": "Of allocated time",
        "context": "Partner-commission calculations completed using BigQuery at FISDOM.",
        "icon": "timer", "project": "commission-processing",
    },
]

# ---------------------------------------------------------------------------
# Experience
# ---------------------------------------------------------------------------

EXPERIENCE = [
    {
        "id": "kpmg",
        "current": True,
        "organization": "KPMG Global Services",
        "unit": "Forensic Technology Services",
        "role": "Associate Consultant – Custom Application Development, Automation and Forensic Technology",
        "previous_role": None,
        "location": "Bengaluru, India",
        "start": "Jan 2025",
        "end": "Present",
        "summary": (
            "I develop and enhance enterprise applications, automation tools, AI-assisted solutions, "
            "REST API integrations, data-processing workflows, and custom RelativityOne applications."
        ),
        "lanes": [
            ("PODS", "US Forensic Technology tools and RelativityOne application development."),
            ("KDR", "KPMG Digital Responder case-management and data-collection solutions."),
            ("META", "SBX/RSMF parsing, secure file downloads, high-volume data processing, validation, and quality control."),
        ],
        "stages": [],
        "responsibilities": [
            "Develop Python-based applications and automation tools for enterprise forensic-technology workflows.",
            "Build and enhance custom-page applications for RelativityOne.",
            "Integrate REST APIs and enterprise services with application workflows.",
            "Develop AI-enabled summarization and translation features.",
            "Build Azure-based automation using Azure Functions and Azure Logic Apps.",
            "Process and validate structured data in CSV, Excel, DBF, HTML, JSON, and XML formats.",
            "Perform functional, regression, API, UI, and end-to-end testing.",
            "Troubleshoot deployment and production issues.",
            "Review pull requests and contribute to code-quality practices.",
            "Prepare technical documentation, implementation notes, test cases, and knowledge-transfer material.",
            "Work with stakeholders to refine requirements and validate application behaviour.",
            "Support release readiness, deployment, and post-deployment verification.",
        ],
        "projects": [
            "abl-verification", "query-quick", "ai-summarizer-translator", "meta-sbx-download",
            "kdr-case-management", "kdr-data-collector", "str-application",
            "saved-search-modernization", "meta-matter-support",
        ],
        "technologies": [
            "Python", "Tkinter", "Selenium", "Pandas", "RelativityOne", "REST APIs", "JavaScript",
            "Azure Functions", "Azure Logic Apps", "Swagger/OpenAPI", "Pytest", "Postman", "GitHub",
        ],
        "outcomes": [
            "Approximately 95% reduction in manual attorney-license verification effort (ABL Verification).",
            "More than 50% performance improvement from the Query Quick backend redesign.",
            "Approximately 7,000–8,000 secure file downloads automated for same-day delivery (META SBX).",
        ],
    },
    {
        "id": "fisdom",
        "current": False,
        "organization": "FISDOM",
        "unit": None,
        "role": "SDET – L1",
        "previous_role": "SDE Trainee, Python Backend",
        "location": "Bengaluru, India",
        "start": "Jan 2022",
        "end": "Dec 2024",
        "summary": (
            "I worked across Python backend development, software testing, financial workflow "
            "automation, high-volume file processing, commission calculations, data transformation, "
            "and internal productivity tools."
        ),
        "lanes": [],
        "stages": [
            ("SDE Trainee – Python Backend", "Jan 2022 – Nov 2023",
             "Started as a Python backend trainee working on automation, data processing, backend "
             "utilities, and financial-technology workflows."),
            ("SDET – L1", "Nov 2023 – Dec 2024",
             "Combined development and quality-engineering responsibilities to improve workflow "
             "reliability, product quality, and processing efficiency."),
        ],
        "responsibilities": [
            "Automated commission-processing activities using Python.",
            "Built automated infrastructure for downloading files from fintech and stock-exchange platforms.",
            "Processed financial data using Python, Pandas, Selenium, Flask, and BigQuery.",
            "Developed utilities for bulk DBF, CSV, and Excel file processing.",
            "Built testing tools to improve application quality.",
            "Identified development and workflow gaps.",
            "Performed backend and workflow validation.",
            "Supported data-driven financial processes.",
            "Worked with structured data and database workflows.",
            "Improved operational efficiency through automation.",
        ],
        "projects": [
            "commission-processing", "fintech-file-automation", "bulk-data-utilities",
            "testing-quality-utilities",
        ],
        "technologies": ["Python", "Pandas", "Selenium", "Flask", "SQL", "BigQuery", "CSV", "Excel", "DBF"],
        "outcomes": [
            "Partner-commission calculations completed in BigQuery in less than 50% of the allocated time.",
        ],
    },
]

TEAM_CONTRIBUTIONS = [
    "GitHub repository management", "Pull-request guidance", "Code-review support",
    "Deployment troubleshooting", "Release support", "Technical knowledge transfer",
    "Reusable documentation", "Testing guidance", "Requirements clarification",
    "Production issue diagnosis",
]

# ---------------------------------------------------------------------------
# Projects (rendered as cards and as one case-study page each)
# Optional keys: challenge, solution, capabilities, metric. Missing ones are not shown.
# ---------------------------------------------------------------------------

PROJECTS = [
    {
        "slug": "abl-verification",
        "name": "ABL Verification Standalone Application",
        "employer": "KPMG", "stream": "PODS",
        "category": "Desktop automation",
        "filters": ["Python", "Automation", "Data Processing"],
        "overview": "A Python and Tkinter attorney bar-license verification application that supports nine US states through a unified CSV-driven workflow.",
        "challenge": "Attorney-license verification across multiple states relied on repetitive manual effort.",
        "role": "Co-developed the application.",
        "contributions": [
            "Contributing to state-specific verification workflows",
            "Supporting Python-based scraping and data extraction",
            "Implementing CSV-driven processing",
            "Supporting a unified graphical user interface",
            "Consolidating output generation",
            "Adding input validation and logging",
            "Improving module integration and execution",
            "Supporting packaging through PyInstaller",
            "Validating results across multiple states",
        ],
        "solution": "State-specific results are consolidated through one CSV-driven workflow, with structured logging and automation controls for more reliable execution.",
        "stack": ["Python", "Tkinter", "Selenium", "Pandas", "CSV", "PyInstaller", "Logging"],
        "outcome": "Reduced repetitive manual verification effort by approximately 95% while creating a more consistent multi-state verification process.",
        "metric": ("~95%", "reduction in manual verification effort"),
    },
    {
        "slug": "query-quick",
        "name": "Query Quick",
        "employer": "KPMG", "stream": "PODS",
        "category": "RelativityOne application",
        "filters": ["Python", "RelativityOne"],
        "overview": "A RelativityOne saved-search analytics application.",
        "challenge": "The existing backend architecture had performance bottlenecks affecting saved-search analytics.",
        "role": "Independently redesigned the backend architecture.",
        "contributions": [
            "Reviewing the existing backend architecture",
            "Identifying performance bottlenecks",
            "Redesigning backend processing",
            "Improving saved-search analytics performance",
            "Supporting functional and UI enhancements",
            "Performing testing and defect resolution",
            "Supporting production deployment in RelativityOne",
            "Preparing supporting technical documentation",
        ],
        "stack": ["Python", "RelativityOne", "REST APIs", "JavaScript", "JSON", "Testing"],
        "outcome": "Improved application performance by more than 50%, resulting in faster processing and a better user experience.",
        "metric": ("50%+", "documented performance improvement"),
    },
    {
        "slug": "ai-summarizer-translator",
        "name": "AI Summarizer and AI Translator",
        "employer": "KPMG", "stream": "PODS",
        "category": "AI-enabled RelativityOne components",
        "filters": ["Python", "AI", "RelativityOne"],
        "overview": "AI-enabled RelativityOne review components that support document summarization and multilingual translation directly within review workflows.",
        "role": "Developed the components.",
        "contributions": [
            "Designing prompt-driven summarization and translation workflows",
            "Integrating enterprise AI APIs",
            "Implementing field-value persistence",
            "Supporting previously generated output reuse",
            "Improving token utilization",
            "Supporting multilingual translation",
            "Validating AI-generated responses",
            "Conducting functional and UI testing",
            "Resolving defects",
            "Supporting deployment and production readiness",
        ],
        "capabilities": [
            "AI-generated document summaries",
            "Multilingual document translation",
            "Prompt configuration",
            "Token-aware content processing",
            "Saved output reuse",
            "Relativity field-value storage",
            "Error and response handling",
        ],
        "stack": ["Python", "REST APIs", "RelativityOne", "AI Prompt Workflows", "KPMG Workbench", "JSON"],
        "outcome": "Document summarization and multilingual translation available directly within review workflows, with token-aware processing and reusable saved output.",
    },
    {
        "slug": "meta-sbx-download",
        "name": "META SBX Download Tool",
        "employer": "KPMG", "stream": "META",
        "category": "File automation",
        "filters": ["Python", "Automation", "Data Processing"],
        "overview": "An automation tool built for an urgent requirement involving secure-portal file downloads.",
        "challenge": "An urgent requirement to download a large dataset from a secure portal and deliver it the same day.",
        "role": "Developed the automation tool.",
        "contributions": [
            "Understanding the urgent operational requirement",
            "Automating secure-portal downloads",
            "Managing high-volume file processing",
            "Tracking download progress",
            "Supporting output completeness",
            "Handling failures and retries",
            "Validating the downloaded dataset",
            "Supporting same-day delivery",
        ],
        "stack": ["Python", "Selenium", "File Automation", "Logging", "Data Validation"],
        "outcome": "Automated approximately 7,000–8,000 secure file downloads, enabling same-day delivery for a priority requirement.",
        "metric": ("7,000–8,000", "secure file downloads automated"),
    },
    {
        "slug": "kdr-case-management",
        "name": "KDR Case Management",
        "employer": "KPMG", "stream": "KDR",
        "category": "Enterprise case management",
        "filters": ["Python", "Azure", "Testing"],
        "overview": "An enterprise forensic case-management solution.",
        "role": "Contributed to engineering, testing, validation, and release readiness.",
        "contributions": [
            "Resolving Data Transfer Object issues",
            "Aligning API models and application behaviour",
            "Creating automated comparison utilities",
            "Performing functional and end-to-end testing",
            "Identifying workflow and user-interface defects",
            "Supporting production issue resolution",
            "Validating application behaviour against requirements",
            "Preparing release-readiness documentation",
            "Supporting technical and functional teams during issue resolution",
        ],
        "stack": ["Python", "REST APIs", "Swagger/OpenAPI", "Azure", "Pytest", "Postman", "GitHub"],
        "outcome": "Supported release readiness and production issue resolution through API alignment, validation, and end-to-end testing.",
    },
    {
        "slug": "kdr-data-collector",
        "name": "KDR Data Collector",
        "employer": "KPMG", "stream": "KDR",
        "category": "API alignment and test automation",
        "filters": ["Python", "Azure", "Automation", "Testing"],
        "overview": "Engineering contributions to KDR Data Collector through API alignment, Python automation, OpenAPI validation, test-suite development, defect resolution, and release support.",
        "role": "Contributed to engineering, validation, and release support.",
        "contributions": [
            "Comparing Swagger and OpenAPI contracts",
            "Automating API specification comparisons using Python",
            "Identifying model and DTO inconsistencies",
            "Supporting automated test-suite creation",
            "Validating API responses",
            "Supporting Azure automation",
            "Troubleshooting production issues",
            "Performing end-to-end validation",
            "Supporting release readiness",
        ],
        "stack": ["Python", "Swagger/OpenAPI", "REST APIs", "Azure Functions", "Azure Logic Apps", "Pytest"],
        "outcome": "Supported release readiness through contract comparison, automated testing, and end-to-end validation.",
    },
    {
        "slug": "str-application",
        "name": "STR Application",
        "employer": "KPMG", "stream": "PODS",
        "category": "RelativityOne application",
        "filters": ["Python", "RelativityOne", "Testing"],
        "overview": "A custom RelativityOne application covering requirement clarification, documentation, development, stakeholder refinements, test-data preparation, and functional validation.",
        "role": "Independently led the delivery.",
        "contributions": [
            "Requirement clarification",
            "Solution planning",
            "Technical documentation",
            "Application development",
            "API research and integration",
            "Test-data creation",
            "UI and workflow refinements",
            "Stakeholder feedback implementation",
            "End-to-end functional testing",
            "Defect identification and resolution",
            "Delivery validation",
        ],
        "stack": ["RelativityOne", "Python", "REST APIs", "JavaScript", "HTML", "CSS", "Postman"],
        "outcome": "Delivered a custom RelativityOne application validated through comprehensive end-to-end functional testing.",
    },
    {
        "slug": "saved-search-modernization",
        "name": "Saved Search Modernization",
        "employer": "KPMG", "stream": "PODS",
        "category": "RelativityOne application",
        "filters": ["RelativityOne", "Testing"],
        "overview": "Modernization of a custom Saved Search application through improvements to its user interface, filters, API interactions, and bulk workflows.",
        "role": "Modernized the application.",
        "contributions": [
            "Enhancing search and filtering workflows",
            "Improving user-interface components",
            "Supporting API integration",
            "Improving bulk-processing behaviour",
            "Validating saved-search results",
            "Performing functional and regression testing",
            "Incorporating stakeholder feedback",
        ],
        "stack": [],
        "outcome": "Improved search, filtering, and bulk-processing workflows, validated through functional and regression testing.",
    },
    {
        "slug": "meta-matter-support",
        "name": "META Matter Support",
        "employer": "KPMG", "stream": "META",
        "category": "Data processing and quality control",
        "filters": ["Data Processing", "Testing"],
        "overview": "Support for multiple META matters through parsing corrections, data processing, historical validation, regression quality control, and output verification.",
        "role": "Supported multiple matters.",
        "contributions": [
            "Correcting parser behaviour",
            "Processing matter-specific datasets",
            "Validating historical results",
            "Performing regression quality control",
            "Comparing current and previous outputs",
            "Verifying processed datasets",
            "Maintaining delivery continuity",
            "Troubleshooting data-processing issues",
        ],
        "stack": [],
        "outcome": "Maintained delivery continuity across matters, recognised through stakeholder appreciation.",
    },
    {
        "slug": "commission-processing",
        "name": "Commission Processing Automation",
        "employer": "FISDOM", "stream": None,
        "category": "Fintech automation",
        "filters": ["Python", "Automation", "Data Processing"],
        "overview": "Automation of commission-processing activities using Python and data-driven workflows, including partner-commission calculations in BigQuery.",
        "role": "Automated the workflows and supported BigQuery calculations.",
        "contributions": [
            "Automated repetitive commission workflows",
            "Processed partner and transaction data",
            "Used BigQuery for large-scale calculations",
            "Validated calculated commission results",
            "Supported output reconciliation",
            "Reduced overall processing time",
        ],
        "stack": ["Python", "Pandas", "SQL", "BigQuery", "CSV", "Excel"],
        "outcome": "Completed partner-commission calculations in BigQuery in less than 50% of the allocated time.",
        "metric": ("<50%", "of the allocated time"),
    },
    {
        "slug": "fintech-file-automation",
        "name": "Fintech and Stock-Exchange File Automation",
        "employer": "FISDOM", "stream": None,
        "category": "Browser automation",
        "filters": ["Python", "Automation", "Data Processing"],
        "overview": "Automated infrastructure for downloading and processing files from fintech and stock-exchange platforms using Selenium, Flask, and Python libraries.",
        "role": "Built the automation infrastructure.",
        "contributions": [
            "Automated browser-based file downloads",
            "Processed downloaded files",
            "Handled platform-specific workflows",
            "Validated input and output data",
            "Supported scheduled and repeatable execution",
            "Improved traceability and reliability",
        ],
        "stack": ["Python", "Selenium", "Flask", "Requests", "Pandas"],
        "outcome": "Delivered repeatable, traceable file download and processing across multiple platforms.",
    },
    {
        "slug": "bulk-data-utilities",
        "name": "Bulk Data-Processing Utilities",
        "employer": "FISDOM", "stream": None,
        "category": "Data utilities",
        "filters": ["Python", "Data Processing"],
        "overview": "Utilities for bulk processing of DBF, CSV, and Excel files, improving workflow efficiency for multiple internal teams.",
        "role": "Developed the utilities.",
        "contributions": [],
        "capabilities": [
            "Bulk file ingestion", "Format conversion", "Data cleanup", "Record validation",
            "Dataset consolidation", "Output generation", "Exception reporting",
        ],
        "stack": ["Python", "Pandas", "DBF", "CSV", "Excel"],
        "outcome": "Improved workflow efficiency for multiple internal teams.",
    },
    {
        "slug": "testing-quality-utilities",
        "name": "Testing and Quality Utilities",
        "employer": "FISDOM", "stream": None,
        "category": "Quality engineering",
        "filters": ["Python", "Testing"],
        "overview": "Testing tools that improved product efficiency and quality while helping identify critical development gaps.",
        "role": "Developed the testing tools.",
        "contributions": [
            "Created reusable test utilities",
            "Validated backend behaviour",
            "Identified defects and missing scenarios",
            "Improved regression coverage",
            "Supported issue reproduction",
            "Verified fixes and output quality",
        ],
        "stack": ["Python"],
        "outcome": "Improved product efficiency and quality, and surfaced critical development gaps.",
    },
]

PROJECT_FILTERS = ["Python", "AI", "Automation", "RelativityOne", "Azure", "Data Processing", "Testing"]

# ---------------------------------------------------------------------------
# Skills. level: professional | projects | working
# Each skill appears once. "aliases" are other names used in project stacks, so the
# skill-click highlight can find related roles and projects.
# ---------------------------------------------------------------------------

LEVEL_LABELS = {
    "professional": "Applied professionally",
    "projects": "Applied in projects",
    "working": "Working knowledge",
}


def _s(name, level, *aliases):
    return {"name": name, "level": level, "aliases": list(aliases)}


SKILLS = [
    {"name": "Programming Languages", "icon": "code", "skills": [
        _s("Python 3", "professional", "Python"), _s("SQL", "professional"),
        _s("JavaScript", "professional"), _s("TypeScript", "working"),
        _s("Core Java", "working"), _s("Shell scripting", "working"), _s("Python 2", "working"),
    ]},
    {"name": "Backend and Application Development", "icon": "layers", "skills": [
        _s("REST API development and integration", "professional", "REST APIs"),
        _s("RelativityOne custom-page applications", "professional", "RelativityOne"),
        _s("Flask", "professional"),
        _s("Tkinter desktop applications", "professional", "Tkinter"),
        _s("File-processing applications", "professional"),
        _s("Logging and error handling", "professional", "Logging"),
        _s("Backend performance optimization", "professional"),
        _s("Modular application architecture", "professional"),
        _s("Request and response handling", "professional"),
    ]},
    {"name": "Automation and Data Processing", "icon": "workflow", "skills": [
        _s("Selenium", "professional"), _s("Pandas", "professional"), _s("Requests", "professional"),
        _s("Secure file-download automation", "professional", "File Automation"),
        _s("High-volume batch processing", "professional"),
        _s("Data validation and reconciliation", "professional", "Data Validation"),
        _s("CSV processing", "professional", "CSV"), _s("Excel processing", "professional", "Excel"),
        _s("DBF processing", "professional", "DBF"), _s("HTML processing", "professional", "HTML"),
    ]},
    {"name": "Cloud and Integration", "icon": "cloud", "skills": [
        _s("Microsoft Azure", "professional", "Azure"),
        _s("Azure Functions", "professional"), _s("Azure Logic Apps", "professional"),
        _s("Swagger/OpenAPI", "professional"), _s("Postman", "professional"),
        _s("JSON", "professional"), _s("XML", "professional"),
        _s("Google Cloud Platform", "professional"), _s("OAuth", "working"),
    ]},
    {"name": "Artificial Intelligence", "icon": "brain", "skills": [
        _s("AI summarization", "professional"), _s("AI translation", "professional"),
        _s("Prompt engineering", "professional", "AI Prompt Workflows"),
        _s("Token optimization", "professional"), _s("API-based AI integration", "professional"),
        _s("KPMG Workbench integration", "professional", "KPMG Workbench"),
        _s("Copilot-assisted development", "professional"),
        _s("TensorFlow", "projects"), _s("CNN", "projects"), _s("OpenCV", "projects"),
        _s("PyTorch fundamentals", "working"),
    ]},
    {"name": "Testing and Quality Engineering", "icon": "flask", "skills": [
        _s("Pytest", "professional"), _s("Functional testing", "professional", "Testing"),
        _s("Regression testing", "professional"), _s("API testing", "professional"),
        _s("UI testing", "professional"), _s("End-to-end testing", "professional"),
        _s("Test-data preparation", "professional"), _s("Output verification", "professional"),
        _s("Defect reproduction", "professional"),
        _s("Release-readiness validation", "professional"),
        _s("Production issue verification", "professional"),
    ]},
    {"name": "Engineering Tools and Practices", "icon": "terminal", "skills": [
        _s("Git", "professional"), _s("GitHub", "professional"), _s("Pull requests", "professional"),
        _s("Code reviews", "professional"), _s("CI/CD troubleshooting", "professional"),
        _s("Debugging", "professional"), _s("Deployment support", "professional"),
        _s("Release support", "professional"), _s("Technical documentation", "professional"),
        _s("Knowledge transfer", "professional"),
    ]},
    {"name": "Databases and Data Platforms", "icon": "database", "skills": [
        _s("BigQuery", "professional"),
        _s("RelativityOne field and object data", "professional"),
        _s("Structured file-based datasets", "professional"), _s("MySQL", "projects"),
    ]},
    {"name": "Operating Systems", "icon": "cpu", "skills": [
        _s("Windows", "working"), _s("Linux", "working"), _s("macOS", "working"),
    ]},
]

MARQUEE = [
    "Python", "Flask", "Selenium", "Pandas", "Tkinter", "RelativityOne", "REST APIs",
    "Azure Functions", "Azure Logic Apps", "Swagger/OpenAPI", "BigQuery", "SQL", "JavaScript",
    "Pytest", "Postman", "GitHub",
]

# ---------------------------------------------------------------------------
# Certifications, recognition, education
# Add "issuer", "date", "credential_id" or "verify_url" when you have them; they only show if set.
# ---------------------------------------------------------------------------

CERTIFICATIONS = [
    {"name": "KPMG Workbench – Developer Knowledge", "type": "badge",
     "description": "Demonstrates knowledge of the KPMG Workbench platform, its development concepts, and its use in enterprise application workflows."},
    {"name": "AIQ Copilot Studio Maker", "type": "badge",
     "description": "Demonstrates knowledge of creating AI-powered conversational experiences and automated workflows using Microsoft Copilot Studio."},
    {"name": "Copilot Studio Pro Maker", "type": "badge",
     "description": "Demonstrates more advanced knowledge of Copilot Studio development, conversational design, workflow integration, and enterprise AI use cases."},
    {"name": "GitHub Copilot and GitHub Learning", "type": "badge",
     "description": "Completed learning related to GitHub and GitHub Copilot, and applied AI-assisted development practices directly to professional project delivery."},
    {"name": "Java, JavaScript, HTML5 and CSS3", "type": "workshop", "issuer": "JSpiders"},
    {"name": "Python Programming", "type": "workshop", "issuer": "Udemy"},
    {"name": "Python Fundamentals", "type": "workshop", "issuer": "MIT"},
    {"name": "AWS Basics and Fundamentals", "type": "workshop", "issuer": "Amazon Web Services"},
    {"name": "Unity Game Development Workshop", "type": "workshop", "issuer": "GITAM"},
    {"name": "Ethical Hacking Workshop", "type": "workshop", "issuer": "NITK"},
]

RECOGNITION = [
    {"kind": "Formal award", "name": "Mega Star Award", "issuer": "KPMG", "date": "16 June 2026",
     "summary": "Received in recognition of contributions made during the assessment period.", "icon": "star"},
    {"kind": "Stakeholder appreciation", "name": "Stakeholder Appreciation", "issuer": None, "date": None,
     "summary": "Appreciation received for dependable continuity of META data processing, detailed KDR application validation, consistent delivery support, and thorough output and workflow verification.",
     "icon": "users"},
    {"kind": "Achievement", "name": "State-Level Boot Camp – Runner-up", "issuer": "MCE, Hassan", "date": None,
     "summary": "Achieved the runner-up position in a state-level boot camp.", "icon": "trophy"},
    {"kind": "Volunteering", "name": "Technical Event Volunteering", "issuer": "Rajeev Institute of Technology", "date": None,
     "summary": "Participated as a volunteer in Hackintosh 2K19 and Hackberry 2.0.", "icon": "award"},
]

EDUCATION = [
    {"degree": "Bachelor of Engineering in Computer Science and Engineering",
     "institution": "Rajeev Institute of Technology", "location": "Hassan", "period": "2017 – 2021",
     "areas": ["Programming", "Database management", "Web development", "Artificial intelligence",
               "Machine learning", "Computer vision", "Software development lifecycle",
               "Application development"]},
    {"degree": "Pre-University Education", "institution": "Vidhya Ashram Pre-University",
     "location": "Mysuru", "period": "2015 – 2017", "areas": []},
]

INTERNSHIP = {
    "organization": "HEXNBITS", "role": "AI/ML Intern", "location": "Noida", "period": "October 2020",
    "project": "Car Model Acceptance",
    "summary": "Developed an AI and machine-learning concept intended to help users make informed car-purchase decisions based on their selected requirements.",
    "stack": ["Python", "Pandas", "Matplotlib", "OpenCV"],
    "learnings": [
        "Gained practical exposure to the software development lifecycle.",
        "Learned about data refinement and preprocessing.",
        "Explored the application of AI and machine learning to recommendation problems.",
        "Worked with Python-based data-analysis libraries.",
        "Understood the relationship between user requirements, datasets, and model output.",
    ],
}

ACADEMIC_PROJECTS = [
    {"title": "Driver Drowsiness Detection Using AI",
     "summary": "Designed, trained, and evaluated an AI-based drowsiness-detection module that monitors a user's face through a camera, and explored an infrared filter for low-light operation.",
     "capabilities": ["Designing the AI module", "Preparing and processing image data",
                      "Training and evaluating a CNN model", "Implementing face and eye monitoring",
                      "Building an interactive user interface", "Integrating the model with Flask and Tkinter",
                      "Exploring low-light detection using an IR-filter approach"],
     "stack": ["Python", "OpenCV", "TensorFlow", "CNN", "Flask", "Tkinter", "Matplotlib", "HTML5", "CSS3", "JavaScript"],
     "result": "Achieved 80% model accuracy during project evaluation."},
    {"title": "Hi Krita – Personal Voice Assistant",
     "summary": "A personal voice-assistant concept that accepts voice input and responds in both spoken and written form.",
     "capabilities": ["Voice-input processing", "Natural-language interaction", "Text responses",
                      "Spoken responses", "Desktop user interface"],
     "stack": ["Python", "NLP", "Kivy", "Tkinter"], "result": None},
    {"title": "Hitha – Indian Law Suite Management System",
     "summary": "A web-based database-management project for an Indian law-suite management system, where users select keywords describing a crime to access related information.",
     "capabilities": [], "stack": ["HTML5", "CSS3", "JavaScript", "MySQL", "PHP"], "result": None},
    {"title": "V-GradeAssess",
     "summary": "A web-based application intended to support remote examination administration.",
     "capabilities": [], "stack": ["Python", "Flask", "MySQL", "HTML5", "CSS3", "JavaScript"], "result": None},
]

APPROACH = [
    ("Clarify the requirement", "Work with stakeholders to refine requirements and confirm expected behaviour before building.", "search"),
    ("Plan and document", "Turn requirements into solution plans, technical documentation, and test data.", "file"),
    ("Build and integrate", "Develop maintainable Python, RelativityOne, and Azure solutions integrated through REST APIs.", "code"),
    ("Test end-to-end", "Validate with functional, regression, API, UI, and end-to-end testing.", "flask"),
    ("Release and support", "Support deployment, post-deployment verification, and production troubleshooting.", "shield"),
    ("Share knowledge", "Leave reusable documentation, pull-request guidance, and knowledge-transfer material.", "users"),
]
