from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5, stretch_wid=.5)
        self.color("red")
        self.new_food()
        # return (food.xcor, food.ycor)

    def new_food(self):
        x_index = random.randint(-235, 235)
        y_index = random.randint(-235, 235)
        self.goto(x=x_index, y=y_index)

    
