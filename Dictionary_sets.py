#Dictionary and set -Day-6 task

dict1={'Kavi':98,'Bharathi':99,'Sri':89,'Malu':88}
dict2={'Sowmi':76,'Janani':56,'Kavya':100,'Prasath':67}
print(dict1)
print(dict2)
# Merging Dictionary through Update()
print(dict2.update(dict1))    
# Changes made in dictionary2
print("\nAfter merging Dict1 to Dict2 : ",dict2)
  # merging using and 
Dic= dict1 and dict2
print(Dic)

#remove a key from a dictionary
del dict1['Malu']
print("\nAfter Deletion dict1: ",dict1)
#using pop()
dict2.pop('Prasath')
print('\n',dict2) 

#Mapping two lists into a dictionary
d1=[80,45,11,8,88]
d2=['Jaya','Kayal','Sagar','Dharsha','Suga']
n = {}
for key in d1:
    for value in d2:
        n[key] = value
        d2.remove(value)
        break  
print("\nDictionary is ",str(n))

#using zip()
d2=['Jaya','Kayal','Sagar','Dharsha','Suga']
d1=[80,45,11,8,88]
n2 = dict(zip(d1,d2))
print(n2)


#the length of a set
cars={'Rolls Royce','Benz','Ferrari','Ford'}
print("Number of Cares in Set :",len(cars))


#Remove the intersection of a 2nd set from the 1st sets

s1={1,5,8,88,58,85,100,11,22,45}
s2={55,45,99,153,407,68,88}
print(s1.intersection(s2))
