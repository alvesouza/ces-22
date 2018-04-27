import turtle

distance = 350
length = 100
window = turtle.Screen()

turt = turtle.Turtle()

def drawStar():
    #turtle.resetscreen()
    for i in range(0,5):
        turt.forward(length)
        turt.right(144)
def drawAnswer():
    turtle.resetscreen()
    turt.penup()
    turt.right(180)
    turt.forward(200)
    turt.right(180)
    turt.pendown()
    for i in range(0,5):
        turt.penup()
        turt.forward(distance)
        turt.right(144)
        turt.pendown()
        drawStar()
drawAnswer()
