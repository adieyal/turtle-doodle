from random import random
import turtle

t = turtle.Pen()
t1.speed(200)

def draw_shape(t, instructions):
    t.setx(-500)
    t.sety(500)
    for length, angle in instructions:
        t.forward(length)
        t.right(angle)

def draw_square(t, length=10):
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)
    t.forward(length)
    t.right(90)


length = 20
for y in range(20):
    t.penup()
    t.setx(0)
    t.sety(y * length)
    t.pendown()
    for x in range(20):
        draw_square(t, 20)
        t.penup()
        t.setx(x * length)
        if (random() < 0.3):
            t1.pendown()

#border = 1000
#draw_shape([(border, 90), (border, 90), (border, 90), (border, 90)])
draw_square(20)
input("")
