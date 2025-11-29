class C1(object):

    def minCost(self, a1, a2):
        """
        """
        v1 = len(a1)
        v2 = len(a1[0])
        v3 = [[float('inf')] * v2 for v4 in range(v1)]
        v3[-1][-1] = 0
        v5 = max((max(row) for v6 in a1))
        v7 = [float('inf')] * (v5 + 1)
        for v8 in range(a2 + 1):
            for v9 in reversed(range(v1)):
                for v10 in reversed(range(v2)):
                    if v9 + 1 < v1:
                        if v3[v9 + 1][v10] + a1[v9 + 1][v10] < v3[v9][v10]:
                            v3[v9][v10] = v3[v9 + 1][v10] + a1[v9 + 1][v10]
                    if v10 + 1 < v2:
                        if v3[v9][v10 + 1] + a1[v9][v10 + 1] < v3[v9][v10]:
                            v3[v9][v10] = v3[v9][v10 + 1] + a1[v9][v10 + 1]
                    if v7[a1[v9][v10]] < v3[v9][v10]:
                        v3[v9][v10] = v7[a1[v9][v10]]
            for v9 in range(v1):
                for v10 in range(v2):
                    if v3[v9][v10] < v7[a1[v9][v10]]:
                        v7[a1[v9][v10]] = v3[v9][v10]
            for v8 in range(v5):
                if v7[v8] < v7[v8 + 1]:
                    v7[v8 + 1] = v7[v8]
        return v3[0][0]
