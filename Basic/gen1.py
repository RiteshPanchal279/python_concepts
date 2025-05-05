mylis = [1,2,3,4,5,6,7]
gen = (x**3 for x in mylis)
for i in gen:
   print('the i is',i)



# ------------------->
num = [1,2,5,7,9]

iterator=iter(num)
print(next(iterator)) # output 1
print(next(iterator)) # output 2
print(next(iterator)) # output 5

# -----------  ---->
def gen_fun():
   yield 1
   yield 4
   yield 6

obj = gen_fun()
for i in obj:
   print(i)

# ------------------>
def sqr_fun():
   num = [1,2,5,7,9]
   for i in num:
      yield i**2

sqr_obj = sqr_fun()
for i in sqr_obj:
   print("The square is :",i)