import colorgram
import turtle
import random

colors = colorgram.extract('Python/OOP/dot.jpg', 40)
rgb_colors=[]
for color in colors:
    rgb = color.rgb
    r = rgb.r
    g = rgb.g
    b = rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

rgb_colors.reverse()
rgb_colors.pop()
rgb_colors.pop()
rgb_colors.pop()


timmy = turtle.Turtle()
screen = turtle.Screen()

timmy.speed("fastest") # screen.screensize(100,100)
turtle.colormode(255)
# timmy.forward(100)
timmy.hideturtle()
timmy.penup()
timmy.setheading(180)
timmy.forward(600)
timmy.setheading(270)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()

dots = 100
for dot in range(1, 625,+1):
    timmy.dot(18, random.choice(rgb_colors))
    timmy.penup()
    timmy.forward(25)

    if dot % 25 == 0:
        timmy.setheading(90)
        timmy.forward(25)
        timmy.setheading(180)
        timmy.forward(625)
        timmy.setheading(0)
    timmy.pendown()



screen.mainloop()