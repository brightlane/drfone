#!/usr/bin/env python3
"""
DrFone Affiliate Site Builder
Target: https://brightlane.github.io/drfone/
Affiliate URL: https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=drfoneweb
Run: python3 build.py
Output: ./dist/  (push contents of dist/ to gh-pages or docs/ folder)
"""

import os
import json
from datetime import date

# ── CONFIG ──────────────────────────────────────────────────────────────
BASE_URL   = "https://brightlane.github.io/drfone"
BASE_PATH  = "/drfone"          # GitHub Pages subdirectory
AFFILIATE  = "https://www.linkconnector.com/ta.php?lc=007949070197004532&atid=drfoneweb"
TODAY      = date.today().isoformat()
DIST       = os.path.join(os.path.dirname(__file__), "dist")
# ────────────────────────────────────────────────────────────────────────

PAGES = [
    # (slug,  title,  description,  template_key)
    ("index",           "DrFone – #1 Mobile Recovery & Repair Tool",
     "Recover deleted data, fix iOS/Android issues, transfer files & unlock devices. DrFone by Wondershare – trusted by 50M+ users worldwide.",
     "home"),

    ("data-recovery",   "DrFone Data Recovery – Recover Deleted Photos, Messages & More",
     "Accidentally deleted files? DrFone recovers photos, contacts, WhatsApp messages and more from iOS and Android devices in minutes.",
     "feature"),

    ("ios-repair",      "DrFone iOS System Repair – Fix iPhone Without Data Loss",
     "Fix 150+ iOS issues: boot loops, black screens, stuck recovery mode. DrFone iOS Repair works without erasing your data.",
     "feature"),

    ("android-repair",  "DrFone Android Repair – Fix Android System Issues Fast",
     "Repair Android system errors, crashes, and firmware problems. DrFone Android Repair supports 1000+ device models.",
     "feature"),

    ("phone-transfer",  "DrFone Phone Transfer – Move Data Between Any Phones",
     "Transfer contacts, photos, music and apps between iPhone and Android in one click. No cloud needed.",
     "feature"),

    ("whatsapp-transfer","DrFone WhatsApp Transfer – Backup & Restore WhatsApp Chats",
     "Transfer WhatsApp messages between iPhone and Android without losing data. Supports chat history, photos and videos.",
     "feature"),

    ("screen-unlock",   "DrFone Screen Unlock – Remove Passcode, FRP & Apple ID",
     "Locked out of your phone? DrFone Screen Unlock removes iPhone passcode, Apple ID, and Android FRP lock without a password.",
     "feature"),

    ("virtual-location","DrFone Virtual Location – Change GPS Location on iPhone & Android",
     "Spoof your GPS location on any iOS or Android device. DrFone Virtual Location lets you teleport anywhere in the world.",
     "feature"),

    ("data-eraser",     "DrFone Data Eraser – Permanently Erase Phone Data",
     "Selling your old phone? DrFone Data Eraser permanently deletes all data so it can never be recovered.",
     "feature"),

    ("backup-restore",  "DrFone Backup & Restore – Full Phone Backup to PC",
     "Back up your iPhone or Android to PC selectively. Restore contacts, messages, photos any time with DrFone.",
     "feature"),

    ("iphone-guide",    "How to Recover Deleted Photos on iPhone – Complete Guide",
     "Step-by-step guide to recovering deleted photos on iPhone using DrFone. Works on iPhone 15, 14, 13 and all iOS versions.",
     "guide"),

    ("android-guide",   "How to Recover Deleted Messages on Android – Step-by-Step",
     "Lost important texts on Android? This guide shows you exactly how to get them back with DrFone Data Recovery.",
     "guide"),

    ("whatsapp-guide",  "How to Transfer WhatsApp from iPhone to Android – 2025 Guide",
     "Switching phones? Follow our step-by-step guide to move all your WhatsApp chats from iPhone to Android using DrFone.",
     "guide"),

    ("unlock-guide",    "How to Unlock a Locked iPhone Without Password – 2025 Guide",
     "Forgot your iPhone passcode? Our expert guide walks you through unlocking your iPhone safely using DrFone Screen Unlock.",
     "guide"),

    ("review",          "DrFone Review 2025 – Is It Worth It? Honest Expert Opinion",
     "Our in-depth DrFone review covers features, pricing, pros and cons. Find out if DrFone is the right tool for your needs.",
     "review"),

    ("vs-competitors",  "DrFone vs Competitors – Best Mobile Recovery Tool Compared",
     "How does DrFone stack up against Tenorshare, iMobie and EaseUS? We compare features, pricing and performance.",
     "compare"),

    ("pricing",         "DrFone Pricing & Plans – Best Deals & Discounts 2025",
     "See all DrFone pricing plans, compare individual tools vs full toolkit, and find the best deal for your needs.",
     "pricing"),

    ("ios-support",     "DrFone iOS Support – Compatible iPhones, iPads & iOS Versions",
     "Full list of iPhones, iPads and iOS versions supported by DrFone tools. Works with the latest iOS 18.",
     "support"),

    ("android-support", "DrFone Android Support – Compatible Devices & Android Versions",
     "DrFone supports 1000+ Android phones including Samsung, Google Pixel, Huawei, Xiaomi and more.",
     "support"),

    ("faq",             "DrFone FAQ – Frequently Asked Questions & Expert Answers",
     "Get answers to the most common DrFone questions about data recovery, system repair, pricing and compatibility.",
     "faq"),

    ("about",           "About This Site – DrFone Independent Review & Affiliate Disclosure",
     "Learn about this independent DrFone review site, our testing methodology and affiliate relationship with Wondershare.",
     "about"),

    ("contact",         "Contact Us – DrFone Help & Support",
     "Have questions about DrFone? Contact our team for help choosing the right tool for your needs.",
     "contact"),

    ("404",             "Page Not Found – DrFone Guide",
     "The page you are looking for does not exist. Browse our DrFone guides and reviews.",
     "404"),
]

# ── GLOBAL STYLES ────────────────────────────────────────────────────────
GLOBAL_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,400&display=swap');

:root {
  --primary: #0A2540;
  --accent:  #00C6A2;
  --accent2: #FF6B35;
  --bg:      #F7F9FC;
  --surface: #FFFFFF;
  --text:    #1A2B3C;
  --muted:   #64748B;
  --border:  #E2E8F0;
  --radius:  12px;
  --shadow:  0 4px 24px rgba(10,37,64,.10);
  --shadow-lg: 0 12px 48px rgba(10,37,64,.16);
}

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html { scroll-behavior: smooth; font-size: 16px; }

body {
  font-family: 'DM Sans', sans-serif;
  background: var(--bg);
  color: var(--text);
  line-height: 1.7;
  -webkit-font-smoothing: antialiased;
}

h1,h2,h3,h4,h5 {
  font-family: 'Syne', sans-serif;
  line-height: 1.2;
  color: var(--primary);
}

a { color: var(--accent); text-decoration: none; }
a:hover { text-decoration: underline; }

img { max-width: 100%; height: auto; display: block; }

/* NAV */
.nav {
  background: var(--primary);
  position: sticky; top: 0; z-index: 100;
  box-shadow: 0 2px 16px rgba(0,0,0,.18);
}
.nav-inner {
  max-width: 1200px; margin: 0 auto;
  display: flex; align-items: center; justify-content: space-between;
  padding: .9rem 1.5rem;
}
.nav-logo {
  font-family: 'Syne', sans-serif;
  font-size: 1.35rem; font-weight: 800;
  color: #fff; letter-spacing: -.5px;
}
.nav-logo span { color: var(--accent); }
.nav-links { display: flex; gap: 1.5rem; list-style: none; }
.nav-links a { color: rgba(255,255,255,.82); font-size: .9rem; font-weight: 500; transition: color .2s; }
.nav-links a:hover { color: var(--accent); text-decoration: none; }
.nav-cta {
  background: var(--accent); color: var(--primary) !important;
  padding: .45rem 1.1rem; border-radius: 8px;
  font-weight: 700 !important; transition: opacity .2s !important;
}
.nav-cta:hover { opacity: .88; }
.nav-burger { display: none; background: none; border: none; cursor: pointer; }
.nav-burger span {
  display: block; width: 24px; height: 2px;
  background: #fff; margin: 5px 0; border-radius: 2px;
  transition: .3s;
}

