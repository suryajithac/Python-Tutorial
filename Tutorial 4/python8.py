class Book:
    def get_details(self, title, author, cost):
        self.title = title
        self.author = author
        self.cost = cost

    def print_details(self):
        print(self.title, self.author, self.cost)

b = Book()
b.get_details("abc", "tom", 300)
b.print_details()