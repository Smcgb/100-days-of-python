import turtle
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)
screen.listen()

def move_forward():
    t.forward(10)

def move_backwards():
    t.backward(10)

def rotate_left():
    t.left(15)

def rotate_right():
    t.right(15)

def clear_drawing():
    screen.reset()

turtle.onkey(key="w", fun=move_forward)
turtle.onkey(key="s", fun=move_backwards)
turtle.onkey(key="a", fun=rotate_left)
turtle.onkey(key="d", fun=rotate_right)
turtle.onkey(key="c", fun=clear_drawing)

screen.exitonclick()