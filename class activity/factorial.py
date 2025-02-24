# num = int(input("Enter number: "))
# ans=1

# while num > 1:
#     ans=ans*num
#     num-=1

# print("Factorial is ",ans)
    
# ------------>

# def reverse(num):
#     ans=0
#     while num>0:
#         last=num%10
#         ans=ans*10+last
#         num//=10
#     return ans

# ans=reverse(1235)
# print("reverse is",ans)

# ----------------------->
# def armstrong(num):
#     result=0
#     while num>0:
#       last=num%10
#       result+=last**3
#       num//=10
#     return result

# num = int((input("Enter number ")))
# ans= armstrong(num)
# if(ans == num ):
#     print("Number is Armstrong ")
# else:
#    print("Number is not Armstrong ")

# --------------------> using string convert
given_number = int(input("Enter a number: "))

given_number=str(given_number)

string_length = len(given_number)
sum=0

for i in given_number:
    sum+=int(i)**string_length

if sum==int(given_number):
    print("Armstrong number")
else:
    print("Not armstrong no")