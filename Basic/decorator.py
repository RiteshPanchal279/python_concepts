def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("before function call")
        result=func(*args,**kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def greet(name):
    print(f"Hello, {name}!")


# greet("python")

# ------------------------------------>
def decorator_one(func):
    def wrapper(*args, **kwargs):
        print("decorator one-before function execution")
        result=func(*args,**kwargs)
        print("decorator one-after function execution")
        return result
    return wrapper

def decorator_two(func):
    def wrapper(*args, **kwargs):
        print("decorator two-before function execution")
        result=func(*args,**kwargs)
        print("decorator two-after function execution")
        return result
    return wrapper

def decorator_three(func):
    def wrapper(*args, **kwargs):
        print("decorator three-before function execution")
        result=func(*args,**kwargs)
        print("decorator three-after function execution")
        return result
    return wrapper


@decorator_one
@decorator_two
@decorator_three
def my_function():
    print("original function")

# my_function()


def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
               result=func(*args, **kwargs)
            return result
        return wrapper
    return decorator
    
@repeat(5)
def my_data():
    print("pythin programming")
    
my_data()
