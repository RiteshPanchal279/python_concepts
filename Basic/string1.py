# str = "App Dev Using Python !! 2025"
# print("My String : ",str)

# upr,lwr,num, spl=0,0,0,0

# for i in range(len(str)):
#     if str[i]>='A' and str[i]<='Z':
#         upr+=1
#     elif str[i]>='a' and str[i]<='z':
#         lwr+=1
#     elif str[i]>='0' and str[i]<='9':
#         num+=1
#     else:
#         spl+=1


# print("Uppercase letters : ",upr)
# print("Lowercase letters : ",lwr)
# print("Numbers : ",num)
# print("Special chacters ",spl)

# ------------------------------->

# demostr="Welcome to Topic on String"
# vowcount =0

# for i in demostr:
#    if(
#       i=='A'or i=='a' or i=='E'or i=='e'or i=='I'or i=='i'or i=='O'or i=='o'or i=='U'or i=='u'
#      ):
#       vowcount+=1

# print("Total vowels are: ",vowcount)
# ------------------------------->

input_string = "string and string functions"
result_str=""

print("Original String :",input_string)

for char in input_string.split(' '):
    if char not in result_str:
        result_str+=' '+char

print("string as duplicate removed :",result_str)