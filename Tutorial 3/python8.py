
import turtle

def draw_triangle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(3):
        t.forward(60)
        t.left(120)

t = turtle.Turtle()
screen = turtle.Screen()
screen.onscreenclick(draw_triangle)
screen.mainloop()
