from functools import reduce

class C1(object):

    def buildWall(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7

        def backtracking(a1, a2, a3, a4, a5, a6, a7):
            if a5 in a6:
                return
            a6.add(a5)
            if a4 >= a2:
                if a4 == a2:
                    a7.append(a5 ^ 1 << a2)
                return
            for v1 in a3:
                backtracking(a1, a2, a3, a4 + v1, a5 | 1 << a4 + v1, a6, a7)
        v2, v3 = ([], set())
        backtracking(a1, a2, a3, 0, 0, v3, v2)
        v4 = [[j for v5, v6 in enumerate(v2) if not r1 & v6] for v7 in v2]
        v8 = [[1] * len(v2), [0] * len(v2)]
        for v9 in range(a1 - 1):
            v8[(v9 + 1) % 2] = [sum((v8[v9 % 2][k] for v10 in v4[v5])) % v1 for v5 in range(len(v2))]
        return sum(v8[(a1 - 1) % 2]) % v1
