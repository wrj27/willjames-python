def main():
    print ("start here")

    input ("") #add a title for this input

    getYearInSchool (z) #calling back the get yearInSchool Function with input as argument
    #argument gets passed to get yearInSchool
    getYearInSchool ()

    print ("I am a " + str(longYearInSchool))

    myGradesList = [92.4, 97.8, 85.6, 87.1]
    averageGrade #calling the average grade function with average grade as argument
    #pass the aarguments to get the average grade
    calcAverageGrade ()

    print (averageGrade)

    #call the letter grade function with average grade as the argument
    #1 argument gets passed to getLetterGrade
    getLetterGrade()

    print (letterGrade)

    #determine if letter grade is passing or failing

def getYearInSchool (z):
    print ("getYearInSchool")
    myLongGrade = input ("What is your year in school?")
    return longGrade

def calcAverageGrade(x,y):
    print ("calcAverageGrade")
    return calcAverageGrade

def getLetterGrade(w):
    print ("getLetterGrade")
    return getLetterGrade


main()
