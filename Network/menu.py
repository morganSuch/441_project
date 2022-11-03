#!/usr/bin/python
import logging
from tkinter import *
from vault import *

def authenticate():
    root = Tk()
    root.geometry("300x150")
    root.title('Authentication Screen')

    page_title = Label(root, text="  AUTHENTICATE", font=("Courier bold", 25))
    page_title.grid(column=5, row=0)

    login = Button(root, bg="blue", fg="white", text="LOGIN",font=("Courier bold", 30), command=lambda: client_login(root))
    login.grid(column=5, row=6)

    root.mainloop()

def client_login(top_screen):
    vaultScreen(top_screen)
    trigger_auth()


def trigger_auth() -> bool:
    print("Authentication triggered")
    return True

authenticate()