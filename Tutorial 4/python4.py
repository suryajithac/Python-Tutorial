class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def dataprint(self):
        print(self.name, self.roll)

s1 = Student("hari", 1)
s2 = Student("ravi", 2)
s1.dataprint()
s2.dataprint()