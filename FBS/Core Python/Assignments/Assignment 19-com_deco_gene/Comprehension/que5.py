
s = input("Enter a sentence: ")

words = [word for word in s.split() if len(word) < 5]

print(words)
