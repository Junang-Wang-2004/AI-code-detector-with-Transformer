class C1:

    def isPathCrossing(self, a1):
        v1 = [(0, 0)]
        v2, v3 = (0, 0)
        v4 = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        for v5 in a1:
            v6, v7 = v4[v5]
            v2 += v6
            v3 += v7
            v1.append((v2, v3))
        return len(v1) != len(set(v1))
