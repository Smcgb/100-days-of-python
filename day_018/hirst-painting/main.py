from turtle import Turtle, Screen
import random
import colorgram

timmy = Turtle()
timmy.speed("fastest")
screen = Screen()
screen.colormode(255)
startx = -600
starty = -500
colors = colorgram.extract('hirst.jpg', 10)

while starty <= 500:
    timmy.teleport(startx, starty)
    while timmy.xcor() < 600:
        iter_color = random.choice(colors)
        r, g, b = iter_color.rgb.r, iter_color.rgb.g, iter_color.rgb.b
        timmy.color(r,g,b)
        timmy.pd()
        timmy.begin_fill()
        timmy.circle(10)
        timmy.end_fill()
        timmy.pu()
        timmy.forward(30)
    starty += 30


print(screen.screensize())
screen.exitonclick()
