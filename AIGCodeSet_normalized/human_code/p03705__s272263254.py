v1, v2, v3 = list(map(int, input().split()))
if v3 < v2:
    print(0)
elif v3 != v2 and v1 == 1:
    print(0)
else:
    print(v3 * (v1 - 1) + v2 - v2 * (v1 - 1) - v3 + 1)
