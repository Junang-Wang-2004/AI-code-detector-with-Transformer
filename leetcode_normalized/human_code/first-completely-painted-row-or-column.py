class C1(object):

    def firstCompleteIndex(self, a1, a2):
        """
        """
        v1 = {a2[i][j]: (i, j) for v2 in range(len(a2)) for v3 in range(len(a2[0]))}
        v4 = [0] * len(a2)
        v5 = [0] * len(a2[0])
        for v6, v7 in enumerate(a1):
            v2, v3 = v1[v7]
            v4[v2] += 1
            v5[v3] += 1
            if v4[v2] == len(a2[0]) or v5[v3] == len(a2):
                return v6
        return -1
