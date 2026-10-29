
class Television:
    def __init__(self):
        self.model = 0
        self.size = 0
        self.price = 0

    def Accept(self):
        self.model = int(input("Enter Model Number: "))

        if self.model < 0 or len(str(self.model)) > 4:
            raise ValueError("Model number must have maximum 4 digits")

        self.size = float(input("Enter Screen Size: "))

        if self.size < 12 or self.size > 70:
            raise ValueError("Screen size must be between 12 and 70 inches")

        self.price = float(input("Enter Price: "))

        if self.price < 0 or self.price > 5000:
            raise ValueError("Price must be between 0 and 5000")

    def Display(self):
        print("Model Number:", self.model)
        print("Screen Size:", self.size, "inches")
        print("Price: Rs.", self.price)


def main():
    tv = Television()

    try:
        tv.Accept()
    except ValueError as e:
        print("Exception:", e)
        tv.model = 0
        tv.size = 0
        tv.price = 0

    print("\nTelevision Details:")
    tv.Display()


main()
