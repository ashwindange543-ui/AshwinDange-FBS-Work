
class Shirt:
    sizePrice = {
        "small": 0,
        "medium": 100,
        "large": 200,
        "xlarge": 300
    }

    def __init__(self, sid=0, sname="", type="", price=0, size=""):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size.lower()

    def ShowBook(self):
        finalPrice = self.price + Shirt.sizePrice[self.size]

        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", finalPrice)

    def __del__(self):
        print("Shirt object destroyed")

s1 = Shirt(1, "Cotton Shirt", "Formal", 1000, "small")
s2 = Shirt(2, "Cotton Shirt", "Formal", 1000, "medium")
s3 = Shirt(3, "Cotton Shirt", "Formal", 1000, "large")
s4 = Shirt(4, "Cotton Shirt", "Formal", 1000, "xlarge")

s1.ShowBook()
s2.ShowBook()
s3.ShowBook()
s4.ShowBook()
