import itertools

class C1(object):

    def climbStairs(self, a1):
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
            return [[sum((a * b for v2, v3 in zip(row, col))) for v4 in v1] for v5 in a1]
        v1 = [[1, 1], [1, 0]]
        return matrix_mult([[1, 0]], matrix_expo(v1, a1))[0][0]
