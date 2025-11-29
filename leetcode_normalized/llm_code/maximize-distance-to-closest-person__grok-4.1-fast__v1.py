class C1:

    def maxDistToClosest(self, a1):
        v1 = len(a1)
        v2 = [i for v3, v4 in enumerate(a1) if v4]
        if not v2:
            return 0
        v5 = v2[0]
        v5 = max(v5, v1 - 1 - v2[-1])
        for v6 in range(1, len(v2)):
            v5 = max(v5, (v2[v6] - v2[v6 - 1]) // 2)
        return v5
