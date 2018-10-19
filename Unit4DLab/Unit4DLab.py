def main():
    shoppingCart = [["toothpaste", "qtips", "milk"], ["milk", "candy", "apples"], ["paper", "pencils", "qtips"]]
    print (allInOne(myShoppingCart))


def allInOne(myShoppingCart):
    newList = []
    for list in shoppingCart:
        for item in list:
            if item not in newList:
                newList.append (item)
    return (newList)



main()
