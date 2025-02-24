print("press 1 Household pourpose: rate per unit : 2rs")
print("press 2 small business pourpose: rate per unit : 5rs")
print("press 3 industrial pourpose: rate per unit : 10rs")
user_type=input("Enter number : ")
user_consume_unit=int(input("Enter month unit consumption: "))
match user_type:
   case 1 | "1":
      print("your bill is :",2*user_consume_unit)
   case 2 | "2":
      print("your bill is :",5*user_consume_unit)
   case 3 | "3":
      print("your bill is :",10*user_consume_unit)
   case default:
      print("invalid input")
