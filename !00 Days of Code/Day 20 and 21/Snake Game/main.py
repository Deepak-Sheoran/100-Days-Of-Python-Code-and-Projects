# Steps to follow: -
# 1. Create a Snake Body
# 2. Move the snake, so it keeps moving in a particular direction
# 3. Control the snake using arrow keys
# 4. Put food on the screen and detect collision with food
# 5. Create a scoreboard
# 6. Detect collision with wall
# 7. Detect collision with the body.

from snake import Snake
from food import Food
from scoreboard import Score
from turtle import Screen
from random import choice
import time

colors = [
    ("#2E4053", "#D6EAF8"),
    ("#1C2833", "#D5DBDB"),
    ("#283747", "#D5F5E3"),
    ("#212F3D", "#D1F2EB"),
    ("#17202A", "#F2F3F4"),
    ("#4A235A", "#E8DAEF"),
    ("#4D5656", "#FADBD8"),
    ("#1B2631", "#F4ECF7"),
    ("#2C3E50", "#EBF5FB"),
    ("#4E4E50", "#F5EEF8"),
    ("#2C3E50", "#E6E6FA"),
    ("#3E4444", "#FFFACD"),
    ("#2F4F4F", "#E0FFFF"),
    ("#343A40", "#F0FFF0"),
    ("#4B0082", "#FAFAD2"),
    ("#556B2F", "#FFEFD5"),
    ("#483D8B", "#FFF5EE"),
    ("#2E8B57", "#F5F5DC"),
    ("#696969", "#F5DEB3"),
    ("#1C1C1C", "#F0E68C")
]

color = choice(colors)

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor(color[1])
screen.title("Snake Game ver 1.0")

screen.tracer(0)
snake = Snake(color=color[0])
screen.update()
screen.listen()

# 3. Control the snake using the arrow key
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")

color = choice(colors)
food = Food()
t = food.change(color=color[0], screen_color=color[1])

# 5. Create a Scoreboard
score = Score()

while True:
    time.sleep(0.1)
    snake.move()
    screen.update()

    # 4. Detect collision with the food
    if snake.head.data.distance(t) <= 15:
        color_choice = choice(colors)

        color = food.c
        screen_color = food.screen_color

        t = food.change(color_choice[0], screen_color=color_choice[1])

        snake.change_color(color)
        snake.add_node()
        screen.bgcolor(screen_color)

        # Scoreboard gets updates
        score.update()

    # 7. Detect collision with tail
    if snake.detect_collision():
        score.game_over()
        break

    # 6. Detect collision with wall
    if (snake.head.data.xcor() > 280 or snake.head.data.xcor() < -280 or
            snake.head.data.ycor() > 280 or snake.head.data.ycor() < -280):
        score.game_over()
        break

screen.exitonclick()
