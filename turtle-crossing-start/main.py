import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.make_car()
    car_manager.move_car()

    #Detect Collision with car
    for car in car_manager.cars:
        if player.distance(car, 0) < 20:
            scoreboard.game_over()
            game_is_on = False

    #When the turtle reaches the finishline, reset the position
    if player.ycor() == player.finishline:
        player.finish()
        scoreboard.level_up()
        car_manager.next_level()

screen.exitonclick()