Python MySQL Join¶
• Create an Employee Table with employee name,employee ID & Salary
In [1]:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
)

mycursor = mydb.cursor()
print(mydb)
<mysql.connector.connection_cext.CMySQLConnection object at 0x0000028960677160>
In [2]:
dbse = mydb.cursor()

dbse.execute("CREATE DATABASE Employee_Mangement")
In [8]:
dbse = mydb.cursor()

dbse.execute("SHOW DATABASES")

for entry in dbse:
    print(entry)
('doctor',)
('doctors1',)
('employee_mangement',)
('grocerystore',)
('information_schema',)
('mydatabase',)
('mysql',)
('performance_schema',)
('sakila',)
('students_management_system',)
('sys',)
('world',)
In [9]:
mydb = mysql.connector.connect(
  host="localhost",
 user="root",
  password="1234",
  database="employee_mangement"
)
dbse = mydb.cursor()

dbse.execute("CREATE TABLE Employee (emp_id INT , EMP_NAME VARCHAR(255),EMP_SALARY DOUBLE )")
In [10]:
dbse = mydb.cursor()

dbse.execute("SHOW TABLES")

for value in dbse:
  print(value)
('employee',)
In [12]:
dbse = mydb.cursor()

dbse.execute("SHOW COLUMNS FROM employee")

for value in dbse:
  print(value)
('emp_id', b'int', 'YES', '', None, '')
('EMP_NAME', b'varchar(255)', 'YES', '', None, '')
('EMP_SALARY', b'double', 'YES', '', None, '')
In [14]:
dbse = mydb.cursor()

sql = "INSERT INTO employee (emp_id , EMP_NAME , EMP_SALARY) VALUES (%s,%s,%s)"
val = [
  ('1','SARA','10000.0'),
    ('2','ANU','15000.0'),
    ('3','PRIYA','70800.0'),
    ('4','VIBAV','80000.0'),
    ('5','ANURAG','89000.0'),
    ('6','KUHU','50000.0'),
    ('7','KUNAL','56000.0'),
    ('8','ABIR','47000.0'),
    ('9','MAYA','26000.0'),
    ('10','RANA','15000.0'),
    ('11','LAKSHANYA','50500.0'),
    ('12','PRERNA','40500.0'),
    ('13','MISTI','25000.0'),
    ('14','POOJA','20500.0'),
    ('15','ARJUN','100600.0')
       
]

dbse.executemany(sql, val)

mydb.commit()

print(dbse.rowcount, "was inserted.")
15 was inserted.
a. Write a query to get the maximum and minimum salary from employees table
In [16]:
mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select max(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
('ARJUN', 100600.0)
In [17]:
mycursor = mydb.cursor()

mycursor.execute("SELECT EMP_NAME,EMP_SALARY FROM employee where EMP_SALARY = (select min(EMP_SALARY) from employee)")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
('SARA', 10000.0)
b. Write a query to get the number of employees working with the company
In [22]:
mycursor = mydb.cursor()

mycursor.execute("SELECT COUNT(*) from employee")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
(15,)
c. Write a query to get the first 3 characters of first name from employees table
In [24]:
mycursor = mydb.cursor()

mycursor.execute("SELECT * from employee WHERE EMP_NAME LIKE('ANU%')")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
(2, 'ANU', 15000.0)
(5, 'ANURAG', 89000.0)
