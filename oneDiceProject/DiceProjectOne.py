import random
def main():
    gamesPlayed = 0
    while(input("Do you want to play again? y or n - ") == 'y'):
        dice()
        randomNumber()
        gamesPlayed += 1
        print("You have played " + str(gamesPlayed) + " times.\n_____________")
    else:
        print ("Thanks for playing!")


def dice():
    dice1 = (" ------- \n|       |\n|   *   |\n|       |\n ------- ")
    dice2 = (" ------- \n| *     |\n|       |\n|     * |\n ------- ")
    dice3 = (" ------- \n| *     |\n|   *   |\n|     * |\n ------- ")
    dice4 = (" ------- \n| *   * |\n|       |\n| *   * |\n ------- ")
    dice5 = (" ------- \n| *   * |\n|   *   |\n| *   * |\n ------- ")
    dice6 = (" ------- \n| *   * |\n| *   * |\n| *   * |\n ------- ")
    randInt = randomNumber()
    if randInt == 1:
        print(dice1)
    elif randInt == 2:
        print(dice2)
    elif randInt == 3:
        print(dice3)
    elif randInt == 4:
        print(dice4)
    elif randInt == 5:
        print(dice5)
    elif randInt == 6:
        print(dice6)
    else:
        print("I can't believe you've done this.")

def randomNumber():
    return random.randint(1,6)


main()
