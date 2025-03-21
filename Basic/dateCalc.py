from datetime import datetime


def calculate_days_between_dates():
   
   date1_str = input("Enter the first date (YYYY-MM-DD): ")

   date2_str = input("Enter the second date (YYYY-MM-DD): ")

   try:
      
      date1 = datetime.strptime(date1_str, "%Y-%m-%d")
      date2 = datetime.strptime(date2_str, "%Y-%m-%d")
      difference = abs(date2 - date1)  

      print(f"The number of days between {date1_str} and {date2_str} is {difference.days} days.")
   
   except ValueError:
      print("Invalid date format! Please use the format YYYY-MM-DD.")


calculate_days_between_dates()
