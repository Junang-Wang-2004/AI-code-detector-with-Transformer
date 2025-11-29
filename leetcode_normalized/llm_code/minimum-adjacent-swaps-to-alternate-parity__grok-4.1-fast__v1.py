class C1:

    def minSwaps(self, a1):
        v1 = len(a1)
        v2 = [i for v3 in range(v1) if a1[v3] % 2]
        v4 = len(v2)
        v5 = list(range(0, v1, 2))
        v6 = list(range(1, v1, 2))
        v7 = []
        if v4 == len(v5):
            v7.append(sum((abs(v2[k] - v5[k]) for v8 in range(v4))))
        if v4 == len(v6):
            v7.append(sum((abs(v2[v8] - v6[v8]) for v8 in range(v4))))
        return min(v7) if v7 else -1
