from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("C:/Users/me/PycharmProjects/Midterm_Project/Snakegame/highscore.txt") as data:
            high_score = data.read()
            self.high_score = int(high_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("C:/Users/me/PycharmProjects/Midterm_Project/Snakegame/highscore.txt", "w") as data:
            data.write(f"{self.high_score}")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
