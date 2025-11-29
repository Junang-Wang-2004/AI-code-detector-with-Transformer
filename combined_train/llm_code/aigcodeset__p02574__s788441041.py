def f1(a1):
    v1 = [-1] * (a1 + 1)
    for v2 in range(2, a1 + 1):
        if v1[v2] != -1:
            continue
        v3 = v2
        while v3 <= a1:
            v1[v3] = v2
            v3 += v2

    def fuctorization(a1):
        if a1 == 1:
            return 1
        elif a1 < 0:
            a1 = abs(a1)
        elif a1 > a1:
            return -1
        v2 = {}
        while a1 != 1:
            v3 = v1[a1]
            v2.setdefault(v3, 0)
            v2[v3] += 1
            a1 //= v3
        return v2
    return fuctorization
v1 = int(input())
v2 = f1(10 ** 6 + 10)
v3 = list(map(int, input().split()))
v4 = {}
for v5 in v3:
    if v5 == 1:
        continue
    v6 = v2(v5)
    for v7 in v6:
        v4.setdefault(v7, 0)
        v4[v7] += 1
v8 = max(v4.values())
v9 = min(v4.values())
if v8 == 1:
    print('pairwise coprime')
elif v9 == v1:
    print('not coprime')
else:
    print('setwise coprime')
