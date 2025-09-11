class colors:
    c="Aashi" #Variable belongs to the class :- Class Variable
    print("Hi, I'm a class colors")

    # Constructors get called on their own no need to call them 
    def __init__(self): # For constructor "__init__" will only be used
        self.a="Aadhya" # Var belongs to object as self denotes object of the class :- Instance Variable
        self.b='Singh' # Var belongs to object as self denotes object of the class :- Instance Variable
        print('Constructor automatically gets called')

    def rainbow(self):
        print("Rainbow has 7 colors")
        print("Violet")
        print("Indigo")
        print("Blue")
        print("Green")
        print("Yellow")
        print("Orange")
        print("Red")

    def calculate(self,p,q):
        print("Love Colors!!")
        return p+q

black= colors()
beige= colors()
crimson= colors()

print(beige.a)
print(crimson.b)
print(colors.c)
# print(color.a) will give error as var a is not defined for the class colors 