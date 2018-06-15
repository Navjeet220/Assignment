               
			   
			             #ASSIGNMENT5
				  
#QUESTION:1  Take a input from user and check whether it is a leap year or not.
#SOLUTION:
year=int(input("enter the year: "))
if ((year%400==0)or((year%4==0)and(year%100!=0))):
 print("%d is a leap year" %year)
else:
 print("%d is not a leap year" %year) 
 
				  
#QUESTION:2  Take length and breadth input from user and check whether the dimensions are of square and rectangle.
#SOLUTION:
length=int(input("enter the length: "))
breadth=int(input("enter the breadth: "))
print(length)
print(breadth)
if ((length==breadth)):
 print("This is square")
else:
 print("This is rectangle") 
 
 
#QUESTION:3	 Take the input age of 3 people and determine the oldest and the youngest among them.
#SOLUTION:
person1=int(input("enter the age of person1: "))
person2=int(input("enter the age of person2: "))
person3=int(input("enter the age of person3: "))
        #first method
if person1>=person2 and person1>=person3:
 print("person1 is oldest")
elif person2>=person1 and person2>=person3:
  print("person2 is oldest")
elif person3>=person1 and person3>=person2:
 print("person3 is oldest")
else: 
 print("all are same age")  
if person1<=person2 and person1<=person2:
 print("person1 is youngest")
elif person2<=person1 and person2<=person1:
 print("person1 is youngest")
elif person3<=person2 and person3<=person2:
 print("person3 is youngest")
else:
 print("all are same age")  
		#second method
t=(person1,person2,person3)
print("youngest:",min(t))
t=(person1,person2,person3)
print("oldest:",max(t))
 
				  
#QUESTION:4 Write an if statement to lets competitor know which of these prices they won based on the number of points they scored,
#           which is stored in the  integer variable  points(your input).points can only take on positive integer values up to 200.
#           if they won a prize,the message should state "Congratulations!You won a [prize name]!" with the prize name.if there's 
#           no prize,the message should state "Sorry!No prize this time."
#                                
#                              POINTS                PRIZE
#                               1-50                NO PRIZE
#                              51-150               WOODEN PRIZE
#                             151-180               BOOK
#                             181-200               CHOCOLATES
#SOLUTION:
n=int(input("enter number of scored: "))
if n<=50:
 print("NO PRIZE")
elif  n<=150:
 print("WOODEN PRIZE")
elif  n<=180:
 print("BOOK")
else:
 print("CHOCOLATES") 

				  
#QUESTION:5	 A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity.
#            Suppose,one unit will cost 100.Judge and print total cost for user.
#SOLUTION:
qty=int(input("enter the quantity: "))
totalexp=qty*100
if totalexp>1000:
 dis=totalexp*0.1
 totalexp=totalexp-dis
 print("cost is %d" %totalexp)
else:
 print("total cost is %d" %totalexp)
				  