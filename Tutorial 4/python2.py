class Rectangle:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        print(self.w * self.h)

r = Rectangle(4, 5)
r.area()