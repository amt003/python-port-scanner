import socket
import datetime
import sys

print("""
========================================
  EDUCATIONAL PORT SCANNER
  Authorized scanning only.
  Target restricted to localhost.
========================================
""")

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    8000: "HTTP-Alt"
}

target = "127.0.0.1"  # localhost (SAFE)
if target != "127.0.0.1":
    print("Unauthorized target. Exiting.")
    sys.exit()

ports = [21, 22, 23, 25, 53, 80, 443,8000]
print("\nStarting Port Scan on", target)
print("Scan started at:", datetime.datetime.now())
print("-" * 50)

start_time = datetime.datetime.now()

try:
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        service_name = services.get(port, "Unknown Service")

        if result == 0:
          print(f"[+] Port {port} | Service: {service_name} | Status: OPEN")
        else:
          print(f"[-] Port {port} | Service: {service_name} | Status: CLOSED")


        sock.close()

except KeyboardInterrupt:
    print("\nScan interrupted by user.")
    sys.exit()

end_time = datetime.datetime.now()
print("-" * 50)
print("Scan finished at:", end_time)
print("Total scan duration:", end_time - start_time)

