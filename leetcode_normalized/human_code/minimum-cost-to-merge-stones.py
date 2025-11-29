class C1(object):

    def mergeStones(self, a1, a2):
        """
        """
        if (len(a1) - 1) % (a2 - 1):
            return -1
        v1 = [0]
        for v2 in a1:
            v1.append(v1[-1] + v2)
        v3 = [[0] * len(a1) for v4 in range(len(a1))]
        for v5 in range(a2 - 1, len(a1)):
            for v6 in range(len(a1) - v5):
                v3[v6][v6 + v5] = min((v3[v6][j] + v3[j + 1][v6 + v5] for v7 in range(v6, v6 + v5, a2 - 1)))
                if v5 % (a2 - 1) == 0:
                    v3[v6][v6 + v5] += v1[v6 + v5 + 1] - v1[v6]
        return v3[0][len(a1) - 1]
