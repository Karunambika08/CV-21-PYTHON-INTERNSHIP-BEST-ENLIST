Map,Filter,zip,reduce¶

1. Write a program using zip() function and list() function, create a merged list of tuples from the two lists given.

In [1]:

# Using map() and lambda

def listOfTuples(l1, l2):

    return list(map(lambda x, y:(x,y), l1, l2))

In [2]:

list1 = [1, 2, 3]

list2 = ['a', 'b', 'c']

print(listOfTuples(list1, list2))

[(1, 'a'), (2, 'b'), (3, 'c')]

In [3]:

def merge(list1, list2):

      

    merged_list = list(zip(list1, list2)) 

    return merged_list

In [4]:

list1 = [1, 2, 3]

list2 = ['a', 'b', 'c']

print(merge(list1, list2))

[(1, 'a'), (2, 'b'), (3, 'c')]

2. First create a range from 1 to 8. Then using zip, merge the given list and the range together to create a new list of tuples.

In [5]:

list1=[1,2,3,4,5,6,7,8]

list2=['a','b','c','d','e','f','g','h']

result =tuple(zip(list1,list2))

print(result)

((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e'), (6, 'f'), (7, 'g'), (8, 'h'))

3. Using sorted() function, sort the list in ascending order.

In [6]:

list1=[23,45,54,32,78,88,22]

list2=sorted(list1)

print(list2)

[22, 23, 32, 45, 54, 78, 88]

4. Write a program using filter function, filter the even numbers so that only odd numbers are passed to the new list.

In [7]:

def filtereven(nums):

    if nums%2 !=0:

        return True

    else :

        return False

In [8]:

numbers =[23,11,44,34,23,25,26,27,28,34,35,36]

result=filter(filtereven,numbers)

for i in result:

    print(i)

23

11

23

25

27

35
