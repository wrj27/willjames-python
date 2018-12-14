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
    def getDanger(self):
        input("Is this animal dangerous? - t ot f -")
        if "t":
            return ("This animal is dangerous")
        elif "f":
            return ("This animal is not dangerous.")
        else:
            "y"
    def getcName(self):
        return (self.name2)
x = input("Is this animal dangerous?")

myCage = cagePet(input("Give a caged animal"), x, input("Name it. - "))
print(myCage.getcType())
if x is "t":
    print("This animal is dangerous.")
elif x is "f":
    print("This animal is not dangerous.")
else:
    "y"
print(myCage.getcName())





