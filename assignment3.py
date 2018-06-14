
              #ASSIGNMENT3


#QUESTION:1  Create a list with user-defined inputs.
#SOLUTION:
x=input("enter a number: ")
y=input("enter a number: ")
z=input("enter a number: ")
u=input("enter a number: ")
v=input("enter a number: ")
l=[x,y,z,u,v]
print(l)


#QUESTION:2   Add the following list to above created list:
#            ['google','apple','facebook','microsoft','tesla']
#SOLUTION:
l2=['google','apple','facebook','microsoft','tesla']
print(l.extend(l2))
print(l)


#QUESTION:3  Count the number of time an object occurs in the list.
#SOLUTION:
l=[1,3,3,3,3,4,4,5,7]
print(l.count(3))


#QUESTION:4  Create the number of list and sort this in ascending order.
#SOLUTION:
l=[5,2,1,4,3]
l.sort()
print(l)


#QUESTION:5  Given are two one-dimensional arrays A and B which are in unsorted form.Arrange them in ascending order.
#            Write a program to merge them into a single sorted array C that contains every single item from arrays A and B in ascending order list.   
#SOLUTION:    
A=[3,9,8,7] 
print(A)
B=[1,5,2,4]
print(B)
A.sort() 
print(A)
B.sort()
print(B)
C=(A,B)
print(C)
C=A+B
print(C)
C.sort()
print(C)
       	   

#QUESTION:6 Implement stack and queue using list.
#SOLUTION:
    #for stack
l=[1,2,3,4,5]
print(l.pop())
print(l)
	#for queue	
l=[1,2,3,4,5]
print(l)
l.reverse()
print(l)
print(l.pop())
print(l)

	
#QUESTION:7 Count even and odd in a list. 
#SOLUTION 
n=int(input("enter a number: "))
if (n % 2)==0:
 print("n is even")
else: 
 print("n is odd")  