#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE PASSWORDS
         (APPLICATION           CARCHAR(255)    NOT NULL,
         EMAIL_USERNAME         CHAR(50)        NOT NULL,
         PASSWORD                CHAR(50));''')
print("Table created successfully")


conn.execute("INSERT INTO PASSWORDS (APPLICATION,EMAIL_USERNAME,PASSWORD) \
      VALUES ('Facebook', 'georgelopez3@gmail.com', 'IamGeorgeLopez3')");

conn.execute("INSERT INTO PASSWORDS (APPLICATION,EMAIL_USERNAME,PASSWORD) \
      VALUES ('Myspace', 'gregory.bilt@gmail.com', 'biltlikegreg2')");

conn.commit()
print("Records created successfully")
conn.close()
