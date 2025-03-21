from datetime import datetime


current_time = datetime.now()
current_hour = current_time.hour

if current_hour<12:
    greet ="Good Morning"
elif 12<= current_hour<18:
    greet = "Good Afternoon"
else :
    greet = "Good Evening"



print(f"{greet} !  The current time is : {current_time.strftime('%H:%M:%S')}")