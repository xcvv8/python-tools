import subprocess

def  ping_host(ip):
    try:
        result = subprocess.run(["ping", "-c", "1", ip], capture_output=True)
    except subprocess.SubprocessError:
        return 
    if result.returncode == 0:
        return ip
    
    return 
