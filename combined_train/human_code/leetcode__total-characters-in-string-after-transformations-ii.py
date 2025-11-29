import itertools
from functools import reduce

class C1(object):

    def lengthAfterTransformations(self, a1, a2, a3):
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
        v2 = [0] * 26
        for v3 in a1:
            v2[ord(v3) - ord('a')] += 1
        v4 = [[0] * 26 for v5 in range(26)]
        for v6 in range(len(a3)):
            for v7 in range(1, a3[v6] + 1):
                v4[v6][(v6 + v7) % 26] = 1
        v8 = matrix_expo(v4, a2)
        return reduce(lambda accu, x: (accu + v3) % v1, matrix_mult([v2], v8)[0], 0)
