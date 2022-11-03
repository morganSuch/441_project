def send_authenticate(conn) -> bool:
    conn.send("authorize".encode())
    response = conn.recv(1024).decode()
    if str(response) == "yes":
        return True
    else:
        return False