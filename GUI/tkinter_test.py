#!/usr/bin/python

from curses import panel
from tkinter import *
from turtle import bgcolor, color
window = Tk()

# title on top of the window
window.title("Password Manager")

# text that can be displayed on the screen in a grid
lbl = Label(window, text="Welcome to the Vault", font=("Arial Bold", 30), bg="blue", fg="white")
lbl.grid(column=2, row=0)


# adding a text box that can be used for user input
#txt = Entry(window,width=10)
#txt.grid(column=1, row=0)
#txt.focus()

def clicked():
    lb2 = Label(window, text="show password", font=("Arial Bold", 20), bg="blue", fg="red")
    lb2.grid(column=2, row=3)

# Creating a command that will occur on a button click
def clicked():
    lbl.configure(text="Button was clicked !!", font=("Arial Bold", 20))

# def getText():
#     res = "Welcome to " + txt.get()
#     lbl.configure(text= res)

# Associating command with button click
#btn = Button(window, text="Click Me", command=clicked)
#btn.grid(column=0, row=1)
for i in range(8):
    button_text = "Password " + str(i);
    btn = Button(window, text=button_text, bg="orange", fg="red", command=clicked
    , font=("Arial Bold", 20))
    btn.grid(column=0, row=3 + i)

# btn = Button(window, text="Password 1", bg="orange", fg="red", command=clicked)
# btn.grid(column=0, row=3)

window.geometry('600x600')
window.configure(bg="blue")

window.mainloop()