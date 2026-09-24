import sys
from nettools.scanner import scan_port
from nettools.pinger import ping_host
from nettools.grabber import grab_header
from concurrent.futures import ThreadPoolExecutor
import socket
import ipaddress


if len(sys.argv) < 3:
    print("Benutzung: python3 main.py <modus> <ziel>")
    print("Beispiel: python3 main.py grab-header example.com")
    sys.exit(1)

modus = sys.argv[1]
ziel = sys.argv[2]

if modus == "grab-header":
    grab_header(ziel)
    
    
elif modus == "port-scan":
    if  len(sys.argv) < 4:
        print("Benutzung: python script.py port-scan <Ziel-IP> <Ports>")
        sys.exit(1)
        
    host =sys.argv[2]
    range_str = sys.argv[3]
    
    
    try:
        ip = socket.gethostbyname(host)
    except socket.gaierror:
        print (f"Fehler: Host '{host}' konnte nicht aufgelöst werden.")    
        sys.exit(1)
        
        
    teile = range_str.split("-")
    start = int(teile[0])
    ende = int(teile[1])
    
    
    print(f"Host:{host}")
    print(f"Ip: {ip}")
    print(f"start: {start}")
    print(f"ende: {ende}")
    
    
    offene_ports = []
    futures = []
    with  ThreadPoolExecutor(max_workers=100) as pool:
        for port in range(start , ende + 1):
            future = pool.submit(scan_port , ip , port)
            futures.append(future)
            
            
        for future in futures:
            result = future.result()
            if result is not None:
                offene_ports.append(result)
                print(f"port {result} ist offen")    
                
    print(f"Es wurden {len(offene_ports)} offene ports gefunden")
    
    
    
    
    
elif modus == "ping-sweep":
    if len(sys.argv) < 3:
        print("Benutzung: python script.py port-scan <Ziel-IP> <Ports>")
        sys.exit(1)
        
    subnetz_str = sys.argv[2]
    
    try:
        netz = ipaddress.ip_network(subnetz_str , strict=False)
    except ValueError:
        print("Ungültiges Subnetz")
        sys.exit(1)
    
    
    hosts = []
    for ip in netz.hosts():
        hosts.append(str(ip))
        
    print(f"Scanne Subnetz  {subnetz_str} ({len(hosts)} Hosts") 
    
    
    offene_hosts = []
    futures = []
    with ThreadPoolExecutor(max_workers=100) as pool:
        for host in hosts:
            future = pool.submit(ping_host , host)
            futures.append(future)
            
        for future in futures:
            result = future.result()
            if result is not None:
                offene_hosts.append(result)
                print(f" {result} ist erreichbar")
                
    print(f" Es wurden {len(offene_hosts)} erreichbare Hosts gefunden")