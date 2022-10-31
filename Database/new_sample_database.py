#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
cursor = conn.cursor()
print("Opened database successfully")

#cursor.execute("DROP TABLE IF EXISTS PASSWORDS")

cursor.execute('''CREATE TABLE PASSWORDS
         (APPLICATION           CHAR(255)    NOT NULL,
         EMAIL_USERNAME         CHAR(50)        NOT NULL,
         PASSWORD                CHAR(50));''')
print("Table created successfully")

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
#Populating the Table
"""
cursor.execute("INSERT INTO PASSWORDS (APPLICATION,EMAIL_USERNAME,PASSWORD) \
      VALUES ('Facebook', 'georgelopez3@gmail.com', 'IamGeorgeLopez3')");

cursor.execute("INSERT INTO PASSWORDS (APPLICATION,EMAIL_USERNAME,PASSWORD) \
      VALUES ('Myspace', 'gregory.bilt@gmail.com', 'biltlikegreg2')");
"""
conn.commit()
print("Records created successfully")

#Facial Recognition Table
"""
cursor.execute("DROP TABLE IF EXISTS FACIAL_RECOGNITION")

cursor.execute('''CREATE TABLE FACIAL_RECOGNITION
         (NAMEID INT IDENTTITY PRIMARY KEY            NOT NULL,
         FULL_NAME               NVARCHAR(50)        NOT NULL,
         PICFILENAME             NVARCHAR(100),
         IMAGE_ID                VARBINARY(max));''')

print("Table2 created successfully")

conn.commit()

print("Records 2 created successfully")
"""
#closes SQLite connection
if (conn):
         conn.close()
         print("\nThe SQLite connection is closed.")
