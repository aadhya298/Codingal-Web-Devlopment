a= int(input("Enter a number:"))
b= int(input("Enter a number:"))

ans= a^b
count=0

while ans>0:
    if (ans & 1)==1:
        count+=1
    ans=ans>>1
print(count)

#Power set
sets=[1,2,3]
n=2**len(sets)
for i in range(0,n):
    for j in range(0,len(sets)):
        if (i &(1<<j))>0:
            print(sets[j] , end=" ")
    print("")