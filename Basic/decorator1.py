def deco_one(func):
   def wrapper(*args,**kwargs):
      print("Hello i am deco one before call fun")
      result = func(*args,**kwargs)
      print("Hello i am deco one after call fun")
      return result
   return wrapper

@deco_one
def test_deco():
   print("Test deco")

# test_deco()

@deco_one
def sum(a,b):
   print("The sum is : ",a+b)

# sum(23,45)

# -------------------------->

def num(n):
   def decorator(fun):
      def wrapper(*args,**kwargs):
         for _ in range(n):
            result = fun(*args,**kwargs)
         return result
      return wrapper
   return decorator
   

@deco_one
@num(6)
def test():
   print("Test only")

test()
