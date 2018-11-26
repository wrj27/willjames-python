import turtle

pen = turtle.Pen()
turtle.title("Swirly")
pen.speed(0)
turtle.bgcolor("black")
pen.color("white") #body

#rosette part
def mainDraw():
    coolThing()


def coolThing():
    pen.color(input("Choose your first color - "))
    for x in range(100):
        pen.circle(100)
        pen.left(angle = 35)
    pen.color(input("Choose your second color - "))
    for y in range(100):
        pen.circle(200)
        pen.left(angle = 95)

mainDraw()
turtle.exitonclick()


#drawing part
#def main():
#     head()
#     body()
#     legs()
#     arms()
#
#
# def head():
#     pen.up()
#     pen.sety(200)
#     pen.down()
#     pen.circle(100)
#     pen.up()
#     pen.setx(-35)
#     pen.sety(325)
#     pen.color("blue") #eyes
#     pen.down()
#     pen.circle(10)
#     pen.up()
#     pen.setx(35)
#     pen.down()
#     pen.circle(10)
#     pen.up()
#     pen.setx(0)
#     pen.sety(300)
#     pen.left(angle = 270)
#     pen.color("white")
#     pen.down()
#     pen.forward(25)
#     pen.left(angle = 90)
#     pen.forward(25)
#     pen.up()
#     pen.setx(-45)
#     pen.sety(250)
#     pen.color("red") #lips
#     pen.down()
#     pen.right(angle = 25)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.left(5)
#     pen.forward(10)
#     pen.up()
#
# def body():
#     pen.sety(200)
#     pen.setx(0)
#     pen.color("white") #body
#     pen.down()
#     pen.right(angle = 115)
#     pen.forward(250)
#     pen.up()
#
# def legs():
#     pen.left(angle = 45)
#     pen.down()
#     pen.forward(150)
#     pen.up()
#     pen.setx(0)
#     pen.sety(-50)
#     pen.right(angle = 90)
#     pen.down()
#     pen.forward(150)
#     pen.up()
#
# def arms():
#     pen.setx(0)
#     pen.sety(75)
#     pen.down()
#     pen.right(angle = 90)
#     pen.forward(100)
#     pen.up()
#     pen.setx(0)
#     pen.sety(75)
#     pen.right(angle = 90)
#     pen.down()
#     pen.forward(100)
#     pen.up()
#
#
#
# main()
# turtle.exitonclick()
