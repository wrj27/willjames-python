def theMain():
    for z in range(0,7):
        draw7()

    for v in range(0,3):
        starsAndStripes()


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

def incTriangle():
    for a in range(0,7):
        print (input("num"))




theMain()
