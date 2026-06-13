# E-mailové šablony

Knihovna **14 HTML e-mailů**: tabulkový layout, inline CSS, web-safe fonty,
šířka 600 px. Cílené na reálné e-mailové klienty (Outlook, Gmail). Každý e-mail
je samostatný HTML soubor, který lze rovnou vložit do rozesílače.

> Obsahuje **ukázkový (dummy) obsah**. Před použitím nahraď vlastním.

Živá galerie: `index.html`.

## Typy
uvítací, newsletter, potvrzení platby (receipt), pozvánka na akci, obnova hesla,
oznámení produktu, týdenní přehled, opuštěný košík, dotazník, odesláno,
připomínka webináře, slevový kód, měsíční report, reaktivace.

## Jak to funguje
Každý e-mail je seznam **bloků**: `header, h, p, btn, divider, stats, receipt,
code, list, card, signoff, spacer`. Render do tabulkového HTML s inline styly je
v `build/build.py`. Obsah a barvy jsou v `build/content.py`.

## Použití
1. Uprav e-mail v `build/content.py` (bloky a `theme`).
2. `python3 build/build.py`. Galerie: `python3 build/gallery.py`.
3. Náhledy: `node ../21_ai_academia/...` nebo libovolný screenshot nástroj.

## Pravidla
Inline CSS (žádné externí styly), web-safe fonty, 600 px kontejner. Nikdy znak
dlouhé pomlčky (em dash). Nasazení `vercel deploy --prod`.
