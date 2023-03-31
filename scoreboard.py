from turtle import Turtle
ALIGNMENT = "center"
SCORE_FONT = ("Arial", 18, "bold")
OVER_FONT = ("Arial", 32, "bold")

with open("data.txt", mode='r') as file:
    HIGHSCORE = int(file.read())

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = HIGHSCORE
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(0, 300)
        self.color("white")
        self.print_score()

    # Clears the current text object then writes the current score to the screen again
    def print_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=SCORE_FONT)

    # Moves the text object to the center of the screen (does not clear previous text) and writes game over
    def print_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=OVER_FONT)
        self.goto(0, -100)
        self.write(arg=f"High Score: {self.highscore}", align=ALIGNMENT, font=SCORE_FONT)
        with open("data.txt", mode='w') as file:
            file.write(str(self.highscore))

    def update_score(self):
        self.score += 1
        if self.score > self.highscore:
            self.highscore = self.score
        self.print_score()


