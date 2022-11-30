#!/usr/bin/python
#from ssl import _PasswordType
from tkinter import *
import tkinter as tk
from server_functions import *
from password_screens import *
import threading

# For storing button locations when passwords need to be shown
button_dict = {}

def vaultScreen(root, conn):
    window = Toplevel(root)
    window.geometry('850x490')
    left = tk.Canvas(window, bg='#CECECE')
    left.place(x=-1,y=-1, width=200, height=1000 )
    middle = tk.Canvas(window, bg="#52595D")
    middle.place(x=190,y=-1, width=600, height=1000 )
    right = tk.Canvas(window, bg="#CECECE")
    right.place(x=590,y=-1, width=900, height=1000 )
    header = tk.Canvas(window, bg='#52595D')
    header.place(x=-1,y=-1, width=1000, height=90 )



    def hide(conn):
        window.withdraw()
        send_logout(conn)

    # Setting delay time for lockout function
    lockout_time = 30
    start_time = threading.Timer(lockout_time, hide)
    start_time.start()

    window.title("Password Manager")
    page_title = Label(window, text="VAULT", font=("Courier bold", 40), bg='#52595D', fg='white')
    page_title.grid(column=2, row=0, pady=10)
    password_names= fetch_application_names(conn)

    # LEFT COLUMN BUTTONS
    pass_title = Label(window, text="\nPassword Menu", font=("Courier bold", 15), bg='#CECECE', fg="black")
    pass_title.grid(column=0, row=1)

    add = Button(window, text="ADD",font=("Courier bold", 12), bg = "#3B9C9C", fg ="white",height=1, width=15,command=lambda: add_pass(root, conn))
    add.grid(column=0, row=2, padx=20)

    delete = Button(window, text="DELETE",font=("Courier bold", 12), bg = "#3B9C9C",fg ="white",height=1, width=15, command=lambda: delete_pass(root, conn))
    delete.grid(column=0, row=3, padx=20)

    modify = Button(window, text="MODIFY",font=("Courier bold", 12),bg = "#3B9C9C", fg ="white", height=1, width=15,command=lambda: modify_pass(root, conn))
    modify.grid(column=0, row=4, padx=20)

    user_title = Label(window, text="\nUser Menu", font=("Courier bold", 15), bg='#CECECE', fg="black")
    user_title.grid(column=0, row=6)    
    
    add1 = Button(window, text="ADD FINGER",font=("Courier bold", 12), bg = "#6495ED", fg ="white",height=1, width=15,command=lambda: add_finger(root, conn))
    add1.grid(column=0, row=7, padx=20)

    delete1 = Button(window, text="REMOVE FINGER",font=("Courier bold", 12), bg = "#6495ED", fg ="white",height=1, width=15,command=lambda: remove_finger(root, conn))
    delete1.grid(column=0, row=8, padx=20)

    add2 = Button(window, text="ADD FACE",font=("Courier bold", 12), bg = "#6495ED", fg ="white",height=1, width=15,command=lambda: add_face(root, conn))
    add2.grid(column=0, row=9, padx=20)
    
    delete2 = Button(window, text="REMOVE FACE",font=("Courier bold", 12), bg = "#6495ED", fg ="white",height=1, width=15,command=lambda: remove_face(root, conn))
    delete2.grid(column=0, row=10, padx=20)

    # Right side column
    func_title = Label(window, text="Tools/Settings", font=("Courier bold", 15), bg="#CECECE", fg="black")
    func_title.grid(column=5, row=1, padx=40)

    gen = Button(window, text="GENERATE PASSWORD",font=("Courier bold", 12), bg = "white", fg ="#C24641",height=1, width=20,command=lambda: gen_pass(root, conn))
    gen.grid(column=5, row=2, padx=40)

    gen = Button(window, text="SECURITY QUESTION",font=("Courier bold", 12), bg = "white", fg ="#C24641",height=1, width=20,command=lambda: security_question_screen_init(root, conn))
    gen.grid(column=5, row=3, padx=40)

    lock = Button(window, text="LOGOUT",font=("Courier bold", 12), bg = "white", fg ="#C24641",height=1, width=20,command=lambda window=window: hide_screen(conn))
    lock.grid(column=5, row=4, padx=40)

    ref = Button(window, text="REFRESH",font=("Courier bold", 12), bg = "white", fg ="#C24641",height=1, width=20,command=lambda window=window: reset(root, window, conn))
    ref.grid(column=5, row=5, padx=40)

    gen1 = Button(window, text="CLOSE APPLICATION",font=("Courier bold", 12), bg = "white", fg ="#C24641",height=1, width=20,command=lambda window=window: send_close(window, conn))
    gen1.grid(column=5, row=6, padx=40)
    
    # MIDDLE COLUMN
    count = 2

    user_title = Label(window, text="Application", font=("Courier bold", 17), bg='#52595D', fg="white")
    user_title.grid(column=1, row=1)
    # Password Vault
    for name in password_names:
        print(name)
        pass_text = "pass"+name
        hide_button = "new"+name
        app_name = "app"+name
        user_name = "user"+name

        pass_text = Text(window, height=1, borderwidth=5, width= 15, font=("Courier bold", 12))
        user_name = Text(window, height=1, borderwidth=5, width= 15, font=("Courier bold", 12))
        
        app_name = Button(window, text= name ,font=("Courier bold", 12),bg="#F9F6EE", fg="#EB5406",  height=1, width=12, command=lambda name =name: copy_click(pass_text, hide_button, button_dict, name, conn, user_name))
        app_name.grid(column=1, row=count, padx=10)
        hide_button = Button(window, text="Hide",font=("Courier bold", 12), bg="white", fg='black', command=lambda pass_text = pass_text, name = name, hide_button = hide_button: hide_password(hide_button, window, pass_text, name, button_dict))
        #show_button = Button(window, text="Show",font= 15, command=lambda pass_text = pass_text, name = name, show_button = show_button: show_password(show_button, window, pass_text, name, button_dict))
        button_dict[name] = count
        count += 2
 
    space = Label(window, text="xHidex",font=("Courier bold", 12), bg="#52595D", fg='#52595D')
    space.grid(row=20, column=3)
    space1 = Label(window, text="xxxxxxxxxxxxxxx",font=("Courier bold", 12), bg="#52595D", fg='#52595D')
    space1.grid(row=20, column=2)
    space2 = Label(window, text="xxxxxxxxxxxxxxx",font=("Courier bold", 12), bg="#52595D", fg='#52595D')
    space2.grid(row=20, column=1, padx=20)

    window.mainloop()

