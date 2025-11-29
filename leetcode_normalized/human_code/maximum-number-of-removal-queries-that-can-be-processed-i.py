class C1(object):

    def maximumProcessableQueries(self, a1, a2):
        """
        """
        v1 = [[float('-inf')] * len(a1) for v2 in range(len(a1))]
        v1[0][-1] = 0
        for v3 in reversed(range(1, len(a1))):
            for v4 in range(len(a1) - (v3 - 1)):
                v5 = v4 + (v3 - 1)
                if v4 - 1 >= 0:
                    v1[v4][v5] = max(v1[v4][v5], v1[v4 - 1][v5] + (1 if a1[v4 - 1] >= a2[v1[v4 - 1][v5]] else 0))
                if v5 + 1 < len(a1):
                    v1[v4][v5] = max(v1[v4][v5], v1[v4][v5 + 1] + (1 if a1[v5 + 1] >= a2[v1[v4][v5 + 1]] else 0))
                if v1[v4][v5] == len(a2):
                    return len(a2)
        return max((v1[v4][v4] + (1 if a1[v4] >= a2[v1[v4][v4]] else 0) for v4 in range(len(a1))))
