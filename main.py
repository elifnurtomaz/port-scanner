from scanner import scan_port

ip = input("Enter IP address: ")

port = int(input("Enter port: "))

if scan_port(ip, port):
    print(f"Port {port} is OPEN.")
else:
    print(f"Port {port} is CLOSED.")