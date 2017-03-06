# Sarah Barden
# functions for day 5 reading journal

import turtle
import math
bob = turtle.Turtle()


def square(t, length):
    for i in range(4):
        bob.fd(length)
        bob.lt(90)


def polygon(t, length, n):
    for i in range(n):
        bob.fd(length)
        bob.lt(360/n)


def circle(t, r):
    circumf = 2*3.14*r
    n = 100
    length = circumf/n
    polygon(t, length, n)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    for i in range(n):
        bob.fd(step_length)
        bob.lt(step_angle)

arc(bob, 50, 180)

turtle.mainloop()
