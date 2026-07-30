import argparse

from report import save_report
import time
from scanner import scan_port

parser = argparse.ArgumentParser(
    description="Simple TCP Port Scanner"
)

parser.add_argument(
    "--host",
    required=True,
    help="Target IP address or hostname"
)

parser.add_argument(
    "--start",
    type=int,
    required=True,
    help="Start port"
)

parser.add_argument(
    "--end",
    type=int,
    required=True,
    help="End port"
)

args = parser.parse_args()

ip = args.host
start_port = args.start
end_port = args.end

print("\nScanning...\n")

start_time = time.time()

open_ports = []

for port in range(start_port, end_port + 1):

    is_open, banner = scan_port(ip, port)

    if is_open:
        if banner:
            print(f"Port {port} is OPEN. Banner: {banner}")
        else:
            print(f"Port {port} is OPEN.")
        open_ports.append(port)

end_time = time.time()

elapsed_time = end_time - start_time

print("\nScan completed.")

print(f"\nOpen ports found: {len(open_ports)}")

print(f"\nScan time: {elapsed_time:.2f} seconds")

save_report(ip, start_port, end_port, open_ports, elapsed_time)

print("\nReport saved to reports/report.txt")