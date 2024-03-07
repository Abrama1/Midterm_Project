from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def after_collision(snake, scoreboard, food, screen):
    answer = screen.textinput(title="GAME OVER", prompt="Do you want to play again? \n'y' or 'yes' to continue"
                                                        "\nanything else for exit")
    if answer and answer.lower() in ["yes", "y"]:  # If user wants to play again
        snake.reset()
        scoreboard.reset()
        food.refresh()  # Moves food to a new place
        return True  # Continue the game
    else:
        scoreboard.reset()
        screen.bye()
        return False  # End the game


def detect_collision(snake, food, scoreboard):
    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()  # Moves food to a new place
        snake.extend()
        scoreboard.increase_score()
    # Detect collision with wall.
    if abs(snake.head.xcor()) > 280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        return True
    # Detect collision with tail.
    for segment in snake.segments[1:]:  # Iterate over the snake's body segments, excluding the head.
        if snake.head.distance(segment) < 10:
            return True
    return False  # No collision detected


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)  # Turn off animation.

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    game_is_on = True

    while game_is_on:
        screen.listen()  # Start listening to keyboard events.
        screen.onkey(snake.up, "Up")  # Bind the up arrow key to move the snake up.
        screen.onkey(snake.down, "Down")  # Bind the down arrow key to move the snake down.
        screen.onkey(snake.left, "Left")  # Bind the left arrow key to move the snake left.
        screen.onkey(snake.right, "Right")  # Bind the right arrow key to move the snake right.

        screen.update()  # Update the screen to show the changes.
        time.sleep(0.1)  # Controls speed of the game
        snake.move()

        if detect_collision(snake, food, scoreboard):
            game_is_on = after_collision(snake, scoreboard, food, screen)

    screen.mainloop()  # Start the main event loop to keep the screen open.


if __name__ == "__main__":
    main()
