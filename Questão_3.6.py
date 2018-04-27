import turtle

length = 50
window = turtle.Screen()

turt = turtle.Turtle()

def drawTriangule():
    turtle.resetscreen()
    for i in range(0,3):
        turt.forward(length)
        turt.left(120)

def drawSquare():
    turtle.resetscreen()
    for i in range(0,4):
        turt.forward(length)
        turt.left(90)
        
def drawHexagon():
    turtle.resetscreen()
    for i in range(0,6):
        turt.forward(length)
        turt.left(60)
def drawOctagon():
    turtle.resetscreen()
    for i in range(0,8):
        turt.forward(length)
        turt.left(45)
def drawPoligon(n):
    angle = (360)/n
    length2 = length*8/n#para que não seja muito grande
    if n < 2:
        print("Poligono invalido")
    else:
        turtle.resetscreen()
        for i in range(0,n):
            turt.forward(length2)
            turt.left(angle) 
drawTriangule()
drawSquare()
drawHexagon()
drawOctagon()