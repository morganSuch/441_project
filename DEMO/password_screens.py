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

    submit = Button(window, text="SUBMIT",font=("Courier bold", 20), bg = "#C9BE62", fg ="white", height=1, width=10, command=lambda window=window: get_input(window, fields, conn, "add"))
    submit.grid(column=2, row=5)


def deleteScreen(root, conn):
    window = Toplevel(root)
    window.geometry('325x300')
    window.title("Delete Password")

    fields = []

    page_title = Label(window, text="   DELETE PASSWORD", font=("Courier bold", 20))
    page_title.grid(column=1, row=0)

    # Identifier
    id_tag = Label(window, text="Please enter the application name\n for the entry you wish to delete.\n", font=("Courier bold", 12))
    id_tag.grid(column=1, row=2)

    id = Text(window, height=1, width=20)
    id.grid(column=1, row=3)
    
    fields.append(id)
    blank = Label(window, text="", font=("Courier bold", 10))
    blank.grid(column=0, row=4)

    submit = Button(window, text="DELETE",font=("Courier bold", 20), bg = "#C24641", fg ="white", height=1, width=10, command=lambda window=window: get_input(window, fields, conn, "delete"))
    submit.grid(column=1, row=5)

def modifyScreen(root, conn):
    window = Toplevel(root)
    window.geometry('500x325')
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
    field1 = Label(window, text="Update Field", font=("Courier bold", 15))
    field1.grid(column=1, row =3)
    field2 = Label(window, text="Please enter 'username' or 'password'", font=("Courier bold", 10))
    field2.grid(column=2, row=4)
    field = Text(window, height=1, width=20)
    field.grid(column=2, row=3)

    password_tag = Label(window, text="New Value", font=("Courier bold", 15))
    password_tag.grid(column=1, row=5)
    password = Text(window, height=1, width=20)
    password.grid(column=2, row=5)

    password_tag2 = Label(window, text="Confirm Value", font=("Courier bold", 15))
    password_tag2.grid(column=1, row=6)
    password2 = Text(window, height=1, width=20)
    password2.grid(column=2, row=6)

    fields =[id, password, field]
    print("selected: ", value_to_update)

    submit = Button(window, text="SUBMIT",font=("Courier bold", 20), bg = "#6960EC", fg ="white", height=1, width=10, command=lambda window=window: modify_input(window, fields, conn, value_to_update, password2))
    submit.grid(column=2, row=7)    

def get_input(window, fields, conn, function):
    input_list = []
    out = Label(window, text="\n              Required field is missing.                 \nPlease fill in all fields and try again.\n", font=("Courier bold", 12), fg="red")
    for field in fields:
        input = field.get("1.0", "end-1c")       
        if input == "": 
            if function == "add":
                out.grid(column=2, row=6)
            else:
                out.grid(column=1, row=6)
            return
        else:
            input_list.append(input)
            print(input)
            
    if function == "add":
        if send_password(input_list,conn):
            result = Label(window, text="\n         Password successfully added     \n\n", font=("Courier bold", 12), fg="green")
            result.grid(column=2, row=6)
        else:
            result = Label(window, text="\n     Error adding password to database.\n", font=("Courier bold", 12), fg="red")
            result.grid(column=2, row=6)
    elif function == "delete":
        if delete_password(input_list, conn):
            result = Label(window, text="\n     Password successfully deleted               \n\n", font=("Courier bold", 12), fg="green")
            result.grid(column=1, row=6, padx=50)
        else:
            result = Label(window, text="\n     Error removing password from database.\n Please ensure the password you \nare attempting to remove exists.", font=("Courier bold", 12), fg="red")
            result.grid(column=1, row=6)

def modify_input(window, fields, conn, val, check):
    input_list = []
    out = Label(window, text="\n             Required field is missing.                   \nPlease fill in all fields and try again.\n", font=("Courier bold", 12), fg="red")
    for field in fields:
        input = field.get("1.0", "end-1c")
        if input == "":
            out.grid(column=2, row=8)
            return
        else:
            input_list.append(input)
            print(input)
    print(input_list[2])
    print(check.get("1.0", "end-1c"))
    if input_list[1] == check.get("1.0", "end-1c"):
        if edit_password(input_list, conn):
            result = Label(window, text="\n        Password successfully updated          \n\n", font=("Courier bold", 12), fg="green")
            result.grid(column=2, row=8)
        else:
            result = Label(window, text="\n     Error modifying password in database.\n Please ensure the password you \nare attempting to modify exists", font=("Courier bold", 12), fg="red")
            result.grid(column=2, row=8)
    else:
        result2 = Label(window, text="\n     Updated fields do not match. Please\nensure these values are the same \nand try again", font=("Courier bold", 12), fg="red")
        result2.grid(column=2, row=8)


