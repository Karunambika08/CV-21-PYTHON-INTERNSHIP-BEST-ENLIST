import DAY11_MYMODULE
MYMODULE.mymodule()
Content from user defined module !!
#Output:
#('Hello ', 'Harry')
DAY11_MYMODULE.list1[1]='Divi'
print(MYMODULE.mymodule())
Content from user defined module !!
#('Hello ', 'Harry')

list2=['Giri','kayal','Malathi','Nikitha']

DAY11_MYMODULE.mymodule(list2)
Content from user defined module !!

#('Hello ', 'Garima')
#2. Install pandas package (try to import the package in a python file)

pip install pandas
Requirement already satisfied: pandas in d:\anaconda\lib\site-packages (1.1.3)
Requirement already satisfied: python-dateutil>=2.7.3 in d:\anaconda\lib\site-packages (from pandas) (2.8.1)
Requirement already satisfied: numpy>=1.15.4 in d:\anaconda\lib\site-packages (from pandas) (1.19.2)
Requirement already satisfied: pytz>=2017.2 in d:\anaconda\lib\site-packages (from pandas) (2020.1)
Requirement already satisfied: six>=1.5 in d:\anaconda\lib\site-packages (from python-dateutil>=2.7.3->pandas) (1.15.0)
Note: you may need to restart the kernel to use updated packages.
3. Import a module that picks random number and write a program to fetch a random number from 1 to 100 on every run

import numpy as np

np.random.randint(low =1, high=100)
#Output
#77
np.random.randint(low =1, high=100)
#Output:
#11

np.random.randint(low =1, high=100,size=5)

array([75, 52, 10, 75, 79])
#4 . Import sys package and find the python path

import sys
sys.maxsize

9223372036854775807

sys.path
#Output:
['C:\\Users\\SARAVANAN DIVYA\\Desktop\\Best Enlist Asignments\\Day 11',
 'D:\\anaconda\\python38.zip',
 'D:\\anaconda\\DLLs',
 'D:\\anaconda\\lib',
 'D:\\anaconda',
 '',
 'D:\\anaconda\\lib\\site-packages',
 'D:\\anaconda\\lib\\site-packages\\win32',
 'D:\\anaconda\\lib\\site-packages\\win32\\lib',
 'D:\\anaconda\\lib\\site-packages\\Pythonwin',
 'D:\\anaconda\\lib\\site-packages\\IPython\\extensions',
 'C:\\Users\\SARAVANAN DIVYA\\.ipython']
sys.version
#Output:
'3.8.5 (default, Sep  3 2020, 21:29:08) [MSC v.1916 64 bit (AMD64)]'
sys.argv[1]
#Output:
#'-f'
#5. Try to install a package and uninstall a package using pip
pip uninstall django
#Note: you may need to restart the kernel to use updated packages.
#WARNING: Skipping django as it is not installed.
