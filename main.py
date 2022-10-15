import colorgram
from turtle import Turtle, Screen, colormode
import random

colormode(255)
stylus = Turtle()

# Extract 6 colors from an image.
colors = colorgram.extract('can.png', 100)
rgb = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)

    rgb.append(new_color)
print(rgb)

stylus.setheading(225)
stylus.penup()
stylus.forward(250)
stylus.setheading(0)


def dot_string():
    for _ in range(10):
        stylus.dot(20, random.choice(rgb))
        stylus.penup()
        stylus.forward(50)
        stylus.pendown()
    stylus.penup()
    stylus.backward(50)


dot_string()


for _ in range(9):
    stylus.seth(90)
    stylus.forward(50)
    if _ % 2 == 0:
            stylus.seth(180)
    else:
        stylus.seth(0)
    stylus.pendown()
    dot_string()
    stylus.penup()


screen = Screen()
screen.exitonclick()
