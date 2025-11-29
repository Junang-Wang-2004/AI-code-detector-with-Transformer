class C1:

    def countKSubsequencesWithMaxBeauty(self, a1: str, a2: int) -> int:
        v1 = 10 ** 9 + 7
        v2 = collections.Counter(a1)
        if len(v2) < a2:
            return 0
        v3 = sorted(v2.values(), reverse=True)
        v4 = v3[a2 - 1]
        v5 = 0
        while v5 < a2 and v3[v5] > v4:
            v5 += 1
        v6 = a2 - v5
        v7 = sum((1 for v8 in v3[v5:] if v8 == v4))
        if v6 > v7:
            return 0
        v9 = 1
        for v10 in range(v5):
            v9 = v9 * v3[v10] % v1
        v9 = v9 * pow(v4, v6, v1) % v1
        v11 = 1
        for v10 in range(1, v6 + 1):
            v11 = v11 * (v7 - v10 + 1) % v1
            v11 = v11 * pow(v10, v1 - 2, v1) % v1
        return v9 * v11 % v1
