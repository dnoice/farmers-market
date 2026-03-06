"""Module 1 — Pre-Launch Timeline & Master Checklist."""

from armageddon_treats.styles.doc_styles import *


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

    # ── BACKWARD PLANNING FROM MARCH RFP ─────────────────────
    add_heading_styled(doc, "4. Backward Planning: Working from the March RFP Deadline", level=1)
    add_body_para(doc,
        "The March RFP window is an immovable deadline. Everything must be planned backward "
        "from that date. If you are reading this after the current year's window has closed, "
        "target the following March and use the intervening months for alternative revenue."
    )

    add_callout_box(doc,
        "CRITICAL: THE RFP CLIFF",
        "The Santa Monica Farmers Market RFP opens briefly in March and closes. There is no "
        "late application, no waitlist, and no mid-year entry. If you miss March, you wait "
        "12 months. Your ENTIRE launch timeline must work backward from this single date."
    )

    add_styled_table(doc,
        ["Target Date", "Milestone", "Why This Deadline"],
        [
            ["March (RFP month)", "Submit complete RFP application with ALL documents", "The immovable deadline -- everything else flows backward from here"],
            ["Mid-February", "All permits, insurance COIs, and commissary agreement finalized", "RFP requires proof of ready-to-operate status, not 'in progress'"],
            ["January", "Pass LACDPH vehicle inspection; MFF Health Permit issued", "Permit must be in hand before RFP submission"],
            ["December (prior year)", "Trailer build-out complete; schedule LACDPH inspection", "Inspection scheduling takes 1-3 weeks; allow buffer for re-inspection"],
            ["October-November", "LACDPH plan check approval received", "Plan check review takes 4-12 weeks; corrections add 2-4 weeks each cycle"],
            ["August-September", "Submit plan check to LACDPH; sign commissary agreement", "Need signed storage verification form to submit with plan check"],
            ["July-August", "SBA loan funded; trailer acquired; commissary selected", "Trailer must exist (or have manufacturer specs) for plan check submission"],
            ["May-June", "Business entity formed; Seller's Permit obtained; SBA application submitted", "SBA approval takes 30-90 days from application to funding"],
        ],
        col_widths=[1.4, 2.6, 2.8])

    add_body_para(doc,
        "Total lead time from first action to RFP submission: 8-10 months minimum. "
        "For a first-time applicant, budget a full 10 months. If starting in May/June, "
        "you are targeting the following March RFP window.",
        bold=True, italic=True
    )

    doc.save("output/Module_1_Pre_Launch_Timeline.docx")
    print("Module 1 saved: output/Module_1_Pre_Launch_Timeline.docx")


if __name__ == "__main__":
    build_module_1()
