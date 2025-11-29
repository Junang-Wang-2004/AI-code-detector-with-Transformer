class C1(object):

    def mostSimilar(self, a1, a2, a3, a4):
        """
        """
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        v5 = [[0] * a1 for v2 in range(len(a4) + 1)]
        for v6 in range(1, len(a4) + 1):
            for v4 in range(a1):
                v5[v6][v4] = (a3[v4] != a4[v6 - 1]) + min((v5[v6 - 1][v3] for v3 in v1[v4]))
        v7 = [v5[-1].index(min(v5[-1]))]
        for v6 in reversed(range(2, len(a4) + 1)):
            for v3 in v1[v7[-1]]:
                if v5[v6 - 1][v3] + (a3[v7[-1]] != a4[v6 - 1]) == v5[v6][v7[-1]]:
                    v7.append(v3)
                    break
        return v7[::-1]
