class Mec:
    def display(self):
        print("MEc")
class Electric:
    def display(self):
        print("I am Electrical")       
class Mecatronix(Electric,Mec):
    def abc():
        print("I am in mectronix")
m=Mecatronix()
m.display()