def f1(a1, a2):
    v1 = 1
    for v2 in range(a2):
        v1 = int(v1 * (a1 - v2) / (v2 + 1))
    return v1
v1, v2, v3 = map(int, input().split())
v4 = list(map(int, input().split()))
v4.sort(reverse=True)
v5 = v4[v2 - 1]
if v4[0] == v5:
    v6 = 0
    for v7 in range(v2, min(v4.count(v4[0]), v3) + 1):
        v6 += f1(v4.count(v4[0]), v7)
    print(v4[0])
    print(v6)
elif v5 > v4[v2]:
    print(sum(v4[:v2]) / v2)
    print(1)
else:
    v8 = v4.index(v5)
    v9 = v4.count(v5)
    print((sum(v4[:v8]) + v5 * (v2 - v8)) / v2)
    print(f1(v9, v2 - v8))
