num= int(input("Enter a number:"))
a= str(num)
power_count= len(a)
val=num
result=0
while val != 0:
    digit= val % 10
    result= result+ digit**power_count
    val= val//10

if result==num:
    print(f"{num} is an armstrong number")
else:
    print(f"{num} is not an armstrong number")

check_value=1
val1=num
factor=[]
while check_value<=val1:
    remainder= val1 % check_value
    if remainder==0:
        factor.append(check_value)
    check_value+=1
print(factor)

P=input("Enter a roman numeral:")
roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
int_form=0
for i in range(len(P)):
    if i+1<len(P) and roman[P[i]]<roman[P[i+1]]:
        int_form -= roman[P[i]]
    else:
        int_form += roman[P[i]]
print(f"Integer form of {P} is {int_form}")