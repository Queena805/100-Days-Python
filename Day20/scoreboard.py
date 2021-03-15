

from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.lives = 3
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        self.update_lives


    def update_scoreboard(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_lives(self):
        self.write(f"lives: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(200,0)



    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):

        self.score += 1
        self.clear()
        self.update_scoreboard()

    def decrease_lives(self):
        self.lives -= 1
        self.update_lives()










