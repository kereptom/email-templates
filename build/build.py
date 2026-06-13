#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""HTML email templates. Table-based, inline CSS, web-safe fonts, 600px,
dark-mode aware. Block-based content. No em dashes."""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TPL = os.path.join(ROOT, "templates")
from content import ITEMS
def e(s): return html.escape(str(s), quote=True)
F = "Arial, Helvetica, sans-serif"

# ---- block renderers: each returns table rows of the 600px inner table ----
def b_header(d, T):
    return (f'<tr><td style="padding:30px 40px 6px"><span style="font:700 21px {F};color:{T["ink"]};letter-spacing:-.3px">'
            f'<span style="display:inline-block;width:16px;height:16px;border-radius:5px;background:{T["accent"]};vertical-align:-2px"></span>&nbsp; {e(d["brand"])}</span></td></tr>')
def b_h(d, T):
    return f'<tr><td style="padding:18px 40px 0"><h1 style="margin:0;font:800 28px {F};color:{T["ink"]};line-height:1.22;letter-spacing:-.5px">{e(d["text"])}</h1></td></tr>'
def b_p(d, T):
    return f'<tr><td style="padding:14px 40px 0"><p style="margin:0;font:400 16px {F};color:{T["muted"]};line-height:1.62">{e(d["text"])}</p></td></tr>'
def b_btn(d, T):
    return (f'<tr><td style="padding:26px 40px 6px"><table role="presentation" cellpadding="0" cellspacing="0"><tr>'
            f'<td style="border-radius:10px;background:{T["accent"]}"><a href="#" style="display:inline-block;padding:14px 30px;font:700 16px {F};color:{T["btnink"]};text-decoration:none;border-radius:10px">{e(d["label"])}</a></td></tr></table></td></tr>')
def b_divider(d, T):
    return f'<tr><td style="padding:26px 40px 0"><div style="height:1px;background:{T["rule"]};line-height:1px">&nbsp;</div></td></tr>'
def b_stats(d, T):
    cells = "".join(f'<td width="33%" align="center" style="padding:8px"><div style="font:800 30px {F};color:{T["accent"]}">{e(n)}</div><div style="font:400 13px {F};color:{T["muted"]};padding-top:4px">{e(l)}</div></td>' for n, l in d["items"])
    return f'<tr><td style="padding:24px 30px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr>{cells}</tr></table></td></tr>'
def b_receipt(d, T):
    rows = "".join(f'<tr><td style="padding:9px 0;font:400 15px {F};color:{T["ink"]};border-bottom:1px solid {T["rule"]}">{e(label)}</td><td align="right" style="padding:9px 0;font:600 15px {F};color:{T["ink"]};border-bottom:1px solid {T["rule"]}">{e(val)}</td></tr>' for label, val in d["rows"])
    rows += f'<tr><td style="padding:14px 0 0;font:800 17px {F};color:{T["ink"]}">{e(d.get("totallabel","Celkem"))}</td><td align="right" style="padding:14px 0 0;font:800 17px {F};color:{T["accent"]}">{e(d["total"])}</td></tr>'
    return f'<tr><td style="padding:22px 40px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0">{rows}</table></td></tr>'
def b_code(d, T):
    return (f'<tr><td style="padding:22px 40px 0" align="center"><div style="display:inline-block;font:700 26px {F};letter-spacing:6px;color:{T["accent"]};background:{T["soft"]};border:2px dashed {T["accent"]};border-radius:12px;padding:16px 30px">{e(d["code"])}</div></td></tr>')
def b_list(d, T):
    items = "".join(f'<tr><td width="26" valign="top" style="padding:6px 0;font:700 15px {F};color:{T["accent"]}">&#10003;</td><td style="padding:6px 0;font:400 15px {F};color:{T["muted"]};line-height:1.5">{e(x)}</td></tr>' for x in d["items"])
    return f'<tr><td style="padding:18px 40px 0"><table role="presentation" cellpadding="0" cellspacing="0">{items}</table></td></tr>'
def b_card(d, T):
    return (f'<tr><td style="padding:20px 40px 0"><table role="presentation" width="100%" cellpadding="0" cellspacing="0"><tr><td style="background:{T["soft"]};border:1px solid {T["rule"]};border-radius:12px;padding:20px 22px">'
            f'<div style="font:700 17px {F};color:{T["ink"]};margin-bottom:5px">{e(d["title"])}</div>'
            f'<div style="font:400 15px {F};color:{T["muted"]};line-height:1.55">{e(d["text"])}</div></td></tr></table></td></tr>')
def b_signoff(d, T):
    return f'<tr><td style="padding:26px 40px 0"><p style="margin:0;font:400 15px {F};color:{T["muted"]}">{e(d.get("text","S pozdravem,"))}<br><strong style="color:{T["ink"]}">{e(d["name"])}</strong>, {e(d.get("role",""))}</p></td></tr>'
def b_spacer(d, T):
    return f'<tr><td style="height:{d.get("h",20)}px;line-height:1px">&nbsp;</td></tr>'

BLK = dict(header=b_header, h=b_h, p=b_p, btn=b_btn, divider=b_divider, stats=b_stats,
    receipt=b_receipt, code=b_code, list=b_list, card=b_card, signoff=b_signoff, spacer=b_spacer)

WRAP = """<!doctype html><html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><meta name="color-scheme" content="light only">
<title>{subject}</title></head>
<body style="margin:0;padding:0;background:{outer};-webkit-text-size-adjust:100%">
<div style="display:none;max-height:0;overflow:hidden;opacity:0">{preheader}</div>
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="background:{outer}"><tr><td align="center" style="padding:30px 16px">
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%;background:{card};border:1px solid {rule};border-radius:16px;overflow:hidden">
{blocks}
<tr><td style="height:34px;line-height:1px">&nbsp;</td></tr>
</table>
<table role="presentation" width="600" cellpadding="0" cellspacing="0" style="max-width:600px;width:100%"><tr><td align="center" style="padding:22px 20px">
<p style="margin:0;font:400 12.5px {F};color:{foot};line-height:1.7">{brand} &middot; {address}<br><a href="#" style="color:{foot};text-decoration:underline">Odhlásit odběr</a> &middot; <a href="#" style="color:{foot};text-decoration:underline">Zobrazit v prohlížeči</a><br>// ukázkový (dummy) e-mail, šablona pro náhled</p>
</td></tr></table>
</td></tr></table>
</body></html>"""

def build_one(it):
    T = it["theme"]
    blocks = "".join(BLK[b["type"]](b, T) for b in it["blocks"])
    p = WRAP.format(lang=it.get("lang", "cs"), subject=e(it["subject"]), preheader=e(it.get("preheader", "")),
        outer=T["outer"], card=T["card"], rule=T["rule"], foot=T["muted"], F=F,
        brand=e(it["brand"]), address=e(it.get("address", "Praha, CZ")), blocks=blocks)
    d = os.path.join(TPL, it["slug"]); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8").write(p)

if __name__ == "__main__":
    for it in ITEMS: build_one(it)
    print("built", len(ITEMS), "emails")
