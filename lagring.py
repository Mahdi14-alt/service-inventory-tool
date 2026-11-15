import json
import os
import csv
from datetime import datetime
from pathlib import Path

def hamta_filnamn():
    return os.getenv("INVENTORY_DATAFIL", "servrar.json")

def ladda_servrar():
    filnamn = hamta_filnamn()

    if Path(filnamn).exists():
        with open(filnamn, "r", encoding="utf-8") as fil:
            return json.load(fil)
    return []

def spara_servrar(servrar):
    filnamn = hamta_filnamn()

    with open(filnamn, "w", encoding="utf-8") as fil:
        json.dump(servrar, fil, indent=4, ensure_ascii=False)

def exportera_csv(servrar):
    Path("rapporter").mkdir(exist_ok=True)

    tid = datetime.now() .strftime("%Y-%m-%d_%H-%M")
    filnamn = f"rapporter/servrar_{tid}.csv"

    falt = [
        "namn",
        "adress",
        "miljo",
        "roll",
        "status",
        "senast_kontrollerad"

    ]

    with open(filnamn, "w", newline="", encoding="utf-8") as fil:
        skrivare = csv.DictWriter(fil, fieldnames=falt)
        skrivare.writeheader()
        skrivare.writerows(servrar)

    print("CSV-rapport skapad:", filnamn)
    
        