Lambda Function¶
• Create a lambda function that multiplies argument x with argument y
In [1]:
r = lambda x, y : x * y
print(r(10, 4))
40
• Write a Python program to create Fibonacci series to n using Lambda
In [2]:
from functools import reduce
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                 range(n-2), [0, 1])
  
print(fib(11))
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
• Write a Python program that multiply each number of given list with a given number
In [3]:
nums = [2, 4, 6, 9 , 11]
n = 2
print("Original list: ", nums)
print("Given number: ", n)
filtered_numbers=list(map(lambda number:number*n,nums))
print("Result:")
print(' '.join(map(str,filtered_numbers)))
Original list:  [2, 4, 6, 9, 11]
Given number:  2
Result:
4 8 12 18 22
• Write a Python program to find numbers divisible by 9 from a list of numbers
In [10]:
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(map(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))
list2=list(filter(lambda j:j%9==0,list1))
print("Result")
print(' '.join(map(str,list2)))
[2, 4, 5, 6, 7, 8, 9, 21, 12, 14, 15, 27, 36, 81]
Result
False False False False False False True False False False False True True True
Result
9 27 36 81
• Write a Python program to count the even numbers in a given list of integers
In [11]:
list1=[2,4,5,6,7,8,9,21,12,14,15,27,36,81]
print(list1)
list2=list(filter(lambda j:j%2==0,list1))
print("Result :")
print(len(list2))
[2, 4, 5, 6, 7, 8, 9, 21, 12, 14, 15, 27, 36, 81]
Result :
7
