
Hab ich gebaut um Python zu lernen. Ist ein kleines Netzwerk-Tool
mit drei Funktionen die man im Terminal aufruft.


Was es kann

grab-header
Holt die HTTP-Header von einer Website.

python3 main.py grab-header example.com

Zeigt Server, Content-Type, Datum und so. Praktisch um zu
sehen was für Software läuft.

port-scan
Scannt Ports auf einem Host.

python3 main.py port-scan example.com 1-1000

Läuft mit Threading, also schnell. 2000 Ports in 2 Sekunden.

ping-sweep
Findet Geräte in einem Netzwerk.

python3 main.py ping-sweep 192.168.1.0/24

Pingt alle IPs durch und zeigt welche antworten.


Was man braucht

Python 3 und requests.

pip install requests


Wie es aufgebaut ist

main.py ist der Startpunkt, checkt welchen Modus man aufruft.
Im nettools Ordner liegt für jeden Modus eine eigene Datei:
scanner.py für port-scan, pinger.py für ping-sweep,
grabber.py für grab-header.


Warum ich das gebaut hab

Wollte Python lernen und checken wie so Netzwerk-Tools eigentlich funktionieren
