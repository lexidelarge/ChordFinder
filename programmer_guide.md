## ChordFinder - programátorská dokumentace
By Alexandra Delarge, 2026


ChordFinder je program, který slouží k rozpoznávání akordů. Uživatel vybere několik kláves a program mu řekne, o jaký akord se jedná.

## Přehled souborů
- main.py - tento soubor je zodpovědný za celou grafickou stránku programu. Vytváří okno s grafickým rozhraním, vykresluje všechny klávesy a tlačítka a aktualizuje text, který se v oknu zobrazuje. Slouží jako prostředník mezi uživatelským vstupem a výstupem a programem logic.py, který řeší hudební teorii, která za problémem rozpoznání akordu stojí.
- logic.py - tento soubor je zodpovědný za veškerou hudební teorii, která je potřeba k rozpoznávání akordů a převod mezi názvy not, kterým rozumí uživatel, a čísly, se kterými umí nakládat program. Program se sestává hlavně z funkcí, které pak dále využívá main.py.
- chordlib.py - tento soubor pouze obsahuje akordy, které program zná. Akordy by mohly teoreticky být součástí logic.py, ale pro přehlednost jsou v odděleném souboru. V dalším textu namísto rozepisování celého názvu budu referovat k tomuto souboru jako "knihovna".

## main.py
Tento soubor je

Poznámka: soubor main.py často využívá funkce z logic.py. Seznamte se s funkcemi z logic.py, abyste porozuměli tomu, jak je využívá main.py

Každá klávesa je řešená jako objekt typu ttk.Button. Při zmáčknutí klávesy se volá funkce toggle_white_key nebo toggle_black_key v závislosti na tom, jestli se jedná o bílou nebo černou klávesu.

### Klíčové funkce
- toggle_white_key(button, note, pressed_keys, verbosity)/toggle_black_key(button, note, pressed_keys, verbosity)

    - V těchto funkcích jsou použité funkce sort_unique_keys a handle_chord ze souboru logic.py.

    - Tyto funkce jsou zodpovědné za všechno, co se stane, když je zmáčknuté bílé/černé tlačítko. Funkce se chovají stejně, liší se pouze tím, že každá z nich formátuje také vzhled příslušné barvy klávesy při stisknutí a uvolnění.
    - Stisknuté bílé klávesy se stanou světle šedé a stisknuté černé klávesy se stanou tmavě šedé. Když je klávesa uvolněna, vrací se ke své původní barvě. Tyto "styly" tlačítek jsou vyřešené v sekci "Keyboard Config".

    - Funkce bere jako parametry v tomto pořadí:
        1) název tlačítka tak jak je definováno v main.py (c1, cs1, ...)
        2) název noty, které tlačítko reprezentuje (C1, C#1, D1, ...)
        3) seznam not, které jsou v tuto dobu stisknuté. Tento seznam pak funkce upraví odebráním nebo přidáním prvku.
        4) verbosity neboli výřečnost funkce. Tento parametr je implicitně nastavený jako True.

    - Když ještě není nota v seznamu pressed_keys, přidá ji to tam a změní její styl na její stisknutou variantu. Panel "Pressed Keys" se náležitě pomocí funkce sort_unique_keys upraví, aby odpovídal stisknutým klávesám.

    - Když nota je v seznamu pressed keys, odebere ji to z něj a změní její styl zpět na nestisklou variantu. Panel "Pressed Keys" se náležitě pomocí funkce sort_unique_keys upraví, aby odpovídal stisknutým klávesám.

    - Při stisknutí i odebrání klávesy se zavolá funkce handle_chord (vizte logic.py), která vrátí název akordu, o který se jedná. Panel "Chord" se pak upraví, aby zobrazoval ten vrácený akord.

    - Parametr "verbosity" ovlivňuje, zda se stisknutí/odebrání kláves vypisuje do konzole. Při normálním stisknutí/uvolnění jedné klávesy se tato událost vypíše.

- reset_button(pressed_keys)

    - Tato funkce je zodpovědná za funkcionalitu tlačítka "Reset".

    - Funkce převezme seznam pressed_keys a "v podstatě zmáčkne" všechny klávesy, které jsou stisknuté, aby je uvolnila pomocí funkcí toggle_white_key a toggle_black_key, čímž se i vyprázdní seznam.
    - Funkce ve skutečnosti prochází kopii seznamu pressed_keys, aby nedocházelo k problému promazávání seznamu během toho, co ho procházíme.

    - Funkce reset_button volá funkce toggle_white_key a toggle_black_key s parametrem "verbosity" jako False, aby se každé jedno uvolnění klávesy nevypisovalo.

## logic.py
Poznámka: soubor logic.py využívá knihovnu chordlib.py, ve které jsou uloženy všechny trojice a čtveřice not, které program rozpoznává jako akordy.

Slovník KEY_TO_NUM slouží k tomu, aby program mohl jednoduše přecházet od not k číslům a seznam NUM_TO_KEY naopak slouží k přechodu od čísel k notám.

### Klíčové funkce

