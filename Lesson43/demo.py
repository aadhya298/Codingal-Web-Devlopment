# LISTS
fruits=["Apple","Mango","Banana","Strawberry","Tangerines"]

print(fruits)
print(len(fruits))
print(fruits[4])
print(fruits[len(fruits)-3])
print(fruits[-1])
print(fruits[-2])

#Slicing
print(fruits[1:4])
print(fruits[0:3:2])

fruits.append("Blueberries") # Adds an element at last of a list
print(fruits)
fruits.pop() # Removes the last element or particular if value is given
print(fruits)
fruits.reverse()# Reverses order of list
print(fruits)
fruits.sort() # Sorts it in ascending order
print(fruits)
fruits.remove("Banana") # Removes a particular element
print(fruits)

# DICTIONARIES
myDict={'Name':'Aadhya', 'Age':'16', 'Class':'11', 'School':'RIS'}

print(myDict)
print(len(myDict))

myDict['Age']=15
print(myDict)
myDict.pop('School')
print(myDict)