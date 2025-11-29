class C1:

    def minDifference(self, a1):
        v1 = len(a1)
        if v1 <= 4:
            return 0
        a1.sort()
        v2 = float('inf')
        for v3 in range(4):
            v2 = min(v2, a1[v1 - 4 + v3] - a1[v3])
        return v2
