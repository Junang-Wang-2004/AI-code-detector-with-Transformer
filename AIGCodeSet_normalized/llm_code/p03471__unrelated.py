def f1(a1, a2):
    for v1 in range(a1 + 1):
        for v2 in range(a1 - v1 + 1):
            v3 = a1 - v1 - v2
            if 10000 * v1 + 5000 * v2 + 1000 * v3 == a2:
                return (v1, v2, v3)
    return (-1, -1, -1)
v1, v2 = map(int, input().split())
v3, v4, v5 = f1(v1, v2)
print(v3, v4, v5)
