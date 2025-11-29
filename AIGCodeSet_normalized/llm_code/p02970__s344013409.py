v1, v2 = [int(x) for v3 in input().split()]
if v1 / v2 < v1 - v2 * 2:
    print(v1 // v2)
else:
    print(v1 // v2 + 1)
