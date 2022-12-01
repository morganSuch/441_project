from OpenSSL import SSL
import sys, os, select, socket
from finger_functions import *
from database import *

#from ciphers import *
from Crypto.PublicKey import RSA
from face_authentication import *
from encryption_functions import *
camera = PiCamera()

def verify_cb(conn, cert, errnum, depth, ok):
    if conn.cert.get_subject():
        return ok

# Initializing context
ctx = SSL.Context(SSL.SSLv23_METHOD)
ctx.set_verify(SSL.VERIFY_PEER, verify_cb) # Demand a certificate
ctx.use_privatekey_file (os.path.join(dir, 'client.pkey'))
ctx.use_certificate_file(os.path.join(dir, 'client.cert'))
ctx.load_verify_locations(os.path.join(dir, 'CA.cert'))

HOST = "169.254.177.83"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

DATABASE = "vault.db"
ENC_DATABASE = "vault.db.enc"
SEC_DATABASE = 'question.db'
SEC_ENC_DATABASE = 'question.db.enc'

# RSA Keys for image signatures
extern_priv = os.path.join('/441_project/DEMO/', 'image_sign')
extern_pub = os.path.join('/441_project/DEMO/', 'image_sign.pub')

priv_rsa = RSA.import_key(extern_priv)
pub_rsa = RSA.import_key(extern_pub)
print_count = 0

# AES-256 key intialization for database encryption
password = 'yfbgUIG3T4bc8dgtU83' # Password will be changed to something more complicated
key = hashlib.sha256(password.encode('utf-8')).digest()
chunksize = 64*1024

# create socket object
print("Starting Client")
with SSL.Connection(ctx, socket.socket(socket.AF_INET, socket.SOCK_STREAM)):
    try:
        s.connect((HOST, PORT))
        print("Connecting to server...")
    except:
        print("connection failed")

    while (1):
        # Client receives request from server 
        data = s.recv(1024).decode()
        # Counting number of fingerprints in scanner
        prints = countPrints()

        # First communication to see if initiation sequence should be triggered
        if str(data) == "init":
            # If there is no authentication data, run init sequence to create databases
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
                print_count = 0
                s.send("done".encode())
            # If there is, update print count to be number of fingerprints
            else:
                print_count = prints
                s.send("no".encode())

        # Authorizes Finger
        if str(data) == "authorize":
            authenticated = findFinger()
            if authenticated:
                # Decrypt the database
                decrypt_db(key, chunksize, DATABASE)
                decrypt_db(key, chunksize, SEC_DATABASE)
                s.send("yes".encode())
            # This will be the failed response after 3 attempts
            else:
                s.send("no".encode())
        
        # Authorizes Face
        if str(data) == "authorize_face":
            authenticated = authenticate_face(camera, pub_rsa)
            if authenticated:
                # Decrypt the database
                decrypt_db(key, chunksize, DATABASE)
                decrypt_db(key, chunksize, SEC_DATABASE)
                s.send("yes".encode())
            else:
                s.send("no".encode())
        
        # Adds Face
        if str(data) == "add_face":
            # Take new photo and sign
            image_id = str(s.recv(1024).decode())
            new_image = add_face(camera, image_id, priv_rsa)
            if new_image:
                s.send("yes".encode())
            else:
                s.send("no".encode())
        
        # Adds Finger
        if str(data) == "add_finger":
            added = addFinger(print_count + 1)
            if added:
                print_count += 1
                s.send("yes".encode())
            else:
                s.send("no".encode())  

        # Adds Security Question
        if str(data) == "add_question":
            # Receive data from server
            entry = s.recv(4096).decode()
            entry_list = eval(entry)
            question = entry_list[0]
            answer = entry_list[1]
            # Replace question in databse
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
            # Receive data from server
            field_list = s.recv(1024).decode()
            field_list = eval(field_list)
            application = field_list[0]
            username = field_list[1]
            password = field_list[2]
            # Add to database
            database = connect_database(DATABASE)
            cursor = database.cursor()
            if (add_password(cursor, database, application, username, password)):
                close_connection(database)
                s.send("added".encode())
            else:
                s.send("fail".encode())

        # Modifies Password
        elif str(data) == "edit":
            # Receive data from server
            field_list = s.recv(1024).decode()
            field_list = eval(field_list)
            application = field_list[0]
            value = field_list[1]
            type = field_list[2]
            # Update entry in database
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
            decrypt_db(key, chunksize, SEC_DATABASE)
            database = connect_database(SEC_DATABASE)
            cursor = database.cursor()
            info = str(get_question(cursor, database))
            close_connection(database)
            s.send(info.encode())

        # Decrypts database after backup authentication
        if str(data) == "backup_auth":
            decrypt_db(key, chunksize, DATABASE)

        # Gets list of print locations for delete
        if str(data) == "get_prints":
            print_list = str(getPrints())
            print(print_list)
            print("Prints got")
            s.send(print_list.encode())

        # Delete face biometrics
        if str(data) == "delete_face":
            # Delete images
            dir = "/home/pi/Faces/"
            sig = "/home/pi/Signatures/"
            face_id = str(s.recv(1024).decode())
            file_name = dir+face_id+".jpg"
            sig_file = sig+face_id+".jpg.sig"

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

        # Device logout - Encrypt databse
        if str(data) == "logout":
            # encrypt database
            encrypt_db(key, chunksize, DATABASE)
            encrypt_db(key, chunksize, SEC_DATABASE)
            s.send("done".encode())

        # Close Session, break connection with server
        if str(data) == "close":
            break
        
    s.send("closed".encode())
    s.close()