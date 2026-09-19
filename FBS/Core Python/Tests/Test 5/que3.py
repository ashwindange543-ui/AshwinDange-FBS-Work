Data = [
    [101, "Seema", 45000],
    [340, "Rajani", 13000],
    [210, "Tannu", 14000],
    [320, "Suresh", 35000]
]

for i in range(len(Data)):
    for j in range(i + 1, len(Data)):
        if Data[i][2] > Data[j][2]:
            Data[i], Data[j] = Data[j], Data[i]

print(Data)