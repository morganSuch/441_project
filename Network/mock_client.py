# echo-client.py

import socket
from finger_functions import *
from database import *
from recognizeFace import *

#HOST = socket.gethostname()
HOST = "192.168.2.108"  # The server's hostname or IP address
PORT = 65432  # The port used by the server
DATABASE = "test.db"

# create socket object
print("Starting Client")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect to server
    
    try:
        s.connect((HOST, PORT))
        print("Connecting to server...")
    except:
        print("connection failed")
    while (1):
        # Server requests authentication from client 
        data = s.recv(1024).decode()
        if str(data) == "authorize_finger":
            #authenticated = findFinger()
            authenticated = testAuth()
            if authenticated:
                s.send("yes".encode())
            # This will be the failed response after 3 attempts
            else:
                s.send("no".encode())
<<<<<<< Updated upstream

        if str(data) == "authorize_face":
            # first we need to get all the faces from database
            database = connect_database(DATABASE)
            cursor = database.cursor()
            # Saving files to local file directory
            get_images(cursor, database)
            # Calling facial recognition program 
            authenticated = authenticate_face("/home/faces/")

            if authenticated:
                s.send("yes".encode())
            # This will be the failed response after 3 attempts
            else:
                s.send("no".encode())
        if str(data) == "add_face":
            image_id = str(s.recv(1024).decode())
            new_image = capture_face(image_id)
            database = connect_database(DATABASE)
            cursor = database.cursor()
            add_face(cursor, database, image_id, new_image)
            close_connection(database)
        
        if str(data) == "add":
=======
        elif str(data) == "add":
>>>>>>> Stashed changes
            s.send("adding".encode())
            fields = s.recv(4096)
            fields = fields.decode()
            fields = eval(fields)
            
            #application = str(s.recv(1024).decode())
            application = fields[0]
            #username = str(s.recv(1024).decode())
            username = fields[1]
            #password = str(s.recv(1024).decode())
            password = fields[2]
            #s.send("received".encode())
            # Encryption function should be added here!!!
            #if s.recv(1024).decode() == "update":
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (add_password(cursor, database, application, username, password)):
                close_connection(database)
                s.send("added".encode())
        elif str(data) == "edit":
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
        if str(data) == "get_apps":
            database = connect_database(DATABASE)
            cursor = database.cursor()
            app_list = str(get_application_names(cursor, database))
            s.send(app_list.encode())
        if str(data) == "get_pass":
            application = str(s.recv(1024).decode())
            database = connect_database(DATABASE)
            cursor = database.cursor()
            password = fetch_password(cursor, database, application)
            close_connection(database)
            password = password[0]
            print(password)
            s.send(password.encode())
            
    s.close()
