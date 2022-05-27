
#!/bin/python3
# 2/25/2021
# Simple port scanner

import sys
import socket
from datetime import datetime

target = ''

# define target
if len(sys.argv) == 2:
    # translate hostname to ipv4
    target = socket.gethostbyname(sys.argv[1])
else:
    print('Invalid amount of arguments')
    print("Syntax: python port-scanner.py <ip>")

# add a banner
print("-" * 50)
print('Scanning target ' + target)
print('Time started: ' + str(datetime.now()))
print("-" * 50)

try:
    for port in range(1, 1024):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # timeout for port connections
        socket.setdefaulttimeout(1)

        # tests if the port is open or not
        result = s.connect_ex((target, port))
        print(f'Checking port {port}')
        if result == 0:
            print(f"Port {port} is open")
        s.close()

# control + c interrupt       
except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
