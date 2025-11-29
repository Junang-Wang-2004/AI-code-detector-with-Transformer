class C1(object):

    def maxCollectedFruits(self, a1):
        """
        """
        v1 = len(a1)
        for v2 in range(v1):
            for v3 in range(v2 + 1, v1 - (v2 + 1)):
                a1[v2][v3] = 0
        for v2 in range(1, v1 - 1):
            for v3 in range(v2 + 1, v1):
                a1[v2][v3] += max(a1[v2 - 1][v3 - 1], a1[v2 - 1][v3], a1[v2 - 1][v3 + 1] if v3 + 1 < v1 else 0)
        for v3 in range(v1):
            for v2 in range(v3 + 1, v1 - (v3 + 1)):
                a1[v2][v3] = 0
        for v3 in range(1, v1 - 1):
            for v2 in range(v3 + 1, v1):
                a1[v2][v3] += max(a1[v2 - 1][v3 - 1], a1[v2][v3 - 1], a1[v2 + 1][v3 - 1] if v2 + 1 < v1 else 0)
        return sum((a1[v2][v2] for v2 in range(v1))) + a1[-2][-1] + a1[-1][-2]
