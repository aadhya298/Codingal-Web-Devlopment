a=10100
z=0
o=0
while a:
    if a%2==1:
        o+=1
    else:
        z+=1
    a=a//2

print(o,z)    