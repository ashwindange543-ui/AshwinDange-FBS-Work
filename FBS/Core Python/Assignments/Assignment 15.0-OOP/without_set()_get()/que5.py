class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def display(self):
        print(f"ID={self.pid}, Name={self.name}, Price={self.price}")

p1 = Product(101, "Laptop", 55000)
p2 = Product(102, "Mouse", 800)

p1.display()
p2.display()