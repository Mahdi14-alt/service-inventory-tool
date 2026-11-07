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

    
                    


