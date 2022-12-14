#!/usr/bin/python
#from ssl import _PasswordType
from tkinter import *
import tkinter as tk
from server_functions import *
from password_screens import *

# For storing button locations when passwords need to be shown
button_dict = {}

def vaultScreen(root, conn):
    window = Toplevel(root)
    window.geometry('800x500')
    left = tk.Canvas(window, bg="black")
    left.place(x=-1,y=-1, width=192, height=1000 )
    middle = tk.Canvas(window, bg="white")
    middle.place(x=192,y=-1, width=400, height=1000 )

    window.title("Password Manager")
    page_title = Label(window, text="VAULT", font=("Courier bold", 30), bg="white")
    page_title.grid(column=2, row=0)
    password_names= fetch_application_names(conn)

    # LEFT COLUMN BUTTONS
    pass_title = Label(window, text="Password\n Menu", font=("Courier bold", 15), bg="black", fg="white")
    pass_title.grid(column=0, row=0)

    add = Button(window, text="ADD",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda: add_pass(root, conn))
    add.grid(column=0, row=1)

    delete = Button(window, text="DELETE",font=("Courier bold", 12), bg = "white",fg ="black",height=1, width=20, command=lambda: delete_pass(root, conn))
    delete.grid(column=0, row=2)

    modify = Button(window, text="MODIFY",font=("Courier bold", 12),bg = "white", fg ="black", height=1, width=20,command=lambda: modify_pass(root, conn))
    modify.grid(column=0, row=3)

    user_title = Label(window, text="User Menu", font=("Courier bold", 15), bg="black", fg="white")
    user_title.grid(column=0, row=4)    
    
    add1 = Button(window, text="ADD FINGER",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda: add_finger(root, conn))
    add1.grid(column=0, row=5)

    delete1 = Button(window, text="REMOVE FINGER",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda: remove_finger(root, conn))
    delete1.grid(column=0, row=6)

    add2 = Button(window, text="ADD FACE",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda: add_face(root, conn))
    add2.grid(column=0, row=7)
    
    delete2 = Button(window, text="REMOVE FACE",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda: remove_face(root, conn))
    delete2.grid(column=0, row=8)

    func_title = Label(window, text="\nUser Functions", font=("Courier bold", 15), bg="black", fg="white")
    func_title.grid(column=0, row=9)

    gen = Button(window, text="GENERATE PASSWORD",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda: gen_pass(root, conn))
    gen.grid(column=0, row=10)

    gen = Button(window, text="LOGOUT",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda window=window: hide_screen(window))
    gen.grid(column=0, row=11)

    gen1 = Button(window, text="LOGOUT",font=("Courier bold", 12), bg = "white", fg ="black",height=1, width=20,command=lambda window=window: hide_screen(window))
    gen1.grid(column=6, row=1, padx=100)
    
    # MIDDLE COLUMN
    count = 1
    # Password Vault
    for name in password_names:
        print(name)
        pass_text = "pass"+name
        hide_button = "new"+name
        app_name = "app"+name
        user_name = "user"+name

        pass_text = Text(window, height=1, borderwidth=5, width= 15, font=("Courier bold", 12))
        user_name = Text(window, height=1, borderwidth=5, width= 15, font=("Courier bold", 12))
        
        app_name = Button(window, text= name ,font=("Courier bold", 15),  height=1, width=15, command=lambda name =name: copy_click(pass_text, hide_button, button_dict, name, conn, user_name))
        app_name.grid(column=1, row=count)
        hide_button = Button(window, text="Hide",font=("Courier bold", 12), command=lambda pass_text = pass_text, name = name, hide_button = hide_button: hide_password(hide_button, window, pass_text, name, button_dict))
        #show_button = Button(window, text="Show",font= 15, command=lambda pass_text = pass_text, name = name, show_button = show_button: show_password(show_button, window, pass_text, name, button_dict))
        button_dict[name] = count
        count += 2
 
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
    new_output.config(state='normal')
    new_output.delete(0.0, tk.END)

    hide.grid(column=4, row=grid_val+1)
    new_output.insert(0.0, secret)
    new_output.grid(column=2, row=grid_val+1)
    new_output.configure(state='disabled')
    

# function for hiding retreived password
def hide_password(hide_button, window, password, name, dict):
    grid_val = dict[name]
    password.config(state='normal')
    password.delete(0.0, tk.END)
    password.insert(0.0, "   *****************")
    password.config(state='disabled')

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

def hide_screen(window):
    window.withdraw()


