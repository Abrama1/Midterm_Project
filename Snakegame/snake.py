# Import the Turtle module.
from turtle import Turtle

# Define constants for the starting position, movement distance, and directions.
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


# Define the Snake class.
class Snake:

    # Constructor method to initialize the Snake object.
    def __init__(self):
        self.segments = []  # List to store the segments of the snake.
        self.create_snake()  # Method to create the initial snake.
        self.head = self.segments[0]  # Reference to the head segment of the snake.

    # Method to create the initial segments of the snake.
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # Method to add a new segment to the snake.
    def add_segment(self, position):
        new_segment = Turtle("square")  # Create a new Turtle object for the segment.
        new_segment.shapesize(0.9)  # Set the size of the segment.
        new_segment.color("dark green")  # Set the color of the segment.
        new_segment.penup()  # Lift the pen to prevent drawing lines between segments.
        new_segment.goto(position)  # Move the segment to the specified position.
        self.segments.append(new_segment)  # Add the segment to the list of segments.
        self.segments[0].color("green")  # Set the color of the head segment.

    # Method to reset the snake to its initial state.
    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move segments off-screen to hide them.
        self.segments.clear()  # Clear the list of segments.
        self.create_snake()  # Recreate the snake.
        self.head = self.segments[0]  # Update the reference to the head segment.

    # Method to extend the snake by adding a new segment.
    def extend(self):
        self.add_segment(self.segments[-1].position())  # Add a segment at the last position of the snake.

    # Method to move the snake forward.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()  # Get the x-coordinate of the previous segment.
            new_y = self.segments[seg_num - 1].ycor()  # Get the y-coordinate of the previous segment.
            self.segments[seg_num].goto(new_x, new_y)  # Move the segment to the new position.
        self.head.forward(MOVE_DISTANCE)  # Move the head segment forward.

    # Method to set the snake's direction to right.
    def right(self):
        if self.head.heading() != LEFT:  # Prevent the snake from reversing its direction.
            self.head.setheading(RIGHT)

    # Method to set the snake's direction to left.
    def left(self):
        if self.head.heading() != RIGHT:  # Prevent the snake from reversing its direction.
            self.head.setheading(LEFT)

    # Method to set the snake's direction to up.
    def up(self):
        if self.head.heading() != DOWN:  # Prevent the snake from reversing its direction.
            self.head.setheading(UP)

    # Method to set the snake's direction to down.
    def down(self):
        if self.head.heading() != UP:  # Prevent the snake from reversing its direction.
            self.head.setheading(DOWN)
