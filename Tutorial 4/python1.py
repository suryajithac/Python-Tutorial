class Arith:
    def read(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        print(self.a + self.b)

obj = Arith()
obj.read(3, 7)
obj.add()