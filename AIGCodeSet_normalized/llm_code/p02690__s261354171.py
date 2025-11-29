v1 = int(input())
for v2 in range(1, 1000):
    for v3 in range(-1000, 0):
        if v2 ** 5 - v3 ** 5 == v1:
            v4 = v2
            v5 = v3
            break
print(v4, v5)
