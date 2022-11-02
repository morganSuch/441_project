#!/usr/bin/python

from tkinter import *
window = Tk()

# title on top of the window
window.title("Password Manager")

# text that can be displayed on the screen in a grid
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)

# adding a text box that can be used for user input
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
txt.focus()

# Creating a command that will occur on a button click
def clicked():
    lbl.configure(text="Button was clicked !!", font=("Courier", 20))

def getText():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)

# Associating command with button click
btn = Button(window, text="Click Me", command=getText)
btn.grid(column=0, row=1)

btn = Button(window, text="Click Me", bg="orange", fg="red")

window.geometry('500x500')
window.mainloop()