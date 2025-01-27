# Turtle Challenge 2 - Draw a Dashed Line

import turtle as t

kaya = t.Turtle()

for _ in range(15):
    kaya.forward(10)
    kaya.penup()
    kaya.forward(10)
    kaya.pendown()