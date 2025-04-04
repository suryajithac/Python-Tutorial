class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display(self):
        print(self.name, self.age, self.salary)

p1 = Person("maya", 30, 50000)
p2 = Person("raju", 35, 60000)
p1.display()
p2.display()