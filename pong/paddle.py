from turtle import Turtle
WIDTH = 5
LENGTH = 1

class Paddle(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid= WIDTH, stretch_len= LENGTH)
        self.goto(position_x, position_y)
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)