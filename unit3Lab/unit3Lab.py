def school():
    print ("Bellarmine")
    print ("physics")

def whatGrade():
    grade = 12
    years = (int(12))
    print ("I am in " + str(grade) + " grade and i have gone to school for " + str(years) + " years")

def whatCity(myCity, myGrade):
    print ("hello " + str(city))
    print ("I am in " + str(grade2) + " grade")

from random import *
def randomNumbers():
    x = input("what is the starting number?")
    y = input("what is the end number?")
    myNumber = randint(int(x), int(y))
    print (myNumber)

def areaRectangle(myLength, myWidth):
    area = (int(l) * int(w))
    print (str(area))

def perimeterBox(sideA, sideB):
    perimeter = (int(a) * 2 + int(b) * 2)
    return (perimeter)



school()

whatGrade()

city = input ("What city are you in?")
grade2 = input ("What grade are you in?")
whatCity (city, grade2)


randomNumbers()

l = input ("What is your length?")
w = input ("What is your width?")
areaRectangle (l, w)


a = input ("Enter a number.")
b = input ("Enter another number.")
finalNumber = perimeterBox(a, b)

print ("The answer is " + str(finalNumber))
