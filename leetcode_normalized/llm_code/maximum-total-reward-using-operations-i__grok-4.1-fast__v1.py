class C1:

    def maxTotalReward(self, a1):
        if not a1:
            return 0
        v1 = max(a1)
        v2 = sorted((v for v3 in set(a1) if v3 < v1))
        v4 = {0}
        for v5 in v2:
            v4 |= {s + v5 for v6 in v4 if v6 < v5}
        return v1 + max((v6 for v6 in v4 if v6 < v1), default=0)
