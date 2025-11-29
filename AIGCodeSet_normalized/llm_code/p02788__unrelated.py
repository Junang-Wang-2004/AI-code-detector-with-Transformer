def f1():
    v1, v2, v3 = map(int, input().split())
    v4 = []
    for v5 in range(v1):
        v6, v7 = map(int, input().split())
        v4.append((v6, v7))
    v4.sort()
    v8 = 0
    v9 = 0
    while v9 < v1:
        v6, v7 = v4[v9]
        v8 += (v7 + v3 - 1) // v3
        v9 += 1
        while v9 < v1 and v4[v9][0] <= v6 + v2:
            v9 += 1
    print(v8)
f1()
