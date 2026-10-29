class emp():
    def calsal(self):
        print("Emp Calsal")

class Hr():
    def calsal(self):
        print("Hr calsal")

class Admin(emp , Hr):
    def calsal(self):
        print("Admin calsal")

h = Hr()
a = Admin()
h.calsal()
a.calsal()