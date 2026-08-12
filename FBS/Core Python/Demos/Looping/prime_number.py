num = 7

for i in range(2,num):
    print(i)
    if(num % i == 0):
        print(f'{num} is a not a prime number.')
        break
else:
    print(f'{num} is a prime numper.')