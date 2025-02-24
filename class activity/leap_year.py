year = int(input("Enter a year: "))

if  (year%4)==0 and (year%100)!=0:
    print("Leap year :", year)
else:
    print("Not a leap year")