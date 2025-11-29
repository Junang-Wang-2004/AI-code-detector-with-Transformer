class C1(object):

    def getMaxFunctionValue(self, a1, a2):
        """
        """
        v1 = (a2 + 1).bit_length()
        v2 = [a1[:] for v3 in range(v1)]
        v4 = [list(range(len(a1))) for v3 in range(v1)]
        for v5 in range(1, len(v2)):
            for v6 in range(len(a1)):
                v2[v5][v6] = v2[v5 - 1][v2[v5 - 1][v6]]
                v4[v5][v6] = v4[v5 - 1][v6] + v4[v5 - 1][v2[v5 - 1][v6]]
        v7 = 0
        for v6 in range(len(a1)):
            v8 = 0
            for v5 in range(v1):
                if a2 + 1 & 1 << v5:
                    v8 += v4[v5][v6]
                    v6 = v2[v5][v6]
            v7 = max(v7, v8)
        return v7
