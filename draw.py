import turtle
import sys
import random

t = turtle.Pen()
t.speed(100)

def draw(sides, length):
    xyz = (sides - 2) * 180 / sides
    turn_amount = 180 - xyz

    for i in range(0, sides):
        t.forward(length)
        t.left(turn_amount)


for i in range(2, 20):
    sides = random.choice(range(2, 10))
    length = random.choice(range(10, 200))

    draw(sides, length)
input("")


