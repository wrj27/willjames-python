def main():
    grade = int(input ("What grade are you in? - "))
    print (getYearInSchool(grade))
    input ("pause")

    calcAverageGrade(averages)
    print ("Your average grade is", averages)
    input ("pause")

    print ("Your letter grade is", getLetterGrade(averages))
    if averages >= 70:
        print ("Yay, you're passing")
    else:
        print ("You need to study")


def getYearInSchool(grade):
    if grade == 9:
        return ("Freshman")
    elif grade == 10:
        return ("Sophomore")
    elif grade == 11:
        return ("Junior")
    elif grade == 12:
        return ("Senior")
    else:
        return ('Not in highschool.')

def calcAverageGrade(averages):
    num = int (input ("numbers"))
    numList = []
    for i in range (0, int(num)):
        myNum = input ("Pick a number")
        numList.append (myNum)
        print (numList)
    total = 0
    for i in numList:
        total = total + i
        print ("i = " + str(i))
        print ("total = " + str(total))
        input ("pause")

    averages = total / int(num)
    print ("total " + str(total) + " / " + num)
    print (averages)
    return calcAverageGrade(averages)

def getLetterGrade(averages):
    if averages >= 90:
        return "A"
    elif averages >= 80:
        return "B"
    elif averages >= 70:
        return "C"
    elif averages >= 60:
        return "D"
    elif 0<= averages < 60:
        return "F"
    else:
        return "get smart"


main()
