class C1:

    def maximumCoins(self, a1, a2):

        def get_max(a1):
            a1 = sorted(a1)
            v2 = len(a1)
            v3 = [0] * (v2 + 1)
            for v4 in range(v2):
                v5 = a1[v4][1] - a1[v4][0] + 1
                v3[v4 + 1] = v3[v4] + v5 * a1[v4][2]
            v6 = 0
            v7 = 0
            for v8 in range(v2):
                while a1[v8][1] - a1[v7][1] + 1 > a2:
                    v7 += 1
                v9 = v3[v8 + 1] - v3[v7]
                v10 = a1[v8][1] - a1[v7][0] + 1
                v11 = max(v10 - a2, 0) * a1[v7][2]
                v6 = max(v6, v9 - v11)
            return v6
        v1 = get_max(a1)
        v2 = [[-x[1], -x[0], x[2]] for v3 in a1]
        v1 = max(v1, get_max(v2))
        return v1