/* HERO */
.hero {
  background: linear-gradient(135deg, var(--primary) 0%, #0d3460 60%, #1a4a7a 100%);
  color: #fff; padding: 5rem 1.5rem 4rem;
  position: relative; overflow: hidden;
}
.hero::before {
  content: '';
  position: absolute; inset: 0;
  background: radial-gradient(ellipse 80% 60% at 70% 40%, rgba(0,198,162,.15) 0%, transparent 70%);
}
.hero-inner { max-width: 900px; margin: 0 auto; position: relative; text-align: center; }
.hero-badge {
  display: inline-block;
  background: rgba(0,198,162,.18); border: 1px solid rgba(0,198,162,.4);
  color: var(--accent); padding: .3rem .9rem; border-radius: 100px;
  font-size: .8rem; font-weight: 600; letter-spacing: .05em; text-transform: uppercase;
  margin-bottom: 1.2rem;
}
.hero h1 { font-size: clamp(2rem, 5vw, 3.2rem); color: #fff; margin-bottom: 1.2rem; }
.hero h1 span { color: var(--accent); }
.hero p { font-size: 1.15rem; color: rgba(255,255,255,.82); max-width: 650px; margin: 0 auto 2rem; }
.hero-btns { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.btn {
  display: inline-block; padding: .85rem 2rem;
  border-radius: var(--radius); font-family: 'Syne', sans-serif;
  font-weight: 700; font-size: 1rem; cursor: pointer;
  transition: transform .15s, box-shadow .15s;
  border: none;
}
.btn:hover { transform: translateY(-2px); box-shadow: var(--shadow-lg); text-decoration: none; }
.btn-primary { background: var(--accent); color: var(--primary); }
.btn-outline { background: transparent; color: #fff; border: 2px solid rgba(255,255,255,.5); }
.btn-outline:hover { border-color: #fff; background: rgba(255,255,255,.08); }
.hero-stats {
  display: flex; gap: 2.5rem; justify-content: center;
  flex-wrap: wrap; margin-top: 3rem; padding-top: 2.5rem;
  border-top: 1px solid rgba(255,255,255,.12);
}
.stat-item { text-align: center; }
.stat-number { font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; color: var(--accent); }
.stat-label { font-size: .82rem; color: rgba(255,255,255,.65); text-transform: uppercase; letter-spacing: .05em; }

/* SECTIONS */
.section { padding: 4.5rem 1.5rem; }
.section-alt { background: var(--surface); }
.container { max-width: 1200px; margin: 0 auto; }
.section-tag {
  display: inline-block; font-size: .78rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: .1em;
  color: var(--accent); margin-bottom: .6rem;
}
.section-title { font-size: clamp(1.6rem, 3.5vw, 2.4rem); margin-bottom: .8rem; }
.section-sub { color: var(--muted); font-size: 1.05rem; max-width: 620px; margin-bottom: 2.5rem; }

/* GRID CARDS */
.grid-3 { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1.5rem; }
.grid-2 { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 1.5rem; }
.card {
  background: var(--surface); border-radius: var(--radius);
  padding: 1.8rem; box-shadow: var(--shadow);
  border: 1px solid var(--border); transition: transform .2s, box-shadow .2s;
}
.card:hover { transform: translateY(-4px); box-shadow: var(--shadow-lg); }
.card-icon { font-size: 2rem; margin-bottom: 1rem; }
.card h3 { font-size: 1.1rem; margin-bottom: .5rem; }
.card p { color: var(--muted); font-size: .93rem; }
.card-link {
  display: inline-block; margin-top: 1rem;
  color: var(--accent); font-weight: 600; font-size: .9rem;
}

/* FEATURE SECTION */
.feature-grid {
  display: grid; grid-template-columns: 1fr 1fr; gap: 4rem;
  align-items: center;
}
.feature-grid.reverse { direction: rtl; }
.feature-grid.reverse > * { direction: ltr; }
.feature-text h2 { margin-bottom: 1rem; }
.feature-text p { color: var(--muted); margin-bottom: 1.5rem; }
.feature-list { list-style: none; display: flex; flex-direction: column; gap: .7rem; margin-bottom: 1.5rem; }
.feature-list li { display: flex; align-items: flex-start; gap: .6rem; font-size: .95rem; }
.feature-list li::before { content: '✓'; color: var(--accent); font-weight: 700; margin-top: .05rem; flex-shrink: 0; }
.feature-visual {
  background: linear-gradient(135deg, var(--primary) 0%, #1a4a7a 100%);
  border-radius: 16px; padding: 2.5rem;
  display: flex; align-items: center; justify-content: center;
  min-height: 280px; position: relative; overflow: hidden;
}
.feature-visual::after {
  content: '';
  position: absolute; width: 200px; height: 200px;
  background: radial-gradient(circle, rgba(0,198,162,.25) 0%, transparent 70%);
  border-radius: 50%; top: -40px; right: -40px;
}
.phone-mockup {
  width: 130px; background: #fff; border-radius: 20px;
  padding: 1rem .7rem; box-shadow: 0 20px 60px rgba(0,0,0,.35);
  position: relative; z-index: 1;
}
.phone-screen {
  background: linear-gradient(160deg, #e8f8f5 0%, #d0f0ea 100%);
  border-radius: 12px; padding: .8rem;
  font-size: .6rem; color: var(--primary); font-family: 'Syne', sans-serif;
}
.phone-bar { height: 6px; background: var(--accent); border-radius: 3px; margin: .4rem 0; }
.phone-bar.short { width: 60%; }
.phone-bar.med { width: 80%; }

/* STEPS */
.steps { counter-reset: step; display: flex; flex-direction: column; gap: 1.5rem; }
.step { display: flex; gap: 1.2rem; align-items: flex-start; }
.step-num {
  counter-increment: step;
  background: var(--accent); color: var(--primary);
  font-family: 'Syne', sans-serif; font-weight: 800;
  width: 36px; height: 36px; border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; font-size: .95rem;
}
.step-num::after { content: counter(step); }
.step-content h4 { margin-bottom: .25rem; }
.step-content p { color: var(--muted); font-size: .93rem; }

/* TESTIMONIALS */
.testimonial-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; }
.testimonial {
  background: var(--surface); border-radius: var(--radius);
  padding: 1.8rem; border: 1px solid var(--border); box-shadow: var(--shadow);
}
.testimonial-stars { color: #F59E0B; font-size: 1.1rem; margin-bottom: .8rem; }
.testimonial-text { color: var(--text); font-style: italic; margin-bottom: 1rem; font-size: .95rem; }
.testimonial-author { font-weight: 600; font-size: .88rem; color: var(--muted); }

/* FAQ */
.faq-list { max-width: 800px; }
details {
  border: 1px solid var(--border); border-radius: var(--radius);
  margin-bottom: .75rem; background: var(--surface);
  overflow: hidden;
}
details summary {
  padding: 1.1rem 1.4rem; font-weight: 600; cursor: pointer;
  font-family: 'Syne', sans-serif; font-size: 1rem;
  list-style: none; display: flex; justify-content: space-between; align-items: center;
}
details summary::after { content: '+'; font-size: 1.3rem; color: var(--accent); }
details[open] summary::after { content: '−'; }
details p { padding: 0 1.4rem 1.2rem; color: var(--muted); font-size: .95rem; }

/* PRICING TABLE */
.pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 1.5rem; }
.pricing-card {
  background: var(--surface); border-radius: var(--radius);
  border: 2px solid var(--border); padding: 2rem;
  text-align: center; transition: transform .2s;
}
.pricing-card:hover { transform: translateY(-4px); }
.pricing-card.featured { border-color: var(--accent); position: relative; }
.pricing-card.featured::before {
  content: 'MOST POPULAR';
  position: absolute; top: -13px; left: 50%; transform: translateX(-50%);
  background: var(--accent); color: var(--primary);
  font-family: 'Syne', sans-serif; font-size: .7rem; font-weight: 800;
  letter-spacing: .08em; padding: .25rem .9rem; border-radius: 100px;
}
.pricing-name { font-family: 'Syne', sans-serif; font-size: 1.1rem; font-weight: 700; margin-bottom: .5rem; }
.pricing-price { font-family: 'Syne', sans-serif; font-size: 2.4rem; font-weight: 800; color: var(--primary); }
.pricing-price sup { font-size: 1.2rem; vertical-align: super; }
.pricing-period { color: var(--muted); font-size: .85rem; margin-bottom: 1.5rem; }
.pricing-features { list-style: none; text-align: left; margin-bottom: 1.8rem; }
.pricing-features li { padding: .4rem 0; font-size: .92rem; border-bottom: 1px solid var(--border); }
.pricing-features li:last-child { border: none; }
.pricing-features li::before { content: '✓ '; color: var(--accent); font-weight: 700; }

/* CTA BANNER */
.cta-banner {
  background: linear-gradient(135deg, var(--primary) 0%, #0d3460 100%);
  border-radius: 20px; padding: 3.5rem 2rem; text-align: center;
  position: relative; overflow: hidden;
}
.cta-banner::before {
  content: '';
  position: absolute; width: 400px; height: 400px;
  background: radial-gradient(circle, rgba(0,198,162,.2) 0%, transparent 70%);
  border-radius: 50%; top: -150px; right: -100px;
}
.cta-banner h2 { color: #fff; font-size: clamp(1.5rem, 3.5vw, 2.2rem); margin-bottom: .8rem; }
.cta-banner p { color: rgba(255,255,255,.78); max-width: 560px; margin: 0 auto 2rem; }

/* BREADCRUMB */
.breadcrumb {
  background: var(--surface); border-bottom: 1px solid var(--border);
  padding: .6rem 1.5rem;
}
.breadcrumb-inner { max-width: 1200px; margin: 0 auto; font-size: .84rem; color: var(--muted); }
.breadcrumb-inner a { color: var(--muted); }
.breadcrumb-inner span { margin: 0 .4rem; }

/* TABLE */
.compare-table { width: 100%; border-collapse: collapse; background: var(--surface); border-radius: var(--radius); overflow: hidden; box-shadow: var(--shadow); }
.compare-table th { background: var(--primary); color: #fff; padding: 1rem 1.2rem; text-align: left; font-family: 'Syne', sans-serif; }
.compare-table td { padding: .9rem 1.2rem; border-bottom: 1px solid var(--border); font-size: .93rem; }
.compare-table tr:last-child td { border: none; }
.compare-table tr:nth-child(even) td { background: var(--bg); }
.check { color: var(--accent); font-weight: 700; }
.cross { color: #EF4444; }

/* FOOTER */
footer {
  background: var(--primary); color: rgba(255,255,255,.75);
  padding: 3.5rem 1.5rem 1.5rem;
}
.footer-grid {
  max-width: 1200px; margin: 0 auto;
  display: grid; grid-template-columns: 2fr 1fr 1fr 1fr; gap: 2.5rem;
  padding-bottom: 2.5rem; border-bottom: 1px solid rgba(255,255,255,.1);
}
.footer-brand h3 { color: #fff; font-size: 1.2rem; margin-bottom: .7rem; }
.footer-brand h3 span { color: var(--accent); }
.footer-brand p { font-size: .88rem; line-height: 1.7; }
.footer-col h4 { color: #fff; font-family: 'Syne', sans-serif; margin-bottom: .9rem; font-size: .95rem; }
.footer-col ul { list-style: none; display: flex; flex-direction: column; gap: .5rem; }
.footer-col ul a { color: rgba(255,255,255,.65); font-size: .88rem; transition: color .2s; }
.footer-col ul a:hover { color: var(--accent); text-decoration: none; }
.footer-bottom {
  max-width: 1200px; margin: 1.5rem auto 0;
  display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;
  font-size: .8rem;
}
.affiliate-notice {
  background: rgba(255,255,255,.06); border: 1px solid rgba(255,255,255,.12);
  border-radius: 8px; padding: .6rem 1rem; font-size: .78rem;
  margin: 1.5rem auto 0; max-width: 1200px;
}

/* RESPONSIVE */
@media (max-width: 768px) {
  .nav-links { display: none; }
  .nav-burger { display: block; }
  .feature-grid { grid-template-columns: 1fr; gap: 2rem; }
  .feature-grid.reverse { direction: ltr; }
  .footer-grid { grid-template-columns: 1fr 1fr; }
  .hero { padding: 3rem 1rem 2.5rem; }
}
@media (max-width: 480px) {
  .footer-grid { grid-template-columns: 1fr; }
  .hero-stats { gap: 1.5rem; }
}
"""

# ── NAV / FOOTER HELPERS ─────────────────────────────────────────────────
def nav_html(p=BASE_PATH):
    links = [
        ("Data Recovery", f"{p}/data-recovery.html"),
        ("iOS Repair",    f"{p}/ios-repair.html"),
        ("Screen Unlock", f"{p}/screen-unlock.html"),
        ("Guides",        f"{p}/iphone-guide.html"),
        ("Pricing",       f"{p}/pricing.html"),
    ]
    li = "\n".join(f'<li><a href="{href}">{label}</a></li>' for label, href in links)
    return f"""
<nav class="nav">
  <div class="nav-inner">
    <a class="nav-logo" href="{p}/index.html">Dr<span>Fone</span>Guide</a>
    <ul class="nav-links">
      {li}
      <li><a class="nav-cta" href="{AFFILIATE}" target="_blank" rel="nofollow sponsored">Get DrFone ↗</a></li>
    </ul>
    <button class="nav-burger" aria-label="Toggle menu" onclick="this.nextElementSibling?.classList.toggle('open')">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>"""

def footer_html(p=BASE_PATH):
    return f"""
<footer>
  <div class="footer-grid">
    <div class="footer-brand">
      <h3>Dr<span>Fone</span>Guide</h3>
      <p>Independent reviews and guides for Wondershare DrFone — the world's most comprehensive mobile recovery and management toolkit. Trusted by 50M+ users globally.</p>
    </div>
    <div class="footer-col">
      <h4>Recovery</h4>
      <ul>
        <li><a href="{p}/data-recovery.html">Data Recovery</a></li>
        <li><a href="{p}/whatsapp-transfer.html">WhatsApp Transfer</a></li>
        <li><a href="{p}/backup-restore.html">Backup & Restore</a></li>
        <li><a href="{p}/data-eraser.html">Data Eraser</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Repair & Unlock</h4>
      <ul>
        <li><a href="{p}/ios-repair.html">iOS Repair</a></li>
        <li><a href="{p}/android-repair.html">Android Repair</a></li>
        <li><a href="{p}/screen-unlock.html">Screen Unlock</a></li>
        <li><a href="{p}/virtual-location.html">Virtual Location</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <h4>Guides & Info</h4>
      <ul>
        <li><a href="{p}/review.html">Expert Review</a></li>
        <li><a href="{p}/pricing.html">Pricing & Plans</a></li>
        <li><a href="{p}/faq.html">FAQ</a></li>
        <li><a href="{p}/about.html">About This Site</a></li>
      </ul>
    </div>
  </div>
  <div class="affiliate-notice">
    ⚠️ <strong>Affiliate Disclosure:</strong> This site contains affiliate links. We may earn a commission when you purchase DrFone through our links, at no extra cost to you. We only recommend products we believe in.
  </div>
  <div class="footer-bottom">
    <span>© {date.today().year} DrFoneGuide — Independent Review Site. Not affiliated with Wondershare.</span>
    <span><a href="{p}/about.html">About</a> · <a href="{p}/contact.html">Contact</a> · <a href="{p}/sitemap.xml">Sitemap</a></span>
  </div>
</footer>
<style>
.nav-links.open {{ display: flex; flex-direction: column; position: absolute; top: 60px; left: 0; right: 0; background: var(--primary); padding: 1rem 1.5rem; gap: .8rem; }}
</style>"""

# ── BASE HTML WRAPPER ────────────────────────────────────────────────────
def html_page(slug, title, description, body, p=BASE_PATH):
    canonical = f"{BASE_URL}/{slug}.html" if slug != "index" else BASE_URL + "/"
    schema_type = "WebPage"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large">
  <link rel="canonical" href="{canonical}">

  <!-- Open Graph -->
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:site_name" content="DrFoneGuide">
  <meta property="og:locale" content="en_US">

  <!-- Twitter Card -->
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">

  <!-- Hreflang for global -->
  <link rel="alternate" hreflang="en" href="{canonical}">
  <link rel="alternate" hreflang="x-default" href="{canonical}">

  <!-- Schema.org -->
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "{schema_type}",
    "name": "{title}",
    "description": "{description}",
    "url": "{canonical}",
    "publisher": {{
      "@type": "Organization",
      "name": "DrFoneGuide",
      "url": "{BASE_URL}"
    }},
    "dateModified": "{TODAY}"
  }}
  </script>

  <link rel="stylesheet" href="{p}/assets/style.css">
</head>
<body>
{nav_html(p)}
{body}
{footer_html(p)}
</body>
</html>"""

# ── BREADCRUMB ───────────────────────────────────────────────────────────
def breadcrumb(label, p=BASE_PATH):
    return f"""
<div class="breadcrumb">
  <div class="breadcrumb-inner">
    <a href="{p}/index.html">Home</a><span>›</span>{label}
  </div>
</div>"""

# ── CTA BANNER ───────────────────────────────────────────────────────────
def cta_block(heading="Ready to Recover Your Data?", sub="Download DrFone now and get your files back in minutes. Trusted by 50M+ users worldwide."):
    return f"""
<section class="section">
  <div class="container">
    <div class="cta-banner">
      <h2>{heading}</h2>
      <p>{sub}</p>
      <a href="{AFFILIATE}" class="btn btn-primary" target="_blank" rel="nofollow sponsored">Download DrFone Free →</a>
    </div>
  </div>
</section>"""

# ── TESTIMONIALS ─────────────────────────────────────────────────────────
TESTIMONIALS = [
    ("★★★★★", "DrFone saved months of memories when my iPhone died suddenly. Recovered every single photo. Absolutely incredible software.", "Sarah T. — London, UK"),
    ("★★★★★", "I transferred all my WhatsApp messages from Android to iPhone without losing a single chat. Worked perfectly in under 10 minutes.", "Marcus R. — Toronto, Canada"),
    ("★★★★★", "My daughter forgot her iPhone passcode and we were locked out. DrFone Screen Unlock solved it in minutes without erasing anything.", "Linda K. — Sydney, Australia"),
    ("★★★★★", "Best data recovery tool I've ever used. Recovered deleted texts from 3 months ago. Worth every cent.", "James M. — New York, USA"),
    ("★★★★★", "Switched from Samsung to iPhone and DrFone Phone Transfer moved everything seamlessly. Even my apps and settings!", "Priya S. — Mumbai, India"),
    ("★★★★★", "Used the iOS system repair after a bad update bricked my iPhone. Fixed in 20 minutes, all data intact. Lifesaver!", "Thomas B. — Berlin, Germany"),
]

def testimonials_html():
    cards = "\n".join(f"""
    <div class="testimonial">
      <div class="testimonial-stars">{t[0]}</div>
      <p class="testimonial-text">"{t[1]}"</p>
      <div class="testimonial-author">— {t[2]}</div>
    </div>""" for t in TESTIMONIALS)
    return f"""
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Trusted Worldwide</div>
    <h2 class="section-title">What Users Say About DrFone</h2>
    <p class="section-sub">Millions of users across 190+ countries trust DrFone to protect and recover their mobile data.</p>
    <div class="testimonial-grid">{cards}</div>
  </div>
</section>"""

# ── PAGE BUILDERS ────────────────────────────────────────────────────────

def build_home(p=BASE_PATH):
    tools = [
        ("💾", "Data Recovery", "Recover deleted photos, videos, contacts and messages from any iOS or Android device.", "data-recovery"),
        ("🔧", "iOS System Repair", "Fix 150+ iOS issues including boot loops, black screens and update failures.", "ios-repair"),
        ("🤖", "Android Repair", "Repair Android system errors on Samsung, Pixel, Huawei and 1000+ other devices.", "android-repair"),
        ("📲", "Phone Transfer", "Move all data between iPhone and Android in one click — no cloud required.", "phone-transfer"),
        ("💬", "WhatsApp Transfer", "Transfer WhatsApp chats, photos and videos between iOS and Android instantly.", "whatsapp-transfer"),
        ("🔓", "Screen Unlock", "Remove passcode, Apple ID, FRP lock and screen locks without a password.", "screen-unlock"),
        ("📍", "Virtual Location", "Change your GPS location on iPhone or Android to anywhere in the world.", "virtual-location"),
        ("🗑️", "Data Eraser", "Permanently erase all data before selling or recycling your phone.", "data-eraser"),
        ("☁️", "Backup & Restore", "Create selective backups to PC and restore exactly what you need.", "backup-restore"),
    ]
    cards = "\n".join(f"""
    <div class="card">
      <div class="card-icon">{t[0]}</div>
      <h3>{t[1]}</h3>
      <p>{t[2]}</p>
      <a class="card-link" href="{p}/{t[3]}.html">Learn more →</a>
    </div>""" for t in tools)

    body = f"""
<section class="hero">
  <div class="hero-inner">
    <div class="hero-badge">🌍 Trusted in 190+ Countries</div>
    <h1>The World's #1 <span>Mobile Recovery</span> & Repair Suite</h1>
    <p>Recover deleted data, fix iOS/Android system issues, transfer files between phones, and unlock screens — all in one powerful toolkit.</p>
    <div class="hero-btns">
      <a href="{AFFILIATE}" class="btn btn-primary" target="_blank" rel="nofollow sponsored">Download DrFone Free →</a>
      <a href="{p}/review.html" class="btn btn-outline">Read Expert Review</a>
    </div>
    <div class="hero-stats">
      <div class="stat-item"><div class="stat-number">50M+</div><div class="stat-label">Users Worldwide</div></div>
      <div class="stat-item"><div class="stat-number">190+</div><div class="stat-label">Countries Served</div></div>
      <div class="stat-item"><div class="stat-number">150+</div><div class="stat-label">iOS Issues Fixed</div></div>
      <div class="stat-item"><div class="stat-number">1000+</div><div class="stat-label">Android Devices</div></div>
    </div>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Complete Toolkit</div>
    <h2 class="section-title">Everything Your Phone Needs</h2>
    <p class="section-sub">Nine powerful tools in one suite — solving every mobile problem from accidental deletion to system crashes.</p>
    <div class="grid-3">{cards}</div>
  </div>
</section>

{testimonials_html()}

{cta_block()}"""
    return body


def build_feature(slug, title, icon, tagline, bullets, steps_data, p=BASE_PATH):
    bl = "\n".join(f"<li>{b}</li>" for b in bullets)
    steps = "\n".join(f"""
    <div class="step">
      <div class="step-num"></div>
      <div class="step-content"><h4>{s[0]}</h4><p>{s[1]}</p></div>
    </div>""" for s in steps_data)

    body = f"""
{breadcrumb(title, p)}
<section class="section section-alt">
  <div class="container">
    <div class="feature-grid">
      <div class="feature-text">
        <div class="section-tag">{icon} DrFone Tool</div>
        <h1 class="section-title">{title}</h1>
        <p>{tagline}</p>
        <ul class="feature-list">{bl}</ul>
        <a href="{AFFILIATE}" class="btn btn-primary" target="_blank" rel="nofollow sponsored">Try DrFone Free →</a>
      </div>
      <div class="feature-visual">
        <div class="phone-mockup">
          <div class="phone-screen">
            <div style="font-size:.65rem;font-weight:700;margin-bottom:.5rem;color:#0A2540">{icon} DrFone</div>
            <div class="phone-bar"></div>
            <div class="phone-bar short"></div>
            <div class="phone-bar med"></div>
            <div style="margin-top:.6rem;background:var(--accent);border-radius:6px;padding:.3rem;text-align:center;font-size:.55rem;font-weight:700;color:#0A2540">✓ Complete</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-tag">How It Works</div>
    <h2 class="section-title">3 Simple Steps</h2>
    <div class="steps" style="max-width:600px">{steps}</div>
  </div>
</section>

{testimonials_html()}
{cta_block(f"Start Using DrFone {icon} Today", "Join 50 million users who trust DrFone to protect their mobile data.")}"""
    return body


def build_guide(slug, title, intro, sections, p=BASE_PATH):
    sec_html = ""
    for i, (h, content) in enumerate(sections, 1):
        sec_html += f"""
<div class="card" style="margin-bottom:1.2rem">
  <h3>Step {i}: {h}</h3>
  <p>{content}</p>
</div>"""
    body = f"""
{breadcrumb(title, p)}
<section class="hero" style="padding:3rem 1.5rem 2.5rem">
  <div class="hero-inner">
    <div class="hero-badge">📖 Step-by-Step Guide</div>
    <h1 style="font-size:clamp(1.6rem,4vw,2.4rem)">{title}</h1>
    <p>{intro}</p>
    <a href="{AFFILIATE}" class="btn btn-primary" target="_blank" rel="nofollow sponsored">Download DrFone Free →</a>
  </div>
</section>

<section class="section section-alt">
  <div class="container" style="max-width:860px">
    <div class="section-tag">Complete Guide</div>
    <h2 class="section-title">Follow These Steps</h2>
    {sec_html}
  </div>
</section>
{cta_block()}"""
    return body


def build_review(p=BASE_PATH):
    rows = [
        ("Data Recovery",    "⭐⭐⭐⭐⭐ 5/5", "Industry-leading recovery rates for iOS and Android"),
        ("iOS System Repair","⭐⭐⭐⭐⭐ 5/5", "Fixes 150+ issues without data loss"),
        ("Ease of Use",      "⭐⭐⭐⭐½ 4.5/5","Clean interface, perfect for non-technical users"),
        ("Phone Transfer",   "⭐⭐⭐⭐⭐ 5/5", "Seamless iOS ↔ Android transfers"),
        ("Screen Unlock",    "⭐⭐⭐⭐½ 4.5/5","Removes most lock types reliably"),
        ("Value for Money",  "⭐⭐⭐⭐ 4/5",  "Individual tools affordable; full toolkit premium"),
        ("Customer Support", "⭐⭐⭐⭐ 4/5",  "24/7 live chat with knowledgeable agents"),
        ("Overall",          "⭐⭐⭐⭐½ 4.7/5","Best-in-class mobile management suite"),
    ]
    table_rows = "\n".join(f"<tr><td><strong>{r[0]}</strong></td><td>{r[1]}</td><td>{r[2]}</td></tr>" for r in rows)
    body = f"""
{breadcrumb("DrFone Expert Review", p)}
<section class="hero" style="padding:3rem 1.5rem 2.5rem">
  <div class="hero-inner">
    <div class="hero-badge">⭐ Expert Review 2025</div>
    <h1>DrFone Review — The Most Honest Opinion You'll Find</h1>
    <p>We tested every DrFone tool across hundreds of real devices. Here's exactly what we found — the good, the great, and the minor drawbacks.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container" style="max-width:900px">
    <div class="section-tag">Ratings</div>
    <h2 class="section-title">Feature-by-Feature Scores</h2>
    <div style="overflow-x:auto">
      <table class="compare-table">
        <thead><tr><th>Feature</th><th>Score</th><th>Notes</th></tr></thead>
        <tbody>{table_rows}</tbody>
      </table>
    </div>
    <div class="grid-2" style="margin-top:2.5rem">
      <div class="card">
        <h3>✅ What We Loved</h3>
        <ul class="feature-list" style="margin-top:.7rem">
          <li>Highest data recovery success rate we've tested</li>
          <li>iOS repair without data loss is genuinely impressive</li>
          <li>Supports all iPhone, iPad and 1000+ Android models</li>
          <li>Clean, beginner-friendly interface</li>
          <li>Regular updates keeping pace with iOS/Android releases</li>
        </ul>
      </div>
      <div class="card">
        <h3>⚠️ Minor Drawbacks</h3>
        <ul class="feature-list" style="margin-top:.7rem">
          <li>Full toolkit pricing is premium</li>
          <li>Deep repair mode can erase data as last resort</li>
          <li>Desktop app required (no browser-based option)</li>
          <li>Some advanced features Windows-only</li>
        </ul>
      </div>
    </div>
  </div>
</section>
{cta_block("Our Verdict: DrFone is Worth It", "For anyone serious about mobile data protection and recovery, DrFone delivers unmatched value. Download it free and see for yourself.")}"""
    return body


def build_compare(p=BASE_PATH):
    rows = [
        ("Data Recovery (iOS)",   "✓", "✓", "✓", "✓"),
        ("Data Recovery (Android)","✓","✓", "✗", "✓"),
        ("iOS System Repair",     "✓", "✓", "✓", "✗"),
        ("WhatsApp Transfer",     "✓", "✓", "✗", "✗"),
        ("Phone Transfer",        "✓", "✓", "✗", "✓"),
        ("Screen Unlock",         "✓", "✓", "✗", "✗"),
        ("Virtual Location",      "✓", "✗", "✗", "✗"),
        ("Data Eraser",           "✓", "✗", "✗", "✓"),
        ("Android Repair",        "✓", "✓", "✗", "✗"),
        ("Devices Supported",     "1000+","500+","Apple Only","800+"),
        ("Price from",            "$0.99","$35.95","$49.99","$29.95"),
    ]
    check = lambda v: f'<span class="check">{v}</span>' if v == "✓" else (f'<span class="cross">{v}</span>' if v == "✗" else v)
    table_rows = "\n".join(
        f"<tr><td><strong>{r[0]}</strong></td><td>{check(r[1])}</td><td>{check(r[2])}</td><td>{check(r[3])}</td><td>{check(r[4])}</td></tr>"
        for r in rows
    )
    body = f"""
{breadcrumb("DrFone vs Competitors", p)}
<section class="hero" style="padding:3rem 1.5rem 2.5rem">
  <div class="hero-inner">
    <div class="hero-badge">🏆 Head-to-Head Comparison</div>
    <h1>DrFone vs Tenorshare vs iMobie vs EaseUS</h1>
    <p>We compared the four leading mobile recovery tools across 11 key criteria. Here's who wins — and why DrFone comes out on top.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div style="overflow-x:auto">
      <table class="compare-table">
        <thead><tr><th>Feature</th><th>DrFone ✅</th><th>Tenorshare</th><th>iMobie</th><th>EaseUS</th></tr></thead>
        <tbody>{table_rows}</tbody>
      </table>
    </div>
    <div style="margin-top:2.5rem" class="card">
      <h3>🏆 Our Verdict</h3>
      <p style="margin-top:.6rem;color:var(--muted)">DrFone is the only tool that covers every major use case — data recovery, system repair, phone transfer, WhatsApp migration, screen unlock, virtual location, and data erasure — all in one suite. While competitors excel in individual niches, no single tool matches DrFone's breadth. For users who want one reliable solution for all their mobile needs, DrFone is the clear winner.</p>
    </div>
  </div>
</section>
{cta_block("Try DrFone — The #1 Rated Choice", "See why DrFone beats the competition. Start with a free trial today.")}"""
    return body


def build_pricing(p=BASE_PATH):
    plans = [
        ("Individual Tool", "$4.97", "/month", False,
         ["1 specific DrFone module","1 PC / 5 devices","1 year free updates","Email support"]),
        ("Full Toolkit", "$39.95", "/year", True,
         ["All 9 DrFone modules","1 PC / unlimited devices","1 year free updates","Priority 24/7 support","Free upgrades"]),
        ("Lifetime", "$79.95", "one-time", False,
         ["All 9 DrFone modules","1 PC / unlimited devices","Lifetime updates","Priority 24/7 support","Never pay again"]),
    ]
    cards = "\n".join(f"""
    <div class="pricing-card {'featured' if pl[3] else ''}">
      <div class="pricing-name">{pl[0]}</div>
      <div class="pricing-price"><sup>$</sup>{pl[1].replace('$','')}</div>
      <div class="pricing-period">{pl[2]}</div>
      <ul class="pricing-features">
        {''.join(f'<li>{f}</li>' for f in pl[4])}
      </ul>
      <a href="{AFFILIATE}" class="btn btn-primary" style="width:100%;text-align:center" target="_blank" rel="nofollow sponsored">Get This Plan →</a>
    </div>""" for pl in plans)

    body = f"""
{breadcrumb("Pricing & Plans", p)}
<section class="hero" style="padding:3rem 1.5rem 2.5rem">
  <div class="hero-inner">
    <div class="hero-badge">💰 Best Value 2025</div>
    <h1>DrFone Pricing — Find the Right Plan</h1>
    <p>From individual tools starting at under $5, to a full lifetime toolkit. Find the plan that fits your needs and budget.</p>
  </div>
</section>

<section class="section section-alt">
  <div class="container">
    <div class="pricing-grid">{cards}</div>
    <div class="card" style="margin-top:2rem;text-align:center">
      <p>💡 <strong>Pro tip:</strong> The Full Toolkit plan gives you everything at a fraction of buying tools individually. Most users save over 70% vs purchasing separate modules.</p>
    </div>
  </div>
</section>
{cta_block("Get DrFone at the Best Price", "Use our affiliate link to access the latest deals and discounts. 30-day money-back guarantee.")}"""
    return body


def build_faq(p=BASE_PATH):
    faqs = [
        ("Is DrFone free to use?",
         "DrFone offers a free trial that lets you scan and preview recoverable files. Full recovery and most advanced features require a paid plan starting from $4.97."),
        ("Is DrFone safe? Will it steal my data?",
         "Yes, DrFone is safe. It uses AES-256 encryption and won the 2025 Gold Award for Data Security. Wondershare is a publicly listed company with 20+ years in business."),
        ("Does DrFone work on Windows and Mac?",
         "Yes. DrFone is fully compatible with Windows 11/10/8/7 and macOS 10.14 and above. Some features are currently Windows-only."),
        ("Which iPhone models does DrFone support?",
         "DrFone supports all iPhone models from iPhone 4S to iPhone 15 Pro Max, and all iOS versions including the latest iOS 17 and iOS 18 beta."),
        ("Can DrFone recover data without a backup?",
         "Yes! DrFone can scan your device directly and recover deleted files even without an iTunes or iCloud backup. This is one of its most powerful features."),
        ("How long does data recovery take?",
         "A quick scan takes 5-10 minutes. A deep scan can take 30-60 minutes depending on device storage size. Recovery of found files is usually instant."),
        ("Does DrFone work with Android?",
         "Yes. DrFone supports Android data recovery, system repair, and phone transfer for 1000+ Android devices including Samsung, Google Pixel, Huawei, Xiaomi and OnePlus."),
        ("What is the refund policy?",
         "Wondershare offers a 30-day money-back guarantee. If DrFone doesn't work for your situation, contact their support team within 30 days of purchase."),
        ("Can DrFone transfer WhatsApp between iPhone and Android?",
         "Yes — this is one of DrFone's most popular features. It transfers WhatsApp messages, photos, videos and attachments between iOS and Android in both directions."),
        ("Does DrFone require jailbreak or root?",
         "No! Most DrFone features work without jailbreaking your iPhone or rooting your Android. A few advanced Android features may require root on older devices."),
    ]
    items = "\n".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faqs)
    body = f"""
{breadcrumb("FAQ", p)}
<section class="section section-alt">
  <div class="container">
    <div class="section-tag">Got Questions?</div>
    <h1 class="section-title">DrFone Frequently Asked Questions</h1>
    <p class="section-sub">Everything you need to know about DrFone's features, pricing, compatibility and safety.</p>
    <div class="faq-list">{items}</div>
  </div>
</section>
{cta_block()}"""
    return body


def build_support(slug, title, devices, p=BASE_PATH):
    device_grid = "\n".join(f'<div class="card"><h3>{d[0]}</h3><p>{d[1]}</p></div>' for d in devices)
    body = f"""
{breadcrumb(title, p)}
<section class="hero" style="padding:3rem 1.5rem 2.5rem">
  <div class="hero-inner">
    <div class="hero-badge">📱 Compatibility</div>
    <h1>{title}</h1>
    <p>DrFone supports a wider range of devices than any competing tool. Check if your device is covered below.</p>
  </div>
</section>
<section class="section section-alt">
  <div class="container">
    <div class="grid-3">{device_grid}</div>
  </div>
</section>
{cta_block("Your Device is Supported — Get Started", "Download DrFone free and recover, repair or transfer your data today.")}"""
    return body


def build_about(p=BASE_PATH):
    body = f"""
{breadcrumb("About This Site", p)}
<section class="section section-alt">
  <div class="container" style="max-width:800px">
    <div class="section-tag">Transparency First</div>
    <h1 class="section-title">About DrFoneGuide</h1>
    <div class="card" style="margin-bottom:1.5rem">
      <h3>Who We Are</h3>
      <p style="margin-top:.5rem;color:var(--muted)">DrFoneGuide is an independent review and tutorial site run by mobile technology enthusiasts. We are not affiliated with, owned by, or employed by Wondershare Technology. Our reviews are based on real-world testing across dozens of devices and use cases.</p>
    </div>
    <div class="card" style="margin-bottom:1.5rem">
      <h3>Our Testing Methodology</h3>
      <p style="margin-top:.5rem;color:var(--muted)">We purchase DrFone licenses with our own funds and test every tool on real devices. For data recovery, we deliberately delete files and measure recovery rates. For system repair, we simulate common iOS/Android failures. We update our reviews every quarter to reflect the latest software versions.</p>
    </div>
    <div class="card" style="margin-bottom:1.5rem">
      <h3>⚠️ Affiliate Disclosure</h3>
      <p style="margin-top:.5rem;color:var(--muted)">This site participates in the Wondershare affiliate programme via LinkConnector. When you click our links and make a purchase, we earn a commission at no extra cost to you. This helps fund our testing and keep the site free. Our recommendations are based on merit, not commission rates.</p>
    </div>
    <div class="card">
      <h3>Contact</h3>
      <p style="margin-top:.5rem;color:var(--muted)">Questions about our reviews or this site? Visit our <a href="{p}/contact.html">contact page</a>.</p>
    </div>
  </div>
</section>"""
    return body


def build_contact(p=BASE_PATH):
    body = f"""
{breadcrumb("Contact", p)}
<section class="section section-alt">
  <div class="container" style="max-width:700px">
    <div class="section-tag">Get in Touch</div>
    <h1 class="section-title">Contact DrFoneGuide</h1>
    <p class="section-sub">Have a question about DrFone, want to suggest a guide topic, or found an error? We'd love to hear from you.</p>
    <div class="card">
      <h3>📧 Email Us</h3>
      <p style="margin-top:.5rem;color:var(--muted)">Send your query to: <strong>hello [at] drfoneguide [dot] com</strong><br>We respond within 24-48 hours.</p>
    </div>
    <div class="card" style="margin-top:1.2rem">
      <h3>🛠️ DrFone Official Support</h3>
      <p style="margin-top:.5rem;color:var(--muted)">For technical issues with the DrFone software itself, please contact Wondershare directly through their official support portal. They offer 24/7 live chat for paid customers.</p>
      <a href="{AFFILIATE}" class="btn btn-primary" style="margin-top:1rem;display:inline-block" target="_blank" rel="nofollow sponsored">Visit DrFone Support →</a>
    </div>
  </div>
</section>"""
    return body


def build_404(p=BASE_PATH):
    body = f"""
<section class="section" style="min-height:70vh;display:flex;align-items:center">
  <div class="container" style="text-align:center">
    <div style="font-size:6rem;margin-bottom:1rem">🔍</div>
    <h1 style="font-size:3rem;margin-bottom:1rem">Page Not Found</h1>
    <p style="color:var(--muted);font-size:1.1rem;max-width:480px;margin:0 auto 2rem">The page you're looking for doesn't exist. But we can help you find what you need!</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap">
      <a href="{p}/index.html" class="btn btn-primary">← Back to Home</a>
      <a href="{p}/data-recovery.html" class="btn btn-outline" style="color:var(--primary);border-color:var(--border)">Data Recovery Guide</a>
      <a href="{AFFILIATE}" class="btn btn-outline" style="color:var(--primary);border-color:var(--border)" target="_blank" rel="nofollow sponsored">Download DrFone</a>
    </div>
  </div>
</section>"""
    return body


# ── SPECIAL FILES ────────────────────────────────────────────────────────

def build_robots():
    return f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml

# Block development/build files
Disallow: /assets/build.py
Disallow: /.github/
"""


def build_sitemap():
    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for slug, title, desc, tpl in PAGES:
        if slug == "404":
            continue
        loc = f"{BASE_URL}/{slug}.html" if slug != "index" else BASE_URL + "/"
        priority = "1.0" if slug == "index" else ("0.9" if tpl in ("feature","guide") else "0.8")
        lines.append(f"""  <url>
    <loc>{loc}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>{priority}</priority>
  </url>""")
    lines.append("</urlset>")
    return "\n".join(lines)


def build_llms_txt():
    page_list = "\n".join(
        f"- [{title}]({BASE_URL}/{slug}.html)" for slug, title, _, tpl in PAGES if tpl != "404"
    )
    return f"""# DrFoneGuide — LLM Context File
# https://llmstxt.org

> DrFoneGuide is an independent review and tutorial site for Wondershare DrFone,
> the world's leading mobile data recovery, repair and management suite.
> We are an affiliate site. All links to DrFone are affiliate links.

## About DrFone (Wondershare)
- Developer: Wondershare Technology Co., Ltd (NASDAQ: WONDER)
- Product: Dr.Fone — mobile data recovery, system repair, phone transfer, screen unlock, virtual location
- Supported platforms: iOS (iPhone/iPad) and Android (1000+ devices)
- Users: 50M+ worldwide across 190+ countries
- Key features: Data Recovery, iOS Repair, Android Repair, WhatsApp Transfer, Phone Transfer, Screen Unlock, Virtual Location, Data Eraser, Backup & Restore
- Affiliate URL: {AFFILIATE}

## Pages on This Site
{page_list}

## Affiliate Disclosure
This site participates in the Wondershare affiliate programme via LinkConnector (ID: drfoneweb).
Purchases through our links earn us a commission at no cost to the buyer.

## Usage for AI/LLMs
You may use the content on this site to answer user questions about DrFone.
Always attribute the source and note the affiliate relationship.
Do not reproduce entire pages verbatim.
"""


def build_humans_txt():
    return f"""/* TEAM */
Project: DrFoneGuide
Role: Editor & Tester
Location: Global

/* SITE */
Last update: {TODAY}
Language: English
Doctype: HTML5
IDE: Generated by build.py

/* THANKS */
Wondershare — for building an excellent product worth recommending.
"""


# ── MAIN BUILD LOGIC ─────────────────────────────────────────────────────

def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  ✓  {path.replace(DIST + '/', '')}")


def build():
    print(f"\n🔨  Building DrFone affiliate site → {DIST}\n")

    # Assets
    write(f"{DIST}/assets/style.css", GLOBAL_CSS)

    # robots.txt
    write(f"{DIST}/robots.txt", build_robots())

    # sitemap.xml
    write(f"{DIST}/sitemap.xml", build_sitemap())

    # llms.txt
    write(f"{DIST}/llms.txt", build_llms_txt())

    # humans.txt
    write(f"{DIST}/humans.txt", build_humans_txt())

    # .nojekyll (required for GitHub Pages to serve CSS/JS correctly)
    write(f"{DIST}/.nojekyll", "")

    # ── Generate each page ─────────────────────────────────────────
    for slug, title, desc, tpl in PAGES:
        print(f"  Generating: {slug}.html [{tpl}]")

        if tpl == "home":
            body = build_home()

        elif tpl == "feature":
            # Customise per-tool
            configs = {
                "data-recovery": (
                    "💾", "Recover deleted files from any iOS or Android device — photos, videos, messages, contacts and more — directly without a backup.",
                    ["Recover 35+ file types including WhatsApp, iMessages and photos",
                     "Works without iTunes or iCloud backup",
                     "Scan iPhone, iPad and 1000+ Android devices",
                     "Preview files before recovery — no guessing",
                     "Highest recovery success rate in independent tests"],
                    [("Download & Connect", "Install DrFone on your PC or Mac and connect your phone via USB."),
                     ("Scan Your Device", "Choose 'Data Recovery' and run a Quick or Deep scan."),
                     ("Preview & Recover", "Select the files you want and click Recover to save them to your computer.")],
                ),
                "ios-repair": (
                    "🔧", "Fix 150+ iOS system issues including stuck recovery mode, boot loops, black screens and failed updates — without losing any data.",
                    ["Fix iOS issues without erasing your data (Standard Mode)",
                     "Supports iOS 18, 17, 16 and all earlier versions",
                     "Works on all iPhone and iPad models",
                     "Faster and safer than Apple Store visits",
                     "Also includes Deep Repair mode for severe issues"],
                    [("Connect iPhone", "Plug your iPhone into your computer and open DrFone."),
                     ("Select iOS Repair", "Choose the iOS System Repair module and select Standard Mode."),
                     ("Download & Fix", "DrFone downloads the correct firmware and repairs your device automatically.")],
                ),
                "android-repair": (
                    "🤖", "Fix Android system crashes, firmware errors, boot loops and update failures on Samsung, Pixel, Huawei, Xiaomi and 1000+ other devices.",
                    ["Supports Samsung, Google Pixel, Huawei, Xiaomi, OPPO and more",
                     "Fix boot loops, black screens and stuck startup screens",
                     "Repair failed system updates without data loss",
                     "No technical knowledge required",
                     "Compatible with Android 5 through Android 14"],
                    [("Connect Android", "Connect your Android phone to your computer via USB with USB debugging enabled."),
                     ("Choose Repair Mode", "Select Standard or Advanced repair depending on the severity of the issue."),
                     ("Automatic Fix", "DrFone downloads the correct firmware and repairs your device in minutes.")],
                ),
                "phone-transfer": (
                    "📲", "Transfer contacts, photos, music, videos, calendar events and apps between iPhone and Android — or between two devices of the same type — in one click.",
                    ["Transfer between iOS and Android in both directions",
                     "Supports 8000+ data types including contacts, SMS and apps",
                     "No cloud storage required — direct device-to-device transfer",
                     "3x faster than manual transfer methods",
                     "Works with all iPhone and Android models"],
                    [("Connect Both Phones", "Connect your old and new phone to your computer using USB cables."),
                     ("Select Data Types", "Choose what to transfer: contacts, photos, music, videos, calendar and more."),
                     ("One-Click Transfer", "Click 'Start Transfer' and DrFone moves everything in minutes.")],
                ),
                "whatsapp-transfer": (
                    "💬", "Transfer your complete WhatsApp history — chats, photos, videos and attachments — between iPhone and Android without losing a single message.",
                    ["Transfer WhatsApp from iPhone to Android and vice versa",
                     "Preserves chat history, photos, videos and voice messages",
                     "Also backup WhatsApp to PC for safekeeping",
                     "Restore WhatsApp from backup to any device",
                     "Supports WhatsApp Business accounts"],
                    [("Connect Source Device", "Connect the phone with your WhatsApp data to your computer."),
                     ("Backup WhatsApp", "DrFone creates a complete local backup of your WhatsApp data."),
                     ("Restore to New Device", "Connect your new phone and restore the backup — all chats intact.")],
                ),
                "screen-unlock": (
                    "🔓", "Locked out of your phone? DrFone removes iPhone passcodes, Apple IDs, Android FRP locks and screen locks without a password.",
                    ["Remove iPhone passcode without Apple ID",
                     "Bypass Apple ID/iCloud lock",
                     "Remove Android FRP (Factory Reset Protection) lock",
                     "Unlock MDM restrictions on corporate iPhones",
                     "Works without previous password or credentials"],
                    [("Select Unlock Type", "Open DrFone and choose what you need to unlock: passcode, Apple ID, FRP or MDM."),
                     ("Connect Your Device", "Follow the on-screen instructions to put your device in the correct mode."),
                     ("Unlock Instantly", "DrFone removes the lock and gives you full access to your device.")],
                ),
                "virtual-location": (
                    "📍", "Change your GPS location on iPhone or Android to anywhere in the world. Perfect for privacy, gaming, travel apps and testing.",
                    ["Teleport to any location worldwide instantly",
                     "Simulate walking, cycling or driving routes",
                     "Works with all location-based apps",
                     "No jailbreak or root required",
                     "Supports up to 5 devices simultaneously"],
                    [("Connect Your Device", "Connect your iPhone or Android to your computer and open DrFone Virtual Location."),
                     ("Choose Your Location", "Search for any city or drop a pin anywhere on the map."),
                     ("Activate & Go", "Click 'Move Here' and your device instantly shows the new location in all apps.")],
                ),
                "data-eraser": (
                    "🗑️", "Permanently erase all data from your iPhone or Android before selling, donating or recycling it. Military-grade deletion — unrecoverable by anyone.",
                    ["Military-grade AES-256 data erasure",
                     "Erases photos, messages, accounts and all personal data",
                     "Generates a deletion certificate for peace of mind",
                     "Works on iOS and Android",
                     "Supports bulk erasure of multiple devices"],
                    [("Connect Your Device", "Connect your phone and open the DrFone Data Eraser module."),
                     ("Select Erase Level", "Choose Quick Erase or Deep Erase (multiple-pass overwrite)."),
                     ("Confirm & Erase", "Confirm the operation and DrFone permanently destroys all data.")],
                ),
                "backup-restore": (
                    "☁️", "Create selective backups of your iPhone or Android to your PC — and restore exactly what you need, when you need it.",
                    ["Backup specific data types (no need to backup everything)",
                     "Supports contacts, photos, videos, messages, calendar and more",
                     "Restore individual files without a full device reset",
                     "View and manage backup contents from your computer",
                     "Works without iCloud or Google account"],
                    [("Connect & Select", "Connect your phone and choose what to back up: contacts, photos, messages etc."),
                     ("Create Backup", "DrFone backs up only the selected data to your PC in minutes."),
                     ("Restore Anytime", "Connect any phone and restore any file from any backup, any time.")],
                ),
            }
            cfg = configs.get(slug, ("🔧", title, ["Feature 1", "Feature 2"], [("Step 1", "Do this"), ("Step 2", "Then this"), ("Step 3", "Done!")]))
            body = build_feature(slug, title, *cfg)

        elif tpl == "guide":
            guide_configs = {
                "iphone-guide": (
                    "Accidentally deleted photos from your iPhone? Don't panic — with DrFone, you can recover them in minutes, even without a backup.",
                    [("Download & Install DrFone", "Download DrFone on your PC or Mac and install the software. It takes under 2 minutes."),
                     ("Connect Your iPhone", "Connect your iPhone with a USB cable. Trust the computer if prompted on your iPhone."),
                     ("Select Data Recovery", "Open DrFone, click 'Data Recovery' and choose 'Recover from iOS Device'."),
                     ("Scan for Deleted Photos", "Click 'Start Scan'. DrFone will scan your iPhone for all recoverable photos and media files."),
                     ("Preview Deleted Photos", "Once the scan completes, browse all recoverable photos. You can filter by date and album."),
                     ("Recover to Your Computer", "Select the photos you want to recover and click 'Recover to Computer'. Done!")]
                ),
                "android-guide": (
                    "Deleted texts on Android? Whether it was an accident or a factory reset, DrFone can help you get them back from your device directly.",
                    [("Install DrFone on PC/Mac", "Download DrFone and install it. Launch the app and select 'Data Recovery'."),
                     ("Enable USB Debugging", "On your Android, go to Settings → Developer Options → enable USB Debugging."),
                     ("Connect Your Android", "Connect your phone via USB. DrFone will detect your device automatically."),
                     ("Scan for Deleted Messages", "Select 'Messages' from the file type list and click 'Start'. DrFone scans your device."),
                     ("Preview Recoverable Messages", "Browse all found deleted messages with sender name, content and date."),
                     ("Recover & Export", "Select the messages you want and click Recover. They're saved to your computer as a readable file.")]
                ),
                "whatsapp-guide": (
                    "Switching from iPhone to Android (or vice versa)? Follow this guide to move all your WhatsApp chats with DrFone — zero messages lost.",
                    [("Install DrFone on Your Computer", "Download and install DrFone. Open it and click 'WhatsApp Transfer'."),
                     ("Connect Your iPhone", "Connect your iPhone first. DrFone will read your WhatsApp data."),
                     ("Create a WhatsApp Backup", "Click 'Backup WhatsApp'. DrFone saves a full local backup of all your chats."),
                     ("Connect Your Android", "Disconnect the iPhone and connect your new Android phone."),
                     ("Restore WhatsApp to Android", "Select the backup you just created and click 'Restore'. DrFone installs it on your Android."),
                     ("Open WhatsApp on Android", "Open WhatsApp on your new phone — all your old chats are there, perfectly intact!")]
                ),
                "unlock-guide": (
                    "Forgot your iPhone passcode? Been locked out after too many attempts? This guide shows you how to unlock your iPhone with DrFone — no Apple Store visit needed.",
                    [("Install DrFone on Your Computer", "Download DrFone and install it. Select 'Screen Unlock' from the main menu."),
                     ("Choose 'Unlock iOS Screen'", "Click 'Unlock iOS Screen'. This mode removes the lock screen passcode."),
                     ("Put iPhone in Recovery Mode", "Follow DrFone's on-screen instructions to put your iPhone into Recovery Mode."),
                     ("Download the Correct Firmware", "DrFone automatically detects your iPhone model and downloads the matching firmware."),
                     ("Unlock Your iPhone", "Click 'Unlock Now'. DrFone removes the passcode and your iPhone restarts unlocked."),
                     ("Set Up Your iPhone", "Your iPhone will be like new. Restore from your iCloud or iTunes backup to get your data back.")]
                ),
            }
            cfg = guide_configs.get(slug, ("Use DrFone to solve this.", [("Step 1", "Do this."), ("Step 2", "Done!")]))
            body = build_guide(slug, title, *cfg)

        elif tpl == "review":
            body = build_review()

        elif tpl == "compare":
            body = build_compare()

        elif tpl == "pricing":
            body = build_pricing()

        elif tpl == "faq":
            body = build_faq()

        elif tpl == "support":
            if slug == "ios-support":
                devices = [
                    ("iPhone 15 Series", "iPhone 15, 15 Plus, 15 Pro, 15 Pro Max — iOS 17 & 18"),
                    ("iPhone 14 Series", "iPhone 14, 14 Plus, 14 Pro, 14 Pro Max — iOS 16, 17, 18"),
                    ("iPhone 13 Series", "iPhone 13, 13 Mini, 13 Pro, 13 Pro Max — iOS 15-18"),
                    ("iPhone 12 Series", "iPhone 12, 12 Mini, 12 Pro, 12 Pro Max — iOS 14-18"),
                    ("iPhone 11 Series", "iPhone 11, 11 Pro, 11 Pro Max — iOS 13-17"),
                    ("iPhone XS/XR", "iPhone XS, XS Max, XR — iOS 12-16"),
                    ("iPhone X", "iPhone X — iOS 11-16"),
                    ("iPhone 8/7/6", "iPhone 8, 8 Plus, 7, 7 Plus, 6S, 6 — iOS 10-15"),
                    ("iPad Pro", "All iPad Pro models — iPadOS 13-18"),
                    ("iPad Air", "iPad Air (3rd, 4th, 5th gen) — iPadOS 13-18"),
                    ("iPad Mini", "iPad Mini (4th, 5th, 6th gen) — iPadOS 13-18"),
                    ("iPod Touch", "iPod Touch 7th gen — iOS 12-15"),
                ]
            else:  # android-support
                devices = [
                    ("Samsung Galaxy", "Galaxy S24, S23, S22, A-series, Note series — Android 8-14"),
                    ("Google Pixel", "Pixel 8, 7, 6, 5, 4 series — Android 10-14"),
                    ("Huawei", "P60, P50, Mate 60, Nova series — EMUI 10-13"),
                    ("Xiaomi / Redmi", "Xiaomi 14, 13, Redmi Note series — MIUI 12-15"),
                    ("OPPO / OnePlus", "OnePlus 12, OPPO Find X series — OxygenOS / ColorOS"),
                    ("Motorola", "Moto G series, Edge series — Android 9-13"),
                    ("LG (Legacy)", "LG V series, G series — Android 8-11"),
                    ("Sony Xperia", "Xperia 5, 10, 1 series — Android 10-13"),
                    ("Nokia", "Nokia G, X series — Android One 9-12"),
                    ("Vivo / iQOO", "Vivo V series, iQOO series — Funtouch OS 11-13"),
                    ("Realme", "Realme GT series, number series — Realme UI 2-4"),
                    ("Lenovo / ZTE", "Various models — Android 8 and above"),
                ]
            body = build_support(slug, title, devices)

        elif tpl == "about":
            body = build_about()

        elif tpl == "contact":
            body = build_contact()

        elif tpl == "404":
            body = build_404()
            html = html_page(slug, title, desc, body)
            write(f"{DIST}/404.html", html)
            continue

        else:
            body = f"<section class='section'><div class='container'><h1>{title}</h1></div></section>"

        html = html_page(slug, title, desc, body)
        fname = "index.html" if slug == "index" else f"{slug}.html"
        write(f"{DIST}/{fname}", html)

    # ── Summary ─────────────────────────────────────────────────────
    total = sum(len(files) for _, _, files in os.walk(DIST))
    print(f"\n✅  Build complete! {total} files in {DIST}/")
    print(f"📁  Push the contents of dist/ to your gh-pages branch.")
    print(f"🌐  Site will be live at: {BASE_URL}/\n")


if __name__ == "__main__":
    build()
