#!/usr/bin/python
import logging
from tkinter import *
from vault import *
from server_functions import *
from password_screens import *

default_login_method = "finger"

# Main function for bringing up application login screen
def start_authentication(conn):
    root = Tk()
    root.geometry("375x225")
    root.configure(bg='#52595D')
    root.title('Authentication Screen')
    
    fake_window = Toplevel(root)
    fake_window.withdraw()

    # bg = grey     fg = white
    page_title = Label(root, text="LOGIN", font=("Courier bold", 40), bg='#52595D', fg='white')
    page_title.grid(column=0, row=0)

    inst = Label(root, text="Please select your preferred authentication method.\n", font=("Courier bold", 12), bg='#52595D', fg='white')
    inst.grid(column=0, row=1)

    login_finger = Button(root, bg="white", fg="#3B9C9C", text="Finger",font=("Courier bold", 20), width=15, command=lambda: trigger_finger_auth(root, conn, fake_window)) #client_login(root))
    login_finger.grid(column=0, row=2)

    login_face = Button(root, bg="white", fg="#6495ED", text="Face",font=("Courier bold", 20), width=15, command=lambda: trigger_face_auth(root, conn, fake_window)) #client_login(root))
    login_face.grid(column=0, row=3)

    root.mainloop()

# When login button is pressed,triggers send_authenticate server function
# to make authentication request to server
def trigger_finger_auth(top_screen, conn, win2):
    win2.withdraw()
    window = Toplevel(top_screen)
    window.geometry('400x250')
    window.configure(bg='#52595D')
    first_auth = Label(window, text="Attempting to authenticate finger.\nPlease place finger directly on the scanner.", font=("Courier bold", 15), bg="#52595D", fg="white")
    first_auth.grid(column=0, row=0)
    if send_finger_authenticate(conn):
        yes = Label(window, text="Successful Authentication", font=("Courier bold", 15))
        yes.grid(column=0, row=0)
        window.withdraw()
        print("Authentication triggered")
        #vaultScreen(top_screen)
        vaultScreen(top_screen, conn)
    else:
        print("Authentication failed, trying backup method")
        second_auth = Label(window, text="\nPrimary authentication method failed.\nPlease use camera to attempt backup authentication.\n", font=("Courier bold", 12), fg="#C24641", bg="#52595D")
        second_auth.grid(column=0, row=1)
        login_face = Button(window, bg="white", fg="#6495ED", text="Face",font=("Courier bold", 17), width=15, command=lambda win2=window: trigger_face_auth(window, conn, win2)) #client_login(root))
        login_face.grid(column=0, row=2)
        question = Button(window, bg="white", fg="#3B9C9C", text="Security Question",font=("Courier bold", 17), width=15, command=lambda: backup_question(window, conn)) #client_login(root))
        question.grid(column=0, row=3)

def trigger_face_auth(top_screen, conn, win2):
    win2.withdraw()
    window = Toplevel(top_screen)
    window.geometry('400x250')
    window.configure(bg='#52595D')
    first_auth = Label(window, bg="#52595D", fg="white", text="\nAttempting to authenticate face.\nPlease look directly at the camera.", font=("Courier bold", 15))
    first_auth.grid(column=0, row=0, padx=20)
    if send_face_authenticate(conn):
        yes = Label(window, text="Successful Authentication", font=("Courier bold", 15))
        yes.grid(column=0, row=0)
        window.withdraw()
        print("Authentication triggered")
        #vaultScreen(top_screen)
        vaultScreen(top_screen, conn)
    else:
        second_auth = Label(window, fg="#C24641", bg="#52595D", text="Primary authentication method failed.\nPlease use a backup method for authentication.\n", font=("Courier bold", 12))
        second_auth.grid(column=0, row=1, padx=20)
        login_finger = Button(window, bg="white", fg="#3B9C9C", text="Finger",font=("Courier bold", 17), width=15, command=lambda win2=window: trigger_finger_auth(window, conn, win2)) #client_login(root))
        login_finger.grid(column=0, row=2, padx=20)
        question = Button(window, bg="white", fg="#3B9C9C", text="Security Question",font=("Courier bold", 17), width=15, command=lambda: backup_question(window, conn)) #client_login(root))
        question.grid(column=0, row=3, padx=20)

