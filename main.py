import argparse
import sys
from meny import meny, visa_servrar
from lagring import ladda_servrar, spara_servrar, exportera_csv
from kontroller import kontrollera_server, kontrollera_alla

# Skapar argument för att kunna köra programmet i Terminalen
def skapa_parser():
    parser = argparse.ArgumentParser(description="Server Inventory Tool")


    parser.add_argument("--lista", action="store_true")
    parser.add_argument("--miljo")
    parser.add_argument("--kontrollera")
    parser.add_argument("--kontrollera-alla", action="store_true")
    parser.add_argument("--export", action="store_true")

    return parser


# Startar programmet och hanterar CLI-kommandon                
def starta_program():
    servrar = ladda_servrar()

    parser = skapa_parser()
    args = parser.parse_args()

    if args.lista:
        if args.miljo:
            filtrerade_servrar = []

            for server in servrar:
                if server["miljo"] == args.miljo:
                    filtrerade_servrar.append(server)

            visa_servrar(filtrerade_servrar)
        else:
            visa_servrar(servrar)

    elif args.kontrollera:
        hittad = False

        for server in servrar:
            if server["namn"] == args.kontrollera:
                svarar= kontrollera_server(server)
                spara_servrar(servrar)
                hittad = True
                if not svarar:
                    return 1
                break

        if not hittad:
            print("Servern finns inte")
            return 1
    elif args.kontrollera_alla:
        alla_uppe = kontrollera_alla(servrar)
        spara_servrar(servrar)

        if not alla_uppe:
            return 1

       
    elif args.export:
        exportera_csv(servrar)

    else:
        meny(servrar)

    return 0
        
if __name__ == "__main__":
    sys.exit(starta_program())

