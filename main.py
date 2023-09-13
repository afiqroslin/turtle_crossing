import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()

screen.listen()
screen.onkeypress(player.up, "Up")

player.spawn_turtle()

game_is_on = True
speed = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.spawn_cars()
    car.move_cars(speed)

    for car_collide in car.car_list:
        if car_collide.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        player.cross_success()
        score.level_clear()
        speed += 1

    print(speed)
screen.exitonclick()





