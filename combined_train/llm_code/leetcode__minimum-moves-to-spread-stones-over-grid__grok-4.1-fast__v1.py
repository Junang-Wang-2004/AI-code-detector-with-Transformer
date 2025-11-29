class C1(object):

    def minimumMoves(self, a1):
        v1, v2 = (len(a1), len(a1[0]))
        v3 = []
        v4 = []
        for v5 in range(v1):
            for v6 in range(v2):
                v7 = a1[v5][v6]
                if v7 == 0:
                    v4.append((v5, v6))
                elif v7 > 1:
                    for v8 in range(v7 - 1):
                        v3.append((v5, v6))
        import itertools
        v9 = float('inf')
        v10 = len(v4)
        for v11 in itertools.permutations(v4):
            v12 = sum((abs(v3[t][0] - v11[t][0]) + abs(v3[t][1] - v11[t][1]) for v13 in range(v10)))
            v9 = min(v9, v12)
        return int(v9)
