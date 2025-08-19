x = 35
y = "Aadhya Singh"
z = True
a = False
b = 24.67

print(type(x))
print(type(b))
print(type(z))
print(type(y))

X = str(x) #float(), str(), bool(), int() 
print(type(X))

#Operators
# + , - , * , /
print(13%2) #Modulo operator (returns remainder)
print(22//7) #Floor Division (returns floor value)
print(4**3) #Exponentation

# == , != , > , < , >= , <=
p = 40
q = 35
print(p!=q)
print(p<=q)

print(len(y)) # Length of a string
print(y[3])
print(y[3:9:1])
print(y[3:9:2]) #Step is 2 so it will give alternatively

name= input("Hi what is your name:")
print("The name of the user is", name)