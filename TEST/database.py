#!/usr/bin/python
from multiprocessing import connection
import sqlite3

def connect_database(name) -> sqlite3.Connection:
      conn = sqlite3.connect(name)
      return conn

def create_password_databse(cursor):
      cursor.execute("DROP TABLE IF EXISTS PASSWORDS")

      cursor.execute('''CREATE TABLE PASSWORDS
            (APPLICATION      VARCHAR(255)    NOT NULL,
            USERNAME    VARCHAR(50)        NOT NULL,
            PASSWORD    VARCHAR(50));''')
      
      print("Table created successfully\n")

def create_question_databse(cursor):
      cursor.execute("DROP TABLE IF EXISTS SECURITY_QUESTION")

      cursor.execute('''CREATE TABLE SECURITY_QUESTION
      (QUESTION   VARCHAR(500)      NOT NULL,
      ANSWER      VARCHAR(50)       NOT NULL);''')
      
      print("Security Question Table created successfully.\n")

def add_question(cursor, conn, question, answer) -> bool:
      try:
            cursor.execute("""
                  INSERT INTO SECURITY_QUESTION (QUESTION,ANSWER) \
                  VALUES (?,?) \
                  """, (question, answer))
            conn.commit()
            print("Records created successfully")
            return True
      except:
            return False

def delete_question(cursor, conn):
      cursor.execute("""
            DELETE FROM SECURITY_QUESTION
            """)
      conn.commit()
      print("Records successfully deleted") 
      return True

# Need to add the attaching to databse here which probably needs
# to be initialized upon the client starting up
def add_password(cursor, conn, application, username, password) -> bool:
      try:
            cursor.execute("""
                  INSERT INTO PASSWORDS (APPLICATION,USERNAME,PASSWORD) \
                  VALUES (?,?,?) \
                  """, (application, username, password))
            conn.commit()
            print("Records created successfully")
            return True

      except:
            return False

def edit_information(cursor, conn, application, type, value) -> bool:
      appFound = False
      cursor.execute(""" SELECT EXISTS (SELECT APPLICATION FROM PASSWORDS WHERE APPLICATION = ?) """, (application,))
      if(cursor.fetchone()[0]):
            appFound = True
      else:
            appFound= False
      if appFound:
            if type == "password":
                  cursor.execute("""UPDATE PASSWORDS \
                              SET PASSWORD = ? \
                              WHERE APPLICATION = ?
                              """, (value, application))
            else:
                  cursor.execute(""" UPDATE PASSWORDS \
                              SET USERNAME = ? \
                              WHERE APPLICATION = ?
                              """, (value, application))
            conn.commit()
            print("Records successfully edited")
            return True
      else:
            return False

      
def delete_information(cursor, conn, app):
      appFound = False
      cursor.execute(""" SELECT EXISTS (SELECT APPLICATION FROM PASSWORDS WHERE APPLICATION = ?) """, (app,))
      if(cursor.fetchone()[0]):
            appFound = True
      else:
            appFound = False
      if appFound:
            cursor.execute("""
                  DELETE FROM PASSWORDS
                  WHERE APPLICATION = ?
                  """, (app,))
            conn.commit()
            print("Records successfully deleted") 
            return True
      else:
            return False
          

def get_application_names(cursor, conn) -> list:
      cursor.execute("""
      SELECT APPLICATION
      FROM PASSWORDS """)
      
      applicationNamesColumn = cursor.fetchall()
      listAppNames = []
      
      for x in applicationNamesColumn:
            listAppNames.append(x[0])      
      return listAppNames

def get_question(cursor, conn) -> list:
      info = []
      cursor.execute("""
      SELECT QUESTION
      FROM SECURITY_QUESTION """)

      question = cursor.fetchone()
      info.append(question)

      cursor.execute("""
      SELECT ANSWER
      FROM SECURITY_QUESTION """)
      
      answer = cursor.fetchone()
      info.append(answer)

      return info  

def fetch_password(cursor, conn, appName):
      cursor.execute("""
      SELECT PASSWORD
      FROM PASSWORDS
      WHERE APPLICATION = ?
      """, (appName,))
      
      userPassword = cursor.fetchone()
      return userPassword  

def fetch_name(cursor, conn, appName):
      cursor.execute("""
      SELECT USERNAME
      FROM PASSWORDS
      WHERE APPLICATION = ?
      """, (appName,))
      
      userPassword = cursor.fetchone()
      return userPassword  

# Face recognition functions
def convert_to_binary(file):
      #converts the file to binary format
      with open(file, 'rb') as file:
            blobData = file.read()
      return blobData

def write_to_file(blob, file):
      with open(file, 'wb') as file:
            file.write(blob)
      print("Stored blob data into: ", file)


def add_face(cursor, conn, id, photo):
      image = convert_to_binary(photo)
      #personName = input('Who is this image authenticating? Please enter full name. ')
      #picFileName = input('What would you like this image name saved as? ')

      cursor.execute("""
            INSERT INTO FACIALREC (IMAGEID, IMAGE) \
            VALUE (?,?) \
            """, (id, image))
      conn.commit()
      print("Records created successfully")

def close_connection(conn):
      #closes SQLite connection
      if (conn):
            conn.close()


