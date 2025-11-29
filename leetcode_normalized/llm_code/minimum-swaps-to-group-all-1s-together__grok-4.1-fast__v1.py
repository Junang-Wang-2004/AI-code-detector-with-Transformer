class C1:

    def minSwaps(self, a1):
        v1 = sum(a1)
        v2 = len(a1)
        if v1 == 0:
            return 0
        v3 = sum(a1[:v1])
        v4 = v3
        for v5 in range(v1, v2):
            v3 += a1[v5] - a1[v5 - v1]
            v4 = max(v4, v3)
        return v1 - v4
