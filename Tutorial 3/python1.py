
import turtle

def draw_circle(x, y):
    t.clear()
    t.penup()
    t.goto(x, y - 25)
    t.pendown()
    t.circle(25)

t = turtle.Turtle()
screen = turtle.Screen()
screen.onscreenclick(draw_circle)
screen.mainloop()
