def f1():
    v1, v2 = map(int, input().split())
    v3 = []
    for v4 in range(v1):
        v3.append(int(input()))
    v3 = sorted(v3)
    v5 = 10 ** 9 + 2
    for v4 in range(v1 - v2 + 1):
        v6 = v3[v4 + v2 - 1] - v3[v4]
        v5 = min(v6, v5)
    print(v5)
f1()