# User Menu Screens
def finger_add_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.title("ADD FINGER")

    page_title = Label(window, text="Please place your finger on the \nscanner to add a new fingerprint.", font=("Courier bold", 14))
    page_title.grid(column=0, row=0)
    
    inst = Label(window, text="\nThe scanner will take two images for a new print.\n \
        After pressing the button to tigger the scan look \nfor a purple light to signify the device is ready.\n", font=("Courier bold", 12))
    inst.grid(column=0, row=1)
    
    count =1
    prints = fetch_prints(conn)
    for print in prints:
        print(print)
        print = "print"+print

        app_name = Button(window, text= str(print) ,font=("Courier bold", 12),bg="#F9F6EE", fg="#EB5406",  height=1, width=12)
        app_name.grid(column=1, row=count, padx=10)
        count += 1

    # add = Button(window, text="SCAN",font=("Courier bold", 20), bg = "#C9BE62", fg ="white",height=1, width=15,command=lambda window=window: scan_finger(window, conn))
    # add.grid(column=0, row=3)

def security_question_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x300')
    window.title("SET SECURITY QUESTION")

    page_title = Label(window, text="Please type in your new security question \nand answer to update backup authentication info.\n", font=("Courier bold", 12))
    page_title.grid(column=1, row=0)

    q = Label(window, text="Q", font=("Courier Bold", 20))
    q.grid(column=0, row=1)
    question = Text(window, height=3, width=30)
    question.grid(column=1, row=1)

    a = Label(window, text="A", font=("Courier Bold", 20))
    a.grid(column=0, row=2)
    answer = Text(window, height=1, width=30)
    answer.grid(column=1, row=2)

    add = Button(window, text="UPDATE",font=("Courier bold", 20), bg = "#C9BE62", fg ="white",height=1, width=12,command=lambda window=window: update_question(question, answer, conn, window))
    add.grid(column=1, row=3)

#Used for initial setup to bypass authentication requirement 
def security_question_screen_init(root, conn):
    window = Toplevel(root)
    window.geometry('400x300')
    window.title("SET SECURITY QUESTION")

    page_title = Label(window, text="Please type in your new security question \nand answer to update backup authentication info.\n", font=("Courier bold", 12))
    page_title.grid(column=1, row=0)

    q = Label(window, text="Q", font=("Courier Bold", 20))
    q.grid(column=0, row=1)
    question = Text(window, height=3, width=30)
    question.grid(column=1, row=1)

    a = Label(window, text="A", font=("Courier Bold", 20))
    a.grid(column=0, row=2)
    answer = Text(window, height=1, width=30)
    answer.grid(column=1, row=2)

    add = Button(window, text="UPDATE",font=("Courier bold", 20), bg = "#C9BE62", fg ="white",height=1, width=12,command=lambda window=window: update_question_init(question, answer, conn, window))
    add.grid(column=1, row=3)

def update_question(q, a, conn, window):
    entry = []
    entry.append(q.get("1.0", "end-1c"))
    entry.append(a.get("1.0", "end-1c"))
    out = Label(window, text="\nPlease make sure both fields are populated.", font=("Courier bold", 12), fg="blue")
    if entry[0] == "" or entry[1 ]== "": 
        out.grid(column=1, row=4)
    else:
        if send_finger_authenticate(conn):
            if send_question(conn,entry):
                yes = Label(window, text="\n             Question successfully updated.             \n  ", font=("Courier bold", 12), fg="green")
                yes.grid(column=1, row=4)
                print("Success")
            else:
                out.grid_forget()
                no = Label(window, text="\nQuestion could not be updated, some error occured.\n Please try again.", font=("Courier bold", 12), fg="red")
                no.grid(column=1, row=4)
                print("fail")
        else:
            no1 = Label(window, text="\nAuthentication failed, question could not be updated.\n Please try again.", font=("Courier bold", 12), fg="red")
            no1.grid(column=1, row=4)

#Used for initial setup to bypass authentication requirement 
def update_question_init(q, a, conn, window):
    entry = []
    entry.append(q.get("1.0", "end-1c"))
    entry.append(a.get("1.0", "end-1c"))
    out = Label(window, text="\nPlease make sure both fields are populated.", font=("Courier bold", 12), fg="blue")
    if entry[0] == "" or entry[1 ]== "": 
        out.grid(column=1, row=4)
    else:
        if send_question(conn,entry):
            yes = Label(window, text="\n             Question successfully updated.             \n  ", font=("Courier bold", 12), fg="green")
            yes.grid(column=1, row=4)
            print("Success")
        else:
            out.grid_forget()
            no = Label(window, text="\nQuestion could not be updated, some error occured.\n Please try again.", font=("Courier bold", 12), fg="red")
            no.grid(column=1, row=4)
            print("fail")

