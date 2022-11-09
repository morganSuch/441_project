from tkinter import *

def addScreen(root, conn):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title("Add Password")

    page_title = Label(window, text="ADD PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=1, row=0)

def deleteScreen(root, conn):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title("Delete Password")

    page_title = Label(window, text="DELETE PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=1, row=0)

def modifyScreen(root, conn):
    window = Toplevel(root)
    window.geometry('400x400')
    window.title("Modify Password")

    page_title = Label(window, text="MODIFY PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=1, row=0)