v1, v2 = map(int, input().split())
v3 = v1 // (2 * v2 + 1)
if v1 > v3 * (2 * v2 + 1):
    print(v3 + 1)
else:
    print(v3)
