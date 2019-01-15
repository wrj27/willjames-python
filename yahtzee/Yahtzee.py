import random


def main():
    total_score = 0
    for x in range(1,6):
        print("Turn " + str(x) + "!")
        dice = []
        for x in range(5):
            dice.append(random.randint(1,6))
        print("Roll 1: ", end ="")
        for x in range(len(dice)):
            if x < len(dice) - 1:
                print(dice[x], end =" ")
            else:
                print(dice[x])

        keep = input("Which numbers would you like to keep? ")
        keep = keep.split(',')
        print("Roll 2: ", end ="")
        for x in range(5):
            if str(x + 1) not in keep:
                dice[x] = random.randint(1,6)
            if x < len(dice) - 1:
                print(dice[x], end =" ")
            else:
                print(dice[x])
        dice.sort()
        score = patterns(dice)
        total_score = total_score + score
    print("Final score: " + str(total_score) + " points.")



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
    return random.randint(0,6)



main()
