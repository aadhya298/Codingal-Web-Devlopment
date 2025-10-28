arr = [13,45,63,24,3,8,67,9,87,559,381]

print(arr[5]) # Big O[1] constant time complexity for accessing an element through index

for i in range(len(arr)): # Big O[n] time complexity for iterating over a loop
    print(i)

for i in range(len(arr)):# Big O[n^2] time complexity for nested loop
    for j in range(len(arr)):
        print(arr[i],arr[j])
    
# BINARY SEARCH
def binary_search(arr,target):
    left= 0
    right= len(arr)-1

    while left<=right:
        mid=(left+right)//2
        print(f"Left:{left} , Right:{right} , Mid:{mid} and the mid element is {arr[mid]}") #Debugging statement
        
        if arr[mid]==target:
            return mid
        elif arr[mid] < target:
            left= mid+1
        else:
            right= mid-1
    return -1

sorted_array= sorted(arr) # Binary search requires sorted array
aim=87
result= binary_search(sorted_array, aim)
print(f"Target {aim} found at index:{result}")