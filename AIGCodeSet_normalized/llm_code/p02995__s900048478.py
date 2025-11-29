v1, v2, v3, v4 = map(int, input().split())
v5 = (v2 + 1 - v1) // v3
v6 = (v2 + 1 - v1) // v4
v7 = (v2 + 1 - v1) // (v3 * v4)
if v1 % v3 != 1 and v1 % v4 != 0 and (v2 % v3 != 0) and (v2 % v4 != 0):
    print(v2 + 1 - v1 - (v5 + v6 - v7) - 1)
else:
    print(v2 + 1 - v1 - (v5 + v6 - v7))
