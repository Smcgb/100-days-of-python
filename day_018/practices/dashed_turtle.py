from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
screen = Screen()

for i in range(15):
    timmy.pd()
    timmy.forward(15)
    timmy.pu()
    timmy.forward(15)

screen.exitonclick()