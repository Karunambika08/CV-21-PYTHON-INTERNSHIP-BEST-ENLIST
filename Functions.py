#Q1.Create a function getting two integer inputs from user. & print the following:	
def math_function(num1,num2,sign):
    if sign == '+':
        print("Addition of num1 and num2 is ",str(num1+num2))
    elif sign == '-':
        print("Subraction of num1 and num2 is ",str(num1-num2))
    elif sign == '*':
        print("Multiplication of num1 and num2 is ",str(num1*num2))
    elif sign == '/':
        print("Division of num1 and num2 is ",str(num1/num2))
        
num1= int(input("Enter the first value :"))
num2=int(input("Enter the second value: "))

sign=input("Enter your choice:\n'+' for addition \n'-' for Subration\n'*' for multiplication\n'/' for division\n")

math_function(num1,num2,sign)

#Q2. Create a function covid( )& it should accept patient name, and body temperature, by default the body temperature should be 98 degree
def covid(name,temp):
    print("\nPatient name is: ",name)
    if temp==' ':
        print("Body temperature is:98")
    else:
        print("Temperature is is :",temp)

name = input("Enter name Patient name: ")  
temp=float(input("Enter patients temperature:"))

covid(name,temp)
