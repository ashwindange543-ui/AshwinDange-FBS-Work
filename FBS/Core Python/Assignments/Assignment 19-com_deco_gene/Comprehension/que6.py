
s = input("Enter a sentence: ")

d = {word: len(word) for word in s.split()}

print(d)
