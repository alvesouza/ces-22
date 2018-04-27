import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("white")

class trafficLight:
    def __init__(self):
        self.tess = turtle.Turtle()
        self.tess.color("red")
        self.size = 3
        self.tess.shape("circle")
        self.tess.shapesize(self.size)
        self.i = 0
    def changeColor(self):
        self.i = self.i + 1
        self.i = self.i%3
        if self.i == 0:
            self.tess.color("red")
        elif self.i == 1:
            self.tess.color("green")
        elif self.i == 2:
            self.tess.color("blue")
        wn.ontimer(self.changeColor, 2000)
    def add(self):
        self.size = self.size + 1
        self.tess.shapesize(self.size)
    def sub(self):
        self.size = self.size - 1
        if self.size == 0:
            self.size = 1
        self.tess.shapesize(self.size)


light = trafficLight()

wn.ontimer(light.changeColor, 2000)
wn.onkey(light.add,"+")
wn.onkey(light.sub,"-")
wn.listen()
wn.mainloop()
