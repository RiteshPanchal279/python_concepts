mt_set={3,5,7,8}
print("Old set :",mt_set)
new_set=set()
for i in mt_set:
   new_set.add(i*i)

print("New set :",new_set)

# ---------------->
mt_set={3,5,7,8,6}
ne_set={2,8,4,9}
union_set=mt_set.union(mt_set)
intersection_set=mt_set.intersection(mt_set)
print("Union: ",union_set)
print("Intersection : ",intersection_set)

# ---------------->
demo_set={2,3,4,5,6}
demo_set1={7,8,9,3,6}
resultant_set3=demo_set.difference(demo_set1)
print(resultant_set3)                                #difference

resultant_set4 = demo_set.symmetric_difference(demo_set1)   #symmetric difference
print(resultant_set4)

subset1 = demo_set.issubset(demo_set1)                    # subset superset
superset1 = demo_set1.issuperset(demo_set)

print(subset1)
print(superset1)