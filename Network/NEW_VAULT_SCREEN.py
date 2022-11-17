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
    window.geometry('900x900')
    window.title("Password Manager")
    
    #Color different sections of the menu
    password_modifiers_background = Label(window, bg="green")
    password_modifiers_background.grid(row=0,column=0,rowspan=9,columnspan=3)
    
    vault_background = Label(window, bg="red")
    vault_background.grid(row=0,column=3,rowspan=9,columnspan=3)
    
    additional_settings_background = Label(window, bg="blue")
    additional_settings_background.grid(row=0,column=6,rowspan=9,columnspan=3)
    
    page_title = Label(window, text="VAULT", font=("Courier bold", 50))
    page_title.grid(column=4, row=0)
    
    #add buttons on left side of menu
    add = Button(window, text="ADD PASSWORD",font=("Courier bold", 20), bg = "white", fg ="blue",height=1, width=20,command=lambda: add_pass(root, conn))
    add.grid(column=1, row=2)

    delete = Button(window, text="DELETE PASSWORD",font=("Courier bold", 20), bg = "white",fg ="blue",height=1, width=20, command=lambda: delete_pass(root, conn))
    delete.grid(column=1, row=3)

    modify = Button(window, text="MODIFY PASSWORD",font=("Courier bold", 20),bg = "white", fg ="blue", height=1, width=20,command=lambda: modify_pass(root, conn))
    modify.grid(column=1, row=4)

    settings = Button(window, text="USER SETTINGS",font=("Courier bold", 20),bg = "white", fg ="blue", height=1, width=20,command=lambda: show_settings(root, conn))
    settings.grid(column=1, row=5)
    
    #functions on the right side
    generate_password = Button(window, text="GENERATE PASSWORD", font=("Courier bold",20),bg="white",fg="blue",height=1,width=20)
    generate_password.grid(column=7,row=2)
    
    password_names= fetch_application_names(conn)

    count = 1
    #add buttons in center of window for password retrieval and applications
    for name in password_names:
        print(name)
        pass_text = "pass"+name
        hide_button = "new"+name
        app_name = "app"+name
        pass_text = Text(window, height=1, borderwidth=5, width= 15, font=20)
        app_name = Button(window, text= name ,font= 15,  height=1, width=15, command=lambda name =name: copy_click(pass_text, hide_button, button_dict, name, conn))
        app_name.grid(column=3, row=count)
        hide_button = Button(window, text="Hide",font= 15, command=lambda pass_text = pass_text, name = name, hide_button = hide_button: hide_password(hide_button, window, pass_text, name, button_dict))
        #show_button = Button(window, text="Show",font= 15, command=lambda pass_text = pass_text, name = name, show_button = show_button: show_password(show_button, window, pass_text, name, button_dict))
        button_dict[name] = count
        count += 1
    
    
    window.mainloop()

# function for showing password
def copy_click(new_output, hide, dict, name, conn):
    grid_val = dict[name]
    secret = fetch_password(conn, name)
    new_output.config(state='normal')
    new_output.delete(0.0, tk.END)
    print("secret: ", secret)
    hide.grid(column=5, row=grid_val)
    new_output.insert(0.0, secret)
    new_output.grid(column=4, row=grid_val)
    new_output.configure(state='disabled')
    

# function for hiding retreived password
def hide_password(hide_button, window, password, name, dict):
    grid_val = dict[name]
    password.config(state='normal')
    password.delete(0.0, tk.END)
    password.insert(0.0, "***************")
    password.config(state='disabled')
    
"""def show_password(show_button, window, password, name, dict):
    grid_val = dict[name]
    secret = fetch_password(conn, name)
    password.config(state='normal')
    password.delete(0.0 tk.END)
    password.insert(0.0, secret)
    password.config(state='disabled')"""
