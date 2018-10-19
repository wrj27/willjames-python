def Main():
    for z in range(0,7):
        draw7()

    for v in range(0,3):
        starsAndStripes()

    incTriangle(8)


def draw7():
    for w in range (0,7):
        splats = ""
        for w in range (0,7):
            splats += "*"
    print (splats)

def starsAndStripes():
    for t in range(0,7):
        asterix = ""
        dash = ""
        for t in range(0,7):
            asterix += "*"
            dash += "-"
    print (asterix)
    print (dash)

def incTriangle(num):
    for i in range(num):
        for j in range(i):
            print (str(i),end = "")
        print()






Main()
