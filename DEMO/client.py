# echo-client.py
import socket
from finger_functions import *
from database import *
import os
#from ciphers import *
from Crypto.PublicKey import RSA
from face_authentication import *
camera = PiCamera()


HOST = "169.254.177.83"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

DATABASE = "vault.db"
ENC_DATABASE = "vault.db.enc"
SEC_DATABASE = 'question.db'
SEC_ENC_DATABASE = 'question.db.enc'

<<<<<<< Updated upstream
=======
finger_count = 2

>>>>>>> Stashed changes
# RSA Keys for image signatures
extern_priv = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEApIi2HI7XMpNdOZYHSEnMBllQZUEtaXU33O1yCo1lPPh4k5Ou
OizGp2Bjk2iPHeCvlvbVLmHNciOKdXdUwCtNd+H+MMjGKnMo7ohFcUUtzLPqm2kr
IOQoP1rVJCRJNYx7K1edbJNFhujaXmGSLjP/tpzQrgh4GTrr4im7Kv0isfEDnwOJ
oxlZDP9I084496uc4NRvik0okJ5jajDHy/XetyX+fXtzI4tIby68xVPTYkEO6B+I
ZpZAHEddWBW/WvRUdy5qCQZ+mTyo9SLTkLk/v2gNGmv/DK/xd5P3NLWZM8q8KbV2
1wIPdcoVSj/dS2z7mBToJad7XafQOakAwpohMwIDAQABAoIBAEaRsHJNPbWeiRSi
6ZqytERg2F+ldeHOedhTK1+lR6+/7o91fvvKqqWtbOgTp5asAQPh+It9PU3gOomp
VftaV0686nZoFr6sR/kPD6HGhx9OZ6iikfH4id6qidKHkbLa/xUW7hlcjSyRAOAM
P1N70Ai197c9QK2pnPSS64lDqzbgNGreWgIuFhdn8WIFb6mPuhgDZSnKWXNwi2Da
lWRHw7S4jDpr46j1fBrCNnZrzCUFWxju8ah0Kt4z3bEfy60Gp/KUBx6HXihI6L5J
Ap7n7rAZFTi3sqD+iytYzpsPXx8Ru404ww6kcpaHjm531aRhmaJZW5EaX8JK+p6/
BzB6aeECgYEAtqvfeE4K4ZfTPN0yX29LdG4frV3oa/M+xKPSmvDGq/R2LQymRCIq
ldi3Ms0hsQl9FuxlA8+ykB2x9OUcQCFufaiPdRMgzyVEs9ZsG3VW+KgVgnIfDJzl
bLxRTUFlHgjFIKtYsyZeyf3qwr4ksNYbtO7e9KcdqiqtKMokNXPbjbECgYEA5pT2
nSBE5iwDELoQfbrot7ERsqvBgKmh0taY/RR6RU7PnM8xiC1mzt+GDdtuqnoMasCO
smMNOTGyYS522mQ0yI+duun69DnmME6l9AsmQ3v6wvYRxed/SjL+4xLDL+2DB2YG
RykpGkD7EF9nkx1tyDSEhX/+/onwYbY7V/LYYiMCgYB88kTxihghRHMlb3tUEdE/
u0+JivE+XWwynoegmU6bMaRfngZgFiqgwlJUukDwUjgwpNNXbwqJTvZ5NvlC2Fs2
MkSl5MaNScWbaPAbPACYJohH6H1aaDr5TDokKLXcfE0x0mHicD1n1nlsaRi5qEnd
UYJJP8Gnsncsrk9kDHJBkQKBgBWjSPk5u/11h9wb+cwyrAAA585Ce+gdAwiMBtNJ
BqhWWvk2IEnNKOak5ymJu/rXdS7XXwyyat1BIqIoABNCcAmaII0Xw+sDO+ywlLYw
Dakriz6cZNKThMhrvKuGaTaoLTGWi2RGIotKKcVBjrCphFHTS9RTTJSKUTp6JVt9
eHzNAoGBAI0PQ+VfzQAZGKhepcQ1b7paVlreiSEv/algHroUtIHwlYEhwFYAffM4
fuaMJcjIIfsjZA23Q8EGogWrJ61h7X29joFBX3AO22GTYrW9Mmj+zpTjPhKaAVIo
u/xa30s2VxE6vRllGrleWChYlj3tec2UrwSb3EynGOXRUynUdK3o
-----END RSA PRIVATE KEY-----"""

extern_pub = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEApIi2HI7XMpNdOZYHSEnM
BllQZUEtaXU33O1yCo1lPPh4k5OuOizGp2Bjk2iPHeCvlvbVLmHNciOKdXdUwCtN
d+H+MMjGKnMo7ohFcUUtzLPqm2krIOQoP1rVJCRJNYx7K1edbJNFhujaXmGSLjP/
tpzQrgh4GTrr4im7Kv0isfEDnwOJoxlZDP9I084496uc4NRvik0okJ5jajDHy/Xe
tyX+fXtzI4tIby68xVPTYkEO6B+IZpZAHEddWBW/WvRUdy5qCQZ+mTyo9SLTkLk/
v2gNGmv/DK/xd5P3NLWZM8q8KbV21wIPdcoVSj/dS2z7mBToJad7XafQOakAwpoh
MwIDAQAB
-----END PUBLIC KEY-----"""

