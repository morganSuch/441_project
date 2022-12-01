import socket

# triggers finger authentication 
def send_finger_authenticate(conn) -> bool:
    conn.send("authorize".encode())
    response = conn.recv(1024).decode()
    if str(response) == "yes":
        return True
    else:
        return False

# triggers face authentication 
def send_face_authenticate(conn) -> bool:
    conn.send("authorize_face".encode())
    response = conn.recv(1024).decode()
    if str(response) == "yes":
        return True
    else:
        return False

# Adds password to the database
def send_password(fields, conn) -> bool:
    conn.send("add".encode())
    field_list = str(fields)
    conn.send(field_list.encode())
    response = str(conn.recv(1024).decode())

    if str(response) == "added":
        print("Password added.")
        return True
    else:
        print("something went wrong")
        return False

# Adds new backup question to database
def send_question(conn, entry) -> bool:
    conn.send("add_question".encode())
    entry_list = str(entry)
    conn.send(entry_list.encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "added":
        print("Password added.")
        return True
    else:
        print("something went wrong")
        return False

# Gets password from database
def fetch_question(conn) -> list:
    question_info =[]
    conn.send("get_backup".encode())
    app_list = conn.recv(1024).decode()
    app_list = eval(app_list)
    return app_list

# Modifies password in the database
def edit_password(fields, conn) -> bool:
    conn.send("edit".encode())
    field_list = str(fields)
    conn.send(field_list.encode())
    response = str(conn.recv(1024).decode())

    if str(response) == "edited":
        print("Password edited.")
        return True
    else:
        print("something went wrong")
        return False

# Removes password from the database
def delete_password(fields, conn) -> bool:
    conn.send("delete".encode())
    for field in fields:
        conn.send(field.encode())
    response = conn.recv(1024).decode()
    if str(response) == "deleted":
        return True
    else:
        return False

# Gets password from database
def fetch_password(conn, app_name):
    conn.send("get_pass".encode())
    conn.send(app_name.encode())
    response = str(conn.recv(1024).decode())
    # print(response)
    return response

# Gets username from database
def fetch_name(conn, app_name):
    conn.send("get_name".encode())
    conn.send(app_name.encode())
    response = str(conn.recv(1024).decode())
    # print(response)
    return response

# Retreive applicatioon list from the database 
def fetch_application_names(conn) -> list:
    password_ids =[]
    conn.send("get_apps".encode())
    app_list = conn.recv(1024).decode()
    app_list = eval(app_list)
    return app_list

# Get print list from biometric device
def fetch_prints(conn) -> list:
    password_ids =[]
    conn.send("get_prints".encode())
    prints = conn.recv(1024).decode()
    prints = eval(prints)
    return prints

# Add image to client directory
def capture_image(conn, name):
    conn.send("add_face".encode())
    conn.send(name.encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "yes":
        return True
    else:
        return False

# Add fingerprint to biometric device
def capture_finger(conn):
    conn.send("add_finger".encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "yes":
        return True
    else:
        return False

# Perform hard reset on the device 
def trigger_reset(conn):
    conn.send("reset".encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "done":
        return True
    else:
        return False

# Close connection with client
def end_connection(conn):
    conn.send("close".encode())
    response = str(conn.recv(1024).decode())
    if str(response) == 'closed':
        print('received close')
        conn.close()
        
# Remove finger from biometric device
def remove_finger(conn, entry):
    conn.send("delete_print".encode())
    conn.send(entry.encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "yes":
        return True
    else:
        return False

# Remove face from client image directory
def remove_face(conn, id):
    conn.send("delete_face".encode())
    conn.send(id.encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "done":
        return True
    else:
        return False
    
# Send logout message for client to encrypt database 
def send_logout(conn):
    conn.send("logout".encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "done":
        return True
    else:
        return False