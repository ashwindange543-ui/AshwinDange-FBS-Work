class Bank:
    def __init__(self, accno, name, balance):
        self.accno = accno
        self.name = name
        self.balance = balance

    def getName(self):
        return self.name
    def setName(self , newName):
        self.name=newName 

    def getAccNo(self):
        return self.accno
    def setAccNo(self , newAccNo):
        self.accno=newAccNo 

    def getBalance(self):
        return self.balance
    def setBalance(self , newBalance):
        self.balance=newBalance
    
    def display(self):
        print(f"Account={self.accno}, Name={self.name}, Balance={self.balance}")

b1 = Bank(101, "Ritesh", 50000)
b2 = Bank(102, "Pramod", 70000)

b1.display()
b2.display()