# function for showing password
def copy_click(new_output, hide, dict, name, conn, user):
    grid_val = dict[name]

    secret = fetch_password(conn, name)
    user_name = fetch_name(conn, name)

    user.config(state='normal')
    user.delete(0.0, tk.END)
    user.insert(0.0, user_name)
    user.grid(column=2, row=grid_val)
    user.configure(state='disabled')
    new_output.config(state='normal', fg="black")
    new_output.delete(0.0, tk.END)

    hide.grid(column=3, row=grid_val+1)
    new_output.insert(0.0, secret)
    new_output.grid(column=2, row=grid_val+1)
    new_output.configure(state='disabled')
    

# function for hiding retreived password
def hide_password(hide_button, window, password, name, dict):
    grid_val = dict[name]
    password.config(state='normal')
    password.delete(0.0, tk.END)
    password.insert(0.0, "***********************")
    password.config(state='disabled', fg="#C24641")

# functions for all button operations

# Password menu
def add_pass(root, conn):
    addScreen(root, conn)

def delete_pass(root, conn):
    deleteScreen(root, conn)

def modify_pass(root, conn):
    modifyScreen(root, conn)

# User Menu
def add_finger(root, conn):
    finger_add_screen(root, conn)

def remove_finger(root, conn):
    finger_rem_screen(root, conn)

def add_face(root, conn):
    face_add_screen(root, conn)

def remove_face(root, conn):
    face_rem_screen(root, conn)

def gen_pass(root, conn):
    gen_pass_screen(root, conn)

def set_security_question(root, conn):
    security_question_screen(root, conn)

def hide_screen(window):
    #if send_encrypt(conn):
    window.withdraw()

def reset(root, window, conn):
    window.withdraw()
    vaultScreen(root, conn)

def send_close(window, conn):
    window.withdraw()
    end_connection(conn)
