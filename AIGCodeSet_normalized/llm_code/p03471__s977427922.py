v1, v2 = map(int, input().split())
v3, v4, v5 = (-1, -1, -1)
try:
    for v6 in range(v1 + 1):
        for v7 in range(v1 - v6 + 1):
            v8 = v1 - (v6 + v7)
            if v6 * 10000 + v7 * 5000 + v8 * 1000 == v2 and v6 + v7 + v8 == v1:
                v3, v4, v5 = (v6, v7, v8)
                raise StopIteration
finally:
    print(v3, v4, v5)
