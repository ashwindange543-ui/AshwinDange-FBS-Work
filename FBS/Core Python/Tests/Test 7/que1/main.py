from book import Book

books = {}

while True:
    print("\n1. Add Book")
    print("2. Delete Book")
    print("3. Display All Books")
    print("4. Search Book")
    print("5. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        bid = int(input("Enter Book ID: "))
        name = input("Enter Book Name: ")
        price = float(input("Enter Price: "))
        author = input("Enter Author: ")

        books[bid] = Book(bid, name, price, author)
        print("Book Added Successfully")

    elif ch == "2":
        bid = int(input("Enter Book ID to Delete: "))

        if bid in books:
            del books[bid]
            print("Book Deleted")
        else:
            print("Book Not Found")

    elif ch == "3":
        for bid, b in books.items():
            print(bid, b.name, b.price, b.author)

    elif ch == "4":
        bid = int(input("Enter Book ID to Search: "))

        if bid in books:
            b = books[bid]
            print("ID:", b.bid)
            print("Name:", b.name)
            print("Price:", b.price)
            print("Author:", b.author)
        else:
            print("Book Not Found")

    elif ch == "5":
        break

    else:
        print("Invalid Choice")