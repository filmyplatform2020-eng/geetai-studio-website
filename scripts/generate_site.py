#!/usr/bin/env python3
"""Generate 30 tool pages + tool_descriptions.md for GeetAI Studio website."""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TOOLS_DIR = ROOT / "tools"

TOOLS = [
    {
        "slug": "leads",
        "emoji": "🎯",
        "name": "GeetAI Leads",
        "short_desc": "Lead generation platform",
        "cat": "sales",
        "badge": "Sales",
        "product_num": 1,
        "price": "₹1,499",
        "vault": "01_leadgen_prompt_vault.md",
        "headline": "Find, qualify, and reach your ideal prospects — 10× faster",
        "features": [
            "50 prospect discovery & qualification prompts",
            "BANT scoring and lead-tier segmentation",
            "Personalized outreach prep in one flow",
            "Pipeline tracking templates included",
        ],
        "blurb": """Stop guessing who to call next. GeetAI Leads turns scattered prospect research into a repeatable system — discovery prompts that surface the right companies, qualification frameworks that score fit before you dial, and personalization scripts that make cold outreach feel warm. Built for freelancers, agencies, and B2B sellers who need pipeline without hiring an SDR team. Paste into ChatGPT, Claude, or run inside GeetAI Studio for structured outputs you can drop straight into your CRM. From LinkedIn search queries to re-engagement cadences, every prompt produces actionable lists — not generic advice. Whether you're selling services, SaaS, or high-ticket consulting, this vault gives you the research muscle of a full sales ops team in one download.""",
    },
    {
        "slug": "proposals",
        "emoji": "📄",
        "name": "GeetAI Proposals",
        "short_desc": "Proposal generator",
        "cat": "sales",
        "badge": "Sales",
        "product_num": 2,
        "price": "₹1,999",
        "vault": "02_proposal_template_kit.md",
        "headline": "Win more deals with proposals that sell the outcome, not the hours",
        "features": [
            "10 industry-specific proposal templates",
            "Pricing table formats that close",
            "Executive summary & scope frameworks",
            "Copy guidance for every section",
        ],
        "blurb": """A weak proposal kills deals you already earned. GeetAI Proposals gives you ten battle-tested templates — marketing agency, web dev, consulting, coaching, and more — each with section-by-section copy guidance and pricing tables designed to reduce sticker shock and increase yes-rates. No more staring at a blank Google Doc. Fill in the brackets, customize for your client, and send something that looks like it came from a six-figure agency. Every template follows a proven structure: executive summary, scope, timeline, investment, and a clear call to action. Freelancers use these to look enterprise-grade; agencies use them to standardize delivery and onboard junior team members fast. Ship proposals in under an hour that used to take a full day.""",
    },
    {
        "slug": "contracts",
        "emoji": "📋",
        "name": "GeetAI Contracts",
        "short_desc": "Contract generator",
        "cat": "sales",
        "badge": "Legal",
        "product_num": 3,
        "price": "₹1,999",
        "vault": "03_contracts_vault.md",
        "headline": "Protect your work and get paid — without expensive legal bills",
        "features": [
            "10 ready-to-use business agreements",
            "Freelance, retainer & project scopes",
            "Payment terms & IP clauses included",
            "Customization checklist for each type",
        ],
        "blurb": """Handshake deals are how freelancers lose money. GeetAI Contracts packs ten essential agreement templates — service contracts, NDAs, retainer agreements, subcontractor scopes, and more — written in plain language you can actually send to clients. Each template includes notes on what to customize, common pitfalls to avoid, and when to escalate to a lawyer. Stop copying random templates from the internet that miss jurisdiction basics or leave payment terms vague. These are structured for Indian and global freelance/agency work, with clear deliverable definitions, revision limits, and termination clauses. Send professional contracts the same day you close the verbal yes — because momentum matters, and so does getting paid on time.""",
    },
    {
        "slug": "quotations",
        "emoji": "💰",
        "name": "GeetAI Quotations",
        "short_desc": "Quotation builder",
        "cat": "sales",
        "badge": "Sales",
        "product_num": 4,
        "price": "₹1,499",
        "vault": "04_quotation_templates_vault.md",
        "headline": "Quote faster, look sharper, close with confidence",
        "features": [
            "12 industry quotation formats",
            "Pricing psychology guide included",
            "Line-item & package pricing layouts",
            "Validity & terms boilerplate",
        ],
        "blurb": """Speed wins small business sales. GeetAI Quotations gives you twelve polished quote formats — from creative services and IT projects to event planning and manufacturing — plus a pricing psychology guide that helps you present numbers without triggering buyer freeze. Each template is designed for clarity: itemized scope, optional add-ons, payment milestones, and professional branding placeholders. Stop rebuilding quotes from scratch in Excel every time a lead asks for pricing. These layouts help you anchor value before revealing cost, offer good-better-best tiers when appropriate, and include terms that protect you from scope creep. Send quotes in minutes that look like they came from an established firm — because first impressions on price matter as much as the number itself.""",
    },
    {
        "slug": "content",
        "emoji": "✍️",
        "name": "GeetAI Content",
        "short_desc": "Content factory",
        "cat": "content",
        "badge": "Content",
        "product_num": 5,
        "price": "₹1,499",
        "vault": "05_content_idea_vault.md",
        "headline": "Never run out of content ideas again",
        "features": [
            "200 content ideas across niches",
            "20 ready-to-expand outlines",
            "Pillar content & repurposing maps",
            "Platform-specific angle prompts",
        ],
        "blurb": """Content consistency dies when ideation is hard. GeetAI Content ships 200 proven content ideas and 20 full outlines you can expand into blogs, newsletters, videos, or social threads — organized by funnel stage and audience intent. Built for creators, marketers, and agency content teams who need a calendar that fills itself. Each idea includes angle hooks, suggested formats, and repurposing paths so one concept becomes five assets. Stop posting randomly and hoping something lands. Use these prompts to batch-plan a month of content in a single sitting, align topics with business goals, and eliminate the Sunday-night panic of "what do I post tomorrow?" This is your content strategy shortcut — not generic "post consistently" advice.""",
    },
    {
        "slug": "seo",
        "emoji": "🔍",
        "name": "GeetAI SEO",
        "short_desc": "SEO generator",
        "cat": "content",
        "badge": "SEO",
        "product_num": 6,
        "price": "₹1,999",
        "vault": "06_seo_toolkit_vault.md",
        "headline": "Rank higher without hiring an SEO agency",
        "features": [
            "Full site audit checklist",
            "Keyword research framework",
            "50 title & meta description templates",
            "On-page optimization prompts",
        ],
        "blurb": """SEO doesn't have to be a black box. GeetAI SEO bundles a step-by-step audit checklist, keyword research framework, and fifty title/meta templates you can run on any site — yours or a client's. Designed for freelancers offering SEO as a service and business owners who want organic traffic without ₹50K/month retainers. Each prompt produces structured outputs: prioritized fix lists, keyword clusters with intent labels, and SERP-ready metadata you can paste into WordPress, Shopify, or Webflow. Stop guessing what to optimize first. This toolkit tells you exactly what to check, what to write, and how to measure progress — turning SEO from a vague monthly report into concrete actions that move rankings.""",
    },
    {
        "slug": "blog",
        "emoji": "📝",
        "name": "GeetAI Blog",
        "short_desc": "Blog generator",
        "cat": "content",
        "badge": "Content",
        "product_num": 7,
        "price": "₹1,999",
        "vault": "07_blog_content_vault.md",
        "headline": "Publish authority-building articles that actually get read",
        "features": [
            "30 article frameworks by content type",
            "Headline bank with 100+ formulas",
            "SEO structure built into every outline",
            "Intro, body & CTA section guides",
        ],
        "blurb": """Long-form content builds trust — if it's structured right. GeetAI Blog gives you thirty article frameworks covering how-tos, listicles, case studies, comparisons, and thought leadership pieces, plus a headline bank that stops you from publishing boring titles. Every framework includes SEO-friendly section structure, hook formulas for the first paragraph, and CTA placement guidance. Agencies use this to deliver client blogs at scale; founders use it to establish expertise without hiring a content team. Paste your topic, follow the outline, and produce 1,500-word articles that read human — not like AI filler. From keyword placement to internal linking prompts, this vault handles the architecture so you focus on insights.""",
    },
    {
        "slug": "social",
        "emoji": "📱",
        "name": "GeetAI Social",
        "short_desc": "Social media generator",
        "cat": "content",
        "badge": "Social",
        "product_num": 8,
        "price": "₹999",
        "vault": "08_social_caption_vault.md",
        "headline": "300 captions. Six platforms. Zero writer's block.",
        "features": [
            "300 ready-to-customize captions",
            "Instagram, LinkedIn, X, Facebook & more",
            "Hooks, CTAs & hashtag guidance",
            "Batch posting calendar prompts",
        ],
        "blurb": """Social media rewards consistency, but captions drain creative energy fast. GeetAI Social packs 300 captions across six platforms — promotional, educational, storytelling, engagement-bait, and community-building — each with customization brackets for your brand voice. Stop recycling the same three posts or paying ₹500 per caption to a freelancer. These templates are built for batching: customize ten at once, schedule the week, and move on to revenue work. Includes platform-specific length guidance, CTA variations, and hashtag strategy notes. Whether you're a solo creator or an agency managing twelve client accounts, this vault is the fastest path from blank screen to published post — without sounding like every other brand online.""",
    },
    {
        "slug": "emails",
        "emoji": "📧",
        "name": "GeetAI Emails",
        "short_desc": "Email writer",
        "cat": "content",
        "badge": "Email",
        "product_num": 10,
        "price": "₹1,499",
        "vault": "10_business_email_vault.md",
        "headline": "Every business email you'll ever need — pre-written",
        "features": [
            "80 templates for every scenario",
            "Sales, support, HR & ops coverage",
            "Tone variants: formal, friendly, direct",
            "Follow-up sequences included",
        ],
        "blurb": """Email is still where business gets done — and where most people waste hours rewriting the same messages. GeetAI Emails includes eighty templates covering sales follow-ups, client onboarding, payment reminders, partnership outreach, internal updates, and difficult conversations. Each template offers tone variants so you sound like yourself, not a robot. Freelancers save thirty minutes per client email; ops teams standardize communication quality across the org. No more drafting from scratch when a lead goes cold, a project stalls, or you need to say no professionally. Copy, customize three lines, send — and move on. This is the communication layer your business has been missing.""",
    },
    {
        "slug": "outreach",
        "emoji": "🚀",
        "name": "GeetAI Outreach",
        "short_desc": "Cold outreach system",
        "cat": "sales",
        "badge": "Outreach",
        "product_num": 9,
        "price": "₹1,999",
        "vault": "09_cold_email_swipe_file.md",
        "headline": "Cold email that gets replies — not spam folder tickets",
        "features": [
            "25 proven cold email templates",
            "Subject line bank with 50+ options",
            "Multi-touch follow-up sequences",
            "Personalization frameworks per niche",
        ],
        "blurb": """Cold outreach fails when templates sound cold. GeetAI Outreach gives you twenty-five email sequences that balance personalization at scale with clear value propositions — plus a subject line bank tested across B2B niches. Built for agencies prospecting local businesses, SaaS founders doing founder-led sales, and freelancers filling their pipeline between projects. Each template includes the psychology behind why it works, when to use it, and how to adapt for your offer. Follow-up sequences are included because most deals close on touch three, not touch one. Stop A/B testing from zero. Start with templates that respect the reader's time and make replying easier than ignoring.""",
    },
    {
        "slug": "crm",
        "emoji": "🤝",
        "name": "GeetAI CRM",
        "short_desc": "CRM assistant",
        "cat": "operations",
        "badge": "CRM",
        "product_num": 11,
        "price": "₹1,999",
        "vault": "11_crm_playbook_vault.md",
        "headline": "Turn leads into loyal customers with a CRM system that actually gets used",
        "features": [
            "Full customer lifecycle scripts",
            "Pipeline stage templates",
            "Re-engagement & win-back sequences",
            "Referral request frameworks",
        ],
        "blurb": """Most CRMs fail because nobody knows what to say at each stage. GeetAI CRM is a playbook — not software — with scripts for every moment in the customer lifecycle: first contact, discovery, proposal, negotiation, onboarding, check-ins, upsells, and win-backs. Designed for solo operators and small teams who can't afford Salesforce consultants but still lose deals to poor follow-up. Pipeline templates show you exactly what belongs in each stage, when to move deals forward, and how to re-engage cold leads without being annoying. Pair this with GeetAI Leads and Outreach for a complete revenue system. Your CRM should drive action, not collect dust — these scripts make sure every contact gets the right message at the right time.""",
    },
    {
        "slug": "support",
        "emoji": "💬",
        "name": "GeetAI Support",
        "short_desc": "Customer support AI",
        "cat": "operations",
        "badge": "Support",
        "product_num": 12,
        "price": "₹1,499",
        "vault": "12_support_reply_vault.md",
        "headline": "Reply to every customer in minutes — with empathy and consistency",
        "features": [
            "90 support reply templates",
            "Escalation & refund scenarios covered",
            "Tone guides for angry vs confused customers",
            "Macros for chat, email & social DMs",
        ],
        "blurb": """Bad support replies cost you more than one customer — they cost reputation. GeetAI Support includes ninety response templates for refunds, shipping delays, billing disputes, feature requests, angry complaints, and positive feedback — each with tone guidance so your team sounds human under pressure. E-commerce brands, SaaS startups, and service businesses use these to cut response time from hours to minutes without sacrificing quality. Templates work across email, live chat, WhatsApp, and social DMs. Train new support hires in a day instead of a month. When every reply follows a proven empathy-first structure, CSAT scores climb and chargebacks drop. Support shouldn't be improvised — systematize it.""",
    },
    {
        "slug": "whatsapp",
        "emoji": "📲",
        "name": "GeetAI WhatsApp",
        "short_desc": "WhatsApp assistant",
        "cat": "operations",
        "badge": "Messaging",
        "product_num": 29,
        "price": "₹1,499",
        "vault": "29_whatsapp_dm_vault.md",
        "headline": "WhatsApp scripts that convert — built for how India actually sells",
        "features": [
            "70 scripts for every customer stage",
            "Order, payment & follow-up messages",
            "Broadcast & catalog sale templates",
            "Compliance-friendly opt-in language",
        ],
        "blurb": """In India, WhatsApp is the sales floor. GeetAI WhatsApp gives you seventy ready scripts for inquiry responses, order confirmations, payment reminders, delivery updates, review requests, and re-engagement — written for how customers actually buy on mobile. Local businesses, D2C brands, coaches, and freelancers use these to respond instantly without typing the same message fifty times a day. Includes broadcast templates, catalog promotion messages, and polite opt-in language that keeps you compliant. Stop losing sales because you replied three hours late with a typo-filled message. Copy, personalize one line, send — and watch response rates climb on the channel where your customers already live.""",
    },
    {
        "slug": "recruit",
        "emoji": "👥",
        "name": "GeetAI Recruit",
        "short_desc": "Recruitment system",
        "cat": "hr",
        "badge": "HR",
        "product_num": 14,
        "price": "₹1,999",
        "vault": "14_recruitment_vault.md",
        "headline": "Hire faster with job posts and screening that filter the noise",
        "features": [
            "15 job description templates by role",
            "100 screening questions with rubrics",
            "Candidate outreach scripts",
            "Interview scorecard frameworks",
        ],
        "blurb": """Bad hires are expensive. Vague job posts attract bad candidates. GeetAI Recruit fixes both with fifteen JD templates for common roles, a hundred screening questions organized by competency, and outreach scripts that get qualified people on calls. Built for startups hiring their first team, HR consultants serving SMB clients, and agencies scaling delivery capacity. Each job description includes must-have vs nice-to-have framing, culture signals, and salary transparency guidance. Screening questions come with scoring rubrics so different interviewers evaluate consistently. Go from "we need to hire someone" to a structured pipeline in an afternoon — without paying a recruiter ₹2L per placement.""",
    },
    {
        "slug": "resume",
        "emoji": "📑",
        "name": "GeetAI Resume",
        "short_desc": "Resume & career builder",
        "cat": "hr",
        "badge": "HR",
        "product_num": 16,
        "price": "₹1,499",
        "vault": "16_resume_career_vault.md",
        "headline": "Land interviews with resumes that pass ATS and impress humans",
        "features": [
            "Achievement bullet formulas (CAR method)",
            "Cover letter templates by situation",
            "LinkedIn headline & summary optimization",
            "Career pivot & gap explanation scripts",
        ],
        "blurb": """Your resume has six seconds to survive. GeetAI Resume gives you bullet formulas that turn job duties into measurable achievements, cover letters for career pivots and employment gaps, and LinkedIn optimization prompts that get recruiter views. Job seekers, career coaches, and HR consultants use this vault to produce application materials that pass ATS filters and still read human on the other side. Includes industry-specific achievement examples, keyword placement guidance, and follow-up email templates for after you apply. Stop paying ₹5,000 per resume rewrite. Learn the frameworks once, customize for every application, and stack interviews instead of rejection emails.""",
    },
    {
        "slug": "course",
        "emoji": "🎓",
        "name": "GeetAI Course",
        "short_desc": "Course generator",
        "cat": "content",
        "badge": "EdTech",
        "product_num": 17,
        "price": "₹1,999",
        "vault": "17_course_creation_vault.md",
        "headline": "Build and launch a course — from curriculum to sales emails",
        "features": [
            "Curriculum architecture frameworks",
            "Lesson script templates",
            "Launch email sequence (5 emails)",
            "Pricing & module packaging guides",
        ],
        "blurb": """Course creators fail at structure, not expertise. GeetAI Course provides curriculum frameworks that sequence learning properly, lesson scripts that keep students engaged, and a five-email launch sequence that converts your list into enrollments. Coaches, consultants, and subject-matter experts use this to go from "I should teach this" to a sellable product without hiring instructional designers. Includes module packaging guidance, pricing tier recommendations, and worksheet/exercise prompts for each lesson type. Whether you're launching on Teachable, Gumroad, or your own site, this vault handles the architecture so you focus on delivering transformation — not staring at an empty syllabus doc for weeks.""",
    },
    {
        "slug": "local",
        "emoji": "🏪",
        "name": "GeetAI Local",
        "short_desc": "Local business AI",
        "cat": "operations",
        "badge": "Local",
        "product_num": 19,
        "price": "₹1,499",
        "vault": "19_local_business_vault.md",
        "headline": "Get found locally — Google, maps, and community outreach",
        "features": [
            "Google Business Profile optimization",
            "Local SEO checklist & citation guide",
            "Community outreach email templates",
            "Review generation scripts",
        ],
        "blurb": """Local businesses win on visibility, not viral content. GeetAI Local covers Google Business Profile optimization, local SEO checklists, community partnership outreach, and review generation scripts — everything a clinic, restaurant, salon, or service business needs to dominate their neighborhood search results. Agencies selling to local SMBs use this as a productized audit deliverable; owners use it to stop depending entirely on word-of-mouth. Templates include seasonal promotion ideas, local event tie-ins, and citation building workflows. When someone searches "best [service] near me," these frameworks help you show up — and convert searchers into walk-ins and bookings.""",
    },
    {
        "slug": "real-estate",
        "emoji": "🏠",
        "name": "GeetAI Real Estate",
        "short_desc": "Real estate AI",
        "cat": "operations",
        "badge": "Real Estate",
        "product_num": 20,
        "price": "₹1,999",
        "vault": "20_real_estate_vault.md",
        "headline": "Listings that sell properties and scripts that nurture buyers",
        "features": [
            "Property description formulas",
            "Buyer & seller outreach scripts",
            "Follow-up cadences for long sales cycles",
            "Open house & showing promotion templates",
        ],
        "blurb": """Real estate is a copy and follow-up game. GeetAI Real Estate delivers property description formulas that highlight features buyers care about, buyer/seller outreach scripts for every stage of the transaction, and follow-up cadences for deals that take months to close. Agents, brokers, and property marketers use these templates to list faster, nurture leads without being pushy, and stay top-of-mind through long decision cycles. Includes open house promotion templates, investor-focused listing angles, and re-engagement messages for cold leads who went quiet. Stop writing the same listing from scratch. Systematize the language that moves properties and builds referral engines.""",
    },
    {
        "slug": "automation",
        "emoji": "⚡",
        "name": "GeetAI Automation",
        "short_desc": "Workflow builder",
        "cat": "operations",
        "badge": "Automation",
        "product_num": 22,
        "price": "₹4,999",
        "vault": "22_automation_blueprint_pack.md",
        "headline": "Ten workflow blueprints that run your business on autopilot",
        "features": [
            "10 documented n8n/Make-ready blueprints",
            "Lead capture → CRM → follow-up flows",
            "Content publishing automation",
            "Client onboarding sequences",
        ],
        "blurb": """Manual work doesn't scale — but bad automation creates chaos. GeetAI Automation ships ten fully documented workflow blueprints ready for n8n, Make, or Zapier: lead capture to CRM, invoice reminders, content publishing pipelines, client onboarding sequences, and support ticket routing. Each blueprint includes trigger logic, node-by-node setup notes, error handling guidance, and estimated time saved per month. Agencies sell these as ₹25K+ setup projects; founders use them to reclaim forty hours monthly. This isn't vague "you should automate" advice — it's copy-paste architecture with the decision points already made. Build once, run forever, and stop being the bottleneck in your own business.""",
    },
    {
        "slug": "marketplace",
        "emoji": "🛍️",
        "name": "GeetAI Marketplace",
        "short_desc": "Automation marketplace",
        "cat": "operations",
        "badge": "Store",
        "product_num": 23,
        "price": "₹1,499",
        "vault": "23_marketplace_profile_vault.md",
        "headline": "Win on Fiverr, Upwork, and every gig platform",
        "features": [
            "Profile optimization frameworks",
            "Gig description templates by category",
            "Pricing tier structures that convert",
            "Proposal response scripts for platforms",
        ],
        "blurb": """Marketplace success is positioning, not just skill. GeetAI Marketplace gives you profile optimization checklists, gig description templates, pricing tier structures, and proposal response scripts tuned for Fiverr, Upwork, and similar platforms. Freelancers use this to 3× profile views and raise rates without changing their actual deliverables. Includes niche positioning prompts, portfolio presentation guidance, and review request templates that build social proof fast. Stop underpricing because your profile looks amateur. These frameworks help you present outcomes, package services into clear tiers, and respond to inbound leads with pitches that win against cheaper competitors.""",
    },
    {
        "slug": "brand",
        "emoji": "✨",
        "name": "GeetAI Brand",
        "short_desc": "Personal brand system",
        "cat": "agency",
        "badge": "Branding",
        "product_num": 24,
        "price": "₹1,999",
        "vault": "24_brand_identity_vault.md",
        "headline": "Define a brand voice that people remember and trust",
        "features": [
            "Brand voice framework worksheets",
            "Tagline bank with 100+ options",
            "Positioning statement templates",
            "Messaging hierarchy for all channels",
        ],
        "blurb": """Brands that sound like everyone else get ignored. GeetAI Brand provides voice frameworks, positioning templates, and a tagline bank that helps you articulate who you serve, what you stand for, and why you're different — in language that works across website, social, and sales. Founders, creators, and agencies use this before any design work to ensure visual identity matches verbal identity. Includes competitor differentiation prompts, audience persona tie-ins, and messaging hierarchies for consistent communication. Stop rewriting your About page every quarter. Lock in a brand foundation once, then let every piece of content reinforce the same clear promise.""",
    },
    {
        "slug": "agencyos",
        "emoji": "🏢",
        "name": "GeetAI AgencyOS",
        "short_desc": "Agency operating system",
        "cat": "agency",
        "badge": "Agency",
        "product_num": 25,
        "price": "₹4,999",
        "vault": "25_agencyos_vault.md",
        "headline": "Run a one-person AI agency — or scale to ten",
        "features": [
            "10 productized service packages with pricing",
            "Client acquisition playbook",
            "Delivery & fulfillment systems",
            "Solo-to-team scaling roadmap",
        ],
        "blurb": """The flagship playbook for building an AI-powered agency. GeetAI AgencyOS ties every vault together into ten sellable service packages — content retainers, lead gen systems, reputation management, ad campaigns — with pricing, positioning, and delivery workflows for each. Learn how to acquire your first ten clients, productize services so you're not trading hours for rupees, and scale from solo operator to small team without chaos. This isn't theory — it's the operating system for running a modern agency where AI handles delivery and you handle relationships and growth. If you own the other GeetAI vaults, AgencyOS shows you exactly how to turn templates into ₹50K–₹2L monthly retainers.""",
    },
    {
        "slug": "reels",
        "emoji": "🎬",
        "name": "GeetAI Reels Script",
        "short_desc": "Viral short-video scripts",
        "cat": "content",
        "badge": "Video",
        "product_num": 26,
        "price": "₹1,499",
        "vault": "26_reels_script_vault.md",
        "headline": "Scripts that stop the scroll — ready to shoot today",
        "features": [
            "50 scene-by-scene video scripts",
            "20 proven hook formulas",
            "On-screen text & caption pairs",
            "Hashtag strategy per niche",
        ],
        "blurb": """Short video is the highest-ROI content format — if your hook works in three seconds. GeetAI Reels Script includes fifty ready-to-shoot scripts with timestamped scene breakdowns, on-screen text cues, captions, and hashtag sets. Plus twenty hook formulas you can apply to any topic. Creators, brands, and agencies batch a month of Reels in one afternoon instead of improvising on camera. Each script follows retention mechanics: pattern interrupt openers, curiosity gaps, payoff delivery, and CTAs that drive follows or sales. Swap in your niche, shoot in CapCut, publish — no writer's block, no algorithm anxiety. This is the script vault behind accounts that grow while you're still planning content.""",
    },
    {
        "slug": "adcopy",
        "emoji": "📢",
        "name": "GeetAI AdCopy",
        "short_desc": "High-converting ad copy",
        "cat": "sales",
        "badge": "Ads",
        "product_num": 27,
        "price": "₹1,999",
        "vault": "27_adcopy_vault.md",
        "headline": "Meta and Google ads that convert — not just impress",
        "features": [
            "100 ad templates (Meta + Google)",
            "Headline & primary text variations",
            "Audience-specific angle prompts",
            "A/B testing framework included",
        ],
        "blurb": """Ad spend without copy testing is burning money. GeetAI AdCopy delivers a hundred high-converting templates for Meta and Google — headlines, primary text, descriptions, and CTA variations organized by funnel stage and audience awareness level. Media buyers, D2C founders, and agencies use these to launch campaigns fast and iterate with structure instead of guesswork. Includes angle prompts for problem-aware vs solution-aware audiences, urgency frameworks that don't feel scammy, and A/B testing guidance so you know what to split-test first. Stop paying agencies ₹30K/month for copy you could generate in an hour. Start with proven frameworks, customize for your offer, and let data pick winners.""",
    },
    {
        "slug": "reputation",
        "emoji": "⭐",
        "name": "GeetAI Reputation",
        "short_desc": "Review & reputation manager",
        "cat": "operations",
        "badge": "Reputation",
        "product_num": 28,
        "price": "₹1,499",
        "vault": "28_reputation_vault.md",
        "headline": "Turn reviews into revenue — respond like a pro every time",
        "features": [
            "80 review response templates",
            "Review request scripts (email & SMS)",
            "Negative review de-escalation guides",
            "Reputation monitoring checklist",
        ],
        "blurb": """Your Google rating is your storefront. GeetAI Reputation includes eighty response templates for five-star thank-yous, three-star recoveries, and one-star fire drills — plus review request scripts that actually get customers to click. Local businesses, e-commerce brands, and SaaS companies use this to protect and improve their public perception without hiring a PR firm. Templates handle the emotional intelligence of public replies: acknowledging frustration, offering resolution paths, and turning critics into advocates when possible. Includes monitoring checklists and escalation workflows for reviews that need human intervention. Reputation management isn't optional anymore — systematize it.""",
    },
    {
        "slug": "voice",
        "emoji": "🎙️",
        "name": "GeetAI VoiceScript",
        "short_desc": "Podcast & voiceover scripts",
        "cat": "content",
        "badge": "Audio",
        "product_num": 30,
        "price": "₹1,499",
        "vault": "30_voice_script_vault.md",
        "headline": "Podcast episodes and voiceovers — scripted, structured, ready to record",
        "features": [
            "30 episode frameworks by format",
            "Voiceover scripts for ads & explainers",
            "Intro/outro bank with 20 options",
            "Interview question guides",
        ],
        "blurb": """Audio content builds deeper trust than text — but rambling kills retention. GeetAI VoiceScript provides thirty episode frameworks for solo shows, interviews, and narrative formats, plus voiceover scripts for ads, explainers, and course modules. Podcasters, YouTubers doing voice-over, and agencies producing client audio use these to record confidently without endless retakes. Includes intro/outro banks, transition phrases, sponsor read templates, and CTA placements timed for listener attention curves. Stop publishing episodes that lose people at minute four. Structure your audio content like professionals do — with hooks, segments, and payoffs that keep audiences listening to the end.""",
    },
    {
        "slug": "freelance-pitch",
        "emoji": "💼",
        "name": "GeetAI Freelance Pitch",
        "short_desc": "Winning pitch generator",
        "cat": "sales",
        "badge": "Freelance",
        "product_num": 31,
        "price": "₹1,499",
        "vault": "31_freelance_pitch_vault.md",
        "headline": "Win Upwork, Fiverr, and direct clients with pitches that stand out",
        "features": [
            "50 winning pitch templates",
            "Cover letters by project type",
            "Rate negotiation scripts",
            "Portfolio presentation frameworks",
        ],
        "blurb": """Freelancing is a pitching game — and generic proposals lose to specialized ones every time. GeetAI Freelance Pitch includes fifty templates for Upwork, Fiverr, direct outreach, and referral introductions, organized by project type: design, dev, writing, marketing, consulting. Each pitch follows a structure that proves you read the brief, demonstrates relevant experience, and proposes a clear next step — without underselling yourself. Includes rate negotiation scripts, scope clarification messages, and follow-up templates for when clients go silent. New freelancers land first clients faster; experienced ones raise rates by positioning outcomes instead of hours. Your next ₹1L project starts with the pitch — make it count.""",
    },
    {
        "slug": "listing",
        "emoji": "🛒",
        "name": "GeetAI Listing",
        "short_desc": "E-commerce listing optimizer",
        "cat": "sales",
        "badge": "E-com",
        "product_num": 32,
        "price": "₹1,499",
        "vault": "32_ecommerce_listing_vault.md",
        "headline": "Product listings that rank on Amazon, Flipkart, and Shopify",
        "features": [
            "Description formulas by category",
            "60 title & bullet point templates",
            "Keyword placement for marketplaces",
            "A+ content structure guides",
        ],
        "blurb": """E-commerce margins live and die on listing quality. GeetAI Listing provides product description formulas, sixty title and bullet templates, and keyword placement guides for Amazon, Flipkart, Meesho, and Shopify. Sellers and agencies use this to optimize catalogs at scale — turning weak listings into conversion machines without hiring copywriters per SKU. Includes category-specific angle prompts, compliance notes for marketplace rules, and A+ content structure guides for premium placements. Whether you're launching ten products or optimizing a thousand-SKU catalog, these frameworks ensure every listing communicates benefits, handles objections, and ranks for buyer search terms.""",
    },
    {
        "slug": "persona",
        "emoji": "🔬",
        "name": "GeetAI Persona",
        "short_desc": "Customer research & personas",
        "cat": "content",
        "badge": "Research",
        "product_num": 33,
        "price": "₹1,999",
        "vault": "33_persona_research_vault.md",
        "headline": "Know your customer better than they know themselves",
        "features": [
            "Persona building frameworks",
            "Customer interview question banks",
            "Jobs-to-be-done analysis prompts",
            "Market sizing & segment templates",
        ],
        "blurb": """Marketing fails when you're guessing at customer motivations. GeetAI Persona delivers research frameworks, interview question banks, and jobs-to-be-done analysis prompts that turn vague target audiences into actionable personas. Founders use this before building products; marketers use it before writing campaigns; agencies deliver it as high-value strategy work. Includes market segment templates, pain-point mapping exercises, and messaging implication guides so research actually changes your copy and offers. Stop creating content for "everyone." Build detailed personas that inform every ad, email, and landing page — and watch conversion rates climb because you're finally speaking to real human needs.""",
    },
    {
        "slug": "minutes",
        "emoji": "🗒️",
        "name": "GeetAI Minutes",
        "short_desc": "Meeting summaries & action items",
        "cat": "operations",
        "badge": "Productivity",
        "product_num": 34,
        "price": "₹1,499",
        "vault": "34_meeting_minutes_vault.md",
        "headline": "Meetings that end with clarity — not confusion",
        "features": [
            "Minutes templates by meeting type",
            "Action item extraction frameworks",
            "Follow-up email templates",
            "Decision log & accountability trackers",
        ],
        "blurb": """Meetings without follow-through waste everyone's time. GeetAI Minutes provides templates for standups, client calls, board meetings, and brainstorms — plus frameworks that extract action items, owners, and deadlines automatically from any transcript or notes. Team leads, EAs, and consultants use this to send summaries within minutes of hanging up, keeping projects moving and clients confident you're organized. Includes follow-up email templates, decision logs for recurring meetings, and accountability trackers that prevent tasks from vanishing into Slack threads. Stop being the person who says "I'll send notes later" and never does. Systematize meeting output so every conversation produces forward motion.""",
    },
]

