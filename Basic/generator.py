def user_input_gen():
    while True:
        command = input("Enter a command(type 'exit' to quit):")
        if command.lower() == 'exit':
            break
        yield command

def process_commands():
    for command in user_input_gen():
        print(f"execute command : {command}")

process_commands()
# -------------------->

# def count(num):
#     counter=1
#     while counter<=num:
#         yield counter
#         counter+=1

# gen = count(10)


# for n in gen:
#    print(n)

# -------------------->
# numbers=[1,2,3,4,5,6,7,8,9,10]

# even=(num for num in numbers if num%2==0)
# for e in even:
#     print(e)

# odd=(num1 for num1 in numbers if num1%2==1)
# for o in odd:
#     print(o)

# -------------------->

# words = ["FIRST","TOPIC","IN","PYTHON","GENERATORS"]
# lcase = (w.lower() for w in words)

        
# for w in lcase:
#     print(w,end=" ")
# # -------------------->

# words = ["first","topic","in","python","generators"]
# ucase = (w.upper() for w in words)

        
# for w in ucase:
#     print(w,end=" ")

# # -------------------->

def infinite(start=0):
    while True:
        yield start
        start+=1

counter = infinite()

for i in range(5):
    print(next(counter))