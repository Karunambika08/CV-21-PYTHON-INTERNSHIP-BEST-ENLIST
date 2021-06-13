#DAY-2__STRIMG PRACTICE
#KARUNAMBIKA SP
#Printing values using print ()
print("30 days 30 hour challenge")

#Assigning String to Variable:
Hours = "thirty"
print(Hours)

#Indexing using String:
#returs first character
Days = "Thirty days"
print(Days[0])
#returs last character
Days = "Thirty days"
print(Days[-1])


#print the particular character using slicing:
Challenge = "I Will Win"
print(Challenge[7:10])
#print the string in reverse order
Challenge = "I Will Win"
print(Challenge[::-1])
#prints entire stmt 
Challenge = "I Will Win"
print(Challenge[::])
#prints from starting upto mentioned index
Challenge = "I Will Win"
print(Challenge[:5])


#Print the length of Character:
Challenge = "I Will Win"
print(len(Challenge))
#Convert String into lower character;
Challenge = "I will wiN"
print(Challenge.lower())
#Convert String into Upper character;
Challenge = "I will win"
print(Challenge.upper())

#String Concatenation – Joining two strings
a = "30 Days"
b = "30 hours"
c = a + b
print(c)

#Adding space during concatenation
a = "30 Days"
b = "30 hours"
c = a + "  " + b
print(c)

#operations on string
text = "Thirty days and Thirty hours"
#casefold() - Usage(converts string into lower case)
x = text.casefold()
print(x)
#capitalize()-converts first character to upper case
x = text.capitalize()
print(x)
#find()-Searches the string for a specified value and returns the position of where it was found
x = text.find('u')
print(x)
#isalpha()_Returns True if all characters in the string are in the alphabet;
x = text.isalpha()
print(x)
#isalnum-Returns True if all characters in the string are in the alphanumeric;
x = text.isalnum()
print(x)
#replace()
x=text.replace("hours","hours challenge")
print(x)
#split()-Splits the string at the specified separator, and returns a list;
x=text.split()
print(x)
