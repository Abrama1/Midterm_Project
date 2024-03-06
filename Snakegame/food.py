# Import the Turtle module and the random module.
from turtle import Turtle
import random


# Define the Food class, which is a subclass of the Turtle class.
class Food(Turtle):

    # Constructor method to initialize the Food object.
    def __init__(self):
        super().__init__()  # Call the constructor of the superclass (Turtle).

        # Set the attributes and properties of the food.
        self.shape("circle")  # Set the shape of the food to a circle.
        self.penup()  # Lift the pen to prevent drawing lines.
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Stretch the circle to make it look like food.
        self.color("yellow")  # Set the color of the food to yellow.
        self.speed("fastest")  # Set the animation speed of the food to the fastest.

        # Call the refresh method to move the food to a random position.
        self.refresh()

    # Method to move the food to a random position.
    def refresh(self):
        # Generate random coordinates within the range of the screen.
        random_x = random.randint(-270, 270)
        random_y = random.randint(-270, 270)

        # Move the food to the random coordinates.
        self.goto(random_x, random_y)
