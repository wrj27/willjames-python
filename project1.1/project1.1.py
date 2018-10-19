def main():
    grade = int(input ("What grade are you in? - "))
    print (getYearInSchool(grade))
    input ("pause")


    average = calcAverageGrade()
    print ("Your average grade is " + str(average))
    input ("pause")

    getLetterGrade(average)
    print ("Your letter grade is", getLetterGrade(average))
    if average >= 70:
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

def calcAverageGrade():
    sum = float(0)
    num = input ("numbers")
    print (num)
    numList = []
    input ("pause")
    for i in range (0, int(num)):
        myNum = input ("Pick a grade")
        numList.append (int(myNum))
        print (numList)
        input ("pause")
    for i in numList:
        sum = (sum + float(i))
    print (sum)
    average = (sum/len(numList))
    print (average)
    return (average)

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
