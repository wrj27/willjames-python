import turtle


turtle.setup(width=750, height=1000)
screen = turtle.Screen()
pen = turtle.Pen()

turtle.title("Turtle Starter")
turtle.bgcolor('black')
pen.penup()
pen.speed(0)

def drawMain():
    line()
    square()
    circle()
    triangle()

def line():
    pen.color ("white")
    turtle.goto(0, 0)
    pen.down()
    pen.forward(100)
    pen.penup()
    turtle.home()

def square():
    pen.color(.1, .4, .70)
    pen.setx(-100)
    pen.sety(100)
    pen.pendown()
    pen.forward(200)
    pen.right(angle = 90)
    pen.forward(200)
    pen.right(angle = 90)
    pen.forward(200)
    pen.right(angle = 90)
    pen.forward(200)
    pen.penup()


def circle():
    pen.color("orange")
    pen.setx(300)
    pen.sety(0)
    pen.pendown()
    pen.circle(300)
    pen.penup()

def triangle():
    pen.color("#7fff00")
    pen.setx(-200)
    pen.sety(-150)
    pen.pendown()
    pen.right(90)
    pen.forward(400)
    pen.left(angle = 120)
    pen.forward(400)
    pen.left(angle = 120)
    pen.forward(400)
    pen.penup()

drawMain()

turtle.exitonclick()
