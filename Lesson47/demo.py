class names:
    def __init__(self, name):
        self.name= name
    def salutation(self):
        print("Hi",self.name )

class girl_names(names): # girl_names is the child class of names. So it will inherit its methods
    def __init__(self, name):
        super().__init__(name) # Caliing the the constructor of parent class and accessing the methods

inp= input("What's your name")
Ahaan= names(inp)
Aaru= girl_names(inp)

Ahaan.salutation()
Aaru.salutation()