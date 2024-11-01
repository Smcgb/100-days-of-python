from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")
screen = Screen()
timmy.pu()

timmy.forward(200)
timmy.pendown()
for i in range(4):
    timmy.left(90)
    timmy.forward(200)

turtle.teleport(0,0)

screen.exitonclick()