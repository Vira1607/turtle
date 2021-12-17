import random
from turtle import *

shape("turtle")
speed(10)
# pencolor("white")
pensize(6)
Screen().bgcolor("turquoise")
colours = ["#ccff99", "#ccffcc", "#99ffcc", "#ffffcc", "#ffcccc", "#ccccff", "#cc99ff", "#ffccff"]


def vshape():
    right(25)
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)


def snowflakeArm():
    for x in range(0, 4):
        forward(30)
        vshape()
    backward(120)


def snowflake():
    for x in range(0, 6):
        color(random.choice(colours))
        snowflakeArm()
        right(60)


snowflake()


def snowflake():
    for x in range(0, 18):
        color(random.choice(colours))
        snowflakeArm()
        right(20)


snowflake()

# def snowflake():
# for x in range (0,10):
# color(random.choice(colours))
# snowflakeArm()
# right(36)
# snowflake()

import time

time.sleep(10)
