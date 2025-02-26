# claculate sum of numbers in tuple

demo=[(1,5),(3,2),(5.6,)]
total=0
for i in demo:
   for j in i:
      total+= j

print("The sum of given tuple is : ",total)


# iterate through given tuple
student=(111,"Ritesh",88.00,"test@gmail.com","Mumbai")

for i in student:
   print(i,end=", ")

# reapeat 
eam=(1,2)

ans = eam*3
print(ans)
# restul = (1,2,1,2,1,2,1,2)-----> (1,2)