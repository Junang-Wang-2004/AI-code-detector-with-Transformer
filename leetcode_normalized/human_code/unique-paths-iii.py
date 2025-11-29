class C1(object):

    def uniquePathsIII(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def index(a1, a2, a3):
            return 1 << a2 * len(a1[0]) + a3

        def dp(a1, a2, a3, a4, a5):
            if a2 == a3:
                return int(a4 == 0)
            v1 = (a2, a4)
            if v1 in a5:
                return a5[v1]
            v2 = 0
            for v3 in v1:
                v4, v5 = (a2[0] + v3[0], a2[1] + v3[1])
                if 0 <= v4 < len(a1) and 0 <= v5 < len(a1[0]) and (a1[v4][v5] % 2 == 0) and a4 & index(a1, v4, v5):
                    v2 += dp(a1, (v4, v5), a3, a4 ^ index(a1, v4, v5), a5)
            a5[v1] = v2
            return a5[v1]
        v2 = 0
        v3, v4 = (None, None)
        for v5, v6 in enumerate(a1):
            for v7, v8 in enumerate(v6):
                if v8 % 2 == 0:
                    v2 |= index(a1, v5, v7)
                if v8 == 1:
                    v3 = (v5, v7)
                elif v8 == 2:
                    v4 = (v5, v7)
        return dp(a1, v3, v4, v2, {})
