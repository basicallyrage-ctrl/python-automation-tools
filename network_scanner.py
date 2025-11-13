import socket

def basic_port_scan(target):
    print(f"Scanning {target}...")
    common_ports = [21, 22, 23, 80, 443, 3389]
    
    for port in common_ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(f"[+] Port {port} is open")
            s.close()
        except:
            pass

if __name__ == "__main__":
    target_ip = input("Enter target IP: ")
    basic_port_scan(target_ip)
