# Import necessary modules and classes.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # Turn off animation.

# Create snake, food, and scoreboard objects.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for key presses and bind them to snake movement functions.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Initialize game state variable.
game_is_on = True

# Main game loop.
while game_is_on:
    # Update screen.
    screen.update()
    # Pause briefly to control game speed.
    time.sleep(0.1)
    # Move the snake.
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False  # End the game.
        scoreboard.reset()  # Reset the scoreboard.
        scoreboard.game_over()  # Display game over message.

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment == snake.head:  # Skip the head segment.
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False  # End the game.
            scoreboard.reset()  # Reset the scoreboard.
            scoreboard.game_over()  # Display game over message.

# Keep the screen open until clicked.
screen.exitonclick()
