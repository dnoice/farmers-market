"""
Armageddon Treats -- Operational Document Modules
Generates 5 Word documents that build from foundation through Year 2:
  Module 1: Pre-Launch Timeline & Master Checklist
  Module 2: Regulatory & Permit Compliance Guide
  Module 3: Day-to-Day Operations Manual
  Module 4: Brand Identity & Marketing Playbook
  Module 5: Year 1-2 Growth Roadmap & Scaling Plan
"""

from doc_styles import *


# ======================================================================
#  MODULE 1 -- PRE-LAUNCH TIMELINE & MASTER CHECKLIST
# ======================================================================
def build_module_1():
    doc = setup_document()
    add_module_cover(doc, 1, "Pre-Launch Timeline\n& Master Checklist",
        "Foundation to Opening Day",
        meta_lines=[
            "Veteran-Owned Mobile Dessert Operation",
            "Target Launch: Santa Monica Farmers Markets, Q2 2026",
            "Financing: SBA 7(a) Microloan -- $14,000",
        ])
    add_header_footer(doc, "Module 1 -- Pre-Launch Timeline")

    # ── OVERVIEW ──────────────────────────────────────────────
    add_heading_styled(doc, "1. Strategic Overview", level=1)
    add_body_para(doc,
        "Launching Armageddon Treats is not a single event but a tightly sequenced chain of "
        "dependencies. A missed step or botched timeline cascades into months of delay. This "
        "module maps every task from loan funding through your first market day, organized into "
        "five operational phases. Each phase must be completed before the next can begin."
    )
    add_callout_box(doc,
        "CRITICAL PATH WARNING",
        "The Santa Monica Farmers Market RFP window opens only once per year, typically in "
        "March. Every preceding task -- SBA loan closing, trailer procurement, LACDPH plan "
        "check, commissary agreement, insurance binding -- must be fully resolved before that "
        "window opens. Missing it means a 12-month delay to your primary revenue stream."
    )

    # ── PHASE 1 ───────────────────────────────────────────────
    add_heading_styled(doc, "2. Phase-by-Phase Launch Sequence", level=1)

    add_phase_banner(doc, 1, "FINANCING & ENTITY FORMATION", "Months 1-2 (Jan-Feb)", "2D2D2D")

    add_heading_styled(doc, "2.1 Business Entity Formation", level=2)
    add_body_para(doc,
        "Before applying for any permits, loans, or licenses, the business entity must be "
        "legally established. This creates the foundation for every subsequent step."
    )

    tasks_entity = [
        ("Choose entity structure", "Sole proprietorship is fastest and cheapest for a single-owner micro-operation. An LLC offers liability protection but adds $70 (CA filing fee) plus $800/year minimum franchise tax. Recommendation: start as sole prop, convert to LLC after Year 1 profitability is confirmed."),
        ("Register DBA (Fictitious Business Name)", "File \"Armageddon Treats\" DBA with the LA County Registrar-Recorder/County Clerk. Fee: approximately $26. Must be published in a local newspaper for 4 consecutive weeks (cost: $40-$80). Timeline: 4-6 weeks total."),
        ("Obtain EIN from the IRS", "Apply online at irs.gov -- free, instant. Required for business bank accounts and SBA loan processing. Even sole proprietors should get an EIN to avoid using SSN on vendor applications."),
        ("Open a dedicated business bank account", "Required by the SBA and essential for clean bookkeeping. Many banks offer free business checking for veterans. Deposit any personal working capital here."),
        ("Obtain California Seller's Permit", "File with the California Department of Tax and Fee Administration (CDTFA). Free of charge. Required before any taxable sales and before applying for the Santa Monica vendor license."),
    ]

    add_styled_table(doc,
        ["Task", "Details & Notes"],
        [(t, d) for t, d in tasks_entity],
        col_widths=[2.2, 4.6])

    add_heading_styled(doc, "2.2 SBA 7(a) Microloan Application", level=2)
    add_body_para(doc,
        "The $14,000 SBA 7(a) microloan is the financial backbone of the entire operation. "
        "The application process is not instant -- expect 30-90 days from first contact with "
        "an SBA-approved lender to funding disbursement."
    )

    add_styled_table(doc,
        ["Step", "Action", "Timeline", "Notes"],
        [
            ["1", "Identify SBA-approved lender or SBDC", "Week 1", "Veterans should contact the SoCal VBOC (Veteran Business Outreach Center) for guided assistance"],
            ["2", "Gather documentation", "Week 1-2", "Business plan, personal financial statement (SBA Form 413), 2 years tax returns, projected cash flow"],
            ["3", "Submit loan application", "Week 2-3", "Lender reviews and submits to SBA for guarantee approval"],
            ["4", "SBA guarantee approval", "Week 3-6", "SBA reviews and issues guarantee; veteran fee waiver applied automatically"],
            ["5", "Loan closing & disbursement", "Week 6-10", "Funds deposited to business account; begin capital deployment immediately"],
        ],
        col_widths=[0.5, 2.0, 1.2, 3.1])

    add_callout_box(doc,
        "VETERAN ADVANTAGE",
        "Under the SBA Veterans Advantage program, the upfront guarantee fee is completely "
        "waived for veteran borrowers on 7(a) loans under $150,000. This saves approximately "
        "$280 on a $14,000 loan -- money that stays in your working capital. Ensure your DD-214 "
        "(Certificate of Release/Discharge) showing honorable discharge is included with the "
        "application package.")

    # ── PHASE 2 ───────────────────────────────────────────────
    add_phase_banner(doc, 2, "ASSET PROCUREMENT", "Month 2-3 (Feb-Mar)", "4A4A4A")

    add_heading_styled(doc, "2.3 Concession Trailer Acquisition", level=2)
    add_body_para(doc,
        "The trailer is the single largest capital expenditure at $7,500. The recommended "
        "strategy is a direct-to-manufacturer import of a new 10-13ft aluminum concession "
        "trailer, which arrives with basic electrical and the mandatory multi-compartment sinks."
    )

    add_styled_table(doc,
        ["Decision Point", "Recommendation", "Risk if Ignored"],
        [
            ["New import vs. used local", "New import ($7,000-$8,000)", "Used trailers may have hidden code violations that fail LACDPH plan check"],
            ["Trailer size", "10-13 ft (towable by half-ton truck)", "Larger trailers require heavier tow vehicles and wider commissary parking"],
            ["Sink configuration", "Must include 3-compartment warewashing + separate handwash sink", "Automatic plan check failure without proper sinks"],
            ["Electrical", "Must support ice shaver, cotton candy machine, lighting", "Underpowered electrical triggers UL compliance issues"],
            ["Tow vehicle", "Must already own a capable half-ton truck", "$14k budget cannot absorb a $12-18k truck purchase"],
        ],
        col_widths=[1.8, 2.4, 2.6])

    add_heading_styled(doc, "2.4 Commercial Equipment Procurement", level=2)

    add_styled_table(doc,
        ["Equipment", "Specification", "Est. Cost", "Requirement"],
        [
            ["Cotton Candy Machine", "Commercial spinner, ANSI/NSF certified", "$300-$600", "Must have NSF certification stamp"],
            ["Shaved Ice Machine", "Commercial block/cube shaver, ANSI/NSF", "$400-$800", "Must meet UL electrical standards"],
            ["Generator", "3,500-5,000W portable inverter generator", "$400-$700", "Must power all equipment + refrigeration simultaneously"],
            ["Refrigeration Unit", "12+ cu ft commercial under-counter", "$300-$500", "Mandatory for perishable ingredient storage per LACDPH"],
            ["Matte-Black Vinyl Wrap", "Full trailer exterior wrap", "$300-$500", "Brand identity; can be phased if budget tight"],
            ["Menu Board & Signage", "Weather-resistant A-frame + mounted board", "$50-$150", "Essential for impulse-purchase visibility"],
        ],
        col_widths=[1.6, 2.2, 1.2, 1.8])

    # ── PHASE 3 ───────────────────────────────────────────────
    add_phase_banner(doc, 3, "REGULATORY COMPLIANCE", "Month 2-4 (Feb-Apr)", ACCENT_HEX)

    add_heading_styled(doc, "2.5 Commissary Kitchen Agreement", level=2)
    add_body_para(doc,
        "This step runs in parallel with trailer procurement. You cannot obtain your LACDPH "
        "health permit without a signed commissary agreement, and you cannot apply for the "
        "farmers market RFP without the health permit. This is the longest dependency chain."
    )

    add_styled_table(doc,
        ["Step", "Action", "Timeline"],
        [
            ["1", "Research commissary options in LA area (parking + wash-down tier preferred, $300-$500/mo)", "Week 1"],
            ["2", "Tour 2-3 facilities; verify they accept trailers, have dump station, potable water fill", "Week 1-2"],
            ["3", "Sign commissary agreement", "Week 2-3"],
            ["4", "Obtain signed 'Verification of Proper Food Vehicle Storage' form from commissary operator", "Week 3"],
            ["5", "Submit form to LACDPH with health permit application", "Week 3-4"],
        ],
        col_widths=[0.5, 4.8, 1.5])

    add_heading_styled(doc, "2.6 LACDPH Health Permit & Plan Check", level=2)
    add_body_para(doc,
        "The Los Angeles County Department of Public Health (LACDPH) plan check is the most "
        "time-consuming regulatory hurdle. The physical trailer must be inspected and approved "
        "before any food can be sold."
    )

    add_styled_table(doc,
        ["Step", "Action", "Fee", "Timeline"],
        [
            ["1", "Submit Plan Check Application with detailed vehicle blueprints, equipment list, menu, water system specs", "$347+", "Submit ASAP after trailer arrives"],
            ["2", "LACDPH reviews plans; may request modifications or additional documentation", "--", "2-6 weeks (highly variable)"],
            ["3", "Schedule physical vehicle inspection at LACDPH facility", "--", "1-2 weeks after plan approval"],
            ["4", "Pass inspection (inspector checks sinks, hot water, enclosure, equipment certs)", "--", "Same day (pass/fail)"],
            ["5", "If fail: correct deficiencies, schedule re-inspection", "$100+ re-check", "1-3 weeks per re-inspection"],
            ["6", "Receive MFF Health Permit (Moderate Risk)", "$598/year", "Issued upon passing inspection"],
        ],
        col_widths=[0.5, 3.6, 1.0, 1.7])

    add_callout_box(doc,
        "COMMON PLAN CHECK FAILURES",
        "The most frequent causes of plan check rejection or inspection failure:\n"
        "- Handwash sink too small (must be at least 9\"W x 9\"L x 5\"D)\n"
        "- Hot water temperature below 100 deg F at handwash or below 120 deg F at warewash\n"
        "- Service window exceeds 216 sq. in. maximum\n"
        "- Missing 16-mesh screens on openings\n"
        "- Equipment lacking NSF/ANSI certification stamps\n"
        "- No mechanical refrigeration (12 cu ft minimum)\n"
        "Build your trailer to spec BEFORE ordering to avoid costly retrofits."
    )

    add_heading_styled(doc, "2.7 Insurance Binding", level=2)
    add_body_para(doc,
        "Both Commercial General Liability (CGL) and Commercial Auto insurance must be bound "
        "and certificates of insurance (COIs) in hand before the market RFP submission."
    )

    add_styled_table(doc,
        ["Policy", "Coverage", "Est. Monthly", "Required By"],
        [
            ["Commercial General Liability", "$1M per occurrence / $2M aggregate (standard market requirement)", "$120/mo", "Market RFP application"],
            ["Commercial Auto", "Trailer + tow vehicle; $500k-$1M combined single limit", "$156-$260/mo", "Market RFP application"],
            ["Product Liability", "Often bundled with CGL; covers foodborne illness claims", "Included in CGL", "Market RFP application"],
            ["Workers' Compensation", "Required only when hiring employees", "$78-$91/mo (when applicable)", "Before first hire"],
        ],
        col_widths=[1.6, 2.8, 1.2, 1.2])

    # ── PHASE 4 ───────────────────────────────────────────────
    add_phase_banner(doc, 4, "MARKET ACCESS & RFP", "Month 3-4 (Mar-Apr)", "2980B9")

    add_heading_styled(doc, "2.8 Santa Monica Vendor License", level=2)
    add_body_para(doc,
        "Before submitting the Farmers Market RFP, you need the Santa Monica municipal "
        "vendor license. This requires your LACDPH health permit to already be in hand."
    )

    add_styled_table(doc,
        ["License/Permit", "Issuing Authority", "Fee", "Prerequisite"],
        [
            ["Business License + Vendor Permit", "City of Santa Monica", "$157-$176/year", "Valid LACDPH health permit"],
            ["Vehicle Vending Tax", "City of Santa Monica (Tax Rate Group IX)", "$50/year", "Business license approved"],
            ["Seller's Permit", "CA CDTFA", "Free", "Must be obtained before any sales"],
        ],
        col_widths=[2.0, 2.0, 1.4, 1.4])

    add_heading_styled(doc, "2.9 Farmers Market RFP Submission", level=2)
    add_body_para(doc,
        "The Santa Monica Farmers Market RFP is the single most critical milestone in the "
        "entire launch sequence. The application window typically opens in March and is "
        "extremely brief. You must be 100% ready before it opens."
    )

    add_styled_table(doc,
        ["RFP Requirement", "Status Needed", "Where to Obtain"],
        [
            ["Completed vendor application form", "Filled and signed", "santamonica.gov/farmers-market"],
            ["Valid LACDPH MFF Health Permit", "Issued and current", "LACDPH Environmental Health"],
            ["Commissary agreement", "Signed and verified", "Your commissary operator"],
            ["Certificate of Insurance (CGL)", "Current, naming City of SM as additional insured", "Your insurance broker"],
            ["Certificate of Insurance (Auto)", "Current", "Your insurance broker"],
            ["Santa Monica Business License", "Active", "City of Santa Monica Finance Dept"],
            ["California Seller's Permit", "Active", "CDTFA online"],
            ["Menu with pricing", "Finalized", "Internal"],
            ["Photos of trailer/setup", "Professional quality", "Internal"],
            ["Business plan summary", "Concise, highlighting sustainability alignment", "Internal"],
        ],
        col_widths=[2.4, 2.0, 2.4])

    add_callout_box(doc,
        "RFP SELECTION CRITERIA",
        "The selection committee evaluates vendors on: (1) Product quality and uniqueness, "
        "(2) Alignment with market sustainability goals, (3) Operational readiness and "
        "compliance documentation, (4) Visual presentation and brand coherence, (5) Diversity "
        "of vendor mix. Your apocalyptic-meets-organic positioning and veteran-owned status are "
        "powerful differentiators. Emphasize USDA Organic ingredients, compostable PLA packaging, "
        "and zero-waste operational practices in your application narrative."
    )

    # ── PHASE 5 ───────────────────────────────────────────────
    add_phase_banner(doc, 5, "SOFT LAUNCH & FIRST MARKET DAY", "Month 4-6 (Apr-Jun)", "1E8449")

    add_heading_styled(doc, "2.10 Pre-Market Operational Readiness", level=2)

    checklist_items = [
        "Trailer fully wrapped in matte-black branding with logo, menu, and pricing visible",
        "All equipment installed, tested, and NSF/UL certification documents filed",
        "Generator tested under full load (all equipment running simultaneously)",
        "Fresh and grey water systems tested; no leaks under pressure",
        "Hot water verified at handwash (100-108 deg F) and warewash (120+ deg F) sinks",
        "Initial inventory procured: organic floss sugar, pure cane syrups, PLA cups, napkins",
        "POS system (Square, Clover, etc.) installed and tested with card reader",
        "Cash float prepared ($100-$150 in small bills and coins)",
        "Route Sheet template created per LACDPH requirements",
        "Commissary routine practiced: water fill, equipment clean, greywater dump",
        "Dry run at commissary: full load-out, drive to market location, timed setup/breakdown",
        "Emergency kit stocked: first aid, fire extinguisher, extra propane, basic tools",
        "Menu board finalized and installed on trailer",
        "Social media accounts created and pre-launch content scheduled",
    ]

    for item in checklist_items:
        add_checklist_item(doc, item)

    add_heading_styled(doc, "2.11 Backup Revenue Plan (If RFP Denied or Delayed)", level=2)
    add_body_para(doc,
        "If the Santa Monica RFP is denied or delayed, the business must pivot immediately "
        "to alternative revenue streams to service the SBA loan and cover monthly OPEX."
    )

    add_styled_table(doc,
        ["Alternative Venue", "Revenue Potential", "Access Method", "Timeline"],
        [
            ["LA-area swap meets (Rose Bowl, etc.)", "$200-$600/day", "Pay per-day stall fee ($50-$150)", "Immediate"],
            ["Private events & parties", "$300-$500/event", "Word of mouth, social media, Thumbtack/GigSalad", "1-2 weeks to first booking"],
            ["Other farmers markets (Venice, Culver City)", "$200-$500/day", "Separate RFP/application per market", "1-3 months"],
            ["Corporate office catering", "$400-$800/event", "Direct outreach, veteran business networks", "2-4 weeks"],
            ["Food truck festivals", "$500-$1,500/day", "Apply via festival organizer websites", "Seasonal; book 2-3 months ahead"],
            ["Street vending (SB 972 compliant areas)", "$100-$300/day", "LACDPH permit already covers this", "Immediate"],
        ],
        col_widths=[2.0, 1.4, 2.0, 1.4])

    # ── MASTER TIMELINE ───────────────────────────────────────
    add_heading_styled(doc, "3. Master Timeline: Week-by-Week", level=1)

    add_styled_table(doc,
        ["Week", "Phase", "Key Milestones"],
        [
            ["1-2", "Entity & Finance", "Register DBA, obtain EIN, open business bank account, contact SBA lender"],
            ["2-4", "Entity & Finance", "Submit SBA loan application, obtain Seller's Permit, begin commissary research"],
            ["4-6", "Asset Procurement", "Loan funded; order concession trailer, source equipment"],
            ["6-8", "Asset Procurement", "Trailer arrives; begin build-out, install equipment, order vinyl wrap"],
            ["8-10", "Regulatory", "Sign commissary agreement, submit LACDPH plan check, bind insurance policies"],
            ["10-12", "Regulatory", "LACDPH plan review period; apply for Santa Monica Business License"],
            ["12-14", "Regulatory", "LACDPH vehicle inspection; obtain MFF Health Permit"],
            ["12-14", "Market Access", "RFP window opens (March) -- submit complete application package"],
            ["14-16", "Market Access", "RFP review period; prepare for soft launch at swap meets/pop-ups"],
            ["16-18", "Launch", "RFP decision received; first farmers market day (if approved)"],
            ["18-20", "Launch", "Optimize operations; refine setup/breakdown routine; build social media"],
            ["20-24", "Ramp-Up", "Establish regular weekend schedule; pursue first private events"],
        ],
        col_widths=[0.8, 1.6, 4.4])

    doc.save("Module_1_Pre_Launch_Timeline.docx")
    print("Module 1 saved: Module_1_Pre_Launch_Timeline.docx")


