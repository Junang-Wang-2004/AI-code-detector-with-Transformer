class C1(object):

    def maximumStrength(self, a1, a2):
        """
        """
        v1 = [[float('-inf')] * (len(a1) + 1) for v2 in range(a2 + 1)]
        v1[0] = [0] * (len(a1) + 1)
        for v3 in range(a2):
            for v4 in range(len(a1)):
                v1[v3 + 1][v4 + 1] = max(v1[v3 + 1][v4], v1[v3][v4]) + a1[v4] * (a2 - v3) * (1 if v3 % 2 == 0 else -1)
        return max(v1[-1])
