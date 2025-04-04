class Mobile:
    def set_details(self, company, model, price):
        self.company = company
        self.model = model
        self.price = price

    def display_details(self):
        print(self.company, self.model, self.price)

m = Mobile()
m.set_details("nokia", "1100", 1500)
m.display_details()