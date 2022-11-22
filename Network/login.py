#!/usr/bin/python
import logging
from tkinter import *
from vault import *
from print_functions import *
from server_functions import *
from menu import *

default_login_method = "finger"

# Main function for bringing up application login screen
def start_authentication(conn):
    root = Tk()
    root.geometry("375x225")
    root.title('Authentication Screen')

    page_title = Label(root, text="LOGIN", font=("Courier bold", 30))
    page_title.grid(column=0, row=0)

    inst = Label(root, text="Please select your preferred authentication method.", font=("Courier bold", 12))
    inst.grid(column=0, row=1)

    login_finger = Button(root, bg="white", fg="black", text="Finger",font=("Courier bold", 20), width=15, command=lambda: trigger_finger_auth(root, conn)) #client_login(root))
    login_finger.grid(column=0, row=2)

    login_face = Button(root, bg="white", fg="black", text="Face",font=("Courier bold", 20), width=15, command=lambda: trigger_face_auth(root, conn)) #client_login(root))
    login_face.grid(column=0, row=3)

    root.mainloop()

# When login button is pressed,triggers send_authenticate server function
# to make authentication request to server
def trigger_finger_auth(top_screen, conn):
    if send_finger_authenticate(conn):
        print("Authentication triggered")
        #vaultScreen(top_screen)
        vaultScreen(top_screen, conn)
    else:
        print("Authentication failed")

def trigger_face_auth(top_screen, conn):
    if send_face_authenticate(conn):
        print("Authentication triggered")
        #vaultScreen(top_screen)
        vaultScreen(top_screen, conn)
    else:
        print("Authentication failed")