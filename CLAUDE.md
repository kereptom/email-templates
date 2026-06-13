# CLAUDE.md  (read this first, then stop)

Knihovna 14 tabulkových HTML e-mailů (inline CSS). Tahle stránka je celý kontext.

## Jak to funguje
- `templates/NN-slug/index.html` = hotový e-mail (vygenerováno), NEEDITUJ ručně.
- Zdroj pravdy: `build/build.py` (block renderery `b_<name>`, vše inline) a
  `build/content.py` (seznam `ITEMS`, presety témat nahoře, e-mail = seznam bloků).
- Build: `python3 build/build.py`. Galerie: `python3 build/gallery.py`.

## Nejčastější úkol: upravit jeden e-mail
1. Najdi `NN` v tabulce dole.
2. Uprav jeho `dict(...)` v `build/content.py` (pole `blocks` a `theme`).
   Typy bloků: header, h, p, btn, divider, stats, receipt, code, list, card,
   signoff, spacer. Tvar dat bloku odpovídá `b_<type>` v `build/build.py`.
3. `python3 build/build.py`. Hotovo.
4. Deploy jen na vyžádání: `vercel deploy --prod --yes`.
   Web: https://31emailtemplates.vercel.app  GitHub: kereptom/email-templates

## Co NEČÍST: jiné projekty, templates/ ručně.
## Pravidla: dummy obsah; nikdy em dash (U+2014); CSS jen inline, web-safe fonty, 600 px.

## Index (NN -> slug -> typ)

| NN | slug | typ |
|----|------|-----|
| 01 | `01-welcome` | uvítací |
| 02 | `02-newsletter` | newsletter |
| 03 | `03-receipt` | potvrzení platby |
| 04 | `04-event-invite` | pozvánka na akci |
| 05 | `05-password-reset` | obnova hesla |
| 06 | `06-announce` | oznámení produktu |
| 07 | `07-digest` | týdenní přehled |
| 08 | `08-abandoned-cart` | opuštěný košík |
| 09 | `09-survey` | dotazník |
| 10 | `10-shipped` | odesláno |
| 11 | `11-webinar-reminder` | připomínka webináře |
| 12 | `12-discount` | slevový kód |
| 13 | `13-monthly-report` | měsíční report |
| 14 | `14-reengage` | reaktivace |
