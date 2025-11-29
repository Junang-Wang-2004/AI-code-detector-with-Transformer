v1, v2 = map(int, input().split())
v3 = abs(abs(v1) - abs(v2))
if v1 == -v2:
    print(1)
elif v1 * v2 < 0:
    print(v3 + 1)
elif v1 < v2:
    print(v3)
elif v1 * v2:
    print(v3 + 2)
else:
    print(v3 + 1)
