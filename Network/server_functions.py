import socket

# triggers finger authentication 
def send_finger_authenticate(conn) -> bool:
    conn.send("authorize_finger".encode())
    response = conn.recv(1024).decode()
    if str(response) == "yes":
    # TODO try this out in lab to see if it works as expected
        return True
    else:
        return False

# triggers finger authentication 
def send_face_authenticate(conn) -> bool:
    conn.send("authorize_face".encode())
    response = conn.recv(1024).decode()
    if str(response) == "yes":
    # TODO try this out in lab to see if it works as expected
        return True
    else:
        return False

# Adds password to the database
def send_password(fields, conn) -> bool:
    conn.send("add".encode())
    ack0 = str(conn.recv(1024).decode())
    if str(ack0) == "adding":
        for field in fields:
            conn.send(field.encode())
    if str(conn.recv(1024).decode()) == "received":
        conn.send("update".encode())
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
    ack0 = str(conn.recv(1024).decode())
    if str(ack0) == "editing":
        for field in fields:
            conn.send(field.encode())

    response = str(conn.recv(1024).decode())
    if str(response) == "edited":
        print("Password edited.")
        return True
    else:
        print("something went wrong")
        return False

# removes password from the database
def delete_password(conn) -> bool:
    conn.send("delete".encode())
    response = conn.recv(1024).decode()
    if str(response) == "deleted":
        return True
    else:
        return False

# gets password from database

# removes password from the database
def fetch_password(conn, app_name):
    conn.send("get_pass".encode())
    conn.send(app_name.encode())
    response = str(conn.recv(1024).decode())
    print(response)
    return response

# retreive applicatioon list from the database 
def fetch_application_names(conn) -> list:
    password_ids =[]
    conn.send("get_apps".encode())
    app_list = conn.recv(1024).decode()
    app_list = eval(app_list)
    return app_list