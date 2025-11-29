class C1(object):

    def minFlips(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = 0
        for v4 in range(v1 // 2):
            for v5 in range(v2 // 2):
                v6 = a1[v4][v5] + a1[v4][~v5] + a1[~v4][v5] + a1[~v4][~v5]
                v3 += min(v6, 4 - v6)
        v7 = v8 = 0
        if v1 % 2:
            for v5 in range(v2 // 2):
                v7 += a1[v1 // 2][v5] ^ a1[v1 // 2][~v5]
                v8 += a1[v1 // 2][v5] + a1[v1 // 2][~v5]
        if v2 % 2:
            for v4 in range(v1 // 2):
                v7 += a1[v4][v2 // 2] ^ a1[~v4][v2 // 2]
                v8 += a1[v4][v2 // 2] + a1[~v4][v2 // 2]
        if v1 % 2 and v2 % 2:
            v3 += a1[v1 // 2][v2 // 2]
        if v7 == 0:
            v3 += -v8 % 4
        return v3 + v7
