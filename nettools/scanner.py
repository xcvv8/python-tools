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


class ScanResult:
    def __init__(self, host , port , service="unbekannt"):
        self.host = host
        self.port = port
        self.service = service
        
    
    def als_dict(self):
        return {"host": self.host, "port": self.port, "service": self.service}