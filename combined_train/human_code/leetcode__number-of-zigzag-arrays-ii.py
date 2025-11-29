import itertools
from functools import reduce

class C1(object):

    def zigZagArrays(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7

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
        a3 -= a2
        v3 = [[int(i + j < a3) for v4 in range(a3 + 1)] for v5 in range(a3 + 1)]
        v6 = matrix_expo(v3, a1 - 1)
        return reduce(lambda accu, x: (accu + x) % v1, matrix_mult([[1] * (a3 + 1)], v6)[0], 0) * 2 % v1
