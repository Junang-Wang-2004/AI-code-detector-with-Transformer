class C1(object):

    def maxProductPath(self, a1):
        """
        """
        v1 = 10 ** 9 + 7
        v2 = [[0] * len(a1[0]) for v3 in range(2)]
        v4 = [[0] * len(a1[0]) for v3 in range(2)]
        for v5 in range(len(a1)):
            for v6 in range(len(a1[v5])):
                if v5 == 0 and v6 == 0:
                    v2[v5 % 2][v6] = v4[v5 % 2][v6] = a1[v5][v6]
                    continue
                v7 = max(v2[(v5 - 1) % 2][v6] if v5 > 0 else v2[v5 % 2][v6 - 1], v2[v5 % 2][v6 - 1] if v6 > 0 else v2[(v5 - 1) % 2][v6])
                v8 = min(v4[(v5 - 1) % 2][v6] if v5 > 0 else v4[v5 % 2][v6 - 1], v4[v5 % 2][v6 - 1] if v6 > 0 else v4[(v5 - 1) % 2][v6])
                if a1[v5][v6] < 0:
                    v7, v8 = (v8, v7)
                v2[v5 % 2][v6] = v7 * a1[v5][v6]
                v4[v5 % 2][v6] = v8 * a1[v5][v6]
        return v2[(len(a1) - 1) % 2][-1] % v1 if v2[(len(a1) - 1) % 2][-1] >= 0 else -1
