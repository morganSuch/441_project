# echo-server.py

import socket
# this can be a hostname or IP address, empty string for all connections allowed
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
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
    
    # this will automatically close the socket at the end of the block
    with conn:
        print(f"Connected by {addr}")
        # infinite loop that reads whatever data client sends and echoes back
        while True:
            # if client send an empty bytes object connection will close
            # terminating the loop
            data = conn.recv(1024)
            if not data:
                break
            # this is the echo
            conn.sendall(data)