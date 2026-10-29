class PlaceStd:
    placeName = "FBS"
    placeCount = 0

    @staticmethod
    def getPlaceName():
        return PlaceStd.placeName

    @staticmethod
    def setPlaceName(nm):
        PlaceStd.placeName = nm

    def __init__(self, name, rollno, city, companyname):
        self.name = name
        self.rollNo = rollno
        self.city = city
        self.companyName = companyname
        PlaceStd.placeCount += 1

    def display(self):
        print(f"Name = {self.name}, Rollno = {self.rollNo}, City = {self.city}, Company = {self.companyName}")


p1 = PlaceStd("Suraj", 12, "Pune", "TCS")
p2 = PlaceStd("Sauraj", 13, "Mumbai", "Infosys")
p3 = PlaceStd("Ritik", 1, "Nashik", "Wipro")
p4 = PlaceStd("Roshan", 4, "Delhi", "Accenture")

p1.display()
p2.display()
p3.display()
p4.display()

print(PlaceStd.placeCount)

print("Total Places:",PlaceStd.placeCount)

print("Place Name:", PlaceStd.getPlaceName())

PlaceStd.setPlaceName("FBS Pune")

print("Updated Place Name:", PlaceStd.getPlaceName())