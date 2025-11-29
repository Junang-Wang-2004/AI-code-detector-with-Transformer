class C1:

    def minimumDistance(self, a1):
        v1 = 26
        v2 = 10 ** 9

        def get_pos(a1):
            return ord(a1) - 65

        def get_dist(a1, a2):
            if a1 == v1 or a2 == v1:
                return 0
            v1, v2 = divmod(a1, 6)
            v3, v4 = divmod(a2, 6)
            return abs(v1 - v3) + abs(v2 - v4)
        v3 = [[v2] * 27 for v4 in range(27)]
        v3[v1][v1] = 0
        for v5 in a1:
            v6 = get_pos(v5)
            v7 = [[v2] * 27 for v4 in range(27)]
            for v8 in range(27):
                for v9 in range(27):
                    if v3[v8][v9] == v2:
                        continue
                    v10 = v3[v8][v9] + get_dist(v8, v6)
                    v7[v6][v9] = min(v7[v6][v9], v10)
                    v11 = v3[v8][v9] + get_dist(v9, v6)
                    v7[v8][v6] = min(v7[v8][v6], v11)
            v3 = v7
        return min((min(r) for v12 in v3))
