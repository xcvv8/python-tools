# nettools.py — Network Toolkit
#
# Modus 1: grab-header
# 1. Nutzer gibt URL ein
# 2. Wenn URL nicht mit http:// oder https:// beginnt → https:// davor hängen
# 3. Wenn URL gültig ist: HTTP-Anfrage an die URL schicken
# 4. Fehler abfangen: kein Internet / Timeout / ungültige URL
#    Wenn Fehler: Fehlermeldung ausgeben und Programm beenden
# 5. Für jeden Header in der Antwort: Name und Wert ausgeben
#
# Beispielhafte Ausgabe für die URL example.com:
# Server: nginx/1.24.0
# Content-Type: text/html

    # 2. wenn ziel nicht mit http beginnt: https:// davor
    # 3. anfrage mit requests schicken
    # 4. wenn fehler: meldung + ende
    # 5. für jeden header in antwort: print name + wert




#Öffne die requests-Doku (google requests readthedocs quickstart)

#Finde raus wie man auf die Header zugreift

#robiere es erst mit einem einzelnen print(antwort.<was auch immer>) aus

#Dann mit einer Schleife durch alle Header





import sys
import requests

if len(sys.argv) < 3:
    print("Benutzung: python3 nettools.py <modus> <ziel>")
    print("Beispiel: python3 nettools.py grab-header example.com")
    sys.exit(1)

modus = sys.argv[1]
ziel = sys.argv[2]

if modus == "grab-header":
    if not ziel.startswith("http"):
        ziel = "https://" + ziel
    try:
        antwort = requests.get(ziel)
        for key, value in antwort.headers.items():
            print(f"{key}: {value}")
    except requests.exceptions.RequestException as e:
        print(f"Fehler: {e}")
        sys.exit(1)