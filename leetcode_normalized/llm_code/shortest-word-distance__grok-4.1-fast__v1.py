class C1:

    def shortestDistance(self, a1, a2, a3):
        v1, v2 = (-1, -1)
        v3 = float('inf')
        for v4, v5 in enumerate(a1):
            if v5 == a2:
                if v2 != -1:
                    v3 = min(v3, v4 - v2)
                v1 = v4
            elif v5 == a3:
                if v1 != -1:
                    v3 = min(v3, v4 - v1)
                v2 = v4
        return v3
