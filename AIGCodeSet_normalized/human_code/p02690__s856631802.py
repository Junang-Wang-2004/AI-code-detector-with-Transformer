import sys
v1 = int(input())
v2 = 10 ** 9 + 7
v3 = [i * m for v4 in range(0, 10 ** 4) for v5 in [-1, 1]]
for v4 in range(0, 10 ** 4):
    for v6 in v3:
        if v4 == v6:
            break
        if v1 % (v4 - v6) == 0:
            if v4 ** 5 - v6 ** 5 == v1:
                print(v4, v6)
                sys.exit(0)
