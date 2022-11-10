#!/usr/bin/python
from multiprocessing import connection
import sqlite3

def connect_database(name) -> sqlite3.Connection:
      conn = sqlite3.connect(name)
      return conn

def create_databse(cursor):
      cursor.execute("DROP TABLE IF EXISTS PASSWORDS")

      cursor.execute('''CREATE TABLE PASSWORDS
            (APPLICATION      CARCHAR(255)    NOT NULL,
            USERNAME    CHAR(50)        NOT NULL,
            PASSWORD    CHAR(50));''')
      print("Table created successfully\n")


# Need to add the attaching to databse here which probably needs
# to be initialized upon the client starting up
def add_password(cursor, conn, application, username, password) -> bool:
      try:
            cursor.execute("""
                  INSERT INTO PASSWORDS (APPLICATION,EMAIL_USERNAME,PASSWORD) \
                  VALUES (?,?,?) \
                  """, (application, username, password))
            conn.commit()
            print("Records created successfully")
            return True

      except:
            return False

def edit_information(cursor, conn, application, type, value) -> bool:
      appFound = False
      #while appExists:
      cursor.execute(""" SELECT EXISTS (SELECT APPLICATION FROM PASSWORDS WHERE APPLICATION = ?) """, (application,))
      if(cursor.fetchone()[0]):
            appFound = True
            #return True
      else:
            appFound= False
            #print("This application was not in our records. Please try again.\n")
      #correct_input = True
      if appFound:
            #s_changing = input('Would you like to change the email/username or password(Type "email/username" or "password")?\n')
            if type == "password":

            #s_email_user_change = "email/username"
            #if s_changing == s_password_change or s_changing == s_email_user_change:
             #     correct_input = False
           # else:
            #      print("Your input did not match 'email/username' or 'password'. Please try again.\n")
      #noVerify = True
      #while noVerify:
          #  if s_changing == s_password_change:
           #       s_password = input('New Password: ')
            #      s_password2 = input('Verify New Password: ')
             #     if s_password == s_password2:
              #          noVerify = False
                  cursor.execute("""UPDATE PASSWORDS \
                              SET PASSWORD = ? \
                              WHERE APPLICATION = ?
                              """, (value, application))
            else:
                        #print("Your new passwords did not match. Please try again.\n")            
            #if s_changing == s_email_user_change:
                  #s_email_user = input('New Email/Username: ')
                  #s_email_user2 = input('Verify New Email/Username: ')
                  #if s_email_user == s_email_user2:
                  #      noVerify = False
                  cursor.execute(""" UPDATE PASSWORDS \
                              SET EMAIL_USERNAME = ? \
                              WHERE APPLICATION = ?
                              """, (value, application))
                  #else:
                   #     print("Your new email/usernames did not match. Please try again.\n")
            conn.commit()
            print("Records successfully edited")
            return True
      else:
            return False

      
def delete_information(cursor, conn):
      noVerify = True
      while noVerify:
            s_delete = input('What application data would you like to delete? ')
            cursor.execute(""" SELECT EXISTS (SELECT APPLICATION FROM PASSWORDS WHERE APPLICATION = ?) """, (s_delete,))
            if(cursor.fetchone()[0]):
                  cursor.execute("""
                  DELETE FROM PASSWORDS
                  WHERE APPLICATION = ?
                  """, (s_delete,))
                  noVerify = False
            else:
                  print("This application was not in our records.\n")
      conn.commit()
      print("Records successfully deleted\n")     

def close_connection(conn):
      #closes SQLite connection
      if (conn):
            conn.close()


# while(True):
#       print("DATABASE MENU\n")
#       print("1    Create a new database\n")
#       print("2    Add records to a database\n")
#       print("3    Edit records in database\n")
#       print("4    Delete records in database\n")

#       menu_option = input("Please enter a menu option: ")
#       if (menu_option == "1"):
#             name = input("Enter a name for the new database: ")
#             database = connect_database(name)
#             cursor = database.cursor()
#             create_databse(cursor)
#             close_connection(database)
#       if (menu_option == "2"):
#             name = input("Enter a name for the new database: ")
#             database = connect_database(name)
#             cursor = database.cursor()
#             add_password(cursor, database)
#             close_connection(database)
#       if(menu_option == "3"):
#             name = input("Enter a name for the new database: ")
#             database = connect_database(name)
#             cursor = database.cursor()
#             edit_information(cursor, database)
#             close_connection(database)
#       if(menu_option == "4"):
#             name = input("Enter a name for the new database: ")
#             database = connect_database(name)
#             cursor = database.cursor()
#             delete_information(cursor, database)
#             close_connection(database)