# ======================================================================
#  MODULE 2 -- REGULATORY & PERMIT COMPLIANCE GUIDE
# ======================================================================
def build_module_2():
    doc = setup_document()
    add_module_cover(doc, 2, "Regulatory &\nPermit Compliance Guide",
        "Every License, Permit, and Inspection Mapped",
        meta_lines=[
            "Los Angeles County + City of Santa Monica Jurisdiction",
            "Mobile Food Facility (MFF) -- Moderate Risk Classification",
            "Fiscal Year 2025-2026 Fee Schedule",
        ])
    add_header_footer(doc, "Module 2 -- Regulatory Compliance")

    # ── OVERVIEW ──────────────────────────────────────────────
    add_heading_styled(doc, "1. Regulatory Landscape Overview", level=1)
    add_body_para(doc,
        "Operating a mobile food facility in Santa Monica requires navigating three overlapping "
        "layers of government jurisdiction: (1) Los Angeles County Department of Public Health "
        "(LACDPH) for health permits and food safety, (2) the City of Santa Monica for business "
        "licensing and vendor permits, and (3) the State of California for tax registration and "
        "food code compliance. Each layer has its own application process, fee schedule, and "
        "renewal cycle. Missing any single permit can shut down the entire operation."
    )

    add_styled_table(doc,
        ["Jurisdiction", "Primary Authority", "What They Control", "Key Document"],
        [
            ["LA County", "Dept. of Public Health (LACDPH)", "Health permits, vehicle inspection, commissary verification, food safety", "MFF Health Permit"],
            ["City of Santa Monica", "Finance Dept. / Farmers Market Office", "Business license, vendor permit, market stall access, packaging ordinance", "Business License + Vendor Permit"],
            ["State of California", "CDTFA / CRFC", "Sales tax collection, Retail Food Code classification", "Seller's Permit"],
            ["Federal", "SBA / IRS", "Loan guarantee, tax ID, veteran certification", "EIN / DD-214"],
        ],
        col_widths=[1.2, 2.0, 2.4, 1.2])

    # ── LAYER 1: LA COUNTY ────────────────────────────────────
    add_heading_styled(doc, "2. Layer 1: Los Angeles County Public Health", level=1)

    add_heading_styled(doc, "2.1 Facility Classification", level=2)
    add_body_para(doc,
        "Under the California Retail Food Code (CRFC), as modified by SB 972, mobile food "
        "operations are classified based on the level of food preparation performed. Because "
        "Armageddon Treats involves active food preparation -- spinning heated sugar into cotton "
        "candy, shaving ice blocks, and dispensing flavored syrups -- the operation triggers "
        "the Moderate Risk Mobile Food Facility (MFF) classification."
    )

    add_styled_table(doc,
        ["Classification", "Description", "Annual Permit Fee", "Applies to Armageddon Treats?"],
        [
            ["CMFO, Low Risk", "Prepackaged non-hazardous foods only", "$126", "No"],
            ["CMFO, Moderate Risk", "Limited food prep (e.g., shaved ice from pushcart)", "$299", "Possibly, if using a pushcart only"],
            ["MFF, Low Risk", "Prepackaged foods from a vehicle", "$325", "No"],
            ["MFF, Moderate Risk", "Active food prep from a vehicle/trailer", "$598", "YES -- primary classification"],
        ],
        col_widths=[1.4, 2.4, 1.4, 1.6])

    add_heading_styled(doc, "2.2 Plan Check Process (Step-by-Step)", level=2)

    add_styled_table(doc,
        ["Step", "Requirement", "Documents Needed", "Fee"],
        [
            ["1", "Obtain Plan Check application from LACDPH Environmental Health Division",
             "None -- download from publichealth.lacounty.gov", "None"],
            ["2", "Prepare detailed vehicle plans",
             "Floor plan with dimensions, equipment layout, plumbing diagram (hot/cold water system, "
             "grey water tank), electrical diagram, ventilation plan, menu", "None"],
            ["3", "Submit Plan Check application with plans and fee",
             "Completed application, vehicle plans, proposed menu, equipment spec sheets with "
             "NSF/ANSI certification documentation", "$347 minimum"],
            ["4", "LACDPH plan review (office review)",
             "Reviewer checks plans against CRFC structural requirements", "2-6 weeks"],
            ["5", "Address any corrections requested by reviewer",
             "Revised plans addressing deficiencies", "May require additional fees"],
            ["6", "Schedule physical vehicle inspection",
             "Fully built-out trailer, all equipment installed", "Included in plan check"],
            ["7", "Pass vehicle inspection",
             "Inspector verifies physical build matches approved plans", "Same day"],
            ["8", "MFF Health Permit issued",
             "Permit valid for one year from date of issue", "$598 (annual renewal)"],
        ],
        col_widths=[0.5, 2.4, 2.8, 1.1])

    add_heading_styled(doc, "2.3 Structural Requirements Checklist", level=2)
    add_body_para(doc,
        "The following specifications are non-negotiable. The trailer must meet every "
        "requirement to pass the LACDPH vehicle inspection."
    )

    specs = [
        ("Handwashing Sink", "Minimum 9\"W x 9\"L x 5\"D; warm water 100-108 deg F; soap and single-use towel dispensers mounted within arm's reach"),
        ("3-Compartment Warewashing Sink", "Each compartment large enough to fully submerge largest utensil; water temperature minimum 120 deg F; two integral metal drainboards"),
        ("Fresh Water Tank", "Adequate capacity for full day of operation (minimum 30 gallons recommended); food-grade materials; pressurized or gravity-fed delivery"),
        ("Grey Water Tank", "Must be at least 15% larger capacity than fresh water tank; clearly labeled; no ground discharge permitted"),
        ("Mechanical Refrigeration", "Minimum 12 cubic feet usable space; maintains 41 deg F or below; thermometer visible without opening"),
        ("Enclosure", "All food preparation areas fully enclosed with solid walls or 16-mesh screens; customer service windows maximum 216 square inches"),
        ("Flooring", "Smooth, nonabsorbent, easily cleanable; coved at wall junctions; no carpet"),
        ("Equipment Certification", "All food-contact equipment ANSI/NSF certified; all electrical appliances UL listed"),
        ("Ventilation", "Adequate for heat and moisture removal; hood system if cooking with grease (not required for cotton candy/shaved ice)"),
        ("Lighting", "Adequate illumination in all food prep and warewashing areas; shatterproof bulb covers"),
        ("Waste Receptacle", "Covered trash container inside unit; adequate size for full day of operation"),
    ]

    for item, detail in specs:
        add_bullet_point(doc, detail, bold_prefix=item)

    add_heading_styled(doc, "2.4 Commissary Requirements", level=2)
    add_body_para(doc,
        "Every mobile food facility must operate from an approved commissary kitchen. This is "
        "not optional -- it is a foundational requirement of the LA County health code. The "
        "commissary is the permanent base of operations where the mobile unit returns daily."
    )

    add_styled_table(doc,
        ["Commissary Function", "Regulatory Requirement", "Frequency"],
        [
            ["Vehicle Storage", "Overnight parking when not in operation", "Daily"],
            ["Potable Water Fill", "Fill fresh water tank from approved source", "Before each market day"],
            ["Greywater Disposal", "Dump into municipal sanitary sewer via approved drain", "After each market day"],
            ["Grease Disposal", "Dispose in approved grease receptacle (if applicable)", "As needed"],
            ["Equipment Cleaning", "Deep clean all food-contact surfaces", "After each market day"],
            ["Food Storage", "Store raw ingredients in temperature-controlled environment", "Daily"],
            ["Vehicle Cleaning", "Floor wash-down using industrial floor drains", "Weekly minimum"],
        ],
        col_widths=[1.6, 3.2, 2.0])

    add_body_para(doc,
        "The signed \"Verification of Proper Food Vehicle Storage\" form from the commissary "
        "operator must be submitted to LACDPH before the health permit is issued. Health "
        "inspectors conduct random audits to verify active commissary use.",
        bold=True
    )

    add_heading_styled(doc, "2.5 Route Sheet Requirement", level=2)
    add_body_para(doc,
        "All MFF operators must maintain a current Route Sheet that documents the vehicle's "
        "daily operating locations, including address, dates, and hours of operation. This "
        "document must be kept in the vehicle at all times and presented to health inspectors "
        "upon request. Failure to maintain an accurate Route Sheet can result in permit "
        "suspension."
    )

    # ── LAYER 2: CITY OF SANTA MONICA ─────────────────────────
    add_heading_styled(doc, "3. Layer 2: City of Santa Monica", level=1)

    add_heading_styled(doc, "3.1 Business License and Vendor Permit", level=2)

    add_styled_table(doc,
        ["License/Fee", "Amount", "Renewal", "Notes"],
        [
            ["Business License Processing", "$82-$100", "Annual", "Base regulatory fee"],
            ["Vendor Permit (regulatory)", "$75-$80", "Annual", "Includes CASp (ADA) compliance fee"],
            ["Vehicle Vending Tax (Group IX)", "$50/vehicle", "Annual", "Per vehicle or vending operation"],
            ["TOTAL ANNUAL MUNICIPAL COST", "$207-$230", "Annual", "Must present valid LACDPH permit to obtain"],
        ],
        col_widths=[2.0, 1.2, 1.0, 2.6])

    add_heading_styled(doc, "3.2 Disposable Food Service Ware Ordinance", level=2)
    add_body_para(doc,
        "Santa Monica enforces one of the most comprehensive packaging ordinances in the "
        "country. Non-compliance results in fines and potential market expulsion."
    )

    add_styled_table(doc,
        ["Material", "Status in Santa Monica", "Armageddon Treats Compliance"],
        [
            ["Expanded Polystyrene (Styrofoam)", "BANNED -- all forms", "Do not purchase; zero tolerance"],
            ["Clear Plastic #6", "BANNED", "Do not purchase"],
            ["Conventional Plastic Cups", "NOT COMPLIANT", "Replace with PLA bioplastic or sugar cane pulp"],
            ["PLA (Polylactic Acid) Bioplastic", "COMPLIANT -- marine-degradable", "Primary serving vessel (flower cups)"],
            ["Sugar Cane Pulp / Bagasse", "COMPLIANT -- compostable", "Alternative for bowls and containers"],
            ["Paper (uncoated, recyclable)", "COMPLIANT", "For cotton candy cones and wrapping"],
            ["Wooden/Bamboo Utensils", "COMPLIANT", "For spoons (shaved ice)"],
        ],
        col_widths=[2.0, 2.0, 2.8])

    add_heading_styled(doc, "3.3 Farmers Market Vendor Rules", level=2)

    rules = [
        ("Attendance", "Maximum 3 excused absences per calendar year. Beyond 3, vendor pays average historical fees regardless of reason for absence."),
        ("Setup/Breakdown", "All vendors must be fully set up by market opening time and may not begin breakdown until official closing time."),
        ("Stall Fees", "Prepared food vendors pay 12-13% of gross daily market sales (variable fee model)."),
        ("Animals", "No live animals permitted within 20 feet of any food storage or preparation area."),
        ("Insurance", "Current Certificate of Insurance (CGL) must name City of Santa Monica as additional insured."),
        ("Signage", "All vendors must display business name, pricing, and applicable health permits visibly."),
        ("Waste", "Vendors are responsible for removing all waste generated during market operations."),
    ]

    for rule, detail in rules:
        add_bullet_point(doc, detail, bold_prefix=rule)

    # ── LAYER 3: STATE ────────────────────────────────────────
    add_heading_styled(doc, "4. Layer 3: State of California", level=1)

    add_heading_styled(doc, "4.1 Sales Tax Collection", level=2)
    add_body_para(doc,
        "California requires all food vendors to collect and remit sales tax on prepared food "
        "sales. In Santa Monica, the combined state + local sales tax rate is approximately "
        "10.25%. As a vendor with annual sales under $100,000, you will file quarterly returns "
        "with the CDTFA. Sales tax collected is NOT your revenue -- it is held in trust for "
        "the state and must be remitted on schedule."
    )

    add_heading_styled(doc, "4.2 California Food Handler Card", level=2)
    add_body_para(doc,
        "Anyone handling food in California must possess a valid California Food Handler Card. "
        "This requires completing an approved food safety course and passing an exam. Cost: "
        "$10-$15 online. Valid for 3 years. The owner and any future employees must each hold "
        "their own card before handling food."
    )

    # ── MASTER PERMIT TRACKER ─────────────────────────────────
    add_heading_styled(doc, "5. Master Permit and License Tracker", level=1)
    add_body_para(doc,
        "Use this table to track the status of every required permit and license. Keep a "
        "physical copy in the trailer at all times."
    )

    add_styled_table(doc,
        ["Permit/License", "Issuing Authority", "Cost", "Renewal", "Status"],
        [
            ["EIN", "IRS", "Free", "Permanent", ""],
            ["DBA Registration", "LA County Clerk", "$26 + publication", "5 years", ""],
            ["Seller's Permit", "CA CDTFA", "Free", "Permanent", ""],
            ["Food Handler Card", "Approved provider", "$10-$15", "3 years", ""],
            ["MFF Health Permit", "LACDPH", "$598/year", "Annual", ""],
            ["Plan Check Fee", "LACDPH", "$347+", "One-time", ""],
            ["Commissary Agreement", "Commissary operator", "$300-$500/mo", "Per contract", ""],
            ["SM Business License", "City of Santa Monica", "$82-$100/year", "Annual", ""],
            ["SM Vendor Permit", "City of Santa Monica", "$75-$80/year", "Annual", ""],
            ["Vehicle Vending Tax", "City of Santa Monica", "$50/year", "Annual", ""],
            ["CGL Insurance", "Insurance broker", "$120/mo", "Annual policy", ""],
            ["Commercial Auto Insurance", "Insurance broker", "$156-$260/mo", "Annual policy", ""],
            ["FM RFP Approval", "SM Farmers Market Office", "N/A (variable stall fees)", "Annual/per RFP cycle", ""],
        ],
        col_widths=[1.6, 1.4, 1.2, 1.1, 1.5])

    add_callout_box(doc,
        "ANNUAL COMPLIANCE CALENDAR",
        "January: Renew SM Business License and Vendor Permit. File prior-year taxes.\n"
        "March: Farmers Market RFP window (if seeking new/additional markets).\n"
        "June/July: LACDPH Health Permit renewal (date depends on original issue).\n"
        "Quarterly: File CDTFA sales tax returns.\n"
        "Monthly: Pay commissary rent, insurance premiums, SBA loan payment.\n"
        "Daily: Maintain Route Sheet in vehicle. Keep all permits physically in trailer."
    )

    doc.save("Module_2_Regulatory_Compliance_Guide.docx")
    print("Module 2 saved: Module_2_Regulatory_Compliance_Guide.docx")


