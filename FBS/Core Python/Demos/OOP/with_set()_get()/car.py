class Car:
    def __init__(self, no, name, price):
        self.no = no
        self.name = name
        self.price = price

    def getName(self):
        return self.name
    def setName(self , newName):
        self.name=newName

    def getNo(self):
            return self.no
    def setNo(self , newNo):
            self.no=newNo

    def getPrice(self):
        return self.price
    def setPrice(self , newPrice):
        self.price=newPrice

    def display(self):
        print(f"No={self.no}, Name={self.name}, Price={self.price}")

c1 = Car(1, "BMW", 5000000)
c2 = Car(2, "Audi", 4500000)

c1.display()
c2.display()