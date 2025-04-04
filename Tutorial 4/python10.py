class Complex:
    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __add__(self, o):
        return Complex(self.r + o.r, self.i + o.i)

    def show(self):
        print(self.r, "+", self.i, "i")

c1 = Complex(2, 3)
c2 = Complex(4, 5)
c3 = c1 + c2
c3.show()