# ======================================================================
#  MODULE 3 -- DAY-TO-DAY OPERATIONS MANUAL
# ======================================================================
def build_module_3():
    doc = setup_document()
    add_module_cover(doc, 3, "Day-to-Day\nOperations Manual",
        "Standard Operating Procedures for Market Days",
        meta_lines=[
            "Commissary Routines, Setup/Breakdown, Food Safety, Equipment Care",
            "Designed for Solo Operator with Scalable Processes",
        ])
    add_header_footer(doc, "Module 3 -- Operations Manual")

    # ── MARKET DAY TIMELINE ───────────────────────────────────
    add_heading_styled(doc, "1. Market Day: Hour-by-Hour Playbook", level=1)
    add_body_para(doc,
        "A typical market day at the Sunday Main Street Market (8:30 AM - 1:30 PM) requires "
        "approximately 8-9 hours of total work when including commissary prep, transport, "
        "setup, service, breakdown, and post-market commissary return. Consistency in this "
        "routine is what separates profitable vendors from burned-out ones."
    )

    add_styled_table(doc,
        ["Time", "Location", "Activity", "Duration"],
        [
            ["5:00 AM", "Commissary", "Arrive at commissary. Fill fresh water tank (30-50 gal). Load inventory from dry storage: organic floss sugar cartons, syrup bottles, PLA cups, napkins, spoons, cash float. Verify generator fuel level.", "30 min"],
            ["5:30 AM", "Commissary", "Conduct pre-trip vehicle check: tire pressure (trailer + tow vehicle), hitch and safety chains, brake lights, turn signals. Connect trailer to tow vehicle. Secure all loose equipment inside trailer.", "15 min"],
            ["5:45 AM", "In Transit", "Drive to market location. Allow extra time for weekend traffic and parking approach. Typical LA drive: 20-45 min depending on commissary location.", "30-45 min"],
            ["6:15 AM", "Market Site", "Arrive at assigned stall location. Unhitch if needed, position trailer, deploy stabilizer jacks. Connect to shore power if available; otherwise start generator.", "15 min"],
            ["6:30 AM", "Market Site", "Set up service area: deploy menu board/A-frame sign, set out tip jar, position POS terminal. Install cotton candy machine, connect ice shaver. Bring refrigeration to temp.", "30 min"],
            ["7:00 AM", "Market Site", "Prep stations: fill syrup dispensers, pre-stage PLA cups in service window area, verify handwash sink has soap and towels. Perform handwash. Test equipment (spin a test cone, shave a test batch).", "30 min"],
            ["7:30 AM", "Market Site", "Final walkthrough: signage visible, trailer exterior clean, waste bin in position, hand sanitizer accessible. Update Route Sheet with today's location.", "15 min"],
            ["8:00 AM", "Market Site", "Market vendors-only early access may begin (varies by market). Prepare for first customers.", "30 min"],
            ["8:30 AM", "Market Site", "MARKET OPENS. Begin service. Focus: speed, consistency, friendly engagement. Spin cotton candy to order (visual spectacle draws crowd). Pre-shave ice batches during lulls.", "5 hours"],
            ["1:30 PM", "Market Site", "MARKET CLOSES. Stop accepting new orders. Serve remaining queue. Begin breakdown immediately: power down equipment, secure all liquids, cap syrup dispensers.", "15 min"],
            ["1:45 PM", "Market Site", "Pack all inventory, collapse signage, secure equipment. Empty waste into market-provided bins or bag for commissary disposal. Wipe down all food-contact surfaces.", "30 min"],
            ["2:15 PM", "Market Site", "Hitch trailer, conduct post-trip check, depart market.", "15 min"],
            ["2:30 PM", "In Transit", "Drive to commissary.", "30-45 min"],
            ["3:00 PM", "Commissary", "Dump greywater into approved drain. Rinse fresh water tank. Deep clean 3-compartment sink (wash/rinse/sanitize). Clean cotton candy spinner drum, ice shaver blades. Mop trailer floor.", "45 min"],
            ["3:45 PM", "Commissary", "Restock dry storage. Reconcile daily sales (POS report + cash count). Log daily revenue, units sold, and inventory usage. Park and secure trailer.", "30 min"],
            ["4:15 PM", "Done", "Depart commissary. Total time: approximately 11 hours.", "--"],
        ],
        col_widths=[0.8, 1.0, 4.2, 0.8])

    # ── FOOD SAFETY ───────────────────────────────────────────
    add_heading_styled(doc, "2. Food Safety Protocols", level=1)

    add_heading_styled(doc, "2.1 Handwashing Requirements", level=2)
    add_body_para(doc,
        "LA County health code requires handwashing at specific intervals. Inspectors will "
        "observe your practices during unannounced visits."
    )

    add_styled_table(doc,
        ["When to Wash Hands", "Method"],
        [
            ["Before starting any food preparation", "Wet hands, apply soap, scrub 20 seconds, rinse under warm running water (100-108 deg F), dry with single-use paper towel"],
            ["After touching face, hair, or body", "Same method"],
            ["After handling money or phone", "Same method"],
            ["After handling waste or cleaning chemicals", "Same method"],
            ["After each break or leaving the food prep area", "Same method"],
            ["When switching between product types", "Same method"],
        ],
        col_widths=[3.0, 3.8])

    add_heading_styled(doc, "2.2 Temperature Control", level=2)

    add_styled_table(doc,
        ["Item", "Storage Temp", "Notes"],
        [
            ["Organic floss sugar (dry)", "Room temp, < 75 deg F ideal", "Store in airtight containers; humidity causes clumping"],
            ["Pure cane syrups (opened)", "Refrigerate after opening, 35-41 deg F", "Unopened shelf-stable; transfer to fridge after breaking seal"],
            ["Ice blocks/cubes", "Frozen, 0 deg F or below", "Procure day-of from ice supplier or commissary freezer"],
            ["PLA cups and packaging", "Room temp, dry storage", "Keep in sealed bags; moisture degrades PLA"],
            ["Finished cotton candy", "Serve immediately", "Cotton candy degrades rapidly in humidity; do not pre-make large batches"],
            ["Finished shaved ice", "Serve immediately", "Ice melts; prepare to order"],
        ],
        col_widths=[2.0, 2.0, 2.8])

    add_heading_styled(doc, "2.3 Ice Handling", level=2)
    add_body_para(doc,
        "Ice used for shaved ice is classified as food under the California Retail Food Code. "
        "It must be sourced from an approved supplier, stored in a clean and sanitized "
        "container, and handled only with clean scoops or tongs -- never bare hands. Ice "
        "storage containers must be off the ground and covered when not in active use."
    )

    # ── INVENTORY MANAGEMENT ──────────────────────────────────
    add_heading_styled(doc, "3. Inventory Management", level=1)

    add_heading_styled(doc, "3.1 Per-Market-Day Load-Out (Base Case: 70 units)", level=2)

    add_styled_table(doc,
        ["Item", "Quantity", "Unit Cost", "Total", "Notes"],
        [
            ["Organic floss sugar (3.25 lb cartons)", "1 carton (yields 50-60 servings)", "$18.73", "$18.73", "Bring 1.5 cartons on peak summer days"],
            ["Pure cane syrups (assorted flavors)", "3-4 bottles (16 oz each)", "$4-$6/bottle", "$16-$24", "Rotate 6-8 flavors; carry 3-4 per day"],
            ["PLA flower cups (12 oz)", "50 cups", "$0.25/cup", "$12.50", "For shaved ice; bring extras"],
            ["Paper cones (cotton candy)", "35 cones", "$0.10/cone", "$3.50", "Pre-rolled or pre-formed"],
            ["Wooden spoons", "50", "$0.03/spoon", "$1.50", "Bamboo or birch; compostable"],
            ["Napkins (recycled/compostable)", "100", "$0.02/napkin", "$2.00", "Overstock -- customers use multiple"],
            ["Ice (block or cubed, 40-60 lbs)", "1-2 bags or blocks", "$3-$5/bag", "$6-$10", "Buy morning-of from ice supplier or commissary"],
            ["Generator fuel (propane or gasoline)", "1-2 gallons", "$4-$6/gallon", "$8-$12", "Depends on runtime; full tank before leaving commissary"],
            ["TOTAL VARIABLE COST PER MARKET DAY", "", "", "$68-$84", "At 70 units sold: COGS ~ $33, remainder is packaging and fuel"],
        ],
        col_widths=[2.2, 1.4, 1.0, 0.8, 1.4])

    add_heading_styled(doc, "3.2 Bulk Purchasing Schedule", level=2)

    add_styled_table(doc,
        ["Item", "Order Frequency", "Supplier Type", "Storage"],
        [
            ["Organic floss sugar", "Bi-weekly (2-4 cartons per order)", "Online specialty (Nature's Flavors, Best Flavors)", "Commissary dry storage, airtight"],
            ["Pure cane syrups", "Monthly (case of 12 bottles)", "Restaurant supply or online", "Commissary; refrigerate after opening"],
            ["PLA cups (1,200-ct case)", "Monthly", "Hawaiian Shaved Ice, Shave Ice Supplies", "Commissary dry storage"],
            ["Paper cones", "Monthly (500-ct pack)", "Popcorn Supply, cotton candy supplier", "Commissary dry storage"],
            ["Wooden spoons", "Monthly (1,000-ct pack)", "Restaurant supply", "Commissary dry storage"],
            ["Napkins", "Monthly (case)", "Restaurant supply / Costco Business", "Commissary dry storage"],
        ],
        col_widths=[1.6, 1.8, 2.0, 1.4])

    # ── EQUIPMENT MAINTENANCE ─────────────────────────────────
    add_heading_styled(doc, "4. Equipment Maintenance Schedule", level=1)

    add_styled_table(doc,
        ["Equipment", "Daily", "Weekly", "Monthly", "Annually"],
        [
            ["Cotton Candy Machine", "Clean spinner head and bowl after each use; wipe exterior", "Deep clean heating element; inspect wiring", "Lubricate motor bearings per manufacturer guide", "Full inspection; replace heating element if degraded"],
            ["Ice Shaver", "Clean blades and chamber after each use; sanitize", "Inspect blade sharpness; tighten mounting bolts", "Sharpen or replace blades", "Full motor inspection"],
            ["Generator", "Check oil level; fuel up", "Clean air filter; inspect spark plug", "Change oil per manufacturer schedule", "Full service; carburetor cleaning"],
            ["Refrigeration Unit", "Verify temp (< 41 deg F); clean exterior", "Clean condenser coils", "Check door seals; verify thermostat accuracy", "Professional service if needed"],
            ["Fresh Water System", "Fill tank; run water to verify flow", "Sanitize tank with food-grade sanitizer", "Inspect hoses and connections for leaks", "Replace hoses and seals"],
            ["Grey Water Tank", "Empty at commissary after each use", "Rinse interior", "Deep clean with approved sanitizer", "Inspect for cracks or leaks"],
            ["Trailer (Exterior)", "Quick wipe of service window area", "Wash exterior", "Inspect vinyl wrap for peeling/damage", "Full detail; touch up wrap"],
            ["Trailer (Interior)", "Sweep/mop floor; wipe all surfaces", "Deep scrub walls and floor", "Inspect caulking and seals", "Re-caulk if needed; pest inspection"],
            ["Tow Vehicle", "Check tire pressure, fluid levels", "Inspect hitch and safety chains", "Rotate tires; check brakes", "Full vehicle service"],
        ],
        col_widths=[1.3, 1.4, 1.4, 1.4, 1.3])

    # ── POS & CASH ────────────────────────────────────────────
    add_heading_styled(doc, "5. Point of Sale & Cash Management", level=1)

    add_heading_styled(doc, "5.1 POS System Selection", level=2)
    add_body_para(doc,
        "A mobile POS system is essential for accepting card payments (which represent 60-70% "
        "of transactions at farmers markets) and tracking sales data. The recommended setup "
        "is a tablet-based POS with a cellular data connection."
    )

    add_styled_table(doc,
        ["System", "Hardware Cost", "Transaction Fee", "Pros", "Cons"],
        [
            ["Square", "Free card reader; $49 for tap/chip reader", "2.6% + $0.10", "No monthly fee; excellent reporting; easy setup", "Higher per-transaction fee"],
            ["Clover Go", "$49 reader", "2.3% + $0.10", "Lower transaction fee; robust features", "$14.95/mo software fee"],
            ["PayPal Zettle", "$29 reader", "2.29% + $0.09", "Lowest fees; integrates with PayPal", "Less robust reporting"],
        ],
        col_widths=[1.2, 1.2, 1.2, 1.8, 1.4])

    add_heading_styled(doc, "5.2 Daily Cash Reconciliation", level=2)

    add_styled_table(doc,
        ["Step", "Procedure"],
        [
            ["1", "Start each day with a standard cash float: $100-$150 in small bills ($1, $5, $10) and $10 in coins (quarters)"],
            ["2", "At end of day: count total cash in drawer"],
            ["3", "Subtract starting float = gross cash sales for the day"],
            ["4", "Compare to POS cash sale total -- must match within $5"],
            ["5", "Record total card sales from POS dashboard"],
            ["6", "Total Revenue = Cash Sales + Card Sales"],
            ["7", "Deposit cash (minus next day's float) to business bank account within 48 hours"],
            ["8", "Log in daily sales tracker: date, location, total units, cash sales, card sales, total revenue"],
        ],
        col_widths=[0.5, 6.3])

    add_heading_styled(doc, "5.3 Sales Tax Collection", level=2)
    add_body_para(doc,
        "California sales tax on prepared food in Santa Monica is approximately 10.25%. Your "
        "POS system should be configured to automatically calculate and add tax. Tax collected "
        "is NOT revenue -- set it aside in a separate mental or physical \"bucket\" and remit "
        "quarterly to the CDTFA. Failure to remit sales tax is a criminal offense in California."
    )

    # ── WEATHER & CONTINGENCY ─────────────────────────────────
    add_heading_styled(doc, "6. Weather & Contingency Protocols", level=1)

    add_styled_table(doc,
        ["Condition", "Impact", "Protocol"],
        [
            ["Rain", "Low foot traffic; cotton candy destroyed by moisture; market may close early", "Check forecast 48 hrs ahead. If >60% rain probability, plan for reduced inventory. Bring tarps and rain guards for service window. Cotton candy production stops in rain -- switch to shaved ice only."],
            ["High Wind (>15 mph)", "Cotton candy impossible; signage at risk", "Anchor all signage. Cotton candy cannot be spun in wind -- switch to shaved ice only. Secure all loose items."],
            ["Extreme Heat (>95 deg F)", "Ice melts faster; increased demand; food safety risk", "Bring 50% more ice. Monitor refrigeration temp more frequently. Increase water intake. Shade the service window area."],
            ["Cool/Overcast", "Lower demand for frozen desserts", "Adjust inventory down 30-40%. Focus on cotton candy (less weather-dependent). Consider warm beverage add-on (future menu expansion)."],
            ["Equipment Failure (day-of)", "Partial or total loss of service capability", "Carry spare fuses, extension cords, basic toolkit. If critical failure (ice shaver motor, generator), sell remaining cotton candy inventory and break down early. Call commissary for tow if needed."],
        ],
        col_widths=[1.2, 1.8, 3.8])

    doc.save("Module_3_Operations_Manual.docx")
    print("Module 3 saved: Module_3_Operations_Manual.docx")


