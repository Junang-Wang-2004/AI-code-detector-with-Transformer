v1 = int(input())
v2 = sorted([list(map(int, input().split())) for v3 in range(v1)])
if v1 == 1:
    print(1)
else:

    def f1(a1):
        v1 = [0] * (v1 - 1)
        v2, v3 = a1[0]
        for v4, (v5, v6) in enumerate(a1[1:]):
            v1[v4] = (v5 - v2, v6 - v3)
            v2, v3 = (v5, v6)
        v7 = {}
        for v8 in v1:
            if v8 in v7:
                v7[v8] += 1
            else:
                v7[v8] = 1
        v9 = 0
        for v10 in v7.values():
            v9 = max(v9, v10)
        return v1 - v9
    print(min(f1(v2), f1(sorted(v2, key=lambda x: x[1]))))
