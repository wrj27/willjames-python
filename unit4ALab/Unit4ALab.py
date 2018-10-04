def main():
    someWord = str (input ("Pick a word, any word."))
    print (someWord)

    print(devowel(someWord))




def devowel(someWord):
    someWord2 = someWord
    noVowel = ""
    for w in someWord2:
        if (w != "a" and w != "e" and w != "i" and w != "o" and w != "u"):
            noVowel = noVowel + w
    return (noVowel)


main()
