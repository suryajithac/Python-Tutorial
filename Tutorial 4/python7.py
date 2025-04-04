class Student:
    def readData(self, r, m1, m2):
        self.r = r
        self.m1 = m1
        self.m2 = m2

    def computeTotal(self):
        self.total = self.m1 + self.m2

    def printDetails(self):
        print(self.r, self.m1, self.m2, self.total)

s = Student()
s.readData(5, 40, 50)
s.computeTotal()
s.printDetails()