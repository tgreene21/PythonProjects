from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):

        super().__init__()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
        self.speed("fastest")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over", align=ALIGNMENT, font=FONT)