import turtle
import numpy as np

turtle.speed(1000000)
turtle.colormode(255)
turtle.fillcolor((69, 69, 69))


def go(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def circled(s, times):
    for _ in range(times):
        turtle.circle(s)
        turtle.right(360//times)


go(0, 0)
turtle.begin_fill()
circled(100, 69)
turtle.end_fill()
delay = input()