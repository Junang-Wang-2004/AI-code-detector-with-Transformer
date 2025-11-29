class C1(object):

    def findMaxForm(self, a1, a2, a3):
        """
        """
        v1 = [[0 for v2 in range(a3 + 1)] for v2 in range(a2 + 1)]
        for v3 in a1:
            v4, v5 = (0, 0)
            for v6 in v3:
                if v6 == '0':
                    v4 += 1
                elif v6 == '1':
                    v5 += 1
            for v7 in reversed(range(v4, a2 + 1)):
                for v8 in reversed(range(v5, a3 + 1)):
                    v1[v7][v8] = max(v1[v7][v8], v1[v7 - v4][v8 - v5] + 1)
        return v1[a2][a3]
