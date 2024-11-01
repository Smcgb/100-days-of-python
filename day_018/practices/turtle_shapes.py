from turtle import Turtle, Screen
from random import randint

timmy = Turtle()
screen = Screen()
screen.colormode(255)

sides = 3

def draw_shape(num_sides):
    degrees = 360 / num_sides
    for i in range(num_sides):
        timmy.pd()
        timmy.forward(100)
        timmy.right(degrees)


while sides < 11:
    rgb = ( randint(0, 255), randint(0, 255), randint(0, 255) )
    timmy.color(rgb)
    draw_shape(sides)
    sides += 1

screen.exitonclick()


