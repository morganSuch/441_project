#!/usr/bin/python
#from ssl import _PasswordType
from tkinter import *

def vaultScreen(root):
    window = Toplevel(root)
    window.geometry('500x500')
    window.title("Password Manager")

    page_title = Label(window, text="VAULT", font=("Courier bold", 50))
    page_title.grid(column=1, row=0)

    hide = Label(window, text="***************", font=("Courier bold", 20))
    hide.grid(column=1, row=1)
    password = Text(window, height=1, borderwidth=5, width= 13, font=20)

    # Set variable for creating password
    #password = Text(window, height=1, borderwidth=5, width= 15, font=20)
    btn = Button(window, text="   password 1   ",font= 15, command=lambda: copy_click(password, window, hide, new_btn))
    btn.grid(column=0, row=1)
    new_btn = Button(window, text="hide",font= 15, command=lambda: hide_password(hide, window, password))
    window.geometry('500x500')
    window.mainloop()

# function for showing password
def copy_click(new_output, window, hide, password):
    # password = Text(window, height=1, borderwidth=5, width= 15, font=20)
    secret = "password"
    # Moving hidden text to the right
    hide.grid(column=3, row=1)
    hide.configure(text= "")
    new_output.insert(1.0, secret)
    new_output.grid(column=1, row=1)
    new_output.configure(state='disabled')
    password.grid(column=2, row=1)

# function for hiding retreived password
def hide_password(hide, window, password):
    password.insert(1.0, "new")
    password.grid(column=0, row=1)
    hide.grid(column=1, row=1)
    hide.configure(text="***************", font=("Courier bold", 20))


#vaultScreen()


    # adding a text box that can be used for user input
    # txt_box = Entry(window,width=20)
    # txt_box.grid(column=0, row=2)
    # txt_box.focus()