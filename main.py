from turtle import Turtle as t, Screen

my_screen = Screen()
my_screen.setup(width=500, height=400)
user_bet = my_screen.textinput(title="Make your bet.", prompt="Which turtle will win?")
print(user_bet)








my_screen.exitonclick()