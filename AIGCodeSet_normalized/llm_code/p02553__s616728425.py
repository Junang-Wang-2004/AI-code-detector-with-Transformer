v1, v2, v3, v4 = map(int, input().split())
if v1 > 0:
    if v3 > 0:
        print(max(v1 * v3, v1 * v4, v2 * v3, v2 * v4))
    else:
        print(max(v1 * v3, v2 * v4))
elif v3 < 0:
    print(max(v1 * v4, v2 * v3))
else:
    print(max(v1 * v3, v1 * v4, v2 * v3, v2 * v4))
