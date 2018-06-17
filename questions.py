#QUESTION:1  Create a program that asks the user to enter their name and their age.
#            Print out a message addressed to them that tells them the year that they will turn 100 years old.
#SOLUTION:
n=input("enter your name: ")                   #(take the input of the name from the user)
a=int(input("enter your current age: "))       #(take the input of the age from user)
b=int(100-a)                                   #(user will become 100 years after the 100-current age)
print("hello")
print(n)
print("your current age is ",a)
print("you will become hundred years old after:" ,b)


#QUESTION:2  Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#            between 2000 and 3200 (both included).
#            The numbers obtained should be printed in a comma-separated sequence on a single line.

#Hints: 
#Consider use range(#begin, #end) method
#SOLUTION:
l=[]                                                            #(take a empty list)
for x in range(2000,3200):                       #(mention the range in which you want to print the list) 
 if (x%7==0) and (x%5==1):    #(if number is divisible by 7 it yields remainder 0 while if number is not a multiple of 5 then it must not be divisible by 5 and yields the remainder 1.)
  l.append(x)
 print(l)


#QUESTION:3  Write a program which accepts a sequence of comma-separated numbers from console 
#             and generate a list and a tuple which contains every number.

#Suppose the following input is supplied to the program:
#34,67,55,33,12,98

#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')
#SOLUTION:
num=34,67,55,33,12,98                #(take the input from user)
t=tuple(num)                         #(store the input in tuple and assigns this value to variable t)
l=list(num)                          #(store the input in list and assigns this  value to variable l)
print("tuple = ",t)
print("list = ",l)


#QUESTION:4  Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

#Suppose the following input is supplied to the program:
#Hello world!
#Then, the output should be:
#UPPER CASE 1
#LOWER CASE 9

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.
#SOLUTION:
str=input("enter the sentence: ")     #(take the input from the user)
count1=0                              #(initialise the counter 1)
count2=0                              #(initialise the counter 2)
for i in str:                         #(for loop is used to traverse the characters in strings)
 if (i.isupper()):
  count1=count1+1                     #(if string is having upper case letter then increement the counter 1)
 elif (i.islower()):                  #(if string is having lower case letter then increement the counter 2)
  count2=count2+1
print("the number of upper case letters: ")
print(count1)
print("the number of lower case letters: ")
print(count2) quiz-assignment
