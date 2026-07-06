## ChordFinder - uživatelská dokumentace
By Alexandra Delarge

Program ChordFinder slouží k rozpoznávání akordů zahraných na virtuální piano. Stiskněte klávesy, které chcete zahrát, a program Vám řekne, jaký akord jste vytvořili.

## Spuštění programu
1. Ujistěte se, že máte správně stažené všechny soubory, které jsou součástí tohoto programu. (main.py, logic.py, chordlib.py)
2. Spusťte program main.py
3. Otevře se okno, na kterém jsou zobrazené celkem 3 oktávy kláves na pianu, včetně jejich popisků, pole "Pressed Keys" (stisknuté klávesy), pole "Chord" (akord) a tlačítka "Reset".

## Hraní not
- kliknutím na klávesu ji stisknete. Po stisknutí změní barvu, čímž lze poznat, že je aktivní.
    - Bílé klávesy po stisknutí změní barvu na světle šedou
    - Černé klávesy po stisknutí změní barvu na tmavě šedou
- odpovídající název noty se přidá do pole "Pressed Keys". Každá nota se tam přidá jen jednou, tj. když stisknete dvě klávesy C, bude v poli jenom jednou C. Provedená akce se pak také vypíše do konzole.
- kliknutím na klávesu, která už je stisklá, ji uvolníte. Vrátí se ke své původní barvě, a pokud není stisklá žádná stejná nota v jiné oktávě, její název se smaže z pole "Pressed Keys".
- můžete stisknout více kláves najednou - klávesy zůstávají stisknuté, dokud je buď neuvolníte ručně, nebo nezmáčknete tlačítko "Reset".

## Vyhodnocení akordu
- Jakmile stisknete dostatečné množství not, program se bude snažit akord vyhodnotit.
- Tento program uvažuje pouze některé akordy o 3 nebo 4 notách, přestože existují i např. "power chords", které mají pouze 2 noty. Vizte seznam akordů níže.
- V poli "Chord" se vypíše příslušný akord, jestliže ho program rozpoznal.
- Jestli je zmáčknuto moc anebo málo not anebo se nejedná o žádný akord, který je programu znám, v poli "Chord" je napsáno "N.C." (z anglického "no chord")

- Pozor: Jestliže existuje teoreticky více možných akordů, které by mohly odpovídat zvoleným notám, program najde pouze jeden z nich. Příkladem jsou noty C, D, G. Může se jednat o akord Csus2, ale také o akord Gsus4. Program vyhodnocuje akordy od první noty v pořadí (C, C#, D, ...), takže v tomto konkrétním případě by program řekl, že se jedná o akord Csus2. (tento problém bude lépe vysvětlen v programátorské dokumentaci)

## Programu jsou známy následující akordy:
- durový akord (major)
- mollový akord (minor)
- sus akordy (sus2, sus4)
- zmenšený akord (dim)
- zvětšený akord (aug)
- velký septakord (maj)
- malý mollový septakord (-7)
- dominantní septakord (7)



## Tlačítko Reset
- kliknutím na tlačítko Reset uvolníte všechny klávesy najednou. Vyprázdní se pole "Pressed Keys" a pole Chord se vrátí do stavu "N.C.". Všechny klávesy na klaviatuře se rovněž vrátí do svého nestisknutého stavu.

## Poznámky
- Stisknutí stejné noty v různých oktávách se považuje za stejnou notu - k akordu se tak nic nepřidá ani se od něj nic neubere, i když by to na skutečném pianu vytvořilo "širší" zvuk.
- Program se ovládá pouze myší (nepodporuje žádné klávesové zkratky).