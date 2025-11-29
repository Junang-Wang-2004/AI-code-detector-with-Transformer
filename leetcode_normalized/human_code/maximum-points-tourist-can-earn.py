class C1(object):

    def maxScore(self, a1, a2, a3, a4):
        """
        """
        v1 = [0] * a1
        for v2 in range(a2):
            v1 = [max(v1[u] + a3[v2][u], max((v1[v] + a4[v][u] for v3 in range(a1)))) for v4 in range(a1)]
        return max(v1)
