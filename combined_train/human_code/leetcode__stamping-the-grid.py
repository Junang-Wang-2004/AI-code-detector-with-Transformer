class C1(object):

    def possibleToStamp(self, a1, a2, a3):
        """
        """
        v1 = [[0] * (len(a1[0]) + 1) for v2 in range(len(a1) + 1)]
        v3 = [[0] * len(a1[0]) for v2 in range(len(a1))]
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v1[v4 + 1][v5 + 1] = v1[v4 + 1][v5] + v1[v4][v5 + 1] - v1[v4][v5] + (1 ^ a1[v4][v5])
                if v4 + 1 >= a2 and v5 + 1 >= a3:
                    v6, v7 = (v4 + 1 - a2, v5 + 1 - a3)
                    v3[v4][v5] = int(v1[v4 + 1][v5 + 1] - v1[v6][v5 + 1] - v1[v4 + 1][v7] + v1[v6][v7] == a3 * a2)
        v8 = [[0] * (len(a1[0]) + 1) for v2 in range(len(a1) + 1)]
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v8[v4 + 1][v5 + 1] = v8[v4 + 1][v5] + v8[v4][v5 + 1] - v8[v4][v5] + v3[v4][v5]
        for v4 in range(len(a1)):
            for v5 in range(len(a1[0])):
                v6, v7 = (min(v4 + a2, len(a1)), min(v5 + a3, len(a1[0])))
                if not a1[v4][v5] and (not v8[v6][v7] - v8[v4][v7] - v8[v6][v5] + v8[v4][v5]):
                    return False
        return True
