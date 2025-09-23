# from abc import ABC

# class fruits(ABC):
#     def ripe(self):
#         pass

#     def fall(self):
#         pass

#     def seeds_dispersing(self):
#         pass

# class blueberry(fruits):
#     def ripe(self):
#         print("Blueberry is ripe")

#     def fall(self):
#         print("Blueberry has fallen")

#     def seeds_dispersing(self):
#         print("Blueberry is dispersing seeds")

# b1=blueberry()

# b1.ripe()
# b1.fall()
# b1.seeds_dispersing()

class square:
    def __init__(self,side):
        self.side=side
    def area(self):
        print("Area=",self.side**2)
class cirle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("Area=",3.14 * self.radius**2)

s1= square(4)
c1= cirle(4)

for shape in [s1,c1]:
    shape.area()

class account:
    def __init__(self):
        self.__balance= 500000
    def check_balance(self):
        print(f'Your balance is {self.__balance}')

a1=account()
a1.__balance= 20000
a1.check_balance()