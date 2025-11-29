class C1(object):

    def maximumStrength(self, a1, a2):
        v1 = len(a1)
        v2 = -10 ** 20
        v3 = [[v2] * (a2 + 1) for v4 in range(v1 + 1)]
        v3[0][0] = 0
        for v5 in range(v1):
            for v6 in range(a2 + 1):
                v3[v5 + 1][v6] = max(v3[v5 + 1][v6], v3[v5][v6])
                if v6 < a2:
                    v7 = 1 if v6 % 2 == 0 else -1
                    v8 = a1[v5] * (a2 - v6) * v7
                    v3[v5 + 1][v6 + 1] = max(v3[v5 + 1][v6 + 1], v3[v5][v6] + v8)
        return v3[v1][a2]
