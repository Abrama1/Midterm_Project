# Import the Turtle module.
from turtle import Turtle

# Define constants for alignment and font.
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


# Define the Scoreboard class, which is a subclass of the Turtle class.
class Scoreboard(Turtle):

    # Constructor method to initialize the Scoreboard object.
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass (Turtle).

        # Initialize attributes to keep track of the current score and high score.
        self.score = 0
        # Open the high score file and read the high score from it.
        with open("Snakegame/highscore.txt") as data:
            high_score = data.read()
            self.high_score = int(high_score)  # Convert the read high score to an integer.

        # Set up the appearance of the scoreboard.
        self.color("white")  # Set the color of the text to white.
        self.penup()  # Lift the pen to prevent drawing lines.
        self.goto(0, 270)  # Move the turtle to the specified position.
        # Write the initial score and high score on the screen.
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()  # Hide the turtle cursor.

    # Method to reset the scoreboard.
    def reset(self):
        # Update the high score if the current score exceeds it.
        if self.score > self.high_score:
            self.high_score = self.score
        # Write the new high score to the high score file.
        with open("Snakegame/highscore.txt", "w") as data:
            data.write(f"{self.high_score}")
        self.update_scoreboard()  # Update the scoreboard appearance.

    # Method to update the scoreboard appearance with the current score and high score.
    def update_scoreboard(self):
        self.clear()  # Clear the previous score display.
        # Write the updated score and high score on the screen.
        self.write(f"Score = {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # Method to display "GAME OVER" on the screen.
    def game_over(self):
        self.goto(0, 0)  # Move the turtle to the center of the screen.
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)  # Write "GAME OVER" on the screen.

    # Method to increase the score by 1 and update the scoreboard.
    def increase_score(self):
        self.score += 1  # Increment the score by 1.
        self.update_scoreboard()  # Update the scoreboard appearance with the new score.
