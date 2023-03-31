from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time
# Controls how fast the game updates
FPS = 10

screen = Screen()
screen.setup(width=660, height=680)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

border = Border()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(snake.extend, "n")

game_on = True
while game_on:
    screen.update()
    time.sleep(1 / FPS)
    # This ensures the snake's head only turns once per cycle
    # TODO add a buffer or queue for which direction to turn the head
    snake.has_turned = False
    # Main move method that moves the snake forward 20 units
    snake.move()

    # Detects if the snake head is within 15 units of the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    # Detects if snake head goes outside the border
    if snake.head.xcor() > 290 or snake.head.xcor() < -290:
        screen.update()
        scoreboard.print_over()
        game_on = False
        break
    elif snake.head.ycor() > 270 or snake.head.ycor() < -310:
        screen.update()
        scoreboard.print_over()
        game_on = False
        break

    # Checks if the snake had comes within 10 units of one of it's segments
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            screen.update()
            scoreboard.print_over()
            game_on = False
            break































screen.exitonclick()