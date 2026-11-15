import subprocess
from datetime import datetime

def kontrollera_server(server):
    
    try:
        resultat = subprocess.run(
            ["ping", "-c", "1", server["adress"]],
            capture_output = True,
            timeout=5
        )
        if resultat.returncode == 0:
            server["status"] = "up"
            print(server["namn"], "svarar! ")
        else: 
            server["status"] = "down"
            print(server["namn"], "svarar inte! ")

    except subprocess.TimeoutExpired:
        server["status"] = "down"
        print(server["namn"], "svarar inte")

    server["senast_kontrollerad"] = datetime.now() .strftime("%Y-%m-%d %H:%M")

    return server["status"] == "up"

def kontrollera_alla(servrar):

    alla_uppe = True

    for server in servrar:
        if not kontrollera_server(server):
            alla_uppe = False

    return alla_uppe
