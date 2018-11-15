import turtle

pen = turtle.Pen()
turtle.setup(width = 1000, height = 750)
turtle.title("Poly Turtle")
pen.speed(0)
turtle.bgcolor(input("Your background color is -"))

def mainDraw():
    side = int(input("What is the length of your sides? - "))
    num = int(input("How many sides does your shape have? - "))
    color = input("What color is your pen? - ")
    pen.pencolor(str(color))
    x = 0
    w = int(((num-2) * 360) / (num / 2))
    #z = int(360 / num)
    #y = int(((num-2) * 360) / (num))
    while x < num:
        pen.pendown()
        pen.forward(side)
        pen.left(angle = w)
        pen.penup()
        x += 1




mainDraw()
turtle.exitonclick()
