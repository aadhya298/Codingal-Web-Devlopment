class flowers:
    def __init__(self,name,color):
        self.fname= name
        self.fcolor= color
        print("Constructor automatically getting called")

    def __del__(self):
        print("Destructor automatically getting called")

    def bouquet(self):
        print("ROSE , DAISY , LILY")

Lavendar= flowers("Lotus","Pink")
Lavendar.bouquet()
del Lavendar
# Lavendar.bouquet() will give an error as we already called destructor was 'Lavendar' and it is now undefined 
Jasmine= flowers("Tulip","Yellow")
Jasmine.bouquet()
del Jasmine

class employ:
    def __init__(self): 
        print("Contructor")
    def __del__(self):
        print("Destructor")

manager= employ()
