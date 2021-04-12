import socket
import termcolor

def scan(targets, ports):
    for port in range(1, ports):
        scan_port(targets, port)

def scan_port(ip_address, port):
    try:
        sock = socket.socket()
        sock.connect((ip_address, port))
        print(termcolor.colored((f"[+] PORT {str(port)} OPENED"), 'green'))
        sock.close()
    except:
        pass

targets = input("[*] Enter Targets To Scan (split by comma): ")
ports = input("[*] Enter How Many Ports You Want To Scan: ")

if ',' in targets:
    print("[*] Scanning Multiple Targets")
    for ip_address in targets.split(","):
        scan(ip_address.strip(" "), int(ports))
else:
    print("[*] Scanning Single Target")
    scan(targets, int(ports))