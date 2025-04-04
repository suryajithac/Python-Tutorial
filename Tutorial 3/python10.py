
import turtle

def draw_rectangle(x, y):
    t.clear()
    t.penup()
    t.goto(x, y)
    t.pendown()
    for _ in range(2):
        t.forward(100)
        t.right(90)
        t.forward(60)
        t.right(90)

t = turtle.Turtle()
screen = turtle.Screen()
screen.ondrag(draw_rectangle)
screen.mainloop()
