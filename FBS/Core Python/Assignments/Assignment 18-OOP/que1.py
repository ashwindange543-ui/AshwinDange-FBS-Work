
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real,
                       self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real,
                       self.imag - other.imag)

    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"

    def __del__(self):
        print("Complex object destroyed")


c1 = Complex(10, 5)
c2 = Complex(4, 2)

c3 = c1 + c2
c4 = c1 - c2

print("Addition:", c3)
print("Subtraction:", c4)
