v1, v2 = map(int, input().split())
v3 = v1 - v2 + 1
v4 = 1
for v5 in range(1, v2 + 1):
    if v1 - v2 + 1 < v5:
        print(0)
    else:
        v6 = v3 * v4 % (10 ** 9 + 7)
        print(v6)
    v3 = v3 * (v1 - v2 - v5 + 1) // (v5 + 1)
    v4 = v4 * (v2 - v5) // v5
