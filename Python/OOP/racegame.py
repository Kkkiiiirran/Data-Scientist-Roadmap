from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)

race_on = False
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?")
colors = ["red", "orange", "yellow", "green","blue", "purple"]

turtles = []
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    y_index = -120 + (i*50)
    new_turtle.goto(x=-220, y=y_index)
    turtles.append(new_turtle)

if bet: 
    race_on= True

while race_on:

    for turtle in turtles:
        if turtle.xcor() > 200:
            race_on=False
            winner = turtle.pencolor()
            if winner == bet:
                print(f"You won! The {winner} turtle is the winner")
            else:
                print(f"You lose! The {winner} turtle is the winner")

        r_dis = random.randint(0,10)
        turtle.forward(r_dis)

    

screen.mainloop()