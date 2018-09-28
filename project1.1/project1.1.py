def main():
    grade = int(input ("What grade are you in? - "))
    print (getYearInSchool(grade))

    myGradesList = [92.4, 97.8, 85.6, 87.1]
    averages = calcAverageGrade(myGradesList)
    print ("Your average grade is", averages)

    print ("Your letter grade is", getLetterGrade(averages))


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

def calcAverageGrade(myGradesList):
    average = float (((myGradesList[0] + myGradesList[1] + myGradesList[2] + myGradesList[3]) / len(myGradesList)))
    return average

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
