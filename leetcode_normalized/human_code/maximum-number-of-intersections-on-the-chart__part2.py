class C1(object):

    def maxIntersectionCount(self, a1):
        """
        """
        v1 = []
        for v2 in range(len(a1) - 1):
            v3, v4 = (2 * a1[v2], 2 * a1[v2 + 1] + (-1 if a1[v2] < a1[v2 + 1] else +1))
            v1.append((min(v3, v4), +1))
            v1.append((max(v3, v4) + 1, -1))
        v1.append((2 * a1[-1], +1))
        v1.append((2 * a1[-1] + 1, -1))
        v1.sort()
        v5 = v6 = 0
        for v7, v8 in v1:
            v6 += v8
            v5 = max(v5, v6)
        return v5
