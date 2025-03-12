class Circle:
    pi = 3.14  

    def __init__(self, radius): 
        self.radius = radius  

    def area(self):  
        return Circle.pi * self.radius ** 2  

circle1 = Circle(5)   
circle2 = Circle(10)    

# print(circle1.pi)  
# print(circle2.pi)
# print(circle1.area())  
# print(circle2.area())

# ------------------------------>
class Rectangle:
    def __init__(self,breadth,length):
        self.length=length
        self.breadth=breadth

    def areaOfRec(self):
        return self.length*self.breadth

rec1 = Rectangle(4,7)
print( "The area of Rectangle:",rec1.areaOfRec())

# ------------------------------>

class Student:
   def __init__(self,name,age):
      self.name=name  
      self.age=age
      self.marks={}
   def add_marks(self,subject,mark):
      self.marks[subject]=mark
   def getAvg(self):
       return sum(self.marks.values())/len(self.marks) if self.marks else 0
   def display_stu(self):
       return f"Studen: {self.name}, Age: {self.age} Marks:{self.marks}"
   
std1=Student("Ritesh",21)
std1.add_marks("Math",94)
std1.add_marks("Phy",70)
std1.add_marks("Chem",84)
std1.add_marks("Sci",66)
print(std1.display_stu())
print(f"The Average of student is : {std1.getAvg()}")

