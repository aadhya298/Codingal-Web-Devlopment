num= int(input("Enter a number:"))

if str(num)==str(num)[::-1]:
    print(num,"it is a palindrome number")
else:
    print(num,"it is not a palindrome number")

a=int(input("Enter I number for HCF:"))
b=int(input("Enter II number for HCF:"))
def hcf(x,y):
    while y:
        x,y=y,x%y
    return x
result_hcf=hcf(a,b)
print(f"The HCF of {a} and {b} is {result_hcf}")


def lcm(x,y):
  return x*y// hcf(x,y)

result_lcm=lcm(a,b)
print(f"The LCM of {a} and {b} is {result_lcm}")