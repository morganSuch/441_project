#!/usr/bin/python
#from ssl import _PasswordType
from tkinter import *
from vault import *
from database import *
from password_screens import *
from multiprocessing import connection
import sqlite3

def menuScreen(root, conn):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title("Main Menu")

    page_title = Label(window, text="MAIN MENU", font=("Courier bold", 45))
    page_title.grid(column=1, row=0)

    # Set variable for creating password
    #password = Text(window, height=1, borderwidth=5, width= 15, font=20)
    vault = Button(window, text="      OPEN VAULT      ",font=("Courier bold", 15), command=lambda: show_vault(root, conn))
    vault.grid(column=1, row=1)

    add = Button(window, text="   ADD PASSWORD   ",font=("Courier bold", 15), bg = "blue", fg ="white",command=lambda: add_pass(root, conn))
    add.grid(column=1, row=2)

    delete = Button(window, text="DELETE PASSWORD",font=("Courier bold", 15), bg = "blue",fg ="white", command=lambda: delete_pass(root, conn))
    delete.grid(column=1, row=3)

    modify = Button(window, text="MODIFY PASSWORD",font=("Courier bold", 15),bg = "blue", fg ="white", command=lambda: modify_pass(root, conn))
    modify.grid(column=1, row=4)

    window.geometry('500x500')
    window.mainloop()

# functions for all button operations
# TODO extract information from the input fields as text boxes

# display vault screen
def show_vault(root, conn):
    vaultScreen(root, conn)

# functions for all button operations
def add_pass(root, conn):
    addScreen(root, conn)
    database = connect_database("test.db")
    cursor = database.cursor()
    add_password(cursor, database)
    close_connection(database)

# functions for all button operations
def delete_pass(root, conn):
    deleteScreen(root, conn)
    database = connect_database("test.db")
    cursor = database.cursor()
    delete_information(cursor, database)
    close_connection(database)

# functions for all button operations
def modify_pass(root, conn):
    modifyScreen(root, conn)
    database = connect_database("test.db")
    cursor = database.cursor()
    edit_information(cursor, database)
    close_connection(database)
