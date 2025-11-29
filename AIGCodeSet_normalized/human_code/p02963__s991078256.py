v1 = int(input())
v2 = int((v1 - 1) ** (1 / 2)) + 1
v3 = v2 ** 2 - v1
if v2 > 10 ** 9:
    v3 = 10 ** 18 - v1
    print(0, 0, 10 ** 9, 1, v3, 10 ** 9)
else:
    print(0, 0, v2, 1, v3, v2)
