from turtle import Turtle
SIZE = 6
COLOR = "red"

# Inherits the Turtle class and initializes the object by drawing a square 610 x 610 units
class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(-305, -325)
        self.color(COLOR)
        self.pensize(SIZE)
        self.pendown()
        for i in range(4):
            self.forward(610)
            self.left(90)
