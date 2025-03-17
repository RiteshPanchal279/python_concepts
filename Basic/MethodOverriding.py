class User:
   def __init__(self,name,email,user_id):
      self.name=name
      self.email=email
      self.user_id=user_id

   def login(self):
      return f"{self.name} logged in"
   
class Student(User):
   def enroll_course(self,course_name):
      return f"student {self.name} enrolled in {course_name}"
   
   def login(self):
      return f"student {self.name} logged in"
   
class Teacher(User):
   def create_course(self,course_name):
      return f"Teacher {self.name} created the course {course_name}"

   def login(self):
      return f"Teacher {self.name} logged in"


stud=Student("ritesh","one@exampel.com",123)
print(stud.login())
print(stud.enroll_course("python"))

tech=Teacher("abc","abc@exampel.com",113)
print(tech.login())
print(tech.create_course("MySQL"))


