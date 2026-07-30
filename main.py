from scanner import scan_port

ip = input("Enter IP address: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print("\nScanning...\n")

open_ports = []

for port in range(start_port, end_port + 1):

    if scan_port(ip, port):
        print(f"Port {port} is OPEN.")
        open_ports.append(port)

print("\nScan completed.")

print(f"\nOpen ports found: {len(open_ports)}")