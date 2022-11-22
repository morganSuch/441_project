# echo-client.py
import socket
from finger_functions import *
from database import *
#from test_recognition import *
#camera = PiCamera()
#from recognizeFace import *

HOST = socket.gethostname()
#HOST = "192.168.2.108"  # The server's hostname or IP address
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
        if str(data) == "authorize":
            #authenticated = findFinger()
            authenticated = testAuth()
            if authenticated:
                s.send("yes".encode())
            # This will be the failed response after 3 attempts
            else:
                s.send("no".encode())

        if str(data) == "authorize_face":
            # first we need to get all the faces from database
            #database = connect_database(DATABASE)
            #cursor = database.cursor()
            # Saving files to local file directory
            #get_images(cursor, database)
            # Calling facial recognition program 
            #authenticated = authenticate_face("/home/faces/")
            #authenticate_face(camera)
            authenticated = testAuth()
            if authenticated:
                s.send("yes".encode())
            else:
                s.send("no".encode())
        if str(data) == "add_face":
            image_id = str(s.recv(1024).decode())
            #new_image = capture_face(camera, image_id)

            # Need something to add image to the face directory here
            new_image = testAuth()
            if new_image:
                s.send("yes".encode())
            else:
                s.send("no".encode())

        if str(data) == "add_finger":
            added = testAuth2()
            #added = add_finger()
            if added:
                s.send("yes".encode())
            else:
                s.send("no".encode())                
        
        if str(data) == "add":
            field_list = s.recv(1024).decode()
            field_list = eval(field_list)
    
            #application = str(s.recv(1024).decode())
            application = field_list[0]
            #username = str(s.recv(1024).decode())
            username = field_list[1]
            #password = str(s.recv(1024).decode())
            password = field_list[2]
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (add_password(cursor, database, application, username, password)):
                close_connection(database)
                s.send("added".encode())

        elif str(data) == "edit":
            field_list = s.recv(1024).decode()
            field_list = eval(field_list)

            application = field_list[0]
            value = field_list[1]
            type = field_list[2]

            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (edit_information(cursor, database, application, type, value)):
                close_connection(database)
                s.send("edited".encode())

        if str(data) == "delete":
            application = str(s.recv(1024).decode())
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (delete_information(cursor, database, application)):
                close_connection(database)
                s.send("deleted".encode())

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
        if str(data) == "get_name":
            application = str(s.recv(1024).decode())
            database = connect_database(DATABASE)
            cursor = database.cursor()
            password = fetch_name(cursor, database, application)
            close_connection(database)
            name = password[0]
            print(name)
            s.send(name.encode())
            
    s.close()
