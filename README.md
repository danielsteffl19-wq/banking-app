# Banking App

Jednoduchá konzolová bankovní aplikace vytvořená v Pythonu jako portfolio projekt.

Projekt simuluje základní práci s bankovním účtem – vytvoření účtu, přihlášení pomocí PINu, vklady, výběry a historii transakcí.

## Funkce

* vytvoření bankovního účtu
* automatické přidělení čísla účtu
* přihlášení pomocí čísla účtu a PINu
* zobrazení zůstatku
* vklad peněz
* výběr peněz
* historie transakcí
* validace uživatelského vstupu
* automatické ukládání dat do JSON (account.json)
* načtení účtů po restartu aplikace (z account.json)
* barevný výstup v konzoli pomocí ANSI escape sekvencí, pro lepší vizuál i přehlednost

## Technologie

* Python 3
* JSON
* objektově orientované programování (OOP)

## Struktura projektu

```text
banking-app/
├── .gitignore
├── README.md
└── src/
    ├── main.py
    ├── account.py
    └── bank.py
```

## Spuštění

Naklonuj repository:

```bash
git clone https://github.com/danielsteffl19-wq/banking-app
```

Přejdi do projektu:

```bash
cd banking-app
```

Spusť aplikaci:

```bash
python src/main.py
```

## Ukládání dat

Aplikace používá soubor `accounts.json` pro lokální ukládání účtů, zůstatků a historie transakcí.

Soubor `accounts.json` není součástí Git repository, protože obsahuje lokální data aplikace.

## Poznámka k bezpečnosti

Tento projekt je vzdělávací portfolio projekt.

PIN je v současné verzi ukládán lokálně v jednoduchém formátu.

## Aktuální stav

**Version: 1.0.0**

Projekt obsahuje základní funkcionalitu bankovní aplikace a slouží jako základ pro možné budoucí další rozšiřování.