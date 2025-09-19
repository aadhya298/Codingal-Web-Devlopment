class names:
    def __init__(self, name):
        self.name= name
    def salutation(self):
        print("Hi",self.name )

class girl_names(names):
    def __init__(self, name):
        super().__init__(name)

inp= input("What's your name")
Ahaan= names(inp)
Aaru= girl_names(inp)

Ahaan.salutation()
Aaru.salutation()