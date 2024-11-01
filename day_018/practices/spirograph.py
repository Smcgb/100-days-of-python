from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)


def random_color():
    return ( randint(0, 255), randint(0, 255), randint(0, 255) )


for i in range(100):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.right(3.6)

screen.exitonclick()