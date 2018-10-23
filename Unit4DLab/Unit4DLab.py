def main():
    shoppingCart = [["toothpaste", "qtips", "milk"], ["milk", "candy", "apples"], ["paper", "pencils", "qtips"]]
    print (allInOne(shoppingCart))
    print (countQtips(shoppingCart))


def allInOne(shoppingCart):
    newList = []
    for list in shoppingCart:
        for item in list:
            if item not in newList:
                newList.append (item)
    return (newList)

def countQtips(shoppingCart):
    list2 = []
    total = 0
    for list in shoppingCart:
        for item in list:
            if item not in shoppingCart:
                list2.append(item)
    for w in range(len(list2)):
        if list2[w] == "qtips":
            total += 1
    return (total)




main()
