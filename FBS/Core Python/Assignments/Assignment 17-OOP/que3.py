
class Student:
    def __init__(self, StudentId, Name, Age, Percentage):
        self.StudentId = StudentId
        self.Name = Name
        self.Age = Age
        self.Percentage = Percentage

    def Accept(self):
        self.StudentId = int(input("Enter Student ID: "))
        self.Name = input("Enter Name: ")
        self.Age = int(input("Enter Age: "))
        self.Percentage = float(input("Enter Percentage: "))

    def Display(self):
        print("Student ID:", self.StudentId)
        print("Name:", self.Name)
        print("Age:", self.Age)
        print("Percentage:", self.Percentage)

    def CalculateRank(self):
        if self.Percentage >= 75:
            return "Distinction"
        elif self.Percentage >= 60:
            return "First Class"
        elif self.Percentage >= 50:
            return "Second Class"
        elif self.Percentage >= 35:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return f"{self.StudentId}, {self.Name}, {self.Age}, {self.Percentage}"


class MedicalStudent(Student):
    def __init__(self, StudentId, Name, Age, Percentage, Specialization, MarksOfInternship):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Specialization = Specialization
        self.MarksOfInternship = MarksOfInternship

    def Accept(self):
        super().Accept()
        self.Specialization = input("Enter Specialization: ")
        self.MarksOfInternship = float(input("Enter Internship Marks: "))

    def Display(self):
        super().Display()
        print("Specialization:", self.Specialization)
        print("Internship Marks:", self.MarksOfInternship)

    def CalculateRank(self):
        total = self.Percentage + self.MarksOfInternship

        if total >= 150:
            return "Distinction"
        elif total >= 120:
            return "First Class"
        elif total >= 100:
            return "Second Class"
        elif total >= 70:
            return "Pass"
        else:
            return "Fail"

    def __str__(self):
        return super().__str__() + f", {self.Specialization}, {self.MarksOfInternship}"


m1 = MedicalStudent(103, "Priya", 22, 80, "Cardiology", 85)

m1.Display()
print("Rank:", m1.CalculateRank())
print("Student Details:", m1)
