# def divide_numbers(x, y):
#     try:
#         result = x/y
#         print("Result : ",result)
#     except ZeroDivisionError:
#         print("Divide by zero not allowed")

# num = 78
# den = 0

# divide_numbers(num,den)
# ------------------------->
def get_input(prompt):
    try:
        value = int(input(prompt))
        return value
    except ValueError:
        print("Error : invalid input")


num = get_input("input an integer: ")
print("input value : ", num)