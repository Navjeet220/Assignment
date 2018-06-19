      
	                          #ASIGNMENT8

#QUESTION:1 What is Time Tuple?
#SOLUTION:

#Many of Python's time functions handle time as a tuple of 9 numbers, as shown below −
# Index	Field	Values
# 0	4-digit year	2008
# 1	Month	1 to 12
# 2	Day	1 to 31
# 3	Hour	0 to 23
# 4	Minute	0 to 59
# 5	Second	0 to 61 (60 or 61 are leap-seconds)
# 6	Day of Week	0 to 6 (0 is Monday)
# 7	Day of year	1 to 366 (Julian day)
# 8	Daylight savings	-1, 0, 1, -1 means library determines DST
 

#QUESTION:2 Write a program to get formatted time.
#SOLUTION:
import time
print(time.asctime(time.localtime(time.time())))


#QUESTION:3 Extract month from the time. 
#SOLUTION:
#first method
import datetime
print(datetime.date.today())
s=datetime.date.today()
print(s.month)

#second method
from datetime import datetime
print(datetime.now().strftime("%m"))

#third method
import time
print(time.localtime(time.time()))
l=list(time.localtime(time.time()))
print(l)
print(l[1])


#QUESTION:4 Extract day from the time.
#SOLUTION:
#first method
from datetime import datetime
print(datetime.now().strftime("%a"))

#second method
import time
print(time.localtime(time.time()))
l=list(time.localtime(time.time()))
print(l)
print(l[6])


#QUESTION:5 Extract date (ex : 11 in 11/01/2021) from the time.
#SOLUTION:
#first method
from datetime import datetime
print(datetime.now().strftime("%d"))

#second method
import datetime
print(datetime.date.today())
s=datetime.date.today()
print(s.day)

#third method
import time
print(time.localtime(time.time()))
l=list(time.localtime(time.time()))
print(l)
print(l[2])


#QUESTION:6 Write a program to print time using localtime method. 
#SOLUTION:
import time 
print(time.localtime())


#QUESTION:7 Find the factorial of a number input by user using math package functions.
#SOLUTION:
import math
print(math.factorial(int(input("enter any number: "))))


#QUESTION:8 Find the GCD of a number input by user using math package functions.
#SOLUTION:
x=int(input("enter a number: "))
y=int(input("enter an another number: "))
import math
print(math.gcd(x,y))


#QUESTION:9 Use OS package and do the following tasks: 
#1. Get current working directory.
#SOLUTION:
import os
print(os.getcwd)

#2. Get the user environment.
#SOLUTION:
import os
print(os.environ)
