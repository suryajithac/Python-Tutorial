class RECTANGLE:
    def __init__(self, height, width, x, y):
        self.height = height
        self.width = width
        self.x = x
        self.y = y

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)

    def center(self):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        return cx, cy

r = RECTANGLE(4, 8, 1, 1)
print(r.area())
print(r.perimeter())
print(r.center())