# ======================================================================
#  MODULE 4 -- BRAND IDENTITY & MARKETING PLAYBOOK
# ======================================================================
def build_module_4():
    doc = setup_document()
    add_module_cover(doc, 4, "Brand Identity &\nMarketing Playbook",
        "Zero-Budget Launch Strategy for Maximum Impact",
        meta_lines=[
            "Visual Identity, Social Media, Market Presence, Event Marketing",
            "Leveraging the Apocalyptic-Meets-Organic Brand Dissonance",
        ])
    add_header_footer(doc, "Module 4 -- Marketing Playbook")

    # ── BRAND IDENTITY ────────────────────────────────────────
    add_heading_styled(doc, "1. Brand Identity System", level=1)

    add_heading_styled(doc, "1.1 The Core Concept", level=2)
    add_body_para(doc,
        "Armageddon Treats is built on a single powerful visual contradiction: a menacing, "
        "post-apocalyptic exterior housing bright, innocent, organic desserts. This dissonance "
        "is the brand. Every visual, verbal, and experiential decision must reinforce this "
        "tension. The brand does not apologize for looking aggressive in a farmers market "
        "full of pastel tents -- it leans in. The shock factor IS the marketing."
    )

    add_callout_box(doc,
        "BRAND POSITIONING STATEMENT",
        "Armageddon Treats is a veteran-owned mobile dessert operation serving premium, "
        "USDA Organic cotton candy and shaved ice from a matte-black apocalyptic-themed "
        "concession trailer. We deliver an unforgettable visual experience and a guilt-free "
        "indulgence, proving that the end of the world never tasted so sweet."
    )

    add_heading_styled(doc, "1.2 Visual Identity Guidelines", level=2)

    add_styled_table(doc,
        ["Element", "Specification", "Rationale"],
        [
            ["Primary Color", "Matte Black (#1A1A1A)", "Apocalyptic, industrial, stark contrast to colorful market environment"],
            ["Accent Color", "Hazard Red (#C0392B)", "Danger/warning aesthetic; draws the eye; pairs with black dramatically"],
            ["Secondary Accent", "Military Olive (#556B2F)", "Subtle nod to veteran/military identity; used sparingly"],
            ["Highlight", "Toxic Yellow (#D4A017)", "Caution tape / biohazard motif; used for callouts and pricing"],
            ["Typography (Logo)", "Stencil / military block lettering (e.g., Stencil Std, Army Rust)", "Evokes military surplus, survival gear, industrial signage"],
            ["Typography (Menu)", "Clean sans-serif (Calibri, Helvetica, or similar)", "Legibility at distance; contrast with aggressive logo font"],
            ["Trailer Wrap", "Full matte-black vinyl with red/yellow hazard striping, distressed texture", "The trailer IS the billboard; must be visible from 50+ feet"],
            ["Logo Treatment", "Distressed/stenciled text with biohazard or radiation symbol integration", "Immediately communicates the \"doomsday\" theme without explanation"],
            ["Product Presentation", "Vibrant, oversized cotton candy on dark cones; neon syrups on white ice", "The bright product against the dark trailer is the core visual tension"],
        ],
        col_widths=[1.4, 2.4, 3.0])

    add_heading_styled(doc, "1.3 Trailer Wrap Design Brief", level=2)
    add_body_para(doc,
        "The trailer wrap is the single most important marketing asset. Budget: $300-$500 for "
        "a full matte-black base wrap with vinyl-cut graphics. This is NOT optional or "
        "deferrable -- an unwrapped aluminum trailer is invisible at a farmers market."
    )

    wrap_elements = [
        ("Matte-black base wrap", "Full exterior coverage. Creates the \"canvas\" for all graphics. Use 3M or Avery commercial-grade vinyl (3-5 year outdoor life)."),
        ("Logo (both sides + rear)", "Large-format stencil logo minimum 18\" tall. Visible from across the market. Hazard red on matte black."),
        ("Menu with pricing (service side)", "Clean, legible menu board area painted or vinyl-applied on the service-facing side. 3-4 items max. Large pricing ($5, $6) visible from 10+ feet."),
        ("Hazard striping (bumper/lower panels)", "Yellow/black caution tape stripe along bottom 6\" of trailer. Cheap, high-impact visual."),
        ("'Veteran-Owned' badge", "Small but visible badge/decal on service side. American flag integration optional. Authenticity signal."),
        ("Social media handle", "Instagram handle (@ArmageddonTreats) prominently displayed. Drives organic follows from market visitors."),
    ]
    for title, desc in wrap_elements:
        add_bullet_point(doc, desc, bold_prefix=title)

    # ── SOCIAL MEDIA ──────────────────────────────────────────
    add_heading_styled(doc, "2. Social Media Strategy (Zero Budget)", level=1)

    add_heading_styled(doc, "2.1 Platform Priority", level=2)

    add_styled_table(doc,
        ["Platform", "Priority", "Content Type", "Posting Frequency"],
        [
            ["Instagram", "PRIMARY", "Product photos, behind-the-scenes reels, market day stories, customer reposts", "5-7x/week (stories daily, feed posts 3-4x/week)"],
            ["TikTok", "HIGH", "Cotton candy spinning videos (hypnotic), trailer reveal, market day montages, \"making of\" content", "3-5x/week (short-form video)"],
            ["Google Business Profile", "ESSENTIAL", "Business info, photos, hours, reviews", "Set up once; update seasonally"],
            ["Facebook", "MODERATE", "Event announcements, market schedule, community engagement", "2-3x/week"],
            ["Yelp", "PASSIVE", "Business listing, respond to reviews", "Claim listing; respond to all reviews"],
        ],
        col_widths=[1.2, 1.0, 2.8, 1.8])

    add_heading_styled(doc, "2.2 Content Pillars", level=2)
    add_body_para(doc,
        "All social media content should fall into one of these five pillars, rotated "
        "throughout the week to maintain variety and engagement."
    )

    pillars = [
        ("THE SPIN (Product Content)", "Mesmerizing close-up videos of cotton candy being spun on the machine. Brightly colored sugar against the dark trailer. Slow-motion syrup pours on shaved ice. This is your most shareable content -- the visual contrast is inherently viral."),
        ("DOOMSDAY DISPATCH (Brand Storytelling)", "Apocalyptic-themed captions and humor. \"Surviving the apocalypse one cotton candy at a time.\" \"Your last meal should be this sweet.\" Dark humor that matches the brand without being offensive. Lean into the irony."),
        ("BEHIND THE BUNKER (Behind the Scenes)", "Show the grind: 5 AM commissary prep, trailer setup at dawn, the drive to market. This humanizes the brand and builds the \"veteran entrepreneur\" narrative. People root for underdogs."),
        ("FIELD REPORT (Market Day Content)", "Real-time stories from market days. Customer reactions, long lines, sold-out moments, market ambiance. User-generated content reposts (\"Tag us for a repost!\")."),
        ("MISSION BRIEFING (Announcements)", "Schedule updates, new flavor launches, event bookings, milestones (\"100th customer!\", \"First month complete\"). Community engagement posts."),
    ]
    for pillar, desc in pillars:
        add_bullet_point(doc, desc, bold_prefix=pillar)

    add_heading_styled(doc, "2.3 Pre-Launch Content Calendar", level=2)
    add_body_para(doc,
        "Begin posting 6-8 weeks before your first market day to build anticipation."
    )

    add_styled_table(doc,
        ["Weeks Before Launch", "Content Focus", "Key Posts"],
        [
            ["8-6 weeks", "Tease the concept", "Logo reveal, \"Something is coming\" dark/cryptic posts, trailer purchase reveal (before wrap)"],
            ["6-4 weeks", "Build-out documentation", "Time-lapse of trailer wrap installation, equipment unboxing, branding process, \"Meet the founder\" veteran story"],
            ["4-2 weeks", "Product previews", "First cotton candy spin video, flavor reveals, behind-the-scenes at commissary, countdown posts"],
            ["2-1 weeks", "Final countdown", "Location and date announcement, \"Opening day\" countdown stories, invite followers to come find you"],
            ["Launch week", "Go live", "Day-of stories every 30 min, first customer photo, line footage, \"We're officially open\" post"],
            ["Post-launch", "Sustain momentum", "Daily market stories, customer reposts, weekly flavor spotlights, event booking announcements"],
        ],
        col_widths=[1.4, 1.6, 3.8])

    # ── MARKET PRESENCE ───────────────────────────────────────
    add_heading_styled(doc, "3. Market Presence & Customer Experience", level=1)

    add_heading_styled(doc, "3.1 Stall Layout & Visual Merchandising", level=2)

    add_styled_table(doc,
        ["Element", "Placement", "Purpose"],
        [
            ["A-Frame Sign", "4-6 feet in front of stall (check market rules)", "Catch foot traffic from both directions; large pricing visible"],
            ["Cotton Candy Display", "Spinning machine visible through service window", "The spinning process is a live visual spectacle that draws crowds"],
            ["Syrup/Flavor Display", "Colorful bottles arranged on service counter", "Visual variety signals choice and premium quality"],
            ["Tip Jar", "Prominent placement near POS", "Labeled with brand humor: \"Apocalypse Fund\" or \"Survival Tips\""],
            ["Social Media Card", "Taped to service counter or handed with orders", "\"Follow @ArmageddonTreats for our schedule!\""],
            ["Menu Board", "Mounted on trailer, perpendicular to foot traffic", "Readable from 10+ feet; 3-4 items, large pricing"],
        ],
        col_widths=[1.4, 2.2, 3.2])

    add_heading_styled(doc, "3.2 Customer Engagement Tactics", level=2)

    tactics = [
        ("The Cotton Candy Show", "Spin every cotton candy cone in full view of customers. The spinning process is mesmerizing and creates a natural crowd. People stop to watch, which creates social proof (a crowd attracts more crowd). This is free marketing."),
        ("Photo-Worthy Presentation", "Oversized, colorful cotton candy against the matte-black trailer is inherently Instagram-worthy. Encourage photos. Consider a small \"photo spot\" with the logo visible in frame."),
        ("Flavor Storytelling", "Don't just say \"strawberry\" -- say \"Organic Strawberry Apocalypse\" or \"Radioactive Watermelon.\" Thematic flavor names reinforce the brand and make the experience memorable."),
        ("The Repeat Customer Hook", "\"See you next Sunday!\" Every interaction ends with a reminder of your schedule. If they came once, they'll come back if reminded."),
        ("Kids First, Parents Pay", "Kids drive impulse dessert purchases. Make eye contact with kids, let them watch the cotton candy spin. The parents' wallets follow."),
    ]
    for tactic, desc in tactics:
        add_bullet_point(doc, desc, bold_prefix=tactic)

    # ── PRIVATE EVENTS ────────────────────────────────────────
    add_heading_styled(doc, "4. Private Event & Catering Pipeline", level=1)

    add_heading_styled(doc, "4.1 Event Pricing Framework", level=2)

    add_styled_table(doc,
        ["Event Type", "Suggested Pricing", "Typical Duration", "Expected Revenue"],
        [
            ["Birthday Party (kids)", "$200 flat + $3/guest over 20 guests", "2 hours", "$200-$350"],
            ["Corporate Office Event", "$400-$600 flat for 2-3 hours", "2-3 hours", "$400-$600"],
            ["Wedding/Reception", "$500-$800 (depends on guest count)", "3-4 hours", "$500-$800"],
            ["Festival/Food Event", "Per-unit sales at retail price", "Full day (6-10 hours)", "$500-$1,500"],
            ["School/Community Event", "$250-$400 flat", "2-3 hours", "$250-$400"],
            ["Farmers Market Pop-Up (non-SM)", "Variable stall fee (typically $50-$150/day)", "4-6 hours", "$200-$600 net"],
        ],
        col_widths=[1.6, 2.0, 1.4, 1.8])

    add_heading_styled(doc, "4.2 Booking Channels", level=2)

    add_styled_table(doc,
        ["Channel", "Cost", "Lead Quality", "Setup Effort"],
        [
            ["Word of mouth / market customers", "Free", "High -- already tried your product", "Low -- hand out business cards at market"],
            ["Instagram/Social media DMs", "Free", "High -- self-selected interest", "Moderate -- respond promptly to inquiries"],
            ["Google Business Profile", "Free", "Moderate", "Low -- set up once, maintain reviews"],
            ["Thumbtack / GigSalad", "$5-$15/lead", "Moderate -- price shoppers", "Moderate -- create profile, respond to leads"],
            ["Veteran business networks (VBOC, VetBiz)", "Free", "High -- community support", "Low -- register and network"],
            ["Local Facebook community groups", "Free", "Moderate", "Low -- post availability in relevant groups"],
        ],
        col_widths=[2.0, 1.0, 1.6, 2.2])

    # ── VETERAN MARKETING ─────────────────────────────────────
    add_heading_styled(doc, "5. Leveraging Veteran-Owned Status", level=1)
    add_body_para(doc,
        "Veteran-owned status is a genuine competitive advantage in the Santa Monica market. "
        "It signals discipline, integrity, and service -- qualities that resonate with "
        "consumers. But it must be communicated authentically, not exploitatively."
    )

    add_styled_table(doc,
        ["Action", "Platform/Method", "Expected Impact"],
        [
            ["Display 'Veteran-Owned' on trailer", "Physical decal on service side", "Immediate trust signal; conversation starter"],
            ["Register with NaVOBA (National Veteran-Owned Business Association)", "Online registration", "Access to corporate supplier diversity programs"],
            ["List on VetBiz directory", "sba.gov/veterans", "Visibility to other veteran-supporting businesses"],
            ["Connect with SoCal VBOC", "In-person / virtual", "Mentorship, networking, grant opportunities"],
            ["Share military-to-entrepreneur story on social media", "Instagram / TikTok", "Humanizes the brand; builds emotional connection"],
            ["Apply for DVBE (Disabled Veteran) certification if eligible", "DGS.ca.gov", "15% bid preference on LA County municipal contracts"],
        ],
        col_widths=[2.4, 1.8, 2.6])

    doc.save("Module_4_Marketing_Playbook.docx")
    print("Module 4 saved: Module_4_Marketing_Playbook.docx")


