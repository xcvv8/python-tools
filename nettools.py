import sys
import requests
import socket
from concurrent.futures import ThreadPoolExecutor


def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    ergebnis = s.connect_ex((ip, port))
    s.close()
    if ergebnis == 0:
        return port
    return None


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

elif modus == "port-scan":
    if len(sys.argv) < 4:
        print("Benutzung: python3 nettools.py port-scan <host> <port-range>")
        sys.exit(1)
    host = sys.argv[2]
    range_str = sys.argv[3]

    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print("Fehlermeldung")
        sys.exit(1)

    teile = range_str.split("-")
    start = int(teile[0])
    ende = int(teile[1])

    print(f"Host: {host}")
    print(f"Ip: {ip}")
    print(f"start: {start}")
    print(f"ende: {ende}")
    
    
    offene_ports = []
    futures = []
    with ThreadPoolExecutor(max_workers=100) as pool:
        for port in range(start, ende + 1):
            future = pool.submit(scan_port, ip, port)
            futures.append(future) 
            
        for future in futures:
            result = future.result()
            if result is not None:
                offene_ports.append(result)
                print(f"Port {result} ist offen")
                
    print(f"Es wurden {len(offene_ports)} offene Ports gefunden")