
import turtle

def draw_circle(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(30)

t = turtle.Turtle()
screen = turtle.Screen()
screen.onscreenclick(draw_circle)
screen.mainloop()