priv_rsa = RSA.import_key(extern_priv)
pub_rsa = RSA.import_key(extern_pub)
print_count = 0

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
        prints = countPrints()
        # First communication to see if initiation sequence should be triggered
        if str(data) == "init":
            if(prints == 0):
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
                print_count = 1
                s.send("done".encode())
            else:
                print_count = prints
                s.send("no".encode())
        # Authorizes Finger
        if str(data) == "authorize":
            authenticated = findFinger()
            #authenticated = testAuth2()
            if authenticated:
                # Decrypt here 
                s.send("yes".encode())
            # This will be the failed response after 3 attempts
            else:
                s.send("no".encode())
        # Authorizes Face
        if str(data) == "authorize_face":
            #authenticated = testAuth2()
            authenticated = authenticate_face(camera, pub_rsa)
            if authenticated:
                # Decrypt here
                #decrypt(ENC_DATABASE, DATABASE)
                s.send("yes".encode())
            else:
                s.send("no".encode())
        # Adds Face
        if str(data) == "add_face":
            image_id = str(s.recv(1024).decode())
            new_image = add_face(camera, image_id, priv_rsa)
            if new_image:
                s.send("yes".encode())
            else:
                s.send("no".encode())
        # Adds Finger
        if str(data) == "add_finger":
            added = addFinger(print_count)
            if added:
                print_count += 1
                s.send("yes".encode())
            else:
                s.send("no".encode())                
        # Adds Security Question
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
        # Adds Password
        if str(data) == "add":
            field_list = s.recv(1024).decode()
            field_list = eval(field_list)
            application = field_list[0]
            username = field_list[1]
            password = field_list[2]
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (add_password(cursor, database, application, username, password)):
                close_connection(database)
                s.send("added".encode())
            else:
                s.send("fail".encode())
        # Modifies Password
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
        
        # Deletes Password
        if str(data) == "delete":
            application = str(s.recv(1024).decode())
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (delete_information(cursor, database, application)):
                close_connection(database)
                s.send("deleted".encode())
            else:
                s.send("fail".encode())
        
        # Gets all application names to populate vault
        if str(data) == "get_apps":
            database = connect_database(DATABASE)
            cursor = database.cursor()
            app_list = str(get_application_names(cursor, database))
            s.send(app_list.encode())
        
        # Gets Password
        if str(data) == "get_pass":
            application = str(s.recv(1024).decode())
            database = connect_database(DATABASE)
            cursor = database.cursor()
            password = fetch_password(cursor, database, application)
            close_connection(database)
            password = password[0]
            print(password)
            s.send(password.encode())
        # Deletes fingerprint
        if str(data) == "delete_print":
            entry = str(s.recv(1024).decode())
            if deletePrint(int(entry)):
                s.send("yes".encode())
            else:
                s.send("no".encode())
        # Gets username
        if str(data) == "get_name":
            application = str(s.recv(1024).decode())
            database = connect_database(DATABASE)
            cursor = database.cursor()
            password = fetch_name(cursor, database, application)
            close_connection(database)
            name = password[0]
            print(name)
            s.send(name.encode())
        # Gets security question and answer for backup authentication
        if str(data) == "get_backup":
            database = connect_database(SEC_DATABASE)
            cursor = database.cursor()
            info = str(get_question(cursor, database))
            close_connection(database)
            s.send(info.encode())
        # Gets list of print locations for delete
        if str(data) == "get_prints":
            print_list = str(getPrints())
            print(print_list)
            print("Prints got")
            s.send(print_list.encode()
        if str(data) == "delete_face":
            # Delete images
            dir = "/home/pi/Faces"
            sig = "/home/pi/Signatures"
            face_id = str(s.recv(1024).decode())
            file_name = dir+face_id+".jpg"
            sig_file = sig+face_id+".jpg"

            if os.path.exists(file_name) and os.path.exists(sig_file):
                os.remove(file_name)
                os.remove(sig_file)
                s.send("done".encode())
            else:
                s.send("fail".encode())
                   
        # Device Hard Reset
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
            dir = "/home/pi/Faces"
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
            # Delete signatures
            dir = "/home/pi/Signatures"
            for f in os.listdir(dir):
                os.remove(os.path.join(dir, f))
            # Erase all fingerprints from device
            removePrints()
            s.send("done".encode())

        if str(data) == "close":
            break
        
    s.send("closed".encode())
    s.close()

