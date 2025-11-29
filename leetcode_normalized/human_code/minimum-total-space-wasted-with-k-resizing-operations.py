class C1(object):

    def minSpaceWastedKResizing(self, a1, a2):
        """
        """
        v1 = float('inf')
        a2 += 1
        v3 = [[v1] * (a2 + 1) for v4 in range(len(a1) + 1)]
        v3[0][0] = 0
        for v5 in range(1, len(a1) + 1):
            v6 = v7 = 0
            for v8 in reversed(range(1, v5 + 1)):
                v6 += a1[v8 - 1]
                v7 = max(v7, a1[v8 - 1])
                for v9 in range(1, a2 + 1):
                    if v3[v8 - 1][v9 - 1] != v1:
                        v3[v5][v9] = min(v3[v5][v9], v3[v8 - 1][v9 - 1] + (v7 * (v5 - v8 + 1) - v6))
        return v3[-1][-1]
