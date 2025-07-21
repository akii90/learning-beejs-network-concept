import socket
import sys

# Parse command line.
try:
    ip = str(sys.argv[1])
    port = 8000
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
except:
    print("usage: client.py ip port(optional)", file=sys.stderr)
    sys.exit(1)

# Init a socket.
s = socket.socket()

# Prevent an "Address already in use" error.
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind, ip is optional.
s.bind((ip, port))

# Listen
s.listen()
