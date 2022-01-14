from turtle import Turtle

ALIGNMENT = "Left"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-280, 240)
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def import_high_score(self):
        file = open("highscore.txt")
        content = file.read()
        self.high_score = int(content)
        file.close()

    def update_scoreboard(self):
        self.write(f'Score = {self.score}    High Score = {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(-20, 0)
        self.write("Game Over", move=False, align=ALIGNMENT, font=FONT)








