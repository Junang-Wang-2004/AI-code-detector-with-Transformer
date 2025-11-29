import itertools

class C1(object):

    def numOfWays(self, a1):
        """
        """

        def matrix_expo(a1, a2):
            v1 = [[int(i == j) for v2 in range(len(a1))] for v3 in range(len(a1))]
            while a2:
                if a2 % 2:
                    v1 = matrix_mult(v1, a1)
                a1 = matrix_mult(a1, a1)
                a2 /= 2
            return v1

        def matrix_mult(a1, a2):
            v1 = list(zip(*a2))
            return [[sum((a * b % MOD for v2, v3 in zip(row, col))) % MOD for v4 in v1] for v5 in a1]
        v1 = 10 ** 9 + 7
        v2 = [[3, 2], [2, 2]]
        return sum(matrix_mult([[6, 6]], matrix_expo(v2, a1 - 1))[0]) % v1
