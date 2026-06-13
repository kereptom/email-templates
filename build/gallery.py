# -*- coding: utf-8 -*-
import os, html
from content import ITEMS
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARD = """      <a class="card" href="templates/{slug}/index.html">
        <div class="thumb"><img src="gallery/shots/{nn}.png" alt="{name}" loading="lazy"></div>
        <div class="meta"><div class="name">{name}</div><div class="cap">{subject}</div></div></a>"""
PAGE = """<!doctype html><html lang="cs"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>E-mailové šablony</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Crect width='28' height='20' x='2' y='6' rx='3' fill='%232f6bff'/%3E%3Cpath d='M3 8l13 9 13-9' stroke='white' stroke-width='2.4' fill='none'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#fbfbfd;--card:#fff;--ink:#1d1d1f;--ink2:#6e6e73;--ink3:#86868b;--line:#e6e6eb;--blue:#0071e3}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--ink);font-family:-apple-system,BlinkMacSystemFont,"Inter","Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;line-height:1.47}
.nav{position:sticky;top:0;z-index:50;background:rgba(251,251,253,.82);backdrop-filter:saturate(180%) blur(20px);border-bottom:1px solid var(--line)}
.nav .in{max-width:1200px;margin:0 auto;padding:0 22px;height:52px;display:flex;align-items:center;justify-content:space-between}
.nav .brand{display:flex;align-items:center;gap:10px;font-weight:600;font-size:16px}
.nav .logo{width:20px;height:14px;border-radius:3px;background:#2f6bff}
.nav a{color:var(--ink2);text-decoration:none;font-size:14px}
.wrap{max-width:1200px;margin:0 auto;padding:0 22px}
.hero{text-align:center;padding:92px 0 26px}
.hero h1{font-size:clamp(42px,7vw,84px);font-weight:800;letter-spacing:-.035em;line-height:1.04}
.hero .grad{background:linear-gradient(110deg,#2f6bff,#0e9e8e 42%,#6d4aff 74%,#ef6a2c);-webkit-background-clip:text;background-clip:text;color:transparent}
.hero p{margin:22px auto 0;max-width:640px;font-size:clamp(18px,2.4vw,22px);color:var(--ink2)}
.note{display:inline-flex;gap:8px;margin-top:24px;background:#eaf1ff;color:#22489a;border:1px solid #d3e0fb;border-radius:999px;padding:8px 16px;font-size:13.5px}
.stats{display:flex;justify-content:center;flex-wrap:wrap;gap:34px;margin-top:30px;color:var(--ink2);font-size:14px}
.stats b{display:block;font-size:30px;font-weight:700;color:var(--ink)}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:22px;padding:40px 0}
.card{display:flex;flex-direction:column;background:var(--card);border:1px solid var(--line);border-radius:18px;overflow:hidden;text-decoration:none;color:inherit;transition:transform .22s,box-shadow .22s}
.card:hover{transform:translateY(-6px);box-shadow:0 18px 40px rgba(0,0,0,.10)}
.thumb{height:260px;overflow:hidden;background:#eef1f6;border-bottom:1px solid var(--line)}
.thumb img{width:100%;display:block}
.meta{padding:14px 16px 16px}.name{font-weight:600;font-size:17px}
.cap{color:var(--ink2);font-size:14px;margin-top:3px}
.how{border-top:1px solid var(--line);margin-top:24px;padding:60px 0 70px;text-align:center;color:var(--ink2)}
.how h2{color:var(--ink);font-size:clamp(26px,4vw,36px);font-weight:700;margin-bottom:14px}
.how code{font-family:ui-monospace,Menlo,monospace;font-size:.85em;background:#f0f0f3;border-radius:5px;padding:2px 6px}
.how a{color:var(--blue);text-decoration:none}
footer{border-top:1px solid var(--line);padding:24px 0 50px;color:var(--ink3);font-size:12.5px;text-align:center}
</style></head><body>
<div class="nav"><div class="in"><div class="brand"><span class="logo"></span> E-mailové šablony</div><a href="#how">Jak to použít</a></div></div>
<div class="wrap"><section class="hero"><h1>Data dovnitř.<br><span class="grad">{count} e-mailů ven.</span></h1>
<p>Tabulkové HTML e-maily s inline CSS, web-safe fonty a šířkou 600 px. Funkční v Outlooku i Gmailu.</p>
<div class="note">⚠︎ Ukázkový (dummy) obsah. Texty uprav v <code>build/content.py</code>.</div>
<div class="stats"><div><b>{count}</b>e-mailů</div><div><b>600px</b>tabulkový layout</div><div><b>inline</b>CSS</div><div><b>0</b>závislostí</div></div></section>
<div class="grid">
{cards}
</div>
<section class="how" id="how"><h2>Jak z toho udělat vlastní e-mail</h2>
<p>Každý e-mail je seznam bloků (header, h, p, btn, receipt, stats, code, list, card, signoff). Uprav je v <code>build/content.py</code> a spusť <code>python3 build/build.py</code>.<br>CSS je inline a fonty web-safe, takže HTML pošleš rovnou do rozesílače.</p>
<p style="margin-top:20px"><a href="README.md">README</a> &middot; <a href="https://github.com/kereptom/email-templates">GitHub</a></p></section>
</div>
<footer>E-mailové šablony &middot; tabulkové HTML, inline CSS &middot; ukázkový obsah</footer></body></html>"""
def main():
    cards = [CARD.format(slug=i["slug"], nn=i["slug"].split("-")[0], name=html.escape(i["name"]),
        subject=html.escape(i["subject"])) for i in ITEMS]
    open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8").write(
        PAGE.replace("{cards}", "\n".join(cards)).replace("{count}", str(len(ITEMS))))
    print("wrote index.html", len(cards))
if __name__ == "__main__": main()
