#Swapping
a=int(input("Enter a no.:"))
b=int(input("Enter another no.:"))
def swap(a,b):
    a= a^b 
    b= a^b
    a= a^b
    print(f"The swapped numbers are a={a} and b={b}")
swap(a,b)

#Divide without Divide
x=int(input("Enter a dividend:"))
y=int(input("Enter a divisor:"))
sign=0
def divi(x,y):
    if x<0 or y<0:      
        sign=-1
    else:
        sign=1

    x=abs(x)
    y=abs(y)
    temp_number=0
    quotient=0

    for i in range(31,-1,-1):
        if temp_number+(y<<i) <= x:
            temp_number+= y<<i
            quotient |= 1<<i 
        else:
            continue
    if sign==-1:
        quotient= -quotient
    
    print(quotient)
divi(x,y)