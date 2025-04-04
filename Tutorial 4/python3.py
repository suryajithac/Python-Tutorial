class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    def cost(self):
        print(self.price)

c1 = Car("abc", 2020, 20000)
c2 = Car("xyz", 2022, 30000)
c1.cost()
c2.cost()