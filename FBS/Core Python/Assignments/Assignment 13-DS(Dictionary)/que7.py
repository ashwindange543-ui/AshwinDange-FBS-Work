d = {"name": "Ashwin", "age": 22, "city": "Pune"}

key = input("Enter key to remove: ")

if key in d:
    del d[key]
    print("Key removed")
else:
    print("Key not found")

print(d)