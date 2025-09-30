file = open('Lesson49/sample.txt', 'r')
print(file.read())


file = open('Lesson49/sample.txt', 'w')
file.write("Hi I'm Naina")
file.close()

file = open('Lesson49/sample.txt', 'a')
file.write(" I'm in 11th")


