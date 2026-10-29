class Emp:
    def __init__(self,nm):
        self.name=nm
    def display(self):
        print("Display ")
class HR(Emp):
    def display(self):
        print("disply of Hr")
class JrHR(HR):
    def display(self):
        print("I am from disply of Jr Hr")
h1=HR("sACHIN")
h1.display()
s1=Emp("jdja")
s1.display()
jhr=JrHR("Smriti")
jhr.display()

