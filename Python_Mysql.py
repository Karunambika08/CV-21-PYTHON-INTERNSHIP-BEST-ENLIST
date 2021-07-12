Python MySql¶

• Create a connection for DB and print the version using a python program

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

<mysql.connector.connection_cext.CMySQLConnection object at 0x0000016A60164700>

In [4]:

import sys

cur = mydb.cursor()

cur.execute("SELECT VERSION()")

data = cur.fetchone()

print("DBMS Version :",str(data))

DBMS Version : ('8.0.25',)

• Create a multiple tables & insert data in table

In [7]:

dbse = mydb.cursor()

dbse.execute("CREATE DATABASE mydatabase")

In [8]:

dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:

  print(entry)

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

  database="mydatabase"

)

dbse = mydb.cursor()

dbse.execute("CREATE TABLE customers (Employee_name VARCHAR(255), Employee_dep VARCHAR(255), Employee_id VARCHAR(255))")

In [11]:

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:

  print(value)

('customers',)

In [14]:

dbse = mydb.cursor()

dbse.execute("CREATE TABLE Office (emp_name VARCHAR(255), Employee_id VARCHAR(255) ,EMP_ADDRESS VARCHAR(255))")

In [15]:

dbse =mydb.cursor()

dbse.execute("CREATE TABLE Student(rollno INT(24) , STUD_NAME VARCHAR(255) , MARK INT(3))")

In [16]:

dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:

  print(value)

('customers',)

('office',)

('student',)

• Create a employee table and read all the employee name in the table using for loop

In [24]:

mydb = mysql.connector.connect(

  host="localhost",

 user="root",

  password="1234",

  database="mydatabase"

)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Employee1 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

In [30]:

mydb = mysql.connector.connect(

  host="localhost",

 user="root",

  password="1234",

  database="mydatabase"

)

mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"

val = ("123","divya","T Nagar 56")

p, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

1 record inserted.

In [31]:

mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"

val = ("124","Renu","T Nagar 58")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

1 record inserted.

In [32]:

mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id, name, address) VALUES (%s, %s,%s)"

val = ("125","Janani","Kamarajar Salai 58")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

1 record inserted.

In [41]:

mycursor = mydb.cursor()

sql = "INSERT INTO Employee1 (id,name, address) VALUES (%s,%s,%s)"

val = [

  ('1','Peter', 'Lowstreet 4'),

  ('2','Amy', 'Apple st 652'),

  ('3','Hannah', 'Mountain 21'),

  ('4','Michael', 'Valley 345'),

  ('5','Sandy', 'Ocean blvd 2'),

  ('6','Viola', 'Sideway 1633')

]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")

6 was inserted.

In [42]:

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:

  print(x)

(1, 'Peter', 'Lowstreet 4')

(2, 'Amy', 'Apple st 652')

(3, 'Hannah', 'Mountain 21')

(4, 'Michael', 'Valley 345')

(5, 'Sandy', 'Ocean blvd 2')

(6, 'Viola', 'Sideway 1633')

(123, 'divya', 'T Nagar 56')

(124, 'Renu', 'T Nagar 58')

(125, 'Janani', 'Kamarajar Salai 58')

In [43]:

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM Employee1")

myresult = mycursor.fetchall()

for x in myresult:

  print(x)

('Peter',)

('Amy',)

('Hannah',)

('Michael',)

('Sandy',)

('Viola',)

('divya',)

('Renu',)

('Janani',)

In [ ]:
