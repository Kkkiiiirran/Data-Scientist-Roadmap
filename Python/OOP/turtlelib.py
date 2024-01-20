from turtle import Turtle, Screen

timmy = Turtle()
shimmy= Turtle()

screen = Screen()
# for i in range(4):
#     timmy.right(90)
#     timmy.forward(100)

# for i in range(4):
#     shimmy.left(90)
#     shimmy.forward(100)
# screen.exitonclick
# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
from random import randint

def colorchange():
    r = randint(0,255)
    g= randint(0,255)
    b = randint(0,255)
    return (r, g, b)
# print(r)
# timmy.right(90)
# print(timmy.pos())
# timmy.penup()
# timmy.hideturtle()
# timmy.setpos(x=0.00, y=100.100)
# timmy.showturtle()
# # timmy.penup()
# # timmy.setpos()
# timmy.pendown()
screen.colormode(255)
# timmy.forward(50)
# for i in range(3, 50, +1):
#     colors = colorchange()
#     timmy.pencolor(colors)
#     for j in range(i):

#         timmy.right(360/i)
#         timmy.forward(25)


    # for i in range(4):
    #     timmy.right(90)
    #     timmy.forward(100)

    # for i in range(5):
    #     timmy.right(72)
    #     timmy.forward(100)

# timmy.right(90)
# timmy.forward(100)
# timmy.


# direction = [0, 1, 2, 3, 4,]
# timmy.pensize(20)

screen.screensize(500, 500)
# print(timmy.pos())
# if timmy.pos() < (500, 500):
    
#     temp, temp1 = timmy.pos()
#     print(temp)
#     # timmy.pos()
#     timmy.position(temp-500, temp1-500)
#     print(timmy.pos())
# timmy.penup()
# timmy.setpos(x=0.500, y=250.100)
# timmy.pendown()
# for i in range(500): 
#     colors = colorchange()
#     timmy.pencolor(colors)
#     timmy.forward(30)
#     dir = randint(0, 10)
#     if dir %2 ==0:
#         timmy.left(90)
#     else: timmy.right(90)
# timmy.hideturtle()
# timmy.penup()
# timmy.right(90)
# timmy.forward(50)
timmy.pendown()

# timmy.tilt(30)
# timmy.forward(5)
# timmy.circle(100)
timmy.speed("fastest")
def sp(gap):
    for i in range(int(360/gap)):
        timmy.color(colorchange())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap)

sp(4)
screen.mainloop()