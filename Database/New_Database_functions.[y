#!/usr/bin/python
from multiprocessing import connection
import sqlite3

def connect_database(name) -> sqlite3.Connection:
      conn = sqlite3.connect(name)
      return conn

def create_databse(cursor):
      cursor.execute("DROP TABLE IF EXISTS PASSWORDS")

      cursor.execute('''CREATE TABLE PASSWORDS
            (APPLICATION           CARCHAR(255)    NOT NULL,
            EMAIL_USERNAME         CHAR(50)        NOT NULL,
            PASSWORD                CHAR(50));''')
      print("Table created successfully")

def update_databse(cursor, conn):
      s_app = input('Application: ')
      s_email_user = input('Email/Username: ')
      noVerify = True
      while noVerify:
            s_password = input('Password: ')
            s_password2 = input('Verify Password: ')
            if s_password == s_password2:
                        noVerify = False

      cursor.execute("""
            INSERT INTO PASSWORDS (APPLICATION,EMAIL_USERNAME,PASSWORD) \
            VALUES (?,?,?) \
            """, (s_app, s_email_user, s_password))

      conn.commit()
      print("Records created successfully")

def close_connection(conn):
      #closes SQLite connection
      if (conn):
            conn.close()


while(True):
      print("DATABASE MENU\n")
      print("1    Create a new database")
      print("2    Add records to a databse\n")

      menu_option = input("Please enter a menu option: ")
      if (menu_option == "1"):
            name = input("Enter a name for the new database: ")
            database = connect_database(name)
            cursor = database.cursor()
            create_databse(cursor)
            close_connection(database)
      if (menu_option == "2"):
            name = input("Enter a name for the new database: ")
            database = connect_database(name)
            cursor = database.cursor()
            update_databse(cursor, database)
            close_connection(database)
