total1 = 0

for i in range(1,100):
    if i % 3 == 0:
        total1 += i
    elif i % 5 == 0:
        total1 += i

print(total1)