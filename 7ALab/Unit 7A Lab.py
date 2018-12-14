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


class myPet1:
    def __init__(self, dType, dName, dBreed):
        self.type = dType
        self.name = dName
        self.breed = dBreed
    def getDType(self):
        return (self.type)
    def getDName(self):
        return (self.name)
    def getDBreed(self):
        return (self.breed)

myDog = myPet1("Dog", input("Give name. - "), input("What breed?"))
print(myDog.getDType())
print(myDog.getDName())
print(myDog.getDBreed())


class myPet2:
    def __init__(self, zType, zName, zBreed):
        self.type = zType
        self.name = zName
        self.breed = zBreed
    def getZType(self):
        return (self.type)
    def getZName(self):
        return (self.name)
    def getZBreed(self):
        return (self.breed)

myCat = myPet2("Cat", input("Give name. - "), input("What breed?"))
print(myCat.getZType())
print(myCat.getZName())
print(myCat.getZBreed())



class cagePet1():
    def __init__(self, cType, cDanger, cName):
        self.type2 = cType
        self.danger = cDanger
        self.name2 = cName
    def getcType(self):
        return (self.type2)
    def getDanger(self):
        return (self.danger)
    def getcName(self):
        return (self.name2)
b = "t"

myCage1 = cagePet1("Snake", b, input("Name it. - "))
print(myCage1.getcType())
if b is "t":
    print("This animal is dangerous.")
elif b is "f":
    print("This animal is not dangerous.")
else:
    "y"
print(myCage1.getcName())


class cagePet2():
    def __init__(self, cType, cDanger, cName):
        self.type2 = cType
        self.danger = cDanger
        self.name2 = cName
    def getcType(self):
        return (self.type2)
    def getDanger(self):
        return (self.danger)
    def getcName(self):
        return (self.name2)

a = "f"
myCage2 = cagePet2("Rat", a, input("Name it. - "))
print(myCage2.getcType())
if a is "t":
    print("This animal is dangerous.")
elif a is "f":
    print("This animal is not dangerous.")
else:
    "y"
print(myCage2.getcName())


