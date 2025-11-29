def f1():
    v1, v2 = map(int, input().split())
    v3 = []
    for v4 in range(v2):
        v5, v6 = map(int, input().split())
        v3.append((v5, v6))
    v3.sort()
    v7 = 0
    v8 = 0
    for v5, v6 in v3:
        if v5 > v7 + 1:
            v8 += v5 - v7 - 1
        v8 += 1
        v7 = v6
    v8 += v1 - v7
    return v8
print(f1())
