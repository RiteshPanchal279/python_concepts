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

# ---------------------> removing element from dictionary
new_dict = {5: 67,6:55,7: None,8:33,9:None,1:87,2:None,3:9,4:90,5:44}
print(new_dict)

for key, value in list(new_dict.items()):
    del new_dict[key]

print("Empty dictionary")
print(new_dict)