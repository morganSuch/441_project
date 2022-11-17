#!/usr/bin/python
#from ssl import _PasswordType
from tkinter import *
import tkinter as tk
from server_functions import *

password_names = ["password 1", "password 2", "password 3", "password 4"]

# For storing button locations when passwords need to be shown
button_dict = {}

def vaultScreen(root, conn):
    window = Toplevel(root)
    window.geometry('500x500')
    window.title("Password Manager")
    page_title = Label(window, text="VAULT", font=("Courier bold", 50))
    page_title.grid(column=1, row=0)
    password_names= fetch_application_names(conn)

    count = 1
    for name in password_names:
        print(name)
        pass_text = "pass"+name
        hide_button = "new"+name
        app_name = "app"+name
        pass_text = Text(window, height=1, borderwidth=5, width= 15, font=20)
        app_name = Button(window, text= name ,font= 15,  height=1, width=15, command=lambda name =name: copy_click(pass_text, hide_button, button_dict, name, conn))
        app_name.grid(column=0, row=count)
        hide_button = Button(window, text="hide",font= 15, command=lambda pass_text = pass_text, name = name, hide_button = hide_button: hide_password(hide_button, window, pass_text, name, button_dict))
        button_dict[name] = count
        count += 1
    
    window.geometry('500x500')
    window.mainloop()

# function for showing password
def copy_click(new_output, hide, dict, name, conn):
    grid_val = dict[name]
    secret = fetch_password(conn, name)
    new_output.config(state='normal')
    new_output.delete(0.0, tk.END)
    print("secret: ", secret)
    hide.grid(column=3, row=grid_val)
    new_output.insert(0.0, secret)
    new_output.grid(column=1, row=grid_val)
    new_output.configure(state='disabled')
    

# function for hiding retreived password
def hide_password(hide_button, window, password, name, dict):
    grid_val = dict[name]
    password.config(state='normal')
    password.delete(0.0, tk.END)
    password.insert(0.0, "***************")
    password.config(state='disabled')