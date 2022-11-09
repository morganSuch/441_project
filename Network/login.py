#!/usr/bin/python
import logging
from tkinter import *
from vault import *
from print_functions import *
from server_functions import *
from menu import *

def start_authentication(conn):
    root = Tk()
    root.geometry("300x150")
    root.title('Authentication Screen')

    page_title = Label(root, text="  AUTHENTICATE", font=("Courier bold", 25))
    page_title.grid(column=5, row=0)

    login = Button(root, bg="blue", fg="white", text="LOGIN",font=("Courier bold", 30), command=lambda: trigger_auth(root, conn)) #client_login(root))
    login.grid(column=5, row=6)

    root.mainloop()

def trigger_auth(top_screen, conn):
    if send_authenticate(conn):
        print("Authentication triggered")
        #vaultScreen(top_screen)
        menuScreen(top_screen, conn)
    else:
        print("Authentication failed")