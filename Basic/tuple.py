demo_tuple=(11,5,77,99,88,90)
# first_member =demo_tuple[0]                       # indexes
# second_member=demo_tuple[1]


# print(first_member)
# print(second_member)

# last_member1=demo_tuple[-1]                      # negative index
# last_member2=demo_tuple[-2]

# print(last_member1)
# print(last_member2)

# subset = demo_tuple[2:4]                         # slicing in tuples
# print(subset)

# --------------------------------->

new_tup=(33 ,0,33,"hello","python",33.2,8,"ok",233,"last")

# print(new_tup[1])
# print(new_tup[-1])

# for item in new_tup:
#    print(item,end=" ")

count = new_tup.count(33)
print(count) # print the count 2

# --------------------------------->

# new_tuple=(11,12,13,14,15)
# old_tuple=(100,200,300,400,500)
# print(new_tuple[0])                            # 

# for item in new_tuple:                          # for loop 
#     print(item)

# add_tuple = new_tuple + old_tuple               # append
# print(add_tuple)

# length = len(add_tuple)                         # length
# print(length) 


# minimum = min(add_tuple)                         #minimum and maximum

# --------------------------------->

tupl=(4,3,24,6,1,2,88)

sorte_tup = tuple(sorted(tupl))
print(sorte_tup)