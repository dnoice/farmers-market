"""Module 4 — Brand Identity & Marketing Playbook."""

from armageddon_treats.styles.doc_styles import *


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

    doc.save("output/Module_4_Marketing_Playbook.docx")
    print("Module 4 saved: output/Module_4_Marketing_Playbook.docx")


if __name__ == "__main__":
    build_module_4()
