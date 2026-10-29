
class EnggStudent(Student):
    def __init__(self, StudentId, Name, Age, Percentage, Branch, InternalMarks):
        super().__init__(StudentId, Name, Age, Percentage)
        self.Branch = Branch
        self.InternalMarks = InternalMarks

    def Accept(self):
        super().Accept()
        self.Branch = input("Enter Branch: ")
        self.InternalMarks = float(input("Enter Internal Marks: "))

    def Display(self):
        super().Display()
        print("Branch:", self.Branch)
        print("Internal Marks:", self.InternalMarks)

    def CalculateRank(self):
        total = self.Percentage + self.InternalMarks

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
        return super().__str__() + f", {self.Branch}, {self.InternalMarks}"


e1 = EnggStudent(102, "Amit", 21, 80, "Computer", 85)
e1.Display()
print("Rank:", e1.CalculateRank())
print(e1)
