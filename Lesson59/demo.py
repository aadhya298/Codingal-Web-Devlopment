num= int(input("Enter a number:"))

if str(num)==str(num)[::-1]:
    print(num,"it is a palindrome number")
else:
    print(num,"it is not a palindrome number")

a=int(input("Enter I number for HCF:"))
b=int(input("Enter II number for HCF:"))
def HCF(x,y):
    while y:
        x,y=y,x%y
    return x
result=HCF(a,b)
print(f"The HCF of {a} and {b} is {result}")