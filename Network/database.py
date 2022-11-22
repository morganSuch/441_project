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

      cursor.execute('''CREATE TABLE FACES
      (IMAGE_ID     INT   IDENTITY    PRIMARY KEY NOT NULL,
      IMAGE                BLOB);''')
      
      print("Facial Recognition Table created successfully.\n")


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
                              SET EMAIL_USERNAME = ? \
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
      SELECT EMAIL_USERNAME
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

def get_images(cursor, conn) -> list:
      cursor.execute("""
      SELECT IMAGE
      FROM FACES """)
      
      images = cursor.fetchall()
      image_list = []
      
      for x in images:
            image_id = x[0]
            image = x[1]
            #image_list.append(x[0])
            print("transferring data to disk")
            image_path = "home/faces"+image_id+".jpg"
            write_to_file(image, image_path)
            print("successfully written to disk")
      # return image_list

def close_connection(conn):
      #closes SQLite connection
      if (conn):
            conn.close()


