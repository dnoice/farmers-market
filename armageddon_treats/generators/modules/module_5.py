"""Module 5 — Year 1-2 Growth Roadmap & Scaling Plan."""

from armageddon_treats.styles.doc_styles import *


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
            ["Corporate/Office Catering", "0%", "~5% of revenue", "Leverage veteran networks, LinkedIn outreach, target Silicon Beach tech offices"],
            ["Brewery Partnerships", "0%", "~5% of revenue", "Free or low-fee setup at LA breweries on busy nights; dessert + beer is a natural pairing"],
        ],
        col_widths=[1.8, 1.4, 1.4, 2.2])

    add_callout_box(doc,
        "HIGH-VALUE FESTIVAL TARGETS",
        "626 Night Market (Arcadia): 50,000+ visitors/weekend, vendor fees $500-$1,000, "
        "revenue potential $3,000-$8,000/weekend. Long waitlist -- apply early.\n\n"
        "Smorgasburg LA (ROW DTLA, Sundays): Vendor fees $300-$600/day, revenue potential "
        "$1,500-$4,000/day. Very competitive application.\n\n"
        "Abbot Kinney First Fridays (Venice): Massive foot traffic, street vendor opportunities.\n\n"
        "These are high-effort, high-reward events. Book 2-3 months in advance."
    )

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
            ["Cotton candy flower bouquets (gift item)", "None -- same machine + packaging", "LOW", "Year 1 Q4+", "$15-$25 each; weddings, holidays, gifts"],
            ["Pre-packaged cotton candy bags (retail)", "Sealed bags + labeling", "LOW", "Year 2 Q1+", "$5-$8 each; passive income at market stall"],
            ["Seasonal LTOs (pumpkin spice, candy cane, etc.)", "None -- new sugar flavors", "LOW", "Year 1 Q4+", "Creates urgency and social media buzz"],
            ["Beverages (lemonade, agua fresca)", "New dispenser + additional permits review", "MEDIUM", "Year 2 Q2+ (if demand justifies)", "New $4-$5 product line"],
            ["Hot desserts (churros, funnel cake)", "Deep fryer + hood + upgraded MFF classification", "HIGH -- AVOID", "Year 3+ at earliest", "Triggers major permit upgrade"],
            ["Soft serve / frozen yogurt", "New machine + higher permit tier", "HIGH -- AVOID", "Year 3+ at earliest", "Different equipment and commissary requirements"],
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

    add_callout_box(doc,
        "CALIFORNIA AB5 WARNING: DO NOT USE 1099 CONTRACTORS",
        "Under California's AB5 law, if a worker uses your equipment, works your schedule, "
        "and operates under your direction, they are a W-2 employee -- not an independent "
        "contractor. Misclassifying employees as 1099 contractors carries severe penalties "
        "in California, including back taxes, penalties, and potential lawsuits. Your market "
        "day helpers are employees. Set up proper payroll (Gusto, Square Payroll, or similar) "
        "from day one."
    )

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

    doc.save("output/Module_5_Growth_Roadmap.docx")
    print("Module 5 saved: output/Module_5_Growth_Roadmap.docx")


if __name__ == "__main__":
    build_module_5()
