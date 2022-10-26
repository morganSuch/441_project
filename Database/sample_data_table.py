import sqlite3
 
# Connecting to sqlite
# connection object
connection_obj = sqlite3.connect('geek.db')
 
# cursor object
cursor_obj = connection_obj.cursor()
 
# Drop the GEEK table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS GEEK")
 
# Creating table
table = """ CREATE TABLE Sample_table (
            Application VARCHAR(255) NOT NULL,
            Email_Username CHAR(25) NOT NULL,
            Password CHAR(25),
        ); """


 
cursor_obj.execute(table)
 
print("Table is Ready")

INSERT INTO Sample_table (Application, Email_Username, Password)
VALUES
    ('Facebook', 'georgelopez3@gmail.com', 'IamGeorgeLopez3'),
    ('Myspace', 'gregory.bilt@gmail.com', 'biltlikegreg2');

print("Table values have been inserted")

#creating picture table
table2 = """ CREATE TABLE Facial_recognition (
             NameID INT IDENTITY PRIMARY KEY NOT NULL
             Full_Name NVARCHAR(50)
             picFileName NVARCHAR(100)
             Image_ID VARBINARY (max)
        ); """
        
cursor_obj.execute(table2)

print("Table 2 is Ready")

# Close the connection
connection_obj.close()
