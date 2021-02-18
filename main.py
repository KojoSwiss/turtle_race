from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win? Enter a color: ")
colors = ["red", "grey", "orange", "green", "blue", "purple"]
y_position = [-80, -50, -20, 10, 40, 70]

all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-235, y=y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You have win, {winner} turtle has won the race")
            else:
                print(f"You have lost!, The {winner} turtle won ")

        rand_dist = random.randint(0, 10)
        turtle.forward(rand_dist)



screen.exitonclick()
