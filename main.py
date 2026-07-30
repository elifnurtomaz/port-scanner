from report import save_report
import time
from scanner import scan_port

ip = input("Enter IP address: ")

start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print("\nScanning...\n")

start_time = time.time()

open_ports = []

for port in range(start_port, end_port + 1):

    if scan_port(ip, port):
        print(f"Port {port} is OPEN.")
        open_ports.append(port)

end_time = time.time()

elapsed_time = end_time - start_time

print("\nScan completed.")

print(f"\nOpen ports found: {len(open_ports)}")

print(f"\nScan time: {elapsed_time:.2f} seconds")

save_report(ip, start_port, end_port, open_ports, elapsed_time)

print("\nReport saved to reports/report.txt")