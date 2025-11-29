class C1(object):

    def maxPathScore(self, a1, a2):
        """
        """
        v1 = ((1, 0), (0, 1))
        v2 = [[[-1] * (a2 + 1) for v3 in range(len(a1[0]))] for v3 in range(len(a1))]
        v2[0][0][0] = 0
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                for v6 in range(a2 + 1):
                    if v2[v4][v5][v6] == -1:
                        continue
                    for v7, v8 in v1:
                        v9, v10 = (v4 + v7, v5 + v8)
                        if not (0 <= v9 < len(a1) and 0 <= v10 < len(a1[0]) and (v6 + (1 if a1[v9][v10] else 0) <= a2)):
                            continue
                        v11 = v6 + (1 if a1[v9][v10] else 0)
                        v2[v9][v10][v11] = max(v2[v9][v10][v11], v2[v4][v5][v6] + a1[v9][v10])
        return max(v2[-1][-1])
