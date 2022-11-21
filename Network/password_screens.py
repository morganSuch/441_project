from tkinter import *
from server_functions import *
import tkinter as tk

# Window for adding a password to the database
def addScreen(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.title("Add Password")

    page_title = Label(window, text="ADD PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=2, row=0)

    # Identifier
    id_tag = Label(window, text="Application", font=("Courier bold", 15))
    id_tag.grid(column=1, row=2)
    id = Text(window, height=1, width=20)
    id.grid(column=2, row=2)
    # Username
    name_tag = Label(window, text="Username", font=("Courier bold", 15))
    name_tag.grid(column=1, row=3)
    username = Text(window, height=1, width=20)
    username.grid(column=2, row=3)
    # Password
    password_tag = Label(window, text="Password", font=("Courier bold", 15))
    password_tag.grid(column=1, row=4)
    password = Text(window, height=1, width=20)
    password.grid(column=2, row=4)

    fields =[id, username, password]

    submit = Button(window, text="SUBMIT",font=("Courier bold", 20), bg = "orange", fg ="white", height=1, width=10, command=lambda: get_input(fields, conn, "add"))
    submit.grid(column=2, row=5)


def deleteScreen(root, conn):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title("Delete Password")

    fields = []

    page_title = Label(window, text="DELETE PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=1, row=0)

    # Identifier
    id_tag = Label(window, text="Please enter the application name\n for the entry you wish to delete.", font=("Courier bold", 15))
    id_tag.grid(column=1, row=2)

    name_tag = Label(window, text="Application", font=("Courier bold", 15))
    name_tag.grid(column=1, row=3)
    id = Text(window, height=1, width=20)
    id.grid(column=2, row=3)
    
    fields.append(id)
    submit = Button(window, text="DELETE",font=("Courier bold", 20), bg = "red", fg ="white", height=1, width=10, command=lambda: get_input(fields, conn, "delete"))
    submit.grid(column=2, row=4)

def modifyScreen(root, conn):
    window = Toplevel(root)
    window.geometry('500x250')
    window.title("Modify Password")

    page_title = Label(window, text="MODIFY PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=2, row=0)
    
    fields = []
    # Application
    id_tag = Label(window, text="Application", font=("Courier bold", 15))
    id_tag.grid(column=1, row=2)
    id = Text(window, height=1, width=20)
    id.grid(column=2, row=2)
    fields.append(id)

    # Type
    user = tk.IntVar()
    passw = tk.IntVar()
    name_tag = Label(window, text="Field to Update", font=("Courier bold", 15))
    name_tag.grid(column=1, row=3)
    username_button = tk.Checkbutton(window, text = "Username", font=("Courier bold", 12), variable=user, onvalue=1, offvalue=0, command=lambda: check_user_click(fields))
    password_button = tk.Checkbutton(window, text = "Password", font=("Courier bold", 12), variable=passw, onvalue=1, offvalue=0, command=lambda: check_pass_click(fields))
    username_button.grid(column=2, row=3)
    password_button.grid(column=2, row=4)

    def check_user_click(fields):
        if user.get():
            field = "username"
            print(field)
            fields.append(field)

    def check_pass_click(fields):
        if passw.get():
            field = "password"
            print(field)
            fields.append(field)

    # username = Text(window, height=1, width=20)
    # username.grid(column=2, row=3)
    # Value
    password_tag = Label(window, text="Updated Value", font=("Courier bold", 15))
    password_tag.grid(column=1, row=5)
    password = Text(window, height=1, width=20)
    password.grid(column=2, row=5)

    fields.append(password)
    #fields =[id, password, field]

    submit = Button(window, text="SUBMIT",font=("Courier bold", 20), bg = "purple", fg ="white", height=1, width=10, command=lambda: get_input(fields, conn, "edit"))
    submit.grid(column=2, row=6)    

# We are most likely going to have to set this up upon the inital
# login so there is a variable set. Every time authentication is triggered
# we need to check this value
def settings_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.title("Advanced User Settings")

    page_title = Label(window, text="SETTINGS", font=("Courier bold", 20))
    page_title.grid(column=0, row=0)




# Function for extracting user input from text boxes
# This will most likely get pretty complex if we are checking for
# password strength and it might need its own class
def get_input(fields, conn, function):
    input_list = []
    for field in fields:
        input = field.get("1.0", "end-1c")
        input_list.append(input)
        print(input)
    # id = fields[0].get("1.0", "end-1c")
    # print("id ", id)
    # input_list.append(id)
    
    # print("choose ", fields[1])
    # input_list.append(fields[1])
    
    # value = fields[2].get("1.0", "end-1c")
    # print("value ", value)
    # input_list.append(value)

    if function == "add":
        send_password(input_list,conn)
    elif function == "edit":
        edit_password(input_list, conn)
    elif function == "delete":
        delete_password(input_list, conn)

# def sendUpdatedAuth(conn, value):

