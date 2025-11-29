class C1(object):

    def maximumLength(self, a1, a2):
        """
        """
        v1 = [[0] * (a2 + 1) for v2 in range(len(a1))]
        v3 = 0
        for v4 in range(len(a1)):
            v1[v4][0] = 1
            for v5 in range(a2 + 1):
                for v6 in range(v4):
                    v1[v4][v5] = max(v1[v4][v5], v1[v6][v5] + 1 if a1[v6] == a1[v4] else 1, v1[v6][v5 - 1] + 1 if v5 - 1 >= 0 else 1)
                v3 = max(v3, v1[v4][v5])
        return v3
