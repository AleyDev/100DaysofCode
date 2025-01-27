# Turtle Challenge 3 - Drawing Different Shapes

import turtle as t
import random

kaya = t.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        kaya.forward(100)
        kaya.right(angle)
        
for shape_side_n in range(3, 11):
    kaya.color(random.choice(colors))
    draw_shape(shape_side_n)