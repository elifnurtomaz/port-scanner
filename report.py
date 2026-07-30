def save_report(ip, start_port, end_port, open_ports, scan_time):
    with open("reports/report.txt", "w") as file:

        file.write("PORT SCAN REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Target: {ip}\n")
        file.write(f"Port Range: {start_port}-{end_port}\n\n")

        file.write("Open Ports:\n")

        if open_ports:
            for port in open_ports:
                file.write(f"- {port}\n")
        else:
            file.write("No open ports found.\n")

        file.write(f"\nTotal Open Ports: {len(open_ports)}\n")
        file.write(f"Scan Time: {scan_time:.2f} seconds\n")