from turtle import Turtle as t, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet.", prompt="Which turtle will win?")
print(user_bet)

colours = ["blue", "red", "green", "yellow", "orange", "purple"]


i=0
x = -230
y = -100
for new_turtle in colours:
    colours[i] = t(shape="turtle")
    colours[i].color(new_turtle)
    colours[i].penup()
    colours[i].goto(x=x, y=y)
    i += 1
    y += 30



my_screen.exitonclick()