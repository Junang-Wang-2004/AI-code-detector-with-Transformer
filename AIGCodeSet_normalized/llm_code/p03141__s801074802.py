def f1():
    v1 = int(input())
    v2 = [[int(i) for v3 in input().split()] for v4 in range(v1)]
    v5 = sorted([[a + b, a, b] for v6, v7 in v2], key=lambda x: x[0])
    v8 = 0
    for v3 in range(v1):
        if v3 % 2 == 0:
            v8 += v5[v3][1]
        else:
            v8 -= v5[v3][2]
    print(v8)
f1()
