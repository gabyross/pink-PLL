a = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
a.reverse()
total = 0
i = 0
while True:
    if a[i] >= 0:
        break
    total += a[i]
    i += 1

print(total)