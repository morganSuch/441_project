from multiprocessing import connection
import sqlite3

def connect_database(name) -> sqlite3.Connection:
      conn = sqlite3.connect(name)
      return conn

def delete_database(cursor):
      cursor.execute('''DROP DATABASE test.db''')
      
