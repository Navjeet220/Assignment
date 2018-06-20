     
	                      # ASSIGNMENT9

#QUESTION:1 Create a circle class and initialize it with radius. 
#Make two methods getArea and getCircumference inside this class.
#SOLUTION:
class circle():
 def __init__(self,radius):
  self.radius=radius
 def getarea(self):
  return 3.14*(self.radius**2)
 def getcircumference(self):
  return 2*3.14*self.radius

r=int(input("Enter radius of circle: "))
obj=circle(r)
print("Area of circle:",obj.getarea())
print("Circumference of circle:",obj.getcircumference())


#QUESTION:2 Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.
#SOLUTION:
class student():
 def __init__(self,name,rollno):
  self.name=name
  self.rollno=rollno
 def display(self):
  print(self.name,self.rollno)
name=input("enter your name: ")
rollno=int(input("enter your rollno: "))
s1=student(name,rollno)
s1.display()


#QUESTION:3 Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#SOLUTION:
class temperature():
 def convert_fahrenheit(self):
  celsius=int(input("enter the temperature in celsius: "))
  print(celsius,"C")
  fahrenheit=(celsius*1.8)+32
  print("temperature in fahrenheit: ",fahrenheit,"F")
obj=temperature()
obj.convert_fahrenheit()


#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.
#SOLUTION:
class temperature():
 def convert_celsius(self):
  fahrenheit=int(input("enter the temperature in fahrenheit: "))
  print(fahrenheit,"F")
  celsius=(fahrenheit-32)/1.8
  print("temperature in celsius: ",celsius,"C")
obj=temperature()
obj.convert_celsius()


#QUESTION:4 Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.
#SOLUTION:
class MovieDetails():
    def __init__ (self,movie_name,artist_name,releasing_date,ratings):
        self.movie_name=movie_name
        self.artist_name=artist_name
        self.releasing_date=releasing_date
        self.ratings=ratings

    def update(self, movie_name, artist_name, releasing_date, ratings):
        self.movie_name = movie_name
        self.artist_name = artist_name
        self.releasing_date = releasing_date
        self.ratings = ratings

    def show(self):
         print(self.movie_name,self.artist_name,self.ratings,self.releasing_date)
movie_name=input("enter movie name: ")
artist_name=input("enter artist name: ")
ratings=int(input("enter the ratings out of 5: "))
releasing_date=input("enter releasing date: ")
s1=MovieDetails(movie_name,artist_name,ratings,releasing_date)
s1.show()
s1.update("abcd","dance","5","1999")
s1.show()


#QUESTION:5 Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#1. Display expenditure and savings 
#2. Calculate total salary
#3. Display salary
#SOLUTION:
class expenditure():
	def __init__(self,exp,sav):
	 self.exp=exp
	 self.sav=sav
	def totalsalary(self):
	  t=exp+sav
	  return t
	def salary(self,b):
	  self.b=b
	  print(b)
exp=int(input("enter the expenditure: "))
sav=int(input("enter the savings: "))
obj=expenditure(exp,sav)
a=obj.totalsalary()
c=obj.salary(a)