# Setup Method
# Main function for bringing up application login screen
def run_setup(conn):
    root = Tk()
    root.geometry("390x350")
    root.configure(bg='#52595D')
    root.title('Setup Screen')

    # bg = grey     fg = white
    page_title = Label(root, text="INITIAL SETUP", font=("Courier bold", 30), bg='#52595D', fg='white')
    page_title.grid(column=0, row=0, padx=20)

    inst = Label(root, text="Please follow the prompts to setup your device.\n", font=("Courier bold", 12), bg='#52595D', fg='white')
    inst.grid(column=0, row=1, padx=20)

    inst1 = Label(root, text="When finished close this window to trigger\n an initial authentication.", font=("Courier bold", 12), bg='#52595D', fg='white')
    inst1.grid(column=0, row=2, padx=20)
    
    finger = Button(root, bg="#FF5F1F", fg="white", text="ADD FINGER",font=("Courier bold", 20), width=15, command=lambda: finger_add_screen(root, conn)) #client_login(root))
    finger.grid(column=0, row=3, padx=20)

    face = Button(root, bg="#6495ED", fg="white", text="ADD FACE",font=("Courier bold", 20), width=15, command=lambda: face_add_screen(root, conn)) #client_login(root))
    face.grid(column=0, row=4, padx=20)

    question = Button(root, bg="#3B9C9C", fg="white", text="ADD BACKUP",font=("Courier bold", 20), width=15, command=lambda: security_question_screen_init(root, conn)) #client_login(root))
    question.grid(column=0, row=5, padx=20)

    root.mainloop()

def backup_question(root, conn):
    window = Toplevel(root)
    window.geometry('400x250')
    window.configure(bg='#52595D')
    # Get question and answer from client
    # print out question as a label
    page_title = Label(window,bg="#52595D", fg="white", text="Please answer the security question\nfor backup authentication\n", font=("Courier bold", 12))
    page_title.grid(column=1, row=0)

    backup_info = fetch_question(conn)
    question= backup_info[0]
    real = backup_info[1]

    q = Label(window, bg="#52595D", fg="white", text="Q:", font=("Courier Bold", 20))
    q.grid(column=0, row=1, padx=10)
    q1 = Label(window, bg="#52595D", fg="white", text=question[0], font=("Courier Bold", 14))
    q1.grid(column=1, row=1, padx=10)

    a = Label(window, bg="#52595D", fg="white", text="A:", font=("Courier Bold", 20))
    a.grid(column=0, row=2, padx=10)
    answer = Text(window, height=1, width=30)
    answer.grid(column=1, row=2, padx=10)

    add = Button(window, text="LOGIN",font=("Courier bold", 20), bg = "#FF5F1F", fg ="white",height=1, width=12,command=lambda window=window: validate_backup(root, conn, answer, real, window))
    add.grid(column=1, row=3)

    # Extract text from box and compare with answer

def validate_backup(root, conn, answer, real, window):
    answer = answer.get("1.0", "end-1c")
    print(answer)
    print(real)
    if answer == real[0]:
        window.withdraw()
        vaultScreen(root, conn)
    else:
        second_auth = Label(window, fg="#C24641", bg="#52595D", text="Answers do not match.\nPlease try again or try another method.\n", font=("Courier bold", 12))
        second_auth.grid(column=1, row=4, padx=20)
        window.geometry("400x420")
        fail = Label(window, fg="white", bg="#52595D", text="If you are unable to to access the device\nyou can perform a hard reset.", font=("Courier bold", 12))
        fail2 = Label(window, fg="#C24641", bg="#52595D", text="WARNING: This will clear all saved data.", font=("Courier bold", 12))
        fail.grid(column=1, row=5, padx=20)
        
        fail2.grid(column=1, row=6, padx=20)
        reset = Button(window, text="RESET",font=("Courier bold", 20), bg = "white", fg ="black",height=1, width=12,command=lambda window=window: reset_device(conn, window))
        reset.grid(column=1, row=7)

def reset_device(conn, window):
    if trigger_reset(conn):
        window.withdraw()
        print("cleared")
    else:
        print("failed")


