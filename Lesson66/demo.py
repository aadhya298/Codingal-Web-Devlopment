a= int(input("Enter a number:"))
b= int(input("Enter a number:"))

ans= a^b
count=0

while ans>0:
    if (ans & 1)==1:
        count+=1
    ans=ans>>1
print(count)

