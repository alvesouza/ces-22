import turtle

length = 100
window = turtle.Screen()

turt = turtle.Turtle()

def drawStar():
    turtle.resetscreen()
    for i in range(0,5):
        turt.forward(length)
        turt.right(144)

drawStar()