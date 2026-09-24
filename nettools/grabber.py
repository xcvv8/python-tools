import requests



def grab_header(ziel):
    if not ziel.startswith("http"):
        ziel = "https://" + ziel
        
    try:
        antwort = requests.get(ziel)
        for key, value in antwort.headers.items():
            print(f" {key}: {value} ")
    except requests.exceptions.RequestException as e:
            print(f"Fehler: {e}")