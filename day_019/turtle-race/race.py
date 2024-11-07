from turtle import Turtle, Screen
import random

# drives main logic of code
is_race_on = False

# expand this to create more turtles
colors = ["red", "orange", 'yellow', 'green', 'blue', 'purple']

# starting positions to place turtles
startx = -225
starty = -175

screen = Screen()
screen.colormode(255)
screen.setup(500, 400)
screen.title("Welcome to the turtle race!")
bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
while bet.lower() not in colors:
    bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtles = []

for c in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(c)
    turtles.append(turtle)
    turtle.pu()
    turtle.goto(startx, starty)
    starty += 30

if bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        turtle.forward(random.randint(0,10))
        if turtle.xcor() >= 210:
            if bet == turtle.pencolor():
                print(f"You've won! The {turtle.pencolor()} turtle completed the race first!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle completed the race first!")
            is_race_on = False


screen.exitonclick()