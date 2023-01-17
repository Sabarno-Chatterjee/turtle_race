from turtle import Turtle as t, Screen
import random

is_race_on = False
my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet.", prompt="Which turtle will win?")


def finish_line():
    finish = t()
    finish.hideturtle()
    finish.pencolor("black")
    finish.setheading(90)
    finish.penup()
    finish.goto(x=210, y=-150)
    finish.pendown()
    finish.pensize(10)
    finish.forward(300)
    finish.speed(0)


def spectators(x_position, y_position, direction):
    for spectator in range(4):
        tim = t(shape="turtle")
        tim.speed(0)
        tim.hideturtle()
        tim.penup()
        tim.goto(x=x_position, y=y_position)
        tim.setheading(direction)
        tim.showturtle()
        x_position += 35


spectators(x_position=20, y_position=-170, direction=90)
spectators(x_position=20, y_position=170, direction=270)
finish_line()
colours = ["blue", "red", "green", "yellow", "orange", "purple"]
all_turtles = []


def generate_turtles(turtle_count, starting_position):
    for new_turtle in colours:
        colours[turtle_count] = t(shape="turtle")
        colours[turtle_count].speed("fastest")
        colours[turtle_count].color(new_turtle)
        colours[turtle_count].penup()
        colours[turtle_count].goto(x=-230, y=starting_position)
        all_turtles.append(colours[turtle_count])
        turtle_count += 1
        starting_position += 50


generate_turtles(turtle_count=0, starting_position=-125)
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
