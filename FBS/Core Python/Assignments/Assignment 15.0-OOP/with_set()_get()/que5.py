class Book:
    def __init__(self, bid, name, price):
        self.bid = bid
        self.name = name
        self.price = price

    def getName(self):
        return self.name
    def setName(self , newName):
        self.name=newName  

    def getPID(self):
        return self.pid
    def setPID(self , newPID):
        self.pid=newPID 
    
    def getPrice(self):
        return self.price
    def setPrice(self , newPrice):
        self.price=newPrice

    def display(self):
        print(f"ID={self.bid}, Name={self.name}, Price={self.price}")

b1 = Book(1, "Python", 500)
b2 = Book(2, "Java", 600)

b1.display()
b2.display()