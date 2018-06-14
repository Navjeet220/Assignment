
                             #ASSIGNMENT4
		     
	                            #TUPLE
								 
#QUESTION:1 Write a program to create a tuple with different data types.
#SOLUTION:
t=('a','b',2,4.9,1,"nav")
print(t)

#QUESTION:2 Find the length of the tuples.
#SOLUTION:
t=(1,2,3,4)
print(len(t))
y=(5,3,6,3)
print(len(y))

#QUESTION:3 Find largest and smallest elements of a tuples.
#SOLUTION:
    #for largest
t=(2,2,3,6,9)	
print(max(t))
    #for smallest	
print(min(t))	

#QUESTION:4 Write a program to find the product of all elements of a tuple.
#SOLUTION:
t=(1,2,3,4)
p=1
p=p*t[0]
p=p*t[1]
p=p*t[2]
p=p*t[3]
print(p)

                                 #SETS
								  
#QUESTION:1 Create two sets using user defined values.  
#SOLUTION:
s1=set(input("enter a number: "))
print(s1)
s2=set(input("enter a number: "))
print(s2)

#QUESTION:2	Calculate difference between two sets.
#SOLUTION:
s1=set([1,2,3,4])
s2=set([2,6,5,1])
print(s1-s2)

#QUESTION:3 Compare two sets.
#SOLUTION:

#QUESTION:4	Print the  result of intersection of two sets.
#SOLUTION:
s1=set([1,2,3,4])
s2=set([2,6,5,1])
print(s1&s2)

                 				#DICTIONARY
							
#QUESTION:1 Create a dictionary to store  name and marks of 10 students by user input.
#SOLUTION:
d={}
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
name=input("enter your name: ")
marks=int(input("enter your marks: "))
d[name]=marks
print(d)

#QUESTION:2 Sort the dictionary created in previous question according to the marks.
#SOLUTION:
values=list(d.values())
print(values)
values.sort()
print(values)


#QUESTION:3 Count the number of occurence of each letter in word "MISSISSIPPI".
#           Store count of every letter with the letter in a dictionary.
#SOLUTION:
t=list("MISSISSIPPI")
d={}
d['M']=t.count('M')
d['I']=t.count('I')
d['S']=t.count('S')
d['P']=t.count('P')
print(d)
 

								