#List down all the error types and check all the errors using a python program for all errors¶
Name error

list=12
print(list1)
---------------------------------------------------------------------------
#NameError                                 Traceback (most recent call last)
#<ipython-input-3-51ca8c6ba761> in <module>
      1 list=12
----> 2 print(list1)

#NameError: name 'list1' is not defined
#Type error

a='123'
a+=123  # int is added with string
---------------------------------------------------------------------------
#TypeError                                 Traceback (most recent call last)
#<ipython-input-5-d41115771e5f> in <module>
      1 a='123'
----> 2 a+=123

#TypeError: can only concatenate str (not "int") to str

l=[1,2,3,4,5,56,6,7]
for i in range(2,l):
    print(i+1)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-9-3b3fb02e4682> in <module>
      1 l=[1,2,3,4,5,56,6,7]
----> 2 for i in range(2,l):
      3     print(i+1)

TypeError: 'list' object cannot be interpreted as an integer
Syntax errror
In [6]:
for i range(1,10):  #for i in range(1,10):   in keyword missing
    print(i)
#  File "<ipython-input-6-519d01f069aa>", line 1
#    for i range(1,10):
#          ^
#SyntaxError: invalid syntax

in =123 # keyword is used as variable
#  File "<ipython-input-7-a055b203b7b3>", line 1
#    in =123
#    ^
#SyntaxError: invalid syntax
#index error

l=[1,2,3,4,5,56,6,7]
for i in range(len(l)):
    print(l[i+1])
2
3
4
5
56
6
7
---------------------------------------------------------------------------
#IndexError                                Traceback (most recent call last)
#<ipython-input-10-1af7c3ce58a8> in <module>
      1 l=[1,2,3,4,5,56,6,7]
      2 for i in range(len(l)):
----> 3     print(l[i+1])

#IndexError: list index out of range
#Module not found error

import modulexyz
---------------------------------------------------------------------------
ModuleNotFoundError                       Traceback (most recent call last)
<ipython-input-11-278d43f9a72a> in <module>
----> 1 import modulexyz

ModuleNotFoundError: No module named 'modulexyz'
Key error
In
dict1=dict()
dict1={1:12,11:12,13:14}
print(dict1[23])
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-13-99e2dd8094cf> in <module>
      1 dict1=dict()
      2 dict1={1:12,11:12,13:14}
----> 3 print(dict1[23])

#KeyError: 23
Import error

from math import x
---------------------------------------------------------------------------
#ImportError                               Traceback (most recent call last)
#<ipython-input-14-7c042d96054e> in <module>
#----> 1 from math import x
#ImportError: cannot import name 'x' from 'math' (unknown location)

#Value error

int("abc")
---------------------------------------------------------------------------
#ValueError                                Traceback (most recent call last)
#<ipython-input-15-2dda1cc00c48> in <module>
#----> 1 int("abc")

#ValueError: invalid literal for int() with base 10: 'abc'
#Zero Division Error

100/0
---------------------------------------------------------------------------
#ZeroDivisionError                         Traceback (most recent call last)
#<ipython-input-16-bbe761e74a70> in <module>
#----> 1 100/0

#ZeroDivisionError: division by zero
#Design a simple calculator app with try and except for all use cases

def calculate():
    try:
        print('+')
        print('-')
        print('*')
        print('/')
        print('%')
        print('**')
        operation = input("Select an operator:n")
        print("Enter two numbers")
        number_1 = int(input())
        number_2 = int(input())
        if operation == '+': # To add two numbers
            print(number_1 + number_2)
        elif operation == '-': # To subtract two numbers
            print(number_1 - number_2)
        elif operation == '*': # To multiply two numbers
            print(number_1 * number_2)
        elif operation == '/': # To divide two numbers
            print(number_1 / number_2)
        elif operation == '%': # To remainder two numbers
            print(number_1 % number_2)
        elif operation == '**': # To num1 exponent num2
            print(number_1 ** number_2)
        else:
            print('Invalid Input')
    except Exception as e:
        print(e)
calculate()
#+
#-
#*
#/
#%
#**
#Select an operator:ns
#Enter two numbers
#45
#56
#Invalid Input

calculate()
#+
#-
#*
#/
#%
#**
#Select an operator:n*
#Enter two numbers
#56
#hh
#invalid literal for int() with base 10: 'hh'
#print one message if the try block raises a NameError and another for other errors

try:
    a = 123
    if a==123:
        print(b)
        raise NameError("Name error")
    if a >0:
        raise ValueError("Value error")
except NameError as ne:
        print(ne)
except ValueError as ve:
    pritn(ve)
name 'b' is not defined
When try-except scenario is not required?
Python Exceptions are error scenarios that alter the normal execution flow of the program The process of The code inside the else block is executed if there are no exceptions raised.
Try getting an input inside the try catch block

try:
    age=int(input('Enter your age: '))
except:
    print ('You have entered an invalid value.')
#Enter your age: eighteen
#You have entered an invalid value.
