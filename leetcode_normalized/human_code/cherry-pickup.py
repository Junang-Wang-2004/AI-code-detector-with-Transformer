class C1(object):

    def cherryPickup(self, a1):
        """
        """
        v1 = len(a1)
        v2 = [[-1 for v3 in range(v1)] for v3 in range(v1)]
        v2[0][0] = a1[0][0]
        v4 = 2 * (v1 - 1)
        v5 = [(0, 0), (-1, 0), (0, -1), (-1, -1)]
        for v6 in range(1, v4 + 1):
            for v7 in reversed(range(max(0, v6 - v1 + 1), min(v6 + 1, v1))):
                for v8 in reversed(range(v7, min(v6 + 1, v1))):
                    if a1[v7][v6 - v7] == -1 or a1[v8][v6 - v8] == -1:
                        v2[v7][v8] = -1
                        continue
                    v9 = a1[v7][v6 - v7]
                    if v7 != v8:
                        v9 += a1[v8][v6 - v8]
                    v10 = -1
                    for v11 in v5:
                        v12, v13 = (v7 + v11[0], v8 + v11[1])
                        if v12 >= 0 and v13 >= 0 and (v2[v12][v13] >= 0):
                            v10 = max(v10, v2[v12][v13] + v9)
                    v2[v7][v8] = v10
        return max(v2[v1 - 1][v1 - 1], 0)
