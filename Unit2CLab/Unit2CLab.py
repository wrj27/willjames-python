numList = [9, 18, 27, 36, 45, 54, 63, 72, 81, 90]
print (numList)
print (len (numList))
print (numList [1]), print (numList [9])

subList = numList[0:5]
print (subList)
subList.insert(0,7)
print (subList)
subList.append(99)
print (subList)
subList2 = numList+[100]
print (subList2)

List2 = ["Calculus", "Comp", "French", "Gov", "Python", "Physics", "Eniro"]
List2.remove("Gov")
favClass = List2.pop(3)
print ("My favorite class is " + favClass)
