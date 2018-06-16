          
		             #ASSIGNMENT6
			  
#QUESTION:1 Take 10 integers from the user and print it on the screen.
#SOLUTION:
l=[]
for n in range(0,10):
 l.append(int(input("enter the integer: ")))
 print(l)
 

#QUESTION:2 Write an infinite loop.An infinite loop never ends.Condition is always true. 
#SOLUTION:
    
	#first method
i=1
while i<10:
 print("hello world")
print(i)
     
	 #second method
i=1
while i!=10:
 print("hello world")
print(i)
  
  
#QUESTION:3  Create a list of integer elements by user input.
#            Make a new list which will store square of elements of previous list.
#SOLUTION:
     #using whie loop  
l=[]
s=[]
for x in range(4):
 l.append(int(input("enter a number: ")))
for x in l:
 s.append(x**2)
print(l)
print(s) 

	
#QUESTION:4 From a list containing ints, strings and floats, make three lists to store them separately
#SOLUTION: 
l=[]
for x in range(0,3):
 x=int(input("enter numbers: "))
 l.append(x)
for x in range(3,6):
 x=input("enter strings: ")
 l.append(x)
for x in range(6,9):
 x=float(input("enter floats: "))
 l.append(x)
print(l)
list1=[]
list2=[]
list3=[]
for x in l:
 if type(x)==int:
  list1.append(x)
 elif type(x)==str:
  list2.append(x)
 elif type(x)==float:
  list3.append(x)
print(list1)
print(list2)
print(list3)


#QUESTION:5  Using range(1,101), make a list containing even and odd numbers. 
#SOLUTION:
list1=[]
list2=[]
for i in range(1,101):
 if (i%2==0): 
  print("even",i)
  list1.append(i)
 elif (i%2==1):
  print("odd",i)
  list2.append(i)
 print(list2) 
 
 
#QUESTION:6 Print the following patterns: 
#*
#**
#***
#***
#SOLUTION:	
num=int(input("enter the number of rows: "))
for i in range(0,10):
 for j in range(0,i):
  print("*",end="")
 print()


#QUESTION:7 Create a user defined dictionary and get keys corresponding to the value using for loop.
#SOLUTION:
d={}
for x in range(5):
 keys=str(input("enter the keys: "))
 values=int(input("enter value item: "))
 d[keys]=values
print(d)


#QUESTION:8 Take inputs from user to make a list. Again take one input from user 
#          and search it in the list and delete that element, if found. Iterate over list using for loop.
#SOLUTION:	
l=[]
flag=0
for x in range(5):
 x=int(input("enter the number: "))
 l.append(x)
print(l)
y=int(input("select any number you want to search: "))
for x in l:
 if x==y:
  l.remove(x)
  flag=1
print(l)
if flag==0:
 print("the number you entered is not in the list")
