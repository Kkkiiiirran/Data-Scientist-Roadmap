from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard
import random
import time
#Setting up the screen
screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.update()

game_on = True

while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.new_food()
        snake.extend_snake()
        scoreboard.increase_score()

    if snake.head.xcor() > 250 or snake.head.xcor() < -250 or snake.head.ycor() > 250 or snake.head.ycor() < -250:
        game_on = False
        scoreboard.gameover()
    
    for segment in snake.snake_body[1:]:
        if  snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.gameover()


screen.mainloop()