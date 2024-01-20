from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    
    def create_snake(self):
        for i in range(3):
            x_index=(i) * -20
            posi = (x_index, 0)
            self.appendBody(posi)
    
    def appendBody(self, cords):
        snake_head = Turtle("square")
        snake_head.color("white")
        snake_head.penup()
        snake_head.goto(cords)
        self.snake_body.append(snake_head)
    
    def extend_snake(self):
        self.appendBody(self.snake_body[-1].position())


    def move(self):
        for seg_num in range(len(self.snake_body)-1, 0,-1):
            new_x = self.snake_body[seg_num-1].xcor()
            new_y = self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x,new_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
