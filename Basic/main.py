from Finance import *

if __name__ =="__main__":
   expenses = [1500,400,100]
   income=[4000,1200]

   total_expenses = calculate_expenses(expenses)
   total_income = calculate_income(income)
   total_savings = calculate_savings(total_income,total_expenses)

   print(f"Total Expenses: ${total_expenses}")
   print(f"Total Income: ${total_income}")
   print(f"Total Savings: ${total_savings}")
