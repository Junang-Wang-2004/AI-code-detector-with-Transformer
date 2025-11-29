class C1:

    def closestToTarget(self, a1, a2):
        v1 = float('inf')
        v2 = set()
        for v3 in a1:
            v4 = set()
            v4.add(v3)
            for v5 in v2:
                v4.add(v5 & v3)
            v2 = v4
            for v6 in v4:
                v1 = min(v1, abs(v6 - a2))
        return v1
