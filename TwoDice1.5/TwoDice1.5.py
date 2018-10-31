import random
def main():

    setOfDice = [0] * 6     #creatw a list to store 6 dice
    setOfDice = dice()

    printDice(setOfDice)


    play = "y"
    gamesPlayed = 0

    while play == "y":
        for i in range(0,22):
            print("_", end = "")  #print line between games
        dice()

        gamesPlayed += 1
        print("You have played " + str(gamesPlayed) + " times.")
    else:
        print ("You played " + str(gamesPlayed) + " games.\nThanks for playing!")


def dice():
    dice = [0] * 6
    topBot = "-------"
    blank = "|       |"
    mid = "|   *   |"
    left = "| *     |"
    right = "|     * |"
    deux = "| *   * |"

    for num in range(0,6):
        if num == 0:
            dice[num] = [topBot,blank,mid,blank,topBot]
        elif num == 1:
            dice[num] = [topBot,left,blank,right,topBot]
        elif num == 2:
            dice[num] = [topBot,left,mid,right,topBot]
        elif  num == 3:
            dice[num] = [topBot,deux,blank,deux,topBot]
        elif num == 4:
            dice[num] = [topBot,deux,mid,deux,topBot]
        else:
            dice[num] = [topBot,deux,deux,deux,topBot]
    return dice

#generate a rand num between 1 and 6 to rep dice
def rollDice():
    return random.num(1,6)


def printDice():
    print(dice)



main()
