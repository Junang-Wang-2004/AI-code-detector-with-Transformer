class C1(object):

    def minDistance(self, a1, a2):
        """
        """
        v1, v2 = (len(a1), len(a2))
        v3 = [[0] * (v2 + 1) for v4 in range(2)]
        for v5 in range(v1):
            for v6 in range(v2):
                v3[(v5 + 1) % 2][v6 + 1] = max(v3[v5 % 2][v6 + 1], v3[(v5 + 1) % 2][v6], v3[v5 % 2][v6] + (a1[v5] == a2[v6]))
        return v1 + v2 - 2 * v3[v1 % 2][v2]
