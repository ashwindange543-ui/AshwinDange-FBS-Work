class Mobile:
    def __init__(self, model, brand, price):
        self.model = model
        self.brand = brand
        self.price = price

    def display(self):
        print(f"Model={self.model}, Brand={self.brand}, Price={self.price}")

m1 = Mobile("S24", "Samsung", 80000)
m2 = Mobile("15", "iPhone", 90000)

m1.display()
m2.display()
