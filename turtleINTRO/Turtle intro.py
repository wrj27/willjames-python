import turtle

pen = turtle.Pen()
turtle.bgcolor("black")
pen.speed(1)

def main():
    firstSquare()
    secondSquare()
    rectangle1()
    rectangle2()
    turtle.exitonclick()



def firstSquare():
    pen.color(1.0, 0.0, 0.0)
    pen.pendown()
    pen.forward(20)
    pen.left(angle = 90)
    pen.forward(20)
    pen.left(angle = 90)
    pen.forward(20)
    pen.left(angle = 90)
    pen.forward(20)
    pen.left(angle = 90)
    pen.penup()

def secondSquare():
    pen.color(.16, .45, .1)
    pen.pendown()
    pen.forward(100)
    pen.right(angle = 90)
    pen.forward(100)
    pen.right(angle = 90)
    pen.forward(100)
    pen.right(angle = 90)
    pen.forward(100)
    pen.right(angle = 90)
    pen.penup()

def rectangle1():
    pen.color(.0, 1.0, .0)
    pen.pendown()
    pen.left(angle = 180)
    pen.forward(35)
    pen.left(angle = 90)
    pen.forward(55)
    pen.left(angle = 90)
    pen.forward(35)
    pen.left(angle = 90)
    pen.forward(55)
    pen.penup()

def rectangle2():
    pen.color(.34, .87, 1.0)
    pen.pendown()
    pen.forward(250)
    pen.left(angle = 90)
    pen.forward(100)
    pen.left(angle = 90)
    pen.forward(250)
    pen.left(angle = 90)
    pen.forward(100)




main()
