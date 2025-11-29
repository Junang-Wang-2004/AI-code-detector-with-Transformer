class C1(object):

    def maxScore(self, a1):
        """
        """
        v1 = float('inf')
        v2 = float('-inf')
        v3 = v2
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v6 = v1
                if v4 - 1 >= 0:
                    v6 = min(v6, a1[v4 - 1][v5])
                if v5 - 1 >= 0:
                    v6 = min(v6, a1[v4][v5 - 1])
                v3 = max(v3, a1[v4][v5] - v6)
                a1[v4][v5] = min(a1[v4][v5], v6)
        return v3
