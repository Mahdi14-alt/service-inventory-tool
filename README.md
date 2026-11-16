# service-inventory-tool


## 1. Beskrivning
Server Inventory Tool är ett Python-program som används för att hantera servrar.

Med programmet kan man:
- Visa alla servrar.
- Visa servrar i en viss miljö.
- Lägga till servrar.
- Ta bort servrar.
- Kontrollera om en server svarar.
- Kontrollera alla servrar.
- Exportera serverinformation till CSV.

Serverinformationen sparas i filen servrar.json.

## 2. Vad krävs för att köra programmet?
För att köra programmet behöver man:
- Python 3.
- Projektets Python-filer.


## 3. Hur startar man programmet?

### Interaktivt läge
För att starta menyn skriver man:

```bash
python3 main.py
```

Då visas programmets meny med åtta alternativ.

### Kommandoradsläge
Programmet kan också startas med argument.

Visa alla servrar:

```bash
python3 main.py --lista
```

Visa servrar i prod:

```bash
python3 main.py --lista --miljo prod
```

Kontrollera en server:

```bash
python3 main.py --kontrollera web01
```

Kontrollera alla servrar:

```bash
python3 main.py --kontrollera-alla
```

Exportera CSV:

```bash
python3 main.py --export
```

Visa hjälp:

```bash
python3 main.py --help
```

## 4. Miljövariabel
Programmet använder miljövariabeln INVENTORY_DATAFIL för att välja vilken JSON-fil som ska användas.

Om miljövariabeln inte anges används servrar.json.

Exempel:

```bash
INVENTORY_DATAFIL=mina_servrar.json python3 main.py --lista
```

## 5. Projektets uppbyggnad

- main.py – programmets huvudfil och meny.
- meny.py – hanterar funktionen för att lägga till servrar.
- lagring.py – läser och sparar serverinformation samt exporterar CSV.
- kontroller.py – kontrollerar om servrar svarar.
- servrar.json – innehåller serverinformationen.
- .gitignore – anger vilka filer och mappar Git ska ignorera.
- README.md – dokumentation för projektet.
- REDOGORELSE.md – redogörelse för arbetet med uppgiften.
