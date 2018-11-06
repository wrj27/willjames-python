import random
DICENUM = 2


def main():


    gamesPlayed = 0
    setOfDice = diceBuild()

    while input("Do you want to play? y or n -") == "y":
        diceSet = [0] * DICENUM
        addsets = []
        for i in range(DICENUM):
            roll = randomNum()
            addsets.append(roll + 1)
            diceSet[i] = setOfDice[roll]
        printDice(diceSet)
        print(addsets)

        gamesPlayed += 1
        print("You have played " + str(gamesPlayed) + " times.")
    else:
        print ("You played " + str(gamesPlayed) + " games.\nThanks for playing!")


def diceBuild():
    topBot = " ------- "
    blank = "|       |"
    mid = "|   *   |"
    left = "| *     |"
    right = "|     * |"
    twodot = "| *   * |"
    one = [topBot,blank,mid,blank,topBot]
    two = [topBot,left,blank,right,topBot]
    three = [topBot,left,mid,right,topBot]
    four = [topBot,twodot,blank,twodot,topBot]
    five = [topBot,twodot,mid,twodot,topBot]
    six = [topBot,twodot,twodot,twodot,topBot]
    allDice = [one, two, three, four, five, six]
    return allDice


def printDice(allDice):
    for dice in range(len(allDice[0])):
        for side in range(len(allDice)):
            print (allDice[side][dice], end = "\t")
        print()


def randomNum():
    return random.randint(0,5)



main()
