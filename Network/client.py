# echo-client.py

import socket

from menu import *

#HOST = socket.gethostname()
HOST = "169.254.177.83"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

# create socket object
print("Starting Client")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    print("Connecting to server...")
    try:
        s.connect((HOST, PORT))
    except:
        print("connection failed")
    message = input("->")
    while message.lower().strip() != 'bye':
<<<<<<< Updated upstream
=======
#        if(message.lower().strip() == 'menu'):
#            authenticate()
>>>>>>> Stashed changes
        s.send(message.encode())
        data = s.recv(1024).decode()
        print("Received from server: " + data)
        message = input("->")
    
    s.close()


print(f"Received {message!r}")

