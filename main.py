from turtle import Turtle as t, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet.", prompt="Which turtle will win?")
# print(user_bet)

finish = t()
finish.hideturtle()
finish.pencolor("black")
finish.setheading(90)
finish.penup()
finish.goto(x=210, y=-170)
finish.pendown()
finish.pensize(10)
finish.forward(340)

colours = ["blue", "red", "green", "yellow", "orange", "purple"]
all_turtles = []
i = 0
x = -230
y = -125
for new_turtle in colours:
    colours[i] = t(shape="turtle")
    colours[i].color(new_turtle)
    colours[i].penup()
    colours[i].goto(x=x, y=y)
    all_turtles.append(colours[i])
    i += 1
    y += 50

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:

        if turtle.xcor() > 200:
            print("Race finished!")
            winning_colour = turtle.pencolor()
            is_race_on = False
            if user_bet == winning_colour:
                print("You won!")
            else:
                print(f"You lost, {winning_colour} turtle won the race.")
        turtle.forward(random.randint(0, 10))

my_screen.exitonclick()
