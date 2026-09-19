class Vehicle:

    def __new__(cls, *args):
        if cls == Vehicle:
            raise TypeError("Vehicle object cannot be created")
        return object.__new__(cls)


class TwoWheeler(Vehicle):

    def toll(self, persons):
        amount = 20

        if persons > 2:
            amount = amount + (persons - 2) * 10

        return amount


class ThreeWheeler(Vehicle):

    def toll(self, persons):
        amount = 30

        if persons > 3:
            amount = amount + (persons - 3) * 20

        return amount


class FourWheeler(Vehicle):

    def toll(self, persons):
        amount = 40

        if persons > 4:
            amount = amount + (persons - 4) * 40

        return amount


class HeavyVehicle(Vehicle):

    def toll(self, persons):
        amount = 60

        if persons > 6:
            amount = amount + (persons - 6) * 100

        return amount


# Main
print("1. Two Wheeler")
print("2. Three Wheeler")
print("3. Four Wheeler")
print("4. Heavy Vehicle")

choice = int(input("Enter choice: "))
persons = int(input("Enter persons: "))

if choice == 1:
    v = TwoWheeler()
elif choice == 2:
    v = ThreeWheeler()
elif choice == 3:
    v = FourWheeler()
elif choice == 4:
    v = HeavyVehicle()
else:
    print("Invalid choice")
    exit()

print("Toll =", v.toll(persons))