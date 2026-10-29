
s = input("Enter a string: ")

result = ''.join([ch for ch in s if ch.lower() not in 'aeiou'])

print("String without vowels:", result)
