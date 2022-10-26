# echo-client.py

import socket

HOST = "104.194.99.98"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# create socket object
print("Starting Client")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    print("Connecting to server...")
    s.connect((HOST, PORT))
    # send message to server
    s.sendall(b"Hello, world")
    # receive server reply
    data = s.recv(1024)

print(f"Received {data!r}")