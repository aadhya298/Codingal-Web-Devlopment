my_file = open("Lesson50/sample.txt")

# Reading specific characters
# content= my_file.read(20)
# print(content)

# Reading line by line
# firstline = my_file.readline()
# secondline = my_file.readline()
# thirdline = my_file.readline()
# fourthline = my_file.readline()

# print(firstline)
# print(secondline)
# print(thirdline)
# print(fourthline)

# Reading all lines 
# alllines= my_file.readlines() # It retruns list of the str not only str like in read() method

# print(alllines)

# Looping over all lines and printing the str
for l in my_file:
    print(l)