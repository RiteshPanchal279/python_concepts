import mysql.connector

db = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="root",
   database="employeedb"
)
c=db.cursor()

# structure of tabel not for run 
# emp_create = """
#    CREATE TABLE IF NOT EXISTS employee (
#       empid VARCHAR(15) NOT NULL,
#       empname VARCHAR(45),
#       department VARCHAR(45),
#       PRIMARY KEY (empid)
#    )"""
# c.execute(emp_create)


# ----------------> Insert

employee_insert = """INSERT INTO employee(
    
    empid,
    empname,
    department
    )  VALUES (%s, %s,%s)"""
    
records = [("101","Aman","HR"),
            ("102","vijay","Testing"),
            ("103","karan","Finance")]

c.executemany(employee_insert,records)

# ----------------> Select all

emp_read =  """SELECT * FROM employee"""
c.execute(emp_read)
emp_data = c.fetchall()

for e in emp_data:
    print(e)

# ----------------> UPDATE

# update_query = "UPDATE employee SET department = %s WHERE empid = %s"
# data = ("Development", "102")

# c.execute(update_query, data)

# # ----------------> Delete specific row
# emp_delete = "DELETE FROM employee WHERE empid=103"
# c.execute(emp_delete)

# # ----------------> Delete all rows of employee table
# emp_delete = "DELETE FROM employee"
# c.execute(emp_delete)

db.commit()
c.close()
db.close()