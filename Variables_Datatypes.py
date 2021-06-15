#PYTHON-VARIABLE AND DATA TYPES 
#DAY-4 TASK 
#1) MULTIPLE ASSIGNMENTS
a=b=c=80
print("The values of \na=",a,"\nb=",b,"\nc=",c)
# a) Divide a by 10 
print("Division of a by 10 : ",a/10)
# b) Multiply b by 50
print("Multiplication of b by 50 : ",b*50)
# c) Add c by 60
print("Addition of c value by 60 : " ,c+60)


#2) String variable charachter replacement
#USIMG SLICING
str_var="ABCDE"
print(str_var)
print("After replacement : ", str_var[:2]+'G'+str_var[3:])

#USING replace()
print(str_var)
print("After replacement : ", str_var.replace("C","G"))

#3 Typecasting
a=8
b=8.5
print("a=",a)
print("Typecasting a to float =",float(a))
print("b=",b)
print("Typecasting a to int =",int(b))
