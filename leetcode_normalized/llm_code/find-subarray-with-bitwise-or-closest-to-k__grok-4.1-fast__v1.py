class C1:

    def minimumDifference(self, a1, a2):
        v1 = float('inf')
        v2 = set()
        for v3 in a1:
            v1 = min(v1, abs(v3 - a2))
            v4 = set([v3])
            for v5 in v2:
                v6 = v5 | v3
                v4.add(v6)
                v1 = min(v1, abs(v6 - a2))
            v2 = v4
        return v1
