from turtle import Turtle, Screen
from random import randint, choice

timmy = Turtle()
screen = Screen()
screen.colormode(255)

def random_degrees():
    return randint(0,360)

def random_color():
    return ( randint(0, 255), randint(0, 255), randint(0, 255) )

def random_distance():
    return randint(10,50)

def random_turn(turtle):
    turn = [x * 90 for x in range(4)]
    turtle.setheading(choice(turn))


for i in range(randint(10, 50)):
    timmy.color(random_color())
    timmy.forward(random_distance())
    random_turn(timmy)

screen.exitonclick()