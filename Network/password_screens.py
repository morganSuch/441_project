from tkinter import *
from server_functions import *

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

    page_title = Label(window, text="DELETE PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=1, row=0)

def modifyScreen(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.title("Modify Password")

    page_title = Label(window, text="MODIFY PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=2, row=0)

    # Application
    id_tag = Label(window, text="Application", font=("Courier bold", 15))
    id_tag.grid(column=1, row=2)
    id = Text(window, height=1, width=20)
    id.grid(column=2, row=2)
    # Type
    name_tag = Label(window, text="Field to Update", font=("Courier bold", 15))
    name_tag.grid(column=1, row=3)
    username = Text(window, height=1, width=20)
    username.grid(column=2, row=3)
    # Value
    password_tag = Label(window, text="Updated Value", font=("Courier bold", 15))
    password_tag.grid(column=1, row=4)
    password = Text(window, height=1, width=20)
    password.grid(column=2, row=4)

    fields =[id, username, password]

    submit = Button(window, text="SUBMIT",font=("Courier bold", 20), bg = "purple", fg ="white", height=1, width=10, command=lambda: get_input(fields, conn, "edit"))
    submit.grid(column=2, row=5)    

# Function for extracting user input from text boxes
# This will most likely get pretty complex if we are checking for
# password strength and it might need its own class
def get_input(fields, conn, function):
    input_list = []
    for field in fields:
        input = field.get("1.0", "end-1c")
        input_list.append(input)
        print(input)

    if function == "add":
        send_password(input_list,conn)
    elif function == "edit":
        edit_password(input_list, conn)