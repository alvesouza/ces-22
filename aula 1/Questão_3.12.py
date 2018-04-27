import turtle

window = turtle.Screen()

pet = turtle.Turtle()
pet.color("blue")
pet.shape("turtle")

line = turtle.Turtle()
line.color("blue")

def drawAtAngle(angle):
    pet.penup()
    line.penup()
    pet.left(angle)
    line.left(angle)

    pet.forward(90)
    line.forward(50)

    line.pendown()
    line.forward(20)
    line.penup()
    pet.stamp()
    
    pet.left(180)
    line.left(180)

    pet.forward(90)
    line.forward(70)
    
    pet.left(180 - angle)
    line.left(180 - angle)

def drawAnswer():
    pet.stamp()
    angle = 0
    while angle < 360:
        drawAtAngle(angle)
        angle += 30
drawAnswer()