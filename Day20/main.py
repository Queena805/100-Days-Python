import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from superfood import Super


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
super_food = Super()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")






lives = 3
while lives > 0:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.distance(super_food) < 15:
        super_food.refresh()
        for _ in range(2):
            snake.extend()
            scoreboard.increase_score()

    #detect collision with wall.
    if snake.head.xcor() > 290 or snake.head.ycor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290:
        lives -= 1
        snake = Snake()
        screen.listen()
        screen.onkey(snake.up, "Up")
        screen.onkey(snake.down, "Down")
        screen.onkey(snake.left, "Left")
        screen.onkey(snake.right, "Right")


    #detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            lives -= 1
            snake = Snake()
            screen.listen()
            screen.onkey(snake.up, "Up")
            screen.onkey(snake.down, "Down")
            screen.onkey(snake.left, "Left")
            screen.onkey(snake.right, "Right")

scoreboard.game_over()











screen.exitonclick()