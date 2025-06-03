# UDP Server

import sys
import socket

# Parse cmd arg
try:
    port = int(sys.argv[1])
    print(sys.argv[0])
except:
    print("usage: udpserver.py port", file=sys.stderr)
    sys.exit(1)

# New UDP(datagram) socket
s = socket.socket(type=socket.SOCK_DGRAM)

# Bind a port
s.bind(("", port))

# Loop receiving data
while True:
    # Receive data
    data, sender = s.recvfrom(4096)
    print(f"Got data from {sender[0]}:{sender[1]}: \"{data.decode()}\"")

    # Send a reply back to sender
    s.sendto(f"Got your {len(data)} byte(s) of data!".encode(), sender)
