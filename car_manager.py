from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car_list = []
        self.cars = 0
        self.spawn_cars()

    def spawn_cars(self):
        random_spawn = random.randint(1,6)
        if random_spawn == 1:
            cars = Turtle()
            cars.shape('square')
            cars.shapesize(stretch_wid=2, stretch_len=1)
            cars.penup()
            cars.setheading(90)
            cars.color(random.choice(COLORS))
            cars.goto(300, random.randint(-250, 250))
            self.car_list.append(cars)

    def move_cars(self):
        for car in self.car_list:
            new_x = car.xcor() - MOVE_INCREMENT
            car.goto(new_x, car.ycor())
