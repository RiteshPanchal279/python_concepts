myList=[23,45,2,5,67,12,14]
# print(myList)

# subList1=myList[2:6]
# subList2=myList[::2] # skip 1 member 
# print(subList2)

myList.extend(["one","two"])
myList.remove(14)  # it will remove param member
myList.pop(4)  # it will remove index you provided member -- will remove 67 
print(myList)

# ------------>
demo = [1,2,3,4,5,6,7,8,9]
print("Demo List : ",demo)
lengthoflist = len(demo)                # length function
print("Length : ", lengthoflist)
demo.append(10)                         # append function
print(demo)
demo.extend([15,16])                    # extend function
print(demo)
demo.insert(5,55)                       #insert function
print(demo)
demo.remove(5)                          #remove function
print(demo) 
pop_member = demo.pop(4)                #pop function
print(demo)