a=int(input("Enter a no.:"))
def powerof2(a):
    if a==0:
        return 0
    else:
        if a & a-1 == 0:
            return True
        else:
            return False
if powerof2(a):
    print("Divisible by 2")
else:
    print("Not divisible by 2")