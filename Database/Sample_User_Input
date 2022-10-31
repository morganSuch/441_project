import  sqlite3
conn  =  sqlite3 . connect ( 'mydatabase.db' )
cursor  =  conn.cursor ()
#create the salesman table 
cursor.execute("CREATE TABLE salesman(salesman_id n(5), name char(30), city char(35), commission decimal(7,2));")

s_id = input('Salesman ID:')
s_name = input('Name:')
s_city = input('City:')
s_commision = input('Commission:')
cursor.execute("""
INSERT INTO salesman(salesman_id, name, city, commission)
VALUES (?,?,?,?)
""", (s_id, s_name, s_city, s_commision))
conn.commit ()
print ( 'Data entered successfully.' )
conn . close ()
if (conn):
  conn.close()
  print("\nThe SQLite connection is closed.")
