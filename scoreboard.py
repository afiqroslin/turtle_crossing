from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-250, 250)
        self.update_score()

    def update_score(self):
        self.write(arg=f'Level:{self.level} ', align='center', font=("Courier", 10, "bold"))

    def level_clear(self):
        self.level += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)  # Display Game Over, whenever player lose the game
        self.write(arg='Game Over!', align='center', font=("Courier", 50, "bold"))
