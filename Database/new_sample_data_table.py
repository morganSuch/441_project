#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")
max = 800
conn.execute("DROP TABLE IF EXISTS PASSWORDS")

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

conn.execute("DROP TABLE IF EXISTS FACIAL_RECOGNITION")

conn.execute('''CREATE TABLE FACIAL_RECOGNITION
         (NAMEID INT IDENTTITY PRIMARY KEY            NOT NULL,
         FULL_NAME               NVARCHAR(50)        NOT NULL,
         PICFILENAME             NVARCHAR(100),
         IMAGE_ID                VARBINARY(8000));''')

print("Table2 created successfully")

conn.commit()

print("Records 2 created successfully")
conn.close()
