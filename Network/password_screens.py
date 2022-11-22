from tkinter import *
from server_functions import *
import tkinter as tk
import secrets
import string

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
    window.geometry('300x300')
    window.title("Delete Password")

    fields = []

    page_title = Label(window, text="DELETE PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=1, row=0)

    # Identifier
    id_tag = Label(window, text="Please enter the application name\n for the entry you wish to delete.\n", font=("Courier bold", 12))
    id_tag.grid(column=1, row=2)

    # name_tag = Label(window, text="Application", font=("Courier bold", 15))
    # name_tag.grid(column=1, row=3)
    id = Text(window, height=1, width=20)
    id.grid(column=1, row=3)
    
    fields.append(id)
    blank = Label(window, text="", font=("Courier bold", 10))
    blank.grid(column=0, row=4)

    submit = Button(window, text="DELETE",font=("Courier bold", 20), bg = "red", fg ="white", height=1, width=10, command=lambda: get_input(fields, conn, "delete"))
    submit.grid(column=1, row=5)

def modifyScreen(root, conn):
    window = Toplevel(root)
    window.geometry('500x250')
    window.title("Modify Password")

    page_title = Label(window, text="MODIFY PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=2, row=0)
    
    fields = []
    value_to_update = ""

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
    username_button = tk.Checkbutton(window, text = "Username", font=("Courier bold", 12), variable=user, onvalue=1, offvalue=0, command=lambda: check_user_click(value_to_update))
    password_button = tk.Checkbutton(window, text = "Password", font=("Courier bold", 12), variable=passw, onvalue=1, offvalue=0, command=lambda: check_pass_click(value_to_update))
    username_button.grid(column=2, row=3)
    password_button.grid(column=2, row=4)

    def check_user_click(val):
        if user.get():
            val = 'username'
            return val

    def check_pass_click(val):
        if passw.get():
            val = "password"
            return val

    # username = Text(window, height=1, width=20)
    # username.grid(column=2, row=3)
    # Value
    password_tag = Label(window, text="Updated Value", font=("Courier bold", 15))
    password_tag.grid(column=1, row=5)
    password = Text(window, height=1, width=20)
    password.grid(column=2, row=5)

    fields=[id, password]
    #fields =[id, password, field]

    submit = Button(window, text="SUBMIT",font=("Courier bold", 20), bg = "purple", fg ="white", height=1, width=10, command=lambda: modify_input(fields, conn, "username"))
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


def get_input(fields, conn, function):
    input_list = []
    for field in fields:
        input = field.get("1.0", "end-1c")
        input_list.append(input)
        print(input)

    if function == "add":
        send_password(input_list,conn)
    # elif function == "edit":
    #     edit_password(input_list, conn)
    elif function == "delete":
        delete_password(input_list, conn)

def modify_input(fields, conn, val):
    input_list = []

    for field in fields:
        input = field.get("1.0", "end-1c")
        input_list.append(input)
        print(input)

    print("field to modify", val)
    input_list.append(val)
    edit_password(input_list, conn)

# User Menu Screens
def finger_add_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x300')
    window.title("ADD FINGER")

    page_title = Label(window, text="Please place your finger on the \nscanner to add a new fingerprint.", font=("Courier bold", 14))
    page_title.grid(column=0, row=0)
    
    inst = Label(window, text="\nThe scanner will take two images for a new print.\n \
        After pressing the button to tigger the scan look \nfor a purple light to signify the device is ready.\n", font=("Courier bold", 12))
    inst.grid(column=0, row=2)

    add = Button(window, text="SCAN",font=("Courier bold", 20), bg = "black", fg ="white",height=1, width=15,command=lambda window=window: scan_finger(window, conn))
    add.grid(column=0, row=3)


def finger_rem_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.title("REMOVE FINGER")

    page_title = Label(window, text="Please pick a fingerprint to remove.", font=("Courier bold", 12))
    page_title.grid(column=0, row=0)

def face_add_screen(root, conn):
    window = Toplevel(root)
    window.geometry('300x250')
    window.title("ADD FACE")

    page_title = Label(window, text="Please enter a name for the new \nface and press capture.\n", font=("Courier bold", 14))
    page_title.grid(column=0, row=0)

    id = Text(window, height=1, width=20)
    id.grid(column=0, row=1)
    
    blank = Label(window, text="", font=("Courier bold", 10))
    blank.grid(column=0, row=2)

    add = Button(window, text="CAPTURE",font=("Courier bold", 20), bg = "black", fg ="white",height=1, width=12,command=lambda window=window: take_photo(window, conn, id))
    add.grid(column=0, row=3)

def face_rem_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.title("REMOVE FACE")

    page_title = Label(window, text="Add", font=("Courier bold", 10))
    page_title.grid(column=0, row=0)


def take_photo(window, conn, id):
    input = id.get("1.0", "end-1c")
    out = Label(window, text="\nNo name was given. \nPlease enter an image ID and try again.", font=("Courier bold", 12), fg="blue")
    if input == "": 
        out.grid(column=0, row=4)
    else:
        if capture_image(conn, input):
            yes = Label(window, text="\n             Face successfully added.             \n  ", font=("Courier bold", 12), fg="green")
            yes.grid(column=0, row=4)
            print("Success")
        else:
            out.grid_forget()
            no = Label(window, text="\nFingerprint could not be added, some error occured.\n Please try again.", font=("Courier bold", 12), fg="red")
            no.grid(column=0, row=4)
            print("fail")

def scan_finger(window, conn):
    if capture_finger(conn):
        yes = Label(window, text="\nFingerprint successfully added.", font=("Courier bold", 12), fg="green")
        yes.grid(column=0, row=4)
        print("Success")
    else:
        print("fail")
        no = Label(window, text="\nFingerprint could not be added, some error occured.\n Please try again.", font=("Courier bold", 12), fg="red")
        no.grid(column=0, row=4)

def gen_pass_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x300')
    window.title("PASSWORD GENERATOR")

    page_title = Label(window, text="Welcome to the password generator!\nPlease enter the desired length for your new password.\n\
        (recommended length is >10)\n", font=("Courier bold", 12))
    page_title.grid(column=0, row=0)

    id = Text(window, height=1, width=5)
    id.grid(column=0, row=1)
    
    blank = Label(window, text="", font=("Courier bold", 10))
    blank.grid(column=0, row=2)

    add = Button(window, text="GENERATE",font=("Courier bold", 15), bg = "blue", fg ="white",height=1, width=12,command=lambda window=window: password_gen(window, conn, id))
    add.grid(column=0, row=3)

def password_gen(window, conn, id):
    len = int(id.get("1.0", "end-1c"))
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    total_chars = letters + digits + special_chars

    while True:
        password = ""
        for i in range(len):
            password += "".join(secrets.choice(total_chars))
        if (any(char in special_chars for char in password) and
            sum(char in digits for char in password)>=2):
            break

    blank = Label(window, text="\nNew Password", font=("Courier bold", 14), fg="blue")
    blank.grid(column=0, row=4)
    new_pass = Text(window, height=1, width=len)
    new_pass.insert(0.0, password)
    new_pass.grid(column=0, row=5)
    # print(password)
    # return password