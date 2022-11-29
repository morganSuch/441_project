# echo-client.py
import socket
from finger_functions import *
from database import *
import os
#from ciphers import *
from test_recognition import *
camera = PiCamera()


HOST = "169.254.177.83"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

DATABASE = "vault.db"
ENC_DATABASE = "vault.db.enc"
SEC_DATABASE = 'question.db'
SEC_ENC_DATABASE = 'question.db.enc'

finger_count = 1

# create socket object
print("Starting Client")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    try:
        s.connect((HOST, PORT))
        print("Connecting to server...")
    except:
        print("connection failed")

    while (1):
        # Server requests authentication from client 
        data = s.recv(1024).decode()
        # if str(data) == "encrypt":
        #     Encrpt data here
        #     encrypt(DATABASE, ENC_DATABASE)
        if str(data) == "init":
            if(countPrints()):
                # create databases
                database = connect_database(DATABASE)
                cursor = database.cursor()
                # Password vault database
                create_password_databse(cursor)
                close_connection(database)
                # Backup security question database
                database = connect_database(SEC_DATABASE)
                cursor = database.cursor()
                create_question_databse(cursor)
                close_connection(database)
                s.send("done".encode())
            else:
               s.send("no".encode())

        if str(data) == "authorize":
            authenticated = findFinger()
            #authenticated = testAuth2()
            if authenticated:
                # Decrypt here 
                s.send("yes".encode())
            # This will be the failed response after 3 attempts
            else:
                s.send("no".encode())

        if str(data) == "authorize_face":
            #authenticated = testAuth2()
            authenticated = authenticate_face(camera)
            if authenticated:
                # Decrypt here
                #decrypt(ENC_DATABASE, DATABASE)
                s.send("yes".encode())
            else:
                s.send("no".encode())
        if str(data) == "add_face":
            image_id = str(s.recv(1024).decode())
            new_image = add_face(camera, image_id)

            # Need something to add image to the face directory here
            #new_image = testAuth()
            if new_image:
                s.send("yes".encode())
            else:
                s.send("no".encode())

        if str(data) == "add_finger":
            #added = testAuth()
            added = addFinger(finger_count)
            if added:
                finger_count += 1
                s.send("yes".encode())
            else:
                s.send("no".encode())                
        
        if str(data) == "add_question":
            entry = s.recv(4096).decode()
            entry_list = eval(entry)
            question = entry_list[0]
            answer = entry_list[1]

            database = connect_database(SEC_DATABASE)
            cursor = database.cursor()
            delete_question(cursor, database)
            if(add_question(cursor, database, question, answer)):
                close_connection(database)
                s.send("added".encode())
            else:
                s.send("fail".encode())


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
            else:
                s.send("fail".encode())

        elif str(data) == "edit":
            field_list = s.recv(1024).decode()
            field_list = eval(field_list)

            application = field_list[0]
            value = field_list[1]
            type = field_list[2]
            print('app', application)
            print('val', value)
            print('type', type)

            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (edit_information(cursor, database, application, type, value)):
                close_connection(database)
                s.send("edited".encode())
            else:
                s.send("fail".encode())

        if str(data) == "delete":
            application = str(s.recv(1024).decode())
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (delete_information(cursor, database, application)):
                close_connection(database)
                s.send("deleted".encode())
            else:
                s.send("fail".encode())

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
        if str(data) == "get_backup":
            database = connect_database(SEC_DATABASE)
            cursor = database.cursor()
            info = str(get_question(cursor, database))
            close_connection(database)
            s.send(info.encode())

        if str(data) == "reset":
            # Removing all databases
            if os.path.exists(DATABASE):
                os.remove(DATABASE)
            if os.path.exists(ENC_DATABASE):
                os.remove(ENC_DATABASE)
            if os.path.exists(SEC_DATABASE):
                os.remove(SEC_DATABASE)
            if os.path.exists(SEC_ENC_DATABASE):
                os.remove(SEC_ENC_DATABASE)

            # Delete images
            dir = ""
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))

            s.send("done".encode())
        if str(data) == "close":
            break
        
    s.send("closed".encode())
    s.close()
