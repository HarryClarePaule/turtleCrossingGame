from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_POSITION = 300


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.all_cars = []
        self.hideturtle()
        self.penup()

    def create_car(self):
        car_frequency = random.randint(1,6)
        if car_frequency == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(X_POSITION, random.randint(-250, 250))
            self.all_cars.append(new_car)
        else:
            pass

    def car_move(self):
        for car in range(len(self.all_cars)):
            new_x = self.all_cars[car].xcor()
            new_y = self.all_cars[car].ycor()
            self.all_cars[car].goto(new_x - self.car_speed, new_y)

    def increase_car_speed(self):
        self.car_speed *= 1.25




