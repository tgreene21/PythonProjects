from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.p1_score = 0
        self.p2_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-180, 200)
        self.write(self.p1_score, align=ALIGNMENT, font=FONT)
        self.goto(180, 200)
        self.write(self.p2_score, align=ALIGNMENT, font=FONT)

    def p1_point(self):
        self.p1_score += 1
        self.update_scoreboard()

    def p2_point(self):
        self.p2_score += 1
        self.update_scoreboard()