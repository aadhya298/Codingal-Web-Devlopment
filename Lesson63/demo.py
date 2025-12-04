# Check if two numbers are equal without using compariosion operators.
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
if a^b==0:
    print(f"{a} and {b} are equal")
else:
    print(f"{a} and {b} are not equal")

# Check one odd occurence
seq=[4,6,3,4,3]
result=0
for i in range(0,len(seq)):
    result= result^seq[i]
print(result)

# Check two odd occurence
order=[2,4,3,2,8,3]
    