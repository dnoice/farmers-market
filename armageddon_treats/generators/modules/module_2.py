"""Module 2 — Regulatory & Permit Compliance Guide."""

from armageddon_treats.styles.doc_styles import *


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
        ("Grey Water Tank", "Must be at least 150% the capacity of fresh water tank per California Retail Food Code; clearly labeled; no ground discharge permitted"),
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

    # ── COMMON GOTCHAS ──────────────────────────────────────────
    add_heading_styled(doc, "6. Common Gotchas and Pitfalls", level=1)
    add_body_para(doc,
        "First-time MFF applicants frequently encounter these issues. Each one can add "
        "weeks or months to your timeline if not anticipated."
    )

    add_styled_table(doc,
        ["Gotcha", "Why It Happens", "How to Avoid"],
        [
            ["Plan check correction cycles", "Incomplete or non-compliant drawings are the #1 cause of delay. Each correction cycle adds 2-4 weeks.", "Have an experienced plan check preparer or consultant review your drawings before submission. Pay for one hour of professional review -- it saves months."],
            ["Buying trailer before plan check approval", "If the trailer doesn't match what LACDPH approves, you need expensive modifications.", "Submit plans based on manufacturer specs first. Purchase or customize AFTER plan approval, not before."],
            ["Grey water tank undersized", "California Retail Food Code requires waste water tank at minimum 150% of fresh water tank capacity. Many stock trailers don't meet this.", "Verify tank sizing before purchase. A 30-gallon fresh tank requires a 45-gallon grey water tank minimum."],
            ["Equipment without NSF/ANSI certification", "Cheap equipment from consumer retailers lacks required certification stamps. Inspector will fail you on the spot.", "Only purchase from commercial restaurant supply with NSF stickers on every food-contact surface."],
            ["Residential trailer storage", "Even temporarily parking the trailer at your home between commissary contract and permit issuance triggers violations. Inspectors do drive-bys.", "Secure commissary agreement BEFORE taking delivery of the trailer."],
            ["Insurance endorsement delays", "Markets and commissaries require specific named-insured endorsements on your COIs. Getting endorsements takes extra time.", "Request all endorsements when you first bind the policy, not as an afterthought."],
            ["Service window too large", "Many imported trailers have standard windows exceeding the 216 sq. in. maximum.", "Measure the window opening before purchase. If too large, plan to install a compliant reducer panel."],
            ["Commissary waitlists", "Popular commissaries in LA have waitlists, especially for trailer parking slots.", "Start commissary shopping 2-3 months before you need the signed verification form."],
        ],
        col_widths=[1.6, 2.4, 2.8])

    doc.save("output/Module_2_Regulatory_Compliance_Guide.docx")
    print("Module 2 saved: output/Module_2_Regulatory_Compliance_Guide.docx")


if __name__ == "__main__":
    build_module_2()
