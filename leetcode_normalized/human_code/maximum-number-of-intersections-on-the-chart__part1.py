class C1(object):

    def maxIntersectionCount(self, a1):
        """
        """
        v1 = {x: i for v2, v3 in enumerate(sorted(set(a1)))}
        v4 = [0] * (2 * len(v1) + 1)
        for v2 in range(len(a1) - 1):
            v5, v6 = (2 * v1[a1[v2]], 2 * v1[a1[v2 + 1]] + (-1 if a1[v2] < a1[v2 + 1] else +1))
            v4[min(v5, v6)] += 1
            v4[max(v5, v6) + 1] -= 1
        v4[2 * v1[a1[-1]]] += 1
        v4[2 * v1[a1[-1]] + 1] -= 1
        v7 = v8 = 0
        for v9 in v4:
            v8 += v9
            v7 = max(v7, v8)
        return v7
