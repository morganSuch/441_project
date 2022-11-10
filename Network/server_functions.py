import socket

# triggers finger authentication 
def send_authenticate(conn) -> bool:
    conn.send("authorize".encode())
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
def get_password(conn) -> bool:
    conn.send("get".encode())
    response = conn.recv(1024).decode()
    if str(response) == "fetched":
        return True
    else:
        return False

# removes password from the database
def get_password_ids(conn) -> list:
    password_ids =[]
    conn.send("get".encode())
    while str(conn.revc(1024).decode() != "end"):
        next_id = str(conn.recv(1024).decode())
        password_ids.append(next_id)

    return password_ids