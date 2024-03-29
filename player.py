from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move_up(self):
        current_y = self.ycor()
        current_x = self.xcor()
        self.goto(current_x, current_y + MOVE_DISTANCE)

    def turtle_restart(self):
        self.goto(STARTING_POSITION)



