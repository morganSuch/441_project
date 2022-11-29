# echo-server.py
import socket
from pickle import loads, dumps

from login import *

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

    conn.send("init".encode())
    if str(conn.recv(1024).decode()) == 'done':
        run_setup(conn)
        start_authentication(conn)
    else:
    # Check if initialization sequence should be done
    # -> send request to client for fingerprint count
    # if fingerprint count ==0:
    # -> trigger initialization sequence
    # if not
    # -> run normal authentication

    # Trigger authentication sequence upon successful connection to client
        start_authentication(conn)
