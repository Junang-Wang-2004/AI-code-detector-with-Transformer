v1, v2, v3 = map(int, input().split())
if v1 == 1 and v2 != v3:
    print(0)
elif v1 == 1 and v2 == v3:
    print(1)
elif v2 > v3:
    print(0)
elif v1 == 2:
    print(1)
else:
    print(v3 * (v1 - 1) + v2 - (v2 * (v1 - 1) + v3) + 1)
