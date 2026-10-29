class Student:
    inName = "FBS"
    stdCount = 0

    @staticmethod
    def getInName():
        return Student.inName

    @staticmethod
    def setInName(nm):
        Student.inName = nm

    def __init__(self, rollno, name, batch):
        self.rollNo = rollno
        self.name = name
        self.batch = batch
        Student.stdCount += 1

    def display(self):
        print(f"Rollno = {self.rollNo}, Name = {self.name}, batch = {self.batch}")


s1 = Student(12, "Suraj", "July Python")
s2 = Student(13, "Sauraj", "July Python")
s3 = Student(1, "Ritik", "June Python")
s4 = Student(1, "Roshan", "May Python")

s1.display()
s2.display()
s3.display()
s4.display()

print(Student.stdCount)