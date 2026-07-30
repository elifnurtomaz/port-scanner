import socket

def scan_port(ip, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.3)

    result = sock.connect_ex((ip, port))

    if result == 0:

        banner = ""

        try:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode(errors="ignore").strip()

        except:
            pass

        sock.close()

        return True, banner

    sock.close()

    return False, ""