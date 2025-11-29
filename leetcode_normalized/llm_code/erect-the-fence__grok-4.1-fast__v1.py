class C1:

    def outerTrees(self, a1):
        v1 = sorted(set(map(tuple, a1)))
        if len(v1) <= 1:
            return [list(p) for v2 in v1]

        def direction(a1, a2, a3):
            return (a2[0] - a1[0]) * (a3[1] - a1[1]) - (a2[1] - a1[1]) * (a3[0] - a1[0])
        v3 = []
        for v2 in v1:
            while len(v3) >= 2 and direction(v3[-2], v3[-1], v2) < 0:
                v3.pop()
            v3.append(v2)
        v4 = []
        v5 = v1[::-1]
        for v2 in v5:
            while len(v4) >= 2 and direction(v4[-2], v4[-1], v2) < 0:
                v4.pop()
            v4.append(v2)
        v6 = v3[:-1] + v4[:-1]
        v7 = set(map(tuple, v6))
        return [list(pt) for v8 in v7]