PAGE_TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{name} — GeetAI Studio</title>
<meta name="description" content="{meta_desc}">
<link rel="icon" type="image/x-icon" href="../favicon.ico">
<link rel="apple-touch-icon" sizes="180x180" href="../apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="32x32" href="../favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="../favicon-16x16.png">
<meta property="og:type" content="website">
<meta property="og:url" content="https://geetaistudio.com/tools/{slug}.html">
<meta property="og:title" content="{name} — GeetAI Studio">
<meta property="og:description" content="{meta_desc}">
<meta property="og:image" content="https://geetaistudio.com/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{name}">
<meta name="twitter:description" content="{meta_desc}">
<meta name="twitter:image" content="https://geetaistudio.com/og-image.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root {{
  --bg:#03030a; --bg2:#07071a; --surface:rgba(255,255,255,0.04);
  --border:rgba(255,255,255,0.08); --blue2:#60a5fa; --indigo:#6366f1;
  --purple:#8b5cf6; --cyan2:#22d3ee; --white:#f8fafc; --muted:#94a3b8; --accent:#a78bfa;
  --r-md:12px; --r-lg:16px; --r-xl:24px;
}}
*,*::before,*::after {{ box-sizing:border-box; margin:0; padding:0; }}
body {{ font-family:'Plus Jakarta Sans',sans-serif; background:var(--bg); color:var(--white); line-height:1.6; }}
a {{ color:inherit; text-decoration:none; }}
.container {{ max-width:900px; margin:0 auto; padding:0 24px; }}
.nav {{ padding:20px 0; border-bottom:1px solid var(--border); }}
.nav-inner {{ max-width:1200px; margin:0 auto; padding:0 24px; display:flex; align-items:center; justify-content:space-between; }}
.logo {{ font-size:20px; font-weight:800; }}
.logo span {{ background:linear-gradient(135deg,#60a5fa,#a78bfa,#22d3ee); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }}
.nav-back {{ font-size:14px; color:var(--muted); }}
.nav-back:hover {{ color:var(--blue2); }}
.hero {{ padding:64px 0 48px; text-align:center; }}
.tool-emoji {{ font-size:64px; margin-bottom:16px; display:block; }}
.badge {{ display:inline-flex; align-items:center; gap:6px; padding:6px 14px; background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.3); border-radius:100px; font-size:13px; font-weight:600; color:var(--accent); margin-bottom:20px; }}
h1 {{ font-size:clamp(28px,5vw,42px); font-weight:800; line-height:1.15; margin-bottom:16px; }}
.gradient-text {{ background:linear-gradient(135deg,#60a5fa,#a78bfa,#22d3ee); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }}
.subtitle {{ font-size:18px; color:var(--muted); max-width:640px; margin:0 auto 32px; }}
.features {{ display:grid; gap:12px; margin:40px 0; text-align:left; }}
.feature {{ display:flex; gap:12px; align-items:flex-start; padding:16px; background:var(--surface); border:1px solid var(--border); border-radius:var(--r-md); font-size:15px; }}
.feature::before {{ content:'✓'; color:var(--cyan2); font-weight:700; flex-shrink:0; }}
.body-copy {{ font-size:16px; color:var(--muted); line-height:1.8; margin-bottom:40px; }}
.body-copy p {{ margin-bottom:16px; }}
.cta-box {{ background:linear-gradient(135deg,rgba(99,102,241,0.15),rgba(6,182,212,0.1)); border:1px solid rgba(99,102,241,0.3); border-radius:var(--r-xl); padding:40px; text-align:center; margin:48px 0; }}
.cta-box h2 {{ font-size:24px; margin-bottom:12px; }}
.cta-box p {{ color:var(--muted); margin-bottom:24px; }}
.price {{ font-size:28px; font-weight:800; color:var(--blue2); margin-bottom:8px; }}
.btn {{ display:inline-flex; align-items:center; gap:8px; padding:14px 28px; border-radius:var(--r-md); font-size:15px; font-weight:600; border:none; cursor:pointer; transition:all 0.2s; }}
.btn-primary {{ background:linear-gradient(135deg,var(--indigo),var(--purple)); color:white; }}
.btn-primary:hover {{ transform:translateY(-2px); box-shadow:0 8px 32px rgba(99,102,241,0.4); }}
.btn-ghost {{ background:transparent; border:1px solid var(--border); color:var(--white); margin-left:12px; }}
.btn-ghost:hover {{ border-color:var(--indigo); }}
.footer {{ padding:40px 0; border-top:1px solid var(--border); text-align:center; color:var(--muted); font-size:14px; }}
.related {{ margin:48px 0; }}
.related h3 {{ font-size:18px; margin-bottom:16px; }}
.related-links {{ display:flex; flex-wrap:wrap; gap:8px; }}
.related-links a {{ padding:8px 16px; background:var(--surface); border:1px solid var(--border); border-radius:100px; font-size:13px; }}
.related-links a:hover {{ border-color:var(--indigo); color:var(--blue2); }}
</style>
</head>
<body>
<nav class="nav">
  <div class="nav-inner">
    <a href="../index.html" class="logo">Geet<span>AI</span></a>
    <a href="../index.html#tools" class="nav-back">← All 30 Tools</a>
  </div>
</nav>
<main class="container">
  <section class="hero">
    <span class="tool-emoji" aria-hidden="true">{emoji}</span>
    <span class="badge">{badge}</span>
    <h1>{name}</h1>
    <p class="subtitle">{headline}</p>
  </section>
  <div class="features">
{features_html}
  </div>
  <div class="body-copy">
    <p>{blurb_para1}</p>
    <p>{blurb_para2}</p>
  </div>
  <div class="cta-box">
    <div class="price">{price}</div>
    <h2>Get the {name} Vault</h2>
    <p>Instant download · Use with ChatGPT, Claude, or GeetAI Studio</p>
    <a href="https://aniketgai.gumroad.com" class="btn btn-primary" target="_blank" rel="noopener">Buy on Gumroad</a>
    <a href="../index.html#pricing" class="btn btn-ghost">View Platform Plans</a>
  </div>
  <div class="related">
    <h3>Explore more tools</h3>
    <div class="related-links">
      <a href="../index.html#tools">All 30 Tools</a>
      <a href="agencyos.html">AgencyOS</a>
      <a href="leads.html">Leads</a>
      <a href="content.html">Content</a>
    </div>
  </div>
</main>
<footer class="footer">
  <p>© 2025 GeetAI Studio · <a href="../index.html">Home</a> · <a href="mailto:aniketgai.studio@gmail.com">Contact</a></p>
</footer>
</body>
</html>
'''


def split_blurb(blurb: str) -> tuple[str, str]:
    sentences = blurb.replace("—", ". ").split(". ")
    mid = len(sentences) // 2
    p1 = ". ".join(sentences[:mid]).strip()
    p2 = ". ".join(sentences[mid:]).strip()
    if not p1.endswith("."):
        p1 += "."
    if p2 and not p2.endswith("."):
        p2 += "."
    return p1, p2


def generate_tool_pages() -> None:
    TOOLS_DIR.mkdir(parents=True, exist_ok=True)
    for t in TOOLS:
        features_html = "\n".join(
            f'    <div class="feature">{f}</div>' for f in t["features"]
        )
        p1, p2 = split_blurb(t["blurb"])
        meta_desc = t["headline"][:155]
        html = PAGE_TEMPLATE.format(
            name=t["name"],
            slug=t["slug"],
            emoji=t["emoji"],
            badge=t["badge"],
            headline=t["headline"],
            features_html=features_html,
            blurb_para1=p1,
            blurb_para2=p2,
            price=t["price"],
            meta_desc=meta_desc,
        )
        (TOOLS_DIR / f"{t['slug']}.html").write_text(html, encoding="utf-8")
    print(f"Generated {len(TOOLS)} tool pages in {TOOLS_DIR}")


def generate_descriptions_md() -> None:
    lines = [
        "# GeetAI Studio — Tool Descriptions",
        "",
        "30 product blurbs for website listings and Gumroad. Tone matches geetai.html marketing copy.",
        "",
        "---",
        "",
    ]
    for t in TOOLS:
        word_count = len(t["blurb"].split())
        lines.extend([
            f"## {t['name']}",
            "",
            f"**Product #{t['product_num']}** · {t['price']} · Vault: `{t['vault']}`",
            "",
            f"**Tagline:** {t['headline']}",
            "",
            t["blurb"],
            "",
            f"*({word_count} words)*",
            "",
            "---",
            "",
        ])
    out = ROOT / "tool_descriptions.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    generate_tool_pages()
    generate_descriptions_md()
