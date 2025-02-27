# Write a Python program to Remove items from set1 that are not common to
# both set1 and set2.
# Output:{40, 50, 30}

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}


exp_output = set1.intersection(set2)
print("Result: ",exp_output)

both_set=set1.symmetric_difference(set2)
print("Sym Diff : ",both_set)