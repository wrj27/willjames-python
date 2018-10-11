def main():
    someWord = str (input ("Pick a word, any word."))
    print (someWord)

    print(devowel(someWord))

    mathStuff()




def devowel(someWord):
    someWord2 = someWord
    noVowel = ""
    for w in someWord2:
        if (w != "a" and w != "e" and w != "i" and w != "o" and w != "u"):
            noVowel = noVowel + w
    return (noVowel)

def mathStuff ():
    num = input ("numbers")
    numList = []
    for i in range (0, int(num)):
        myNum = input ("Pick a number")
        numList.append (int(myNum) * int(num))
        print (numList)
    return (numList)


main()
