# data=100

# if data==99:
#    print("Equal to 99")
# else:
#    if data > 99:
#       print("Data grater then 99")
#    else:
#       print("data is less then 99")

# --------->While Loop

# num=1
# while num<10:
#    if num % 2==1:
#       print("odd number :",num)
#    else:
#       print("Even number:",num)
#    num+=1


# --------->conditinal statement

# num1 = float(input("Enter a number"))

# if num1>0:
#     print("Positive number")
# elif num1==0:
#     print("its a zero")
# else:
#     print("Negative number")


# ----------->
# num1=221
# num2=44
# num3=51

# if(num1>num2) and (num1>num3):
#     greatest = num1
# elif(num2>num3) and (num2>num1):
#     greatest=num2
# else:
#     greatest=num3

# print("The greatest no. is :", greatest)

# -------------->
num1=221
num2=844
num3=511

if(num1>num2):
    if(num1>num3):
        print("Greatest no: ", num1)
    else:
        print("Greatest no:",num3)
else:
    if(num2>num3):
        print("Greatest no: ", num2)
    else:
        print("Greatest no:",num3)