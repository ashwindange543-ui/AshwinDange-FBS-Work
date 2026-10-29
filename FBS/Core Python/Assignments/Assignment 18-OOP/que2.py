
class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        total = total1 + total2

        km = total // 100000
        m = (total % 100000) // 100
        cm = total % 100

        return Distance(km, m, cm)

    def __sub__(self, other):
        total1 = self.km * 100000 + self.m * 100 + self.cm
        total2 = other.km * 100000 + other.m * 100 + other.cm

        total = abs(total1 - total2)

        km = total // 100000
        m = (total % 100000) // 100
        cm = total % 100

        return Distance(km, m, cm)

    def __str__(self):
        return str(self.km) + " km " + str(self.m) + " m " + str(self.cm) + " cm"

    def __del__(self):
        print("Distance object destroyed")


d1 = Distance(2, 30, 50)
d2 = Distance(1, 20, 70)

d3 = d1 + d2
d4 = d1 - d2

print("Addition:", d3)
print("Subtraction:", d4)
