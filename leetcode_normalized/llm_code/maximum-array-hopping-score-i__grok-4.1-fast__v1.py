class C1:

    def maxScore(self, a1):
        v1 = len(a1)
        if v1 <= 1:
            return 0
        v2 = [0] * v1
        v2[v1 - 1] = a1[v1 - 1]
        for v3 in range(v1 - 2, -1, -1):
            v2[v3] = max(a1[v3], v2[v3 + 1])
        return sum(v2[1:])
