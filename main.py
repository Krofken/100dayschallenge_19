import turtle
from turtle import Turtle, Screen

rafi = Turtle()
screen = Screen()


def move_forward():
    rafi.forward(10)


def turn_rt():
    rafi.rt(10)


def turn_lt():
    rafi.lt(10)


def clear():
    rafi.home()
    rafi.clear()


def move_backwards():
    rafi.backward(10)


turtle.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="d", fun=turn_rt)
screen.onkeypress(key="a", fun=turn_lt)
screen.onkey(key="c", fun=clear)
screen.onkeypress(key="s", fun=move_backwards)

screen.exitonclick()
