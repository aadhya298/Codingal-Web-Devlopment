def intro(a,b):
    return 'Aadhya'
    x=a%b
    y=a//b
    z=b**3

    print(x)
    print(y)
    return z

print("Bonjour!!") #Outside the indentation of function

outside= intro(48,9)
print("Printing outside:", outside) # var will store only the first returned value i.e. Aadhya not z

def reoccur(k):
    if k==1:
        print(k)
        return
    print(k)
    print("Calling func with k-1")
    reoccur(k-1)
    print("Statement to run after ending reoccursion")


reoccur(6)