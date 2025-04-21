import mysql.connector

try:
   db = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="root",
      database="studentdb"
   )

   c = db.cursor()

   student_create = """
   CREATE TABLE IF NOT EXISTS stud1 (
      studid INT NOT NULL AUTO_INCREMENT,
      studname VARCHAR(45),
      department VARCHAR(45),
      PRIMARY KEY (studid)
   )"""

   c.execute(student_create)

except mysql.connector.Error as err:
   print("Error:", err)

finally:
   if c:
      c.close()
   if db:
      db.close()
