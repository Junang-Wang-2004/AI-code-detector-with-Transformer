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
        v2, v3 = ([], set())
        backtracking(a1, a2, a3, 0, 0, v3, v2)
        return reduce(lambda x, y: (x + y) % v1, matrix_mult([[1] * len(v2)], matrix_expo([[int(mask1 & mask2 == 0) for v4 in v2] for v5 in v2], a1 - 1))[0], 0)
