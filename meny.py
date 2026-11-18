from lagring import spara_servrar, exportera_csv
from kontroller import kontrollera_server, kontrollera_alla

# Lägger till en server
def lagg_till_server(servrar):

    namn=input ("Servername: ")

    for server in servrar:
        if server["namn"] == namn:
            print("servern finns redan!")
            return

    adress = input("address: ")

    miljo = input("MiljÖ (dev/test/prod): ")

    while True:
       if miljo in ["dev","test","prod"]:
          break
       print("Försök igen. Fel miljö")
       miljo = input("Miljö (dev/test/prod: )")

    roll=input("Roll: ")

    ny_server = {
           "namn": namn,
           "adress": adress,
           "miljo": miljo,
           "roll": roll,
           "status": "unknown",
           "senast_kontrollerad": ""


       }
    servrar.append(ny_server)
    print("server har lagts till! ")

# Visar alla servrar med deras information
def visa_servrar(servrar):
    print(f"{'Namn':<15} {'Adress':<20} {'Miljö':<10} {'Roll':<20} {'Status':<10}")
    print("-" * 80)
    
    for server in servrar:
        print(f"{server['namn']:<15} {server['adress']:<20} {server['miljo']:<10} {server['roll']:<20} {server['status']:<10}")
# Textmeny
def meny(servrar):
        while True:
            print("\n--- SERVER INVENTORY TOOL. ---")
            print("1. Visa alla servrar")
            print("2. Visa servrar i en viss miljö")
            print("3. Lägg till server")
            print("4. Ta bort server")
            print("5. Kontrollera en server")
            print("6. Kontrollera alla servrar")
            print("7. Exportera CSV")
            print("8. Avsluta")

            val = input("Välj ett alternativ: ")

            # Hanterar användarens val
            if val == "1":
                visa_servrar(servrar)

            elif val == "2":
                miljo = input("Ange miljö (dev/test/prod)")

                for server in servrar:
                    if server["miljo"] == miljo:
                        print(server["namn"], server["adress"],
                          server["miljo"], server["roll"], server["status"])

            elif val == "3":
                lagg_till_server(servrar)
                spara_servrar(servrar)

            elif val == "4":
                namn = input("Ange namnet på servern du vill ta bort: ")
                hittad = False

                for server in servrar:
                    if server["namn"] == namn:

                        if server["miljo"] == "prod":
                            svar = input("Servern är prod. Vill du verkligen ta bort den? (ja/nej): ")

                            if svar != "ja":
                                print("Borttagningen avbruten!")
                                hittad = True
                                break

                        servrar.remove(server)
                        hittad = True
                        print("Servern har tagits bort!")
                        break

                if hittad:
                    spara_servrar(servrar)
                else:
                    print("Servern finns inte")  

            elif val == "5":
                namn = input("Ange namnet på servern du vill kontrollera: ")

                hittad = False

                for server in servrar:
                    if server["namn"] == namn:
                        kontrollera_server(server)
                        spara_servrar(servrar)
                        hittad = True
                        break

                if not hittad:
                        print("Server finns inte")

            elif val == "6":
                kontrollera_alla(servrar)
                spara_servrar(servrar)

            elif val == "7":
                exportera_csv(servrar)

            elif val == "8":
                print("programmet avslutas!")
                break

            else:
                print("Fel val. Försök igen.")

    
                    


