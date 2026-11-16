
# Redogörelse – Server Inventory Tool

## 1. Tre olika konstruktioner i min kod

I min kod använder jag bland annat if-satser, for-loopar och funktioner med parametrar och return.

Ett exempel på en if-sats finns i `main.py`. Där kontrollerar programmet om en server tillhör produktionsmiljön (prod) innan den tas bort. Om serverns miljö är prod frågar programmet användaren om en bekräftelse. En if-sats används för att kontrollera ett villkor och bestämma vilken kod som ska köras.

I `kontroller.py`, i funktionen `kontrollera_alla()`, använder jag en for-loop. Koden `for server in servrar:` går igenom listan och hämtar en server i taget. Sedan kontrolleras varje server. Loopen gör att jag inte behöver skriva samma kod flera gånger.

Jag använder också en funktion med parameter och return i `kontroller.py`. Funktionen `kontrollera_server(server)` tar emot en server som parameter. Funktionen kontrollerar om servern svarar och returnerar True om servern är uppe och False om den inte är uppe. Med `return` skickas resultatet tillbaka till den kod som anropade funktionen.

## 2. Varför jag använder en lista med dictionaries

Jag använder en lista med dictionaries för att lagra servrarna. En lista passar bra eftersom programmet kan innehålla flera servrar. Varje dictionary innehåller information om en enskild server.

Varje server har nycklarna `namn`, `adress`, `miljo`, `roll`, `status` och `senast_kontrollerad`. Värdena är strängar (str), till exempel servernamnet, adressen och statusen. Även datumet och tiden sparas som en sträng.

Det är enkelt att komma åt och ändra informationen eftersom varje värde har en egen nyckel.

## 3. Varför jag använder JSON och CSV

Jag använder JSON för att spara serverinformationen så att den finns kvar när programmet startas igen. I `lagring.py` använder jag `json.load()` för att läsa information från filen och `json.dump()` för att spara informationen. JSON passar bra eftersom min information består av en lista med dictionaries.

Jag använder CSV när användaren vill exportera en rapport. CSV passar bra för rapporter eftersom filen kan öppnas i exempelvis Excel eller andra kalkylprogram. I funktionen `exportera_csv()` i `lagring.py` skapas en CSV-fil med rubriker och information om servrarna.

## 4. Hur jag har delat upp programmet i moduler och funktioner

Jag har delat upp programmet i flera Python-filer för att varje fil ska ha ett eget ansvar.

- `main.py` är programmets huvudfil. Den hanterar menyn, kommandoradsargument med argparse och startar programmets funktioner.
- `meny.py` innehåller funktionen `lagg_till_server()` som låter användaren lägga till en ny server. Den kontrollerar också att servernamnet inte redan finns och att miljön är giltig.
- `lagring.py` ansvarar för att läsa och spara serverinformation i JSON samt exportera information till CSV.
- `kontroller.py` innehåller funktionerna `kontrollera_server()` och `kontrollera_alla()` som kontrollerar om servrarna svarar.
- `servrar.json` innehåller informationen om servrarna.

Genom att dela upp programmet blir det lättare att läsa, förstå och hitta rätt kod när något behöver ändras.

## 5. Vilka moduler från standardbiblioteket jag använder

Jag använder flera moduler från Pythons standardbibliotek.

- `argparse` används i `main.py` för att hantera kommandoradsargument, till exempel `--lista` och `--kontrollera`.
- `sys` används i `main.py` för att avsluta programmet med rätt exitkod.
- `json` används i `lagring.py` för att läsa och spara serverinformationen.
- `os` används i `lagring.py` för att läsa miljövariabeln `INVENTORY_DATAFIL`.
- `csv` används i `lagring.py` för att skapa CSV-rapporter.
- `datetime` används för att skapa datum och tid när en server kontrolleras och när en rapport skapas.
- `pathlib` används i `lagring.py` för att kontrollera om JSON-filen finns och skapa rapportmappen.
- `subprocess` används i `kontroller.py` för att köra ping-kommandot och kontrollera om en server svarar.

## 6. Tre exempel på god praxis från min kod

Ett exempel på god praxis är att jag har delat upp programmet i olika moduler. Varje fil har ett eget ansvar. Det gör koden lättare att läsa och ändra.

Ett annat exempel är att jag använder tydliga funktionsnamn, till exempel `ladda_servrar()`, `spara_servrar()` och `kontrollera_server()`. Namnen beskriver vad funktionerna gör och gör koden lättare att förstå.

Ett tredje exempel är att jag kontrollerar användarens inmatning när en ny server läggs till. Programmet kontrollerar att miljön är dev, test eller prod och att servernamnet inte redan finns. Det hjälper till att undvika felaktig information i serverlistan.

## 7. Vilka källor och hjälpmedel jag har använt

Jag har använt uppgiftsbeskrivningen för att förstå vad programmet ska innehålla och vilka krav jag behöver uppfylla.

Jag har använt Visual Studio Code för att skriva och ändra min Python-kod. Jag har använt terminalen för att starta programmet och testa funktionerna.

Jag har även använt ChatGPT som hjälp när jag har fastnat, behövt förstå felmeddelanden eller behövt förklaringar av olika delar av Python. Jag har sedan arbetat med koden och testat programmet själv för att kontrollera att funktionerna fungerar.
