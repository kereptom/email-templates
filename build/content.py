# -*- coding: utf-8 -*-
# Sample (dummy) emails. em dash forbidden.
def T(accent, soft, outer="#eef1f6"):
    return dict(accent=accent, btnink="#ffffff", ink="#14161d", muted="#5a6273",
                card="#ffffff", outer=outer, rule="#e6eaf1", soft=soft)
BLUE = T("#2f6bff", "#eef3ff"); GREEN = T("#0e9e8e", "#e7f6f4"); VIOLET = T("#6d4aff", "#f0edff")
ORANGE = T("#ef6a2c", "#fdf0e8"); PINK = T("#e0249a", "#fdeaf5"); TEAL = T("#1599c4", "#e6f5fb")
AMBER = T("#c8862a", "#fbf2e2")

ITEMS = [
 dict(slug="01-welcome", name="Uvítací e-mail", subject="Vítejte na palubě!", preheader="Pojďme vás rozjet ve třech krocích.", brand="Značka", theme=BLUE, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Vítejte! Jsme rádi, že jste tu."),
   dict(type="p", text="Děkujeme za registraci. Připravili jsme pár kroků, aby vám to hned začalo dávat smysl."),
   dict(type="btn", label="Dokončit nastavení"), dict(type="divider"),
   dict(type="list", items=["Propojte svá data za dvě minuty","Pozvěte kolegy do týmu","Spusťte první report"]),
   dict(type="signoff", name="Tým Značky", role="zákaznická péče")]),

 dict(slug="02-newsletter", name="Newsletter", subject="Co je nového tento měsíc", preheader="Tři novinky, které stojí za přečtení.", brand="Značka", theme=GREEN, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Novinky za červen"),
   dict(type="p", text="Krátké shrnutí toho nejdůležitějšího. Klikněte na téma, které vás zajímá."),
   dict(type="card", title="Nová funkce: automatické reporty", text="Ušetřete hodiny týdně, sestaví se samy."),
   dict(type="card", title="Případovka: jak firma X zrychlila o 40 %", text="Konkrétní čísla a postup krok za krokem."),
   dict(type="btn", label="Číst celé vydání")]),

 dict(slug="03-receipt", name="Potvrzení platby", subject="Vaše potvrzení o platbě", preheader="Děkujeme za nákup.", brand="Značka", theme=BLUE, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Děkujeme za platbu"),
   dict(type="p", text="Tady je rekapitulace vaší objednávky č. 2026-0419."),
   dict(type="receipt", rows=[["Roční plán Tým","3 588 Kč"],["Sleva (PODZIM40)","-1 435 Kč"],["DPH 21 %","452 Kč"]], total="2 605 Kč", totallabel="Celkem s DPH"),
   dict(type="p", text="Doklad najdete také ve svém účtu. Potřebujete fakturu na firmu? Stačí napsat.")]),

 dict(slug="04-event-invite", name="Pozvánka na akci", subject="Pozvánka: AI workshop 19. 6.", preheader="Praktický den pro vedení a klíčové role.", brand="Značka", theme=VIOLET, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Zveme vás na AI workshop"),
   dict(type="p", text="Praktický den o tom, co AI dnes umí a kde firmě reálně pomůže."),
   dict(type="card", title="Kdy a kde", text="19. června, 9:00, Vinohradská, Praha"),
   dict(type="btn", label="Potvrdit účast"),
   dict(type="list", items=["Dopoledne: krajina nástrojů a agenti","Odpoledne: nasazení a bezpečnost","Po celý den: živé ukázky"])]),

 dict(slug="05-password-reset", name="Obnova hesla", subject="Obnovení hesla", preheader="Odkaz platí 60 minut.", brand="Značka", theme=TEAL, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Obnovení hesla"),
   dict(type="p", text="Dostali jsme žádost o obnovení hesla. Klikněte na tlačítko níže, odkaz platí 60 minut."),
   dict(type="btn", label="Nastavit nové heslo"),
   dict(type="p", text="Pokud jste o obnovení nežádali, tento e-mail klidně ignorujte. Vaše heslo zůstává beze změny.")]),

 dict(slug="06-announce", name="Oznámení produktu", subject="Verze 2.0 je tady", preheader="Rychlejší, chytřejší, vaše.", brand="Značka", theme=ORANGE, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Největší aktualizace v historii"),
   dict(type="p", text="Verze 2.0 přináší rychlost, nové reporty a klid na práci."),
   dict(type="stats", items=[["3x","rychlejší"],["+12","nových funkcí"],["0 Kč","pro stávající"]]),
   dict(type="btn", label="Co je nového")]),

 dict(slug="07-digest", name="Týdenní přehled", subject="Váš týdenní přehled", preheader="Pět věcí, které jste možná minuli.", brand="Značka", theme=GREEN, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Co se stalo tento týden"),
   dict(type="list", items=["Přibylo 320 nových registrací","Spustili jsme integraci s kalendářem","Nejčtenější článek: jak psát zadání","Webinář ve čtvrtek, ještě jsou místa","Tip týdne: zkratky, které ušetří čas"]),
   dict(type="divider"), dict(type="btn", label="Otevřít nástěnku")]),

 dict(slug="08-abandoned-cart", name="Opuštěný košík", subject="Něco vám zůstalo v košíku", preheader="Dokončete objednávku, držíme vám ji.", brand="Značka", theme=PINK, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Zapomněli jste na něco?"),
   dict(type="p", text="Necháváme vám košík připravený. Stačí dokončit objednávku."),
   dict(type="card", title="Roční plán Tým", text="3 588 Kč / rok &middot; 25 uživatelů &middot; přednostní podpora"),
   dict(type="btn", label="Dokončit objednávku")]),

 dict(slug="09-survey", name="Žádost o zpětnou vazbu", subject="Máte dvě minuty?", preheader="Vaše názory nám pomáhají.", brand="Značka", theme=VIOLET, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Jak se vám u nás daří?"),
   dict(type="p", text="Krátký dotazník na dvě minuty. Každá odpověď nám pomůže zlepšit se."),
   dict(type="btn", label="Vyplnit dotazník"),
   dict(type="p", text="Jako poděkování vám pošleme slevový kód na další období.")]),

 dict(slug="10-shipped", name="Odesláno", subject="Vaše objednávka je na cestě", preheader="Sledujte zásilku v reálném čase.", brand="Značka", theme=TEAL, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Objednávka je na cestě"),
   dict(type="p", text="Zabalili jsme a předali přepravci. Doručení čekejte do dvou pracovních dnů."),
   dict(type="card", title="Sledovací číslo", text="CZ 1234 5678 9 &middot; přepravce Ukázka"),
   dict(type="btn", label="Sledovat zásilku")]),

 dict(slug="11-webinar-reminder", name="Připomínka webináře", subject="Začínáme za hodinu", preheader="Připojte se jedním kliknutím.", brand="Značka", theme=BLUE, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Webinář začíná za hodinu"),
   dict(type="p", text="Těšíme se na vás. Připojit se můžete jedním kliknutím, není potřeba nic instalovat."),
   dict(type="card", title="Automatizace bez kódu", text="Dnes 18:00 &middot; online &middot; záznam dostanete e-mailem"),
   dict(type="btn", label="Připojit se")]),

 dict(slug="12-discount", name="Slevový kód", subject="Dárek pro vás: sleva 40 %", preheader="Platí 48 hodin.", brand="Značka", theme=ORANGE, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Máme pro vás slevu"),
   dict(type="p", text="Použijte kód u pokladny a získejte 40 % na roční plán. Platí 48 hodin."),
   dict(type="code", code="PODZIM40"), dict(type="btn", label="Uplatnit kód")]),

 dict(slug="13-monthly-report", name="Měsíční report", subject="Váš report za červen", preheader="Čísla, která se počítají.", brand="Značka", theme=GREEN, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Report za červen"),
   dict(type="stats", items=[["+24 %","růst"],["1 240","aktivních"],["4,9","hodnocení"]]),
   dict(type="divider"), dict(type="list", items=["Nejlepší den: 18. června","Nejčtenější obsah: návod na reporty","Doporučení: zapněte týdenní souhrn"]),
   dict(type="btn", label="Otevřít plný report")]),

 dict(slug="14-reengage", name="Reaktivace", subject="Chybíte nám", preheader="Vraťte se, máme novinky.", brand="Značka", theme=PINK, blocks=[
   dict(type="header", brand="Značka"), dict(type="h", text="Dlouho jsme se neviděli"),
   dict(type="p", text="Od vaší poslední návštěvy přibylo dost novinek. Mrkněte, co je nového, ať vám nic neuteče."),
   dict(type="btn", label="Vrátit se zpět"),
   dict(type="p", text="Nechcete už e-maily? Rozumíme, odhlásit se můžete dole jedním kliknutím.")]),
]
