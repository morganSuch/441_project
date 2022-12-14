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

# removes password from the database
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

# removes password from the database
def delete_password(fields, conn) -> bool:
    conn.send("delete".encode())
    for field in fields:
        conn.send(field.encode())
    response = conn.recv(1024).decode()
    if str(response) == "deleted":
        return True
    else:
        return False

# gets password from database
def fetch_password(conn, app_name):
    conn.send("get_pass".encode())
    conn.send(app_name.encode())
    response = str(conn.recv(1024).decode())
    # print(response)
    return response

# gets username from database
def fetch_name(conn, app_name):
    conn.send("get_name".encode())
    conn.send(app_name.encode())
    response = str(conn.recv(1024).decode())
    # print(response)
    return response

# retreive applicatioon list from the database 
def fetch_application_names(conn) -> list:
    password_ids =[]
    conn.send("get_apps".encode())
    app_list = conn.recv(1024).decode()
    app_list = eval(app_list)
    return app_list

def capture_image(conn, name):
    conn.send("add_face".encode())
    conn.send(name.encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "yes":
        return True
    else:
        return False

def capture_finger(conn):
    conn.send("add_finger".encode())
    response = str(conn.recv(1024).decode())
    if str(response) == "yes":
        return True
    else:
        return False