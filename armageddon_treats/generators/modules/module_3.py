"""Module 3 — Day-to-Day Operations Manual."""

from armageddon_treats.styles.doc_styles import *


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

    doc.save("output/Module_3_Operations_Manual.docx")
    print("Module 3 saved: output/Module_3_Operations_Manual.docx")


if __name__ == "__main__":
    build_module_3()
