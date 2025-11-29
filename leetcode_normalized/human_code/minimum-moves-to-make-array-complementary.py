class C1(object):

    def minMoves(self, a1, a2):
        """
        """
        v1 = [0] * (2 * (a2 + 1))
        for v2 in range(len(a1) // 2):
            v3, v4 = (a1[v2], a1[-1 - v2])
            v1[min(v3, v4) + 1] -= 1
            v1[v3 + v4] -= 1
            v1[v3 + v4 + 1] += 1
            v1[max(v3, v4) + a2 + 1] += 1
        v5 = v6 = len(a1)
        for v7 in range(2, 2 * a2 + 1):
            v6 += v1[v7]
            v5 = min(v5, v6)
        return v5
