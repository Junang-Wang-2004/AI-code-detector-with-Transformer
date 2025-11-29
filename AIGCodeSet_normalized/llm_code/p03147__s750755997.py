def f1(a1):

    def rec(a1, a2):
        if a1 == a2:
            return 0
        v1 = 0
        if not 0 in a1[a1:a2]:
            v2 = min(a1)
            for v3 in range(a1, a2):
                a1[v3] = a1[v3] - v2
            v1 += v2
        v2 = 1000
        for v3 in range(a1, a2):
            if a1[v3] > 0:
                v2 = min(v2, a1[v3])
            else:
                for v4 in range(a1, v3):
                    a1[v4] = a1[v4] - v2
                if a1 != v3:
                    v1 += v2
                return v1 + rec(a1, v3) + rec(v3 + 1, a2)
    return rec(0, len(a1))
v1 = int(input())
v2 = list(map(int, input().split()))
print(f1(v2))
