class Emp:
    def __init__(self, nm, sal):
        self.name = nm
        self.sal = sal

    def getName(self):
        return self.name

    def setName(self, nm):
        self.name = nm

    def display(self):
        print("Name:", self.name)
        print("Salary:", self.sal)


class HR(Emp):
    def __init__(self, nm, sal, commission):
        super().__init__(nm, sal)
        self.commission = commission

    def getCommission(self):
        return self.commission

    def setCommission(self, commission):
        self.commission = commission

    def display(self):
        print("HR Name:", self.name)
        print("Commission:", self.commission)


class Developer(Emp):
    def __init__(self, nm, sal, bonus):
        super().__init__(nm, sal)
        self.bonus = bonus

    def getBonus(self):
        return self.bonus

    def setBonus(self, bonus):
        self.bonus = bonus

    def display(self):
        print("Developer Name:", self.name)
        print("Bonus:", self.bonus)


h1 = HR("Sachin", 50000, 5000)
d1 = Developer("Ashwin", 60000, 10000)

print(h1.getCommission())
h1.setCommission(7000)
h1.display()

print(d1.getBonus())
d1.setBonus(12000)
d1.display()