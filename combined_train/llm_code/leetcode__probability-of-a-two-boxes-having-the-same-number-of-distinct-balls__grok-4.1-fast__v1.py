class C1:

    def getProbability(self, a1):

        def choose(a1, a2):
            if a2 < 0 or a2 > a1:
                return 0
            a2 = min(a2, a1 - a2)
            v2 = 1
            for v3 in range(1, a2 + 1):
                v2 = v2 * (a1 - v3 + 1) // v3
            return v2
        v1 = {(0, 0): 1}
        v2 = sum(a1)
        for v3 in a1:
            v4 = {}
            for (v5, v6), v7 in v1.items():
                for v8 in range(v3 + 1):
                    v9 = choose(v3, v8)
                    v10 = v5 + 2 * v8 - v3
                    v11 = v6 - 1 if v8 == 0 else v6 + 1 if v8 == v3 else v6
                    v4[v10, v11] = v4.get((v10, v11), 0) + v7 * v9
            v1 = v4
        v12 = v1.get((0, 0), 0)
        v13 = choose(v2, v2 // 2)
        return v12 / v13
