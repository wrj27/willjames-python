import random
DICENUM = 5

print("Welcome to yahtzee. If you already know how to play, great! If not, the game will score for you; however, it does not score ones, two, ect.")
print("You will get to roll twice each round for a total of five rounds. After five rounds the game is finished and your final score will be printed.")
print("To keep the numbers you want after the first roll you must type the number of the position it is in beginning with the number 1.")
print("For example: I rolled a 1 5 6 3 3. I want to keep both threes but nothing else. I type 4,5. When I hit enter, the threes reappear.")
print("This time though I roll a four of a kind that looks like this: 3 3 4 3 3.")
print("Good luck and have fun.")
input("-- Press Enter to Begin --")


def of_kind(dice):
    of_a_kind = 1
    for x in range(5):
        current = x
        count = 1
        while count != -1:
            if current + 1 < 5:
                if dice[current + 1] == dice[x]:
                    current = current + 1
                    count = count + 1
                    if count > of_a_kind:
                        of_a_kind = count
                else:
                    count = -1
            else:
                count = -1

    if of_a_kind == 5:
        print("Five of a Kind: 50 points.")
        return 50

    elif of_a_kind == 4 or of_a_kind == 3:
        total = 0
        for index in range(5):
            total = total + int(dice[index])
        if of_a_kind == 4:
            total = total + 10
            print("Four of a Kind: " + str(total) + " points.")
            return total
        else:
            no_duplicates = []
            for index in range(5):
                if dice[index] not in no_duplicates:
                    no_duplicates.append(dice[index])
            if len(no_duplicates) == 2:
                print("Full House: 25 points.")
                return 25
            else:
                total = total + 5
                print("Three of a Kind: " + str(total) + " points.")
                return total
    else:
        return 0

def straight(dice):
    straight = 1
    for index in range(len(dice)):
        current = index
        count = 1
        while(current != -1):
            if current + 1 < len(dice):
                if int(dice[current + 1]) - int(dice[current]) == 1:
                    current = current + 1
                    count = count + 1
                elif int(dice[current + 1]) == int(dice[current]):
                    current = current + 1
                else:
                    current = -1
            else:
                current = -1
            if count > straight:
                straight = count
    if straight == 4:
        print("Small Straight: 30 points.")
        return 30
    elif straight ==5:
        print("Large Straight: 40 points.")
        return 40
    else:
        return 0

def patterns(dice):
    score = of_kind(dice)
    if score == 0:
        score = straight(dice)
    if score == 0:
        print("No Pattern: 0 points.")
    return score

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
    print("Thanks for playing!")
main()
