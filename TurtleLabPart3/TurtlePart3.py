import turtle


turtle.setup(width=750, height=1000)
screen = turtle.Screen()
pen = turtle.Pen()

turtle.title("Yurtle the Turtle")
turtle.bgcolor('black')
pen.penup()
pen.speed(10)

def drawMain():
    line()
    square()
    circle()
    triangle()

def line():
    pen.color ("white")
    pen.setx(-400)
    pen.sety(200)
    pen.pendown()
    pen.forward(300)
    pen.right(angle = 90)
    pen.forward(150)
    pen.right(angle = 90)
    pen.forward(300)
    pen.right(angle = 90)
    pen.forward(150)
    turtle.home()
    pen.penup()

def square():
    pen.color(.1, .4, .70)
    pen.setx(-300)
    pen.sety(-350)
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
    pen.setx(150)
    pen.sety(200)
    pen.pendown()
    pen.circle(150)
    pen.penup()

def triangle():
    pen.color("#7fff00")
    pen.setx(200)
    pen.sety(-400)
    pen.pendown()
    pen.right(90)
    pen.forward(100)
    pen.left(angle = 120)
    pen.forward(100)
    pen.left(angle = 120)
    pen.forward(100)
    pen.penup()


drawMain()
turtle.exitonclick()
