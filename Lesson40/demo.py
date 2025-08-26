rng=int(input("Enter for how many times you need to print the stars:"))

for i in range(1,rng+1): # Here if row is 1 then

    for j in range(1,i+1): # This loop determines that no. of stars to be printed in row 1 should be 1 and so on...

        print("*" , end=" ") # end=" " defines:as many times the loop will run the print matter will be in same row

    print("") #after the loop ends then before checking for i's next value it works as an line break so that when again the inner loop runs the outputs should be in a row but next to the previous one. 

totalsum=0
for i in range(1,501):
    totalsum= totalsum+i
print(totalsum)

for i in range(1,11):
    print(f"23 * {i} = {23*i}")