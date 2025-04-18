import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="root",
   database="studentdb"
   
)

c=db.cursor()

student_create = """CREATE TABLE `studentdb`.`stud` (
`studid` INT NOT NULL AUTO_INCREMENT,
`studname` VARCHAR(45) NULL,
`department` VARCHAR(45) NULL,
 PRIMARY KEY (`studid`))"""

c.execute(student_create)

c = db.cursor()
c.close()
db.close()