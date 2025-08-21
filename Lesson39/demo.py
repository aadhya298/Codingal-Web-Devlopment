import datetime 

a= 68

if a> 50:
    print("Bravo")
else:
    print("Oops! got it wrong")

if a>40:
    if a>50:
        if a>60:
            print("Gotcha")
else:
    print("Oh no...")

if a>50:
    print("Condition 1 is true")
elif a<50:
    print("Condition 2 is true")
elif a==50:
    print("Condition 3 is true")
else:
    print("Invalid Syntax")

print(datetime.datetime.now())
k= datetime.datetime(2025, 3, 1)
print(datetime.datetime.astimezone(k))