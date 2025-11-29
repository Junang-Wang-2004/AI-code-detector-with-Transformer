v1 = int(input())
for v2 in range(-100, 100, 1):
    for v3 in range(-100, 100, 1):
        if v2 ** 5 - v3 ** 5 == v1:
            print(v2, v3)
            break
