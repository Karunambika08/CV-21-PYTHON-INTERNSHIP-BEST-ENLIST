#Day5 List and tuples
#Creation amd updating the list
n=int(input("Enter the size of the list : "))
list1=[]
print("Enter the elements : ")
for i in range(n):
    a=int(input())
    list1.append(a)
    print("The list elements are",i,": ",list1)
    
#Adding elements using insert()
x=int(input("\nEnter the index the element to be inserted at : "))
n2=int(input("\nEnter the element: "))
list1.insert(x,n2)
print("\nThe updated list is : ",list1)

#extend method-to add iterables
list2=[100,'Python']
print("The List 2:")
list1.extend(list2)
print ("\nThe Updated list1 is",list1)

#Deletion 
list1.pop()#delets last element in the list
print("\nAfter deletion",list1)
list1.remove(1) #remove the element passed
print("After removing the element 1:")
del list1[5]
print(list1)
del list1[2:5]
print(list1)

#Storing the largest &smallest number from the list to a variable
L1=[88,58,11,8,85,22]
print("List is: ")
a=max(L1)
print("The largest no in the list",a)
b=min(L1)
print("The smallest no in the list",b)


#TUPLES
#Creation of tuples
#reversing tuple using slicing
def Rev(tuples): 
    new_tup = tuples[::-1] 
    return new_tup 
    
tuples = ('a','e','i','o','u') 
print(Rev(tuples))


#Conversion of tuple into list
tup=(12,11,45,32,90)
L=list(tup)
print("Tuple ",tup)
print("Tuple in form of list  ",L)

