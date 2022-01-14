import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()


screen.listen()
screen.onkeypress(player.move_up, 'Up')

game_is_on = True
while game_is_on:

    # increase/decrease card speed by varying screen update rate
    time.sleep(0.1)
    screen.update()

    # add cars and move them
    car_manager.create_car()
    car_manager.car_move()

    # score point and reset turtle
    if player.ycor() >= 290:
        player.turtle_restart()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        car_manager.increase_car_speed()

    # detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

