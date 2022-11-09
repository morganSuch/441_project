# triggers finger authentication 
def send_authenticate(conn) -> bool:
    conn.send("authorize".encode())
    response = conn.recv(1024).decode()
    if str(response) == "yes":
        return True
    else:
        return False

# removes password from the database
def add_password(conn) -> bool:
    conn.send("add".encode())
    response = conn.recv(1024).decode()
    if str(response) == "added":
        return True
    else:
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