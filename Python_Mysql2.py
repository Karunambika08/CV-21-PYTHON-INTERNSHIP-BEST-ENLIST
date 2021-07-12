Python MySql (Insert into & select)¶

1. Create a DB with doctor and doctor ID & patients visited

In [1]:

import mysql.connector

In [2]:

mydb = mysql.connector.connect(

  host="localhost",

  user="root",

  password="1234"

)

In [3]:

print(mydb)

<mysql.connector.connection_cext.CMySQLConnection object at 0x0000021634F8A790>

In [8]:

dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Doctors1")

In [9]:

dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:

  print(entry)

('doctor',)

('doctors1',)

('information_schema',)

('mydatabase',)

('mysql',)

('performance_schema',)

('sakila',)

('sys',)

('world',)

In [10]:

mydb = mysql.connector.connect(

  host="localhost",

 user="root",

  password="1234",

  database="Doctors1"

)

dbse = mydb.cursor()

dbse.execute("CREATE TABLE Doctors (dr_id VARCHAR(255), Patient_visited VARCHAR(255))")

In [11]:

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:

  print(value)

('doctors',)

In [12]:

dbse = mydb.cursor()

sql = "INSERT INTO Doctors (dr_id , Patient_visited) VALUES (%s,%s)"

val = [

  ('DID1','10'),

    ('DID2','3'),

    ('DID3','8'),

    ('DID5','0'),

    ('DID123','15'),

    ('DID26','9'),

    ('DID78','0'),

    ('DID65','0'),

     ('DID23','15'),

    ('DID262','9'),

    ('DID783','0'),

    ('DID651','0'), 

    ('DID13','19'),

    ('DID267','7'),

    ('DID8','0'),

    ('DID59','0')    

]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")

16 was inserted.

2. Get the doctor(s) who have more than 5 patients visited

In [15]:

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")

myresult = mycursor.fetchall()

for x in myresult:

  print(x)

('DID1', '10')

('DID3', '8')

('DID123', '15')

('DID26', '9')

('DID23', '15')

('DID262', '9')

('DID13', '19')

('DID267', '7')

3. Get the doctors with no patients visit

In [14]:

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Doctors where Patient_visited=0")

myresult = mycursor.fetchall()

for x in myresult:

  print(x)

('DID5', '0')

('DID78', '0')

('DID65', '0')

('DID783', '0')

('DID651', '0')

('DID8', '0')

('DID59', '0')
