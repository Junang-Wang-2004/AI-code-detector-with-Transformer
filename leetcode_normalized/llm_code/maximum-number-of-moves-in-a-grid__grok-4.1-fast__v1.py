class C1:

    def maxMoves(self, a1):
        if not a1 or not a1[0]:
            return 0
        v1, v2 = (len(a1), len(a1[0]))
        v3 = set(range(v1))
        v4 = 0
        while v4 < v2 - 1 and v3:
            v5 = set()
            for v6 in v3:
                v7 = a1[v6][v4]
                for v8 in (-1, 0, 1):
                    v9 = v6 + v8
                    if 0 <= v9 < v1 and v7 < a1[v9][v4 + 1]:
                        v5.add(v9)
            v3 = v5
            v4 += 1
        return v4
