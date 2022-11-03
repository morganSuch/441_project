# echo-server.py
import socket
from pickle import loads, dumps

# this can be a hostname or IP address, empty string for all connections allowed
#HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
HOST = socket.gethostname()
# number from 1-65536
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

# create socket object AF_NET = IPv4 address SOCK_STREAM = TCP
print("Starting server")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # associate socket with specified network interface and port number
    s.bind((HOST, PORT))
    # listen for connections, this can have a value for num of unaccepted
    # connections allowed before refusing new connections
    print("Awaiting connections...\n")
    s.listen()
    # blocks execution, waits for incoming connection
    # this creates a new socket object representing the client
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        data = input('->')
        conn.send(data.encode())
    conn.close()