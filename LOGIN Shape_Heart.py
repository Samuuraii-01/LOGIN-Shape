import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.color("red")
turtle.bgcolor("black")

def samuuraii_01(n):
    x = 16 * math.sin(n) ** 3
    y = 13 * math.cos(n) - 5 * math.cos(2 * n) - 2 * math.cos(3 * n) - math.cos(4 * n)
    return x, y

t.penup()
for j in range(15):
    t.goto(0, 0)
    t.pendown()
    for i in range(0, 100):
        n = i / 10
        x, y = samuuraii_01(n)
        t.goto(x * (j+1), y * (j+1))
    t.penup()

t.hideturtle()
turtle.done()