def finger_rem_screen(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.title("REMOVE FINGER")

    page_title = Label(window, text="Please select a fingerprint to delete.", font=("Courier bold", 14))
    page_title.grid(column=0, row=0)

    sub = Label(window, text="NOTE: The primary print used when\nsetting up the device can not be removed.", font=("Courier bold", 12), fg="#3B9C9C")
    sub.grid(column=0, row=1)
    
    count =2
    prints = fetch_prints(conn)
    #prints = [1,2,3,4]
    prints.pop(0)
    
    if len(prints) == 0:
        out = Label(window, text="There is only one registered print.\n This can not be removed.", font=("Courier bold", 14), fg="#C24641")
        out.grid(column=0, row=1)
    else:
        for p in prints:
            p = str(p)
            p_id = "print "+ p
            p_id = Button(window, text= p ,font=("Courier bold", 20),bg="#C9BE62", fg="white",  height=1, width=5, command=lambda entry=p, window=window: delete_print(conn, window, entry))
            p_id.grid(column=0, row=count, padx=10)
            count += 1
    
def face_add_screen(root, conn):
    window = Toplevel(root)
    window.geometry('425x325')
    window.title("ADD FACE")

    page_title = Label(window, text="Please enter a name for the new \nface and press capture.\n", font=("Courier bold", 14))
    page_title.grid(column=0, row=0)

    inst = Label(window, text="After pressing capture the camera will be active\n \
        for 5 seconds before taking the photo. \nPlease ensure your face is properly positioned in the frame.\n", font=("Courier bold", 12))
    inst.grid(column=0, row=1)

    id = Text(window, height=1, width=20)
    id.grid(column=0, row=2)
    
    blank = Label(window, text="", font=("Courier bold", 10))
    blank.grid(column=0, row=3)

    add = Button(window, text="CAPTURE",font=("Courier bold", 20), bg = "#C9BE62", fg ="white",height=1, width=12,command=lambda window=window: take_photo(window, conn, id))
    add.grid(column=0, row=4)

def face_rem_screen(root, conn):
    window = Toplevel(root)
    window.geometry('350x200')
    window.title("REMOVE FACE")

    page_title = Label(window, text="Please enter the image ID for the\n face you wish to remove.", font=("Courier bold", 14))
    page_title.grid(column=0, row=0, padx=20)

    id = Text(window, height=1, width=20)
    id.grid(column=0, row=2)
    
    blank = Label(window, text="", font=("Courier bold", 10))
    blank.grid(column=0, row=3)

    add = Button(window, text="DELETE",font=("Courier bold", 20), bg = "#6960EC", fg ="white",height=1, width=12,command=lambda window=window: remove_image(conn, window, id))
    add.grid(column=0, row=4, padx=20)


def take_photo(window, conn, id):
    input = id.get("1.0", "end-1c")
    out = Label(window, text="\nNo name was given. \nPlease enter an image ID and try again.", font=("Courier bold", 12), fg="blue")
    if input == "": 
        out.grid(column=0, row=5)
    else:
        if capture_image(conn, input):
            yes = Label(window, text="\n             Face successfully added.             \n  ", font=("Courier bold", 12), fg="green")
            yes.grid(column=0, row=5)
            print("Success")
        else:
            out.grid_forget()
            no = Label(window, text="\nFingerprint could not be added, some error occured.\n Please try again.", font=("Courier bold", 12), fg="red")
            no.grid(column=0, row=5)
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

    add = Button(window, text="GENERATE",font=("Courier bold", 20), bg = "#C9BE62", fg ="white",height=1, width=12,command=lambda window=window: password_gen(window, conn, id))
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

    blank = Label(window, text="\nNew Password", font=("Courier bold", 14), fg="#3B9C9C")
    blank.grid(column=0, row=4)
    new_pass = Text(window, height=1, width=len)
    new_pass.insert(0.0, password)
    new_pass.grid(column=0, row=5)

def delete_print(conn, window, entry):
    if (True):
        out = Label(window, text="Fingerprint successfully removed.", font=("Courier bold", 14), fg="green")
        out.grid(column=0, row=5)
    else:
        out = Label(window, text="Fail!", font=("Courier bold", 14), fg="#C24641")
        out.grid(column=0, row=4)

def remove_image(conn, window, id):
    id = id.get("1.0", "end-1c")
    if remove_face(conn, id):
        out = Label(window, text="Face successfully removed.", font=("Courier bold", 12), fg="green")
        out.grid(column=0, row=5)
    else:
        out = Label(window, text="Unable to remove face,\nplease make ensure image ID exists.", font=("Courier bold", 12), fg="#C24641")
        out.grid(column=0, row=5)
