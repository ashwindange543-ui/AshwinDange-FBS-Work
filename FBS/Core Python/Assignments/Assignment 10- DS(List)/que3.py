li = [30 , 50 , 20 , 90 , 60]
largest = li[0]
second_largest = li[0]
for i in range(len(li)):
    if li[i] > largest:
        second_largest = largest
        largest = li[i]
    elif li[i] > second_largest and li[i] != largest:
        second_largest = li[i]
print("Largest =", largest)
print("Second Largest =", second_largest)