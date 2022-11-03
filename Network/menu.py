#!/usr/bin/python
import logging
from tkinter import *
from vault import *
from print_functions import *

def authenticate():
    root = Tk()
    root.geometry("300x150")
    root.title('Authentication Screen')

    page_title = Label(root, text="  AUTHENTICATE", font=("Courier bold", 25))
    page_title.grid(column=5, row=0)

    login = Button(root, bg="blue", fg="white", text="LOGIN",font=("Courier bold", 30), command=lambda: trigger_auth(root)) #client_login(root))
    login.grid(column=5, row=6)

    root.mainloop()

def client_login(top_screen):
    vaultScreen(top_screen)
    trigger_auth()

def trigger_auth(top_screen) -> bool:
    if testAuthenticate():
        print("Authentication triggered")
        vaultScreen(top_screen)
        return True
    else:
        print("Authentication failed")
        return False