- sort_keys(keys)

    - Funkce k přeuspořádání seznamu sorted_keys k vypsání do konzole při stisknutí/uvolnění klávesy. Tato funkce řadí klávesy podle pořadí v oktávě a také podle oktávy.
    - Tato funkce bere jako vstup seznam kláves. Soubor main.py ji využívá tak, že ji předá seznam kláves, které jsou momentálně stisknuté, a tato funkce vrátí seřazený seznam not včetně oktáv (např. C1, G#1, E2, A2, C3).

    - Nejdříve se vypočítá "hodnota" samotného názvu noty pomocí slovníku KEY_TO_NUM.
    - Jelikož oktáva má 12 půltónů, za každou oktávu se k "hodnotě" připočte 12.
    - Seznam temporary_tuples, který obsahuje dvojice proměnné val a názvu klíče, se pak seřadí podle proměnné val (která uchovává výše zmíněnou "hodnotu" noty).
    - Celkový seřazený seznam not se pak sestaví jako seznam druhých položek v seznamu temporary_tuples.

- sort_unique_keys(keys)

    - Funkce, která ze všech stisknutých kláves vezme každou notu jen jednou i když je stisklá ve více oktávách (tj. C1, C2 a C3 jsou všechny jedno a to samé C z pohledu této funkce) a vrátí seřazený seznam zahraných not.
    - Tato funkce bere jako vstup seznam kláves. Soubor main.py tuto funkci využívá tak, že ji předá seznam kláves, které jsou momentálně stisknuté, a funkce vrací seřazený seznam not, které jsou stisknuté (jako např. C, F, G#).
    - Tato funkce se jednak využívá k vypsání not k panelu "Pressed Keys" v okně programu a jednak se tento seznam dále předává funkci, která vyhodnocuje akord.


    - Podobně jako funkce sort_keys, tato funkce převede název noty na číselnou hodnotu pomocí slovníku KEY_TO_NUM, sestaví seznam temporary_tuples, který uchovává číselnou hodnotu noty (bez oktávy), který se pak seřadí podle číselné hodnoty noty.
    - Celkový seřazený seznam se pak sestaví jako seznam druhých položek v seznamu temporary_tuples.

- handle_chord (unique_keys)

    - Funkce, kterou volá main.py při stisknutí/odebrání klávesy, aby byl zjištěn akord.
    - Jako vstup bere seznam kláves, který byl seřazen pomocí funkce sort_unique_keys.

    - Pokud má seznam právě 3 noty, deleguje svou práci funkci three_note_chord. Pokud má seznam právě 4 noty, deleguje svou práci funkci four_note_chord.
    - Pokud má seznam jiný počet not než 3 nebo 4, rovnou funkce vrátí string "N.C.".

- three_note_chord(keys)/four_note_chord(keys)
    - Obě funkce fungují "v podstatě" stejným způsobem, jenom jedna z nich je určena na zpracovávání akordů o 3 notách a druhá akordů o 4 notách. 

    - Na začátku si funkce pomocí slovníku KEY_TO_NUM převede noty na čísla a uloží si jej do seznamu converted.
    - Protože noty už jsou seřazené pomocí funkce sort_unique_keys, první nota v seznamu má určitě nejnižší hodnotu.
    - Díky tomu si funkce vybere jako "hlavní notu" akordu první notu, co je v seznamu. Číslo hlavní noty je uchované v proměnné root_note.
    - Funkce pak odečte od všech not v seznamu hodnotu v proměnné root_note. Důvodem pro toto je to, že akordy v knihovně jsou uložené tak, jak vypadají, když mají jako svou "hlavní notu" C. Tímto odečtením je pak seznam v takovém tvaru, že odpovídá způsobu, jak jsou akordy zapsané v knihovně.

    - Funkce pak zkontroluje, zda tento upravený seznam je v knihovně akordů. Pokud ano, funkce vrátí název akordu.
    - Jestli tento seznam není v knihovně akordů, funkce se bude snažit "otočit" seznam. Druhá nota v seznamu se nyní stane hlavní notou, a čísla v seznamu se změní tak, aby hlavní nota měla číslo 0 a ostatní čísla udávala počet půltónů, o kolik jsou dané noty vzdáleny nahoru od hlavní noty

    - Jestli po příslušném počtu opakování tohoto procesu funkce nenašla shodu, vrátí string "N.C."

    - Tento způsob kontrolování je hlavní příčinou problému s nejednoznačností akordu, o kterém se zmiňuje uživatelská dokumentace. Například trojice C, D, G by mohla být akord Csus2 nebo Gsus4. Jelikož funkce začne kontrolovat od C, neboť C je první nota v pořadí, najde rovnou shodu s akordem sus2. Ta interpretace, která byla zkontrolována jako první, tak "vyhraje" a dále už program nehledá, i když by našel shodu s akordem sus4, kdyby uvažoval G jako hlavní notu. Tento problém by se dal vyřešit úpravou funkcí tak, aby např. ukládala všechny nalezené shody do nějakého seznamu a pak je vrátila všechny. Tento problém by se také dal rozseknout tak, že by program považoval jako kořen nejnižší notu v akordu.


## chordlib.py
Jedná se pouze o jednoduchou knihovnu, kde jsou ve slovnících uloženy různé akordy, které program zná. Tento soubor je především využíván souborem logic.py

## Další práce na projektu
- Přidání dalších akordů do chordlib.py. Funkce three_note_chord a four_note_chord si dokážou poradit s akordy o třech a čtyřech notách samy a nebylo by tak třeba tyto funkce upravovat.
- Přidání rozeznání akordů, které mají jiný počet akordů než 3 nebo 4 (např. nonový akord, power chord, ...)
- Možné ovládání klávesnicí - např. tlačítko Reset by se mohlo dát naprogramovat tak, aby šlo ovládat pomocí mezerníku
- Náhradní "nejbližší shoda" - Funkce three_note_chord a four_note_chord při nenalezení shody vrací "N.C.". Místo toho by mohla např. vracet nějakou nejbližší shodu. K tomu by bylo třeba naprogramovat funkci, která hodnotí, jak moc "blízko" je nějaký akord jinému.
- Problém nejednoznačnosti akordu - Vizte problém, který je popsán výše v sekci logic.py.
- Přehrávání zvuku - Při stisknutí klávesy by se mohl přehrát příslušný zvuk. Momentálně má program pouze vizuální a textový výstup.