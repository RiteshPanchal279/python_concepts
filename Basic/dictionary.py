num = {1:11, 2:22, 3:33, 4:55, 5:32, 6:7,7:36, 8:90}

# print("Key    value")
# for key, value in num.items():
#     print(key,'   ',value)

# for  value in num.values():
#     print(value)

# for  key in num:
#    print(key)
# -------------------------->
# first={12:33,2:11}
# sec={1:33,20:1}
# third={10:1,17:44}

# fourth={}
# for member in (first,sec,third): fourth.update(member)
# print(fourth)
# -------------------------->

test={"A":7,"B":3,"C":4,"D":5}
res=0
for val in test.values():
   res+=val
   print("res: ",res)
   
res=res/len(test)
print("res total outer :",res)