from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level_speed = 0.1
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-225, 260)
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.level_speed *= 0.8
        self.clear()
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f'GAME OVER', align='center', font=FONT)