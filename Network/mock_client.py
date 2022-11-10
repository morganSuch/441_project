# echo-client.py

import socket
from finger_functions import *
from database import *

HOST = socket.gethostname()
#HOST = "169.254.177.83"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DATABASE = "test.db"

# create socket object
print("Starting Client")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    print("Connecting to server...")
    try:
        s.connect((HOST, PORT))
    except:
        print("connection failed")
    while (1):

        # Server requests authentication from client 
        data = s.recv(1024).decode()
        if str(data) == "authorize":
            authenticated = findFinger()
            #authenticated = testAuth()
            if authenticated:
                s.send("yes".encode())
            # This will be the failed response after 3 attempts
            else:
                s.send("no".encode())
        if str(data) == "add":
            s.send("adding".encode())
            application = str(s.recv(1024).decode())
            username = str(s.recv(1024).decode())
            password = str(s.recv(1024).decode())
            s.send("received".encode())
            # Encryption function should be added here!!!
            if s.recv(1024).decode() == "update":
                database = connect_database(DATABASE)
                cursor = database.cursor()
                if (add_password(cursor, database, application, username, password)):
                    close_connection(database)
                    s.send("added".encode())
        if str(data) == "edit":
            s.send("editing".encode())
            application = str(s.recv(1024).decode())
            type = str(s.recv(1024).decode())
            value = str(s.recv(1024).decode())

            # Encryption function should be added here!!!
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (edit_information(cursor, database, application, type, value)):
                close_connection(database)
                s.send("edited".encode())
    s.close()
