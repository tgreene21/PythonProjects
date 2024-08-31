from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        self.cars = []
        super().__init__()
        self.shape("square")
        self.penup()
        self.move_speed = STARTING_MOVE_DISTANCE
        self.hideturtle()


    def make_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid= 1, stretch_len=2)
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            new_x = car.xcor() - self.move_speed
            car.goto(new_x, car.ycor())

    def next_level(self):
        self.move_speed += MOVE_INCREMENT
