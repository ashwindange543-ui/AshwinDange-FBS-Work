li = [ 2 , 7 , 9 , 1 , 3 , 5 , 2 , 13 , 40 , 54 , 67]
odd_numbers = []

for n in li:
    if n % 2 != 0:
        odd_numbers.append(n)
        
print("Odd numbers:", odd_numbers)