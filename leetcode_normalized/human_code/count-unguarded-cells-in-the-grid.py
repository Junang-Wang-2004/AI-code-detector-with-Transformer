import itertools

class C1(object):

    def countUnguarded(self, a1, a2, a3, a4):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2, v3, v4 = list(range(3))
        v5 = [[v2] * a2 for v6 in range(a1)]
        for v7, v8 in itertools.chain(a3, a4):
            v5[v7][v8] = v4
        for v7, v8 in a3:
            for v9, v10 in v1:
                v11, v12 = (v7 + v9, v8 + v10)
                while 0 <= v11 < a1 and 0 <= v12 < a2 and (v5[v11][v12] != v4):
                    v5[v11][v12] = v3
                    v11, v12 = (v11 + v9, v12 + v10)
        return sum((v5[v7][v8] == v2 for v7 in range(a1) for v8 in range(a2)))
