Python JSON¶
1. Create a JSON of all object types and import the JSON into a SQL Database
Note: The JSON file should have valus of all Datatypes
In [2]:
import json
In [35]:
json_data=[
    {'name':"Dhivya",'age':21,'Permanent_staff':True,'salary':75000.00,'dept_desgn':'Developer'},
     {'name':"Renu",'age':35,'Permanent_staff':False,'salary':56000.00,'dept_desgn':"ML Engineer"},
     {'name':"Manu",'age':34,'Permanent_staff':True,'salary':78000.00,'dept_desgn':'Web Designer'},
     {'name':"Shardha",'age':23,'Permanent_staff':True,'salary':45000.00,'dept_desgn':'Data Scientist'},
     {'name':"Kumar",'age':21,'Permanent_staff':True,'salary':67000.00,'dept_desgn':'Manager'}
    
]
In [18]:
res =json.dumps(json_data)
In [19]:
import mysql.connector
In [20]:
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234"
)
In [21]:
print(mydb)
<mysql.connector.connection_cext.CMySQLConnection object at 0x00000226ED632700>
In [23]:
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE JSONRECORDS1")
In [24]:
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
  print(entry)
('doctor',)
('doctors1',)
('employee_mangement',)
('grocerystore',)
('information_schema',)
('jsonrecords',)
('jsonrecords1',)
('mydatabase',)
('mysql',)
('performance_schema',)
('sakila',)
('students_management_system',)
('sys',)
('world',)
In [25]:
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="jsonrecords1"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE employee (name VARCHAR(255),age INT, permanent_staff VARCHAR(255), salary DOUBLE, dept_and_designation VARCHAR(255))")
In [26]:
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
('employee',)
In [27]:
dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for value in dbse:
  print(value)
('name', b'varchar(255)', 'YES', '', None, '')
('age', b'int', 'YES', '', None, '')
('permanent_staff', b'varchar(255)', 'YES', '', None, '')
('salary', b'double', 'YES', '', None, '')
('dept_and_designation', b'varchar(255)', 'YES', '', None, '')
In [39]:
dbse = mydb.cursor()
sql = "INSERT INTO employee (name ,age, permanent_staff,salary,dept_designation) VALUES (%s)"
value= list(for i in res: res[i])
                         
dbse.execute( sql, value))
  File "<ipython-input-39-34424b7b9576>", line 3
    value= list(for i in res: res[i])
                ^
SyntaxError: invalid syntax
