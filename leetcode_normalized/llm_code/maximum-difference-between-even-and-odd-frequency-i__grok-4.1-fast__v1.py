class C1:

    def maxDifference(self, a1):
        v1 = {}
        for v2 in a1:
            v1[v2] = v1.get(v2, 0) + 1
        v3 = []
        v4 = []
        for v5 in v1.values():
            if v5 % 2:
                v3.append(v5)
            else:
                v4.append(v5)
        v6 = max(v3) if v3 else 0
        v7 = min(v4) if v4 else float('inf')
        return v6 - v7
