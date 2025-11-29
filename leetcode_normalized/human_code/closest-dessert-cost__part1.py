class C1(object):

    def closestCost(self, a1, a2, a3):
        """
        """
        v1 = 2
        v2, v3 = (max(a1), max(a2))
        v4 = [False] * (max(v2, a3 + v3 // 2) + 1)
        for v5 in a1:
            v4[v5] = True
        for v6 in a2:
            for v7 in range(v1):
                for v8 in reversed(range(len(v4) - v6)):
                    if v4[v8]:
                        v4[v8 + v6] = True
        v9 = float('inf')
        for v8 in range(1, len(v4)):
            if not v4[v8]:
                continue
            if abs(v8 - a3) < abs(v9 - a3):
                v9 = v8
            if v8 >= a3:
                break
        return v9