# ======================================================================
#  MODULE 5 -- YEAR 1-2 GROWTH ROADMAP
# ======================================================================
def build_module_5():
    doc = setup_document()
    add_module_cover(doc, 5, "Year 1-2\nGrowth Roadmap",
        "Scaling from First Market Day to Sustainable Operation",
        meta_lines=[
            "Market Expansion, Revenue Diversification, Menu Growth, Hiring",
            "Financial Milestones and Contingency Planning",
        ])
    add_header_footer(doc, "Module 5 -- Growth Roadmap")

    # ── YEAR 1 ROADMAP ────────────────────────────────────────
    add_heading_styled(doc, "1. Year 1: Survive, Learn, Stabilize", level=1)
    add_body_para(doc,
        "Year 1 is not about growth. It is about survival, systems, and proof of concept. "
        "The primary objectives are: (1) establish a consistent market presence, (2) refine "
        "operational efficiency as a solo operator, (3) generate enough revenue to cover OPEX "
        "and loan payments, and (4) build a customer base and social media following."
    )

    add_heading_styled(doc, "1.1 Quarter-by-Quarter Milestones", level=2)

    add_styled_table(doc,
        ["Quarter", "Focus", "Key Milestones", "Revenue Target"],
        [
            ["Q1 (Jan-Mar)", "Setup & Permits", "Entity formed, SBA loan funded, trailer ordered, LACDPH plan check submitted, commissary secured, insurance bound, RFP submitted", "$0 (pre-revenue)"],
            ["Q2 (Apr-Jun)", "Soft Launch", "Health permit obtained, first market day, operational routine established, social media launched, first private event booked", "$4,000-$6,000"],
            ["Q3 (Jul-Sep)", "Peak Season", "Full weekend market schedule, 2 market days/week, peak summer volume, 1-2 private events/month, social media growing", "$8,000-$12,000"],
            ["Q4 (Oct-Dec)", "Seasonal Dip", "Revenue declines with cooler weather, focus on private events and holiday markets, review Year 1 financials, plan Year 2", "$4,000-$6,000"],
        ],
        col_widths=[1.0, 1.2, 3.2, 1.4])

    add_callout_box(doc,
        "YEAR 1 REALITY CHECK",
        "At base-case projections (70 units/day, 2 market days/week after ramp), Year 1 total "
        "revenue is approximately $24,000 with net income after debt service around $1,400. "
        "This is a side-hustle income level, not a full-time salary. The founder must have "
        "other income or savings to support personal living expenses during Year 1. The "
        "business covers its own costs but does not yet pay a salary."
    )

    add_heading_styled(doc, "1.2 Operational Benchmarks", level=2)

    add_styled_table(doc,
        ["Metric", "Month 1-3", "Month 4-6", "Month 7-9", "Month 10-12"],
        [
            ["Market Days / Week", "0 (pre-launch)", "1-2", "2", "2"],
            ["Avg. Units / Day", "--", "40-50 (learning curve)", "60-70", "50-60 (seasonal dip)"],
            ["Private Events / Month", "0", "0-1", "1-2", "1-2"],
            ["Monthly Revenue", "$0", "$1,500-$2,500", "$3,000-$4,500", "$2,000-$3,000"],
            ["Social Media Followers", "0-50", "50-200", "200-500", "500-800"],
            ["Customer Feedback Score", "N/A", "Collecting baseline", "4.5+ stars target", "Maintain 4.5+"],
        ],
        col_widths=[1.6, 1.2, 1.4, 1.4, 1.2])

    # ── YEAR 2 ROADMAP ────────────────────────────────────────
    add_heading_styled(doc, "2. Year 2: Grow, Optimize, Diversify", level=1)
    add_body_para(doc,
        "Year 2 is where the business transitions from survival mode to growth mode. With a "
        "full year of operational data, refined processes, and an established customer base, "
        "the focus shifts to increasing revenue per week, diversifying income streams, and "
        "building toward the business supporting the founder full-time."
    )

    add_heading_styled(doc, "2.1 Market Expansion Strategy", level=2)

    add_styled_table(doc,
        ["Market", "Day", "Application Process", "Estimated Revenue Potential", "Priority"],
        [
            ["Santa Monica Main St (existing)", "Sunday", "Already approved (Year 1)", "$300-$600/day", "ANCHOR"],
            ["Santa Monica Pico Blvd", "Saturday", "Same RFP cycle as Main St", "$200-$400/day", "HIGH"],
            ["Venice Farmers Market", "Friday", "Separate application (Venice Community)", "$150-$350/day", "MEDIUM"],
            ["Beverly Hills Farmers Market", "Sunday", "City of Beverly Hills application", "$250-$500/day", "HIGH (conflicts with SM Sunday)"],
            ["Culver City Farmers Market", "Tuesday", "Culver City Parks & Rec", "$150-$300/day", "MEDIUM"],
            ["Hollywood Farmers Market", "Sunday", "Separate RFP", "$200-$400/day", "LOW (conflicts with SM Sunday)"],
            ["Mar Vista Farmers Market", "Sunday", "Community-organized", "$100-$250/day", "LOW"],
        ],
        col_widths=[1.6, 0.8, 1.8, 1.6, 1.0])

    add_body_para(doc,
        "Target Year 2 schedule: 2.5-3 market days per week. Recommended combination: "
        "Santa Monica Main St (Sunday) + Santa Monica Pico (Saturday) + one weekday market "
        "(Venice Friday or Culver City Tuesday). This avoids schedule conflicts and maximizes "
        "geographic coverage.",
        bold=True
    )

    add_heading_styled(doc, "2.2 Revenue Diversification", level=2)

    add_styled_table(doc,
        ["Revenue Stream", "Year 1 Contribution", "Year 2 Target", "Growth Actions"],
        [
            ["Farmers Market Sales", "~85% of revenue", "~65% of revenue", "Add 1-2 additional markets per week"],
            ["Private Events / Catering", "~15% of revenue", "~25% of revenue", "Active outreach, Thumbtack profile, business cards at every market"],
            ["Food Truck Festivals", "0%", "~5% of revenue", "Apply to 3-4 festivals (Smorgasburg LA, 626 Night Market, etc.)"],
            ["Corporate/Office Catering", "0%", "~5% of revenue", "Leverage veteran networks, LinkedIn outreach"],
        ],
        col_widths=[1.8, 1.4, 1.4, 2.2])

    add_heading_styled(doc, "2.3 Menu Evolution", level=2)
    add_body_para(doc,
        "Menu expansion must be strategic. Adding items that use existing equipment and supply "
        "chains is low-risk. Adding items that require new equipment, new permits, or new "
        "health classifications is high-risk and should be avoided until Year 3+."
    )

    add_styled_table(doc,
        ["Addition", "Equipment Needed", "Risk Level", "Timing", "Revenue Impact"],
        [
            ["Specialty organic flavors (lavender, matcha, chai)", "None -- same machines", "LOW", "Year 1 Q3+", "Premium pricing: +$1-$2/unit"],
            ["Large/XL cotton candy (festival size)", "None -- same machine", "LOW", "Year 1 Q2+", "$8-$10 price point"],
            ["Combination deals (cotton candy + shaved ice)", "None", "LOW", "Year 1 Q2+", "Higher average ticket"],
            ["Toppings bar (mochi, fruit, condensed milk)", "Small cold display", "LOW-MEDIUM", "Year 2 Q1+", "+$1-$3 upsell per unit"],
            ["Seasonal LTOs (pumpkin spice, candy cane, etc.)", "None -- new sugar flavors", "LOW", "Year 1 Q4+", "Creates urgency and social media buzz"],
            ["Beverages (lemonade, agua fresca)", "New dispenser + additional permits review", "MEDIUM", "Year 2 Q2+ (if demand justifies)", "New $4-$5 product line"],
            ["Hot desserts (churros, funnel cake)", "Deep fryer + hood + upgraded MFF classification", "HIGH -- AVOID", "Year 3+ at earliest", "Triggers major permit upgrade"],
        ],
        col_widths=[1.8, 1.4, 1.0, 1.2, 1.4])

    add_callout_box(doc,
        "MENU CREEP WARNING",
        "Do NOT add items that require a fryer, grill, or open flame. These trigger a "
        "High Risk MFF classification, requiring a full commercial hood system, fire "
        "suppression, and a substantially more expensive health permit. The simplicity of "
        "cotton candy and shaved ice (no cooking, no grease, no open flame) is a massive "
        "regulatory advantage. Protect it."
    )

    # ── HIRING ────────────────────────────────────────────────
    add_heading_styled(doc, "3. Scaling the Team", level=1)

    add_heading_styled(doc, "3.1 When to Hire", level=2)
    add_body_para(doc,
        "The trigger for hiring is when solo operation consistently limits revenue. If you are "
        "turning away customers due to long wait times, or if adding a third market day would "
        "generate more revenue than the cost of a helper, it is time to hire."
    )

    add_styled_table(doc,
        ["Indicator", "Threshold", "Action"],
        [
            ["Consistent line of 5+ during peak hours", "Happening every market day", "Hire part-time helper for peak days"],
            ["Revenue per day plateaus despite demand", ">$500/day consistently", "Helper increases throughput 40-60%"],
            ["Adding a 3rd market day is possible", "Year 2+", "Helper covers one day while you cover another"],
            ["Private event requests exceed capacity", ">3/month declined", "Helper enables accepting more bookings"],
        ],
        col_widths=[2.2, 1.6, 3.0])

    add_heading_styled(doc, "3.2 First Hire Profile", level=2)

    add_styled_table(doc,
        ["Attribute", "Requirement"],
        [
            ["Role", "Part-time Market Day Assistant (weekends only initially)"],
            ["Hours", "8-10 hours/week (one full market day)"],
            ["Pay Rate", "$18.42-$20.00/hour (LA minimum + premium for reliability)"],
            ["Burdened Cost", "$22-$24/hour (including payroll taxes, workers' comp)"],
            ["Monthly Cost (2 days/month)", "~$350-$400"],
            ["Monthly Cost (full weekends)", "~$1,400-$1,600"],
            ["Key Skills", "Food handling (must have CA Food Handler Card), friendly, reliable, can follow setup/breakdown routine"],
            ["Legal Requirements", "Workers' Compensation insurance (must bind before first shift), I-9 verification, W-4"],
        ],
        col_widths=[1.6, 5.2])

    # ── FINANCIAL MILESTONES ──────────────────────────────────
    add_heading_styled(doc, "4. Financial Milestones", level=1)

    add_styled_table(doc,
        ["Milestone", "Target", "Significance"],
        [
            ["Break-Even Month", "Month 4-6 (first full market month)", "Revenue covers OPEX + loan payment for the first time"],
            ["Cumulative Net Positive", "Month 9-12", "Total earnings since launch exceed total losses during pre-launch"],
            ["$1,000 Working Capital Reserve", "Month 8-10", "One month of OPEX in reserve; operational safety net"],
            ["SBA Loan Ahead of Schedule", "Year 2 Q2+", "Extra $50-$100/month principal payments accelerate payoff"],
            ["Full-Time Income Threshold", "$4,000-$5,000 net/month", "Business can support founder without external income"],
            ["Second Unit Consideration", "$3,000+ working capital reserve", "Only after Year 2 profitability is proven and repeatable"],
        ],
        col_widths=[2.0, 1.8, 3.0])

    add_heading_styled(doc, "4.1 Reinvestment Priorities", level=2)
    add_body_para(doc,
        "As the business generates profit, reinvestment should follow this priority order. "
        "Do not skip ahead -- each level builds on the previous."
    )

    add_styled_table(doc,
        ["Priority", "Investment", "Cost", "When", "Why"],
        [
            ["1", "Working capital reserve (1 month OPEX)", "$1,500-$2,000", "Year 1", "Survival buffer for slow months, equipment failures, insurance spikes"],
            ["2", "Accelerated SBA loan payoff", "+$50-$100/month extra principal", "Year 1-2", "Eliminate $211/month debt service; free up cash flow permanently"],
            ["3", "Equipment upgrade (better ice shaver)", "$500-$1,000", "Year 2 Q1", "Faster throughput = more units/hour = higher peak revenue"],
            ["4", "Professional trailer detail/re-wrap", "$300-$500", "Year 2 Q1", "Refresh brand appearance after Year 1 wear"],
            ["5", "Part-time labor (peak season help)", "$350-$1,600/month", "Year 2 Q2+", "Unlock 3rd market day or higher throughput on existing days"],
            ["6", "Second trailer or food truck down payment", "$5,000-$10,000", "Year 3+", "Only after Year 2 profitability is proven and loan is paid off"],
        ],
        col_widths=[0.5, 2.0, 1.4, 1.0, 1.9])

    # ── CONTINGENCY ───────────────────────────────────────────
    add_heading_styled(doc, "5. Risk Factors & Contingency Plans", level=1)

    add_styled_table(doc,
        ["Risk", "Probability", "Impact", "Mitigation"],
        [
            ["Santa Monica RFP denied", "Medium (30-40%)", "HIGH -- primary revenue stream blocked for 12 months", "Immediate pivot to swap meets, private events, other farmers markets. Apply to Venice, Culver City, Beverly Hills simultaneously."],
            ["LACDPH plan check fails", "Medium (20-30%)", "MEDIUM -- 2-4 week delay per re-inspection", "Build trailer to exact spec from day one. Get pre-check consultation from LACDPH if offered."],
            ["Equipment failure (critical)", "Low-Medium", "HIGH -- lost market day(s)", "Maintain emergency fund ($500+). Know local equipment repair shops. Carry spare fuses and basic tools."],
            ["Seasonal revenue crash (winter)", "HIGH (certain)", "MEDIUM -- revenue drops 40-50%", "Build cash reserve in summer. Increase private event marketing in Q4. Consider adding warm product (hot chocolate) if feasible."],
            ["Rising insurance/fuel costs", "Medium", "LOW-MEDIUM -- compresses margins", "Shop insurance annually. Optimize commissary location to minimize drive distance."],
            ["Competition enters market", "Medium", "LOW -- high barriers to entry", "Brand differentiation protects market position. Focus on customer experience and loyalty."],
            ["Personal injury/illness", "Low", "HIGH -- solo operator dependency", "Maintain health insurance. Cross-train a reliable friend/family member on basics. Build toward hired help."],
            ["Tow vehicle breakdown", "Medium", "HIGH -- cannot reach market", "Budget for vehicle maintenance. AAA commercial towing membership. Know backup tow options."],
        ],
        col_widths=[1.4, 0.9, 0.8, 3.7])

    # ── LONG-TERM VISION ──────────────────────────────────────
    add_heading_styled(doc, "6. The 3-Year Vision", level=1)
    add_body_para(doc,
        "If execution is disciplined and the market responds favorably, the 3-year trajectory "
        "looks like this:"
    )

    add_styled_table(doc,
        ["Timeframe", "Status", "Revenue (Base Case)", "Key Achievement"],
        [
            ["Month 1-6", "Pre-launch + soft launch", "$0 then ramp to $2,000/mo", "First market day, operational routine established"],
            ["Month 7-12", "Established at 2 markets/week", "$2,500-$4,000/mo", "Consistent revenue, first private events, brand recognition building"],
            ["Month 13-18", "Expanding to 2.5 markets/week", "$3,500-$5,000/mo", "Second market added, event pipeline active"],
            ["Month 19-24", "3 markets/week + events", "$4,500-$6,000/mo", "Part-time help hired, SBA loan payoff accelerating"],
            ["Month 25-30", "Optimized operation", "$5,000-$7,000/mo", "SBA loan approaching payoff, $3k+ working capital reserve"],
            ["Month 31-36", "Mature Year 3", "$5,500-$7,500/mo", "Debt-free, evaluating second unit or food truck upgrade"],
        ],
        col_widths=[1.2, 1.8, 1.6, 2.2])

    add_body_para(doc,
        "Cumulative net profit (base case) over 36 months: approximately $53,000. This is "
        "real money earned by a real business with real constraints -- not a SaaS fantasy "
        "spreadsheet. The path to a second trailer, a food truck, or a brick-and-mortar "
        "location begins here, built on proven unit economics and disciplined execution.",
        bold=True
    )

    doc.save("Module_5_Growth_Roadmap.docx")
    print("Module 5 saved: Module_5_Growth_Roadmap.docx")


# ══════════════════════════════════════════════════════════════
#  MAIN
# ══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("Generating Armageddon Treats operational modules...\n")
    build_module_1()
    build_module_2()
    build_module_3()
    build_module_4()
    build_module_5()
    print("\nAll 5 modules generated successfully.")
