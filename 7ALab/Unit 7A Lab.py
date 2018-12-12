class freePet():
    def __init__(self, fType, fName, fBreed):
        self.type = fType
        self.name = fName
        self.breed = fBreed
    def getfType(self):
        return (self.type)
    def getfName(self):
        return (self.name)
    def getfBreed(self):
        return (self.breed)

myDog = freePet('Dog', 'Rex', 'Corgi')
print(myDog.getfType())
print(myDog.getfName())
print(myDog.getfBreed())


class cagePet():
    def __init__(self, cType, cDanger, cName):
        self.type2 = cType
        self.danger = cDanger
        self.name2 = cName
    def getcType(self):
        return (self.type2)
    def getcDanger(self):
        return (self.danger)
    def getcName(self):
        return (self.name2)

myCage = cagePet(input("Give a caged animal"), x = input("Is this animal dangerous? - t or f", input("Name it. - ")))
print(myCage.getcType())
if x is "t":

