class C1(object):

    def maximumAmount(self, a1):
        """
        """
        v1 = 2
        v2 = [[float('-inf')] * (v1 + 1) for v3 in range(len(a1[0]))]
        for v4 in range(len(a1)):
            v5 = [[float('-inf')] * (v1 + 1) for v3 in range(len(a1[0]))]
            for v6 in range(len(a1[0])):
                for v7 in range(v1 + 1):
                    if v4 == 0 and v6 == 0:
                        v5[v6][v7] = max(a1[v4][v6], 0) if v7 - 1 >= 0 else a1[v4][v6]
                        continue
                    if v4 - 1 >= 0:
                        v5[v6][v7] = max(v5[v6][v7], v2[v6][v7] + a1[v4][v6])
                        if v7 - 1 >= 0:
                            v5[v6][v7] = max(v5[v6][v7], v2[v6][v7 - 1])
                    if v6 - 1 >= 0:
                        v5[v6][v7] = max(v5[v6][v7], v5[v6 - 1][v7] + a1[v4][v6])
                        if v7 - 1 >= 0:
                            v5[v6][v7] = max(v5[v6][v7], v5[v6 - 1][v7 - 1])
            v2 = v5
        return v2[-1][-1]
