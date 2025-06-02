import sys
import socket

# Parse command line
try:
    domain = str(sys.argv[1])
    port = 80
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
except:
    print("usage: client.py domain port(optional)", file = sys.stderr)
    print(domain)
    print(port)
    sys.exit(1)

# Init a socket
s = socket.socket()

# Init a connect
s.connect((domain, port))

# send the request
request_headr = "GET / HTTP/1.1\n"
request_headr +=f"Host: {domain}\n"
request_headr +="Connection: close\n"
request_headr +="\r\n"
print(f"Request header:\n{request_headr}")
s.sendall(request_headr.encode("ISO-8859-1"))

# Receive the web response
response = b''
while True:
    r = s.recv(1024)
    response += r
    if len(r) == 0:
        print("Peer closed")
        break
print(f"Server response:\n{response.decode("ISO-8859-1")}")

# Close the socket
s.close()