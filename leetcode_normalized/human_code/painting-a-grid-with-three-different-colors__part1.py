import collections
import itertools
from functools import reduce

class C1(object):

    def colorTheGrid(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7

        def backtracking(a1, a2, a3, a4):
            if not a3:
                a4.append(a2)
                return
            for v1 in range(3):
                if (a1 == -1 or a1 // a3 % 3 != v1) and (a2 == -1 or a2 // (a3 * 3) % 3 != v1):
                    backtracking(a1, a2 + v1 * a3 if a2 != -1 else v1 * a3, a3 // 3, a4)

        def matrix_mult(a1, a2):
            v1 = list(zip(*a2))
            return [[sum((a * b % v1 for v2, v3 in zip(row, col))) % v1 for v4 in v1] for v5 in a1]

        def matrix_expo(a1, a2):
            v1 = [[int(i == j) for v2 in range(len(a1))] for v3 in range(len(a1))]
            while a2:
                if a2 % 2:
                    v1 = matrix_mult(v1, a1)
                a1 = matrix_mult(a1, a1)
                a2 /= 2
            return v1

        def normalize(a1, a2):
            v1 = {}
            v2 = 0
            while a1:
                v3 = a2 // a1 % 3
                if v3 not in v1:
                    v1[v3] = len(v1)
                v2 += v1[v3] * a1
                a1 //= 3
            return v2
        if a1 > a2:
            a1, a2 = (a2, a1)
        v4 = 3 ** (a1 - 1)
        v5 = []
        backtracking(-1, -1, v4, v5)
        assert len(v5) == 3 * 2 ** (a1 - 1)
        v6 = {mask: normalize(v4, mask) for v7 in v5}
        v8 = collections.Counter((v6[v7] for v7 in v5))
        assert len(v8) == 3 * 2 ** (a1 - 1) // 3 // (2 if a1 >= 2 else 1)
        v9 = collections.defaultdict(list)
        for v7 in v8.keys():
            backtracking(v7, -1, v4, v9[v7])
        v10 = collections.defaultdict(lambda: collections.defaultdict(int))
        for v11, v12 in v9.items():
            for v13 in v12:
                v10[v11][v6[v13]] = (v10[v11][v6[v13]] + 1) % v1
        assert 2 * 3 ** a1 // 3 // 2 // 3 <= sum((len(v) for v14 in v10.values())) <= 2 * 3 ** a1 // 3 // 2
        return reduce(lambda x, y: (x + y) % v1, matrix_mult([list(v8.values())], matrix_expo([[v10[v11][v13] for v13 in v8.keys()] for v11 in v8.keys()], a2 - 1))[0], 0)
