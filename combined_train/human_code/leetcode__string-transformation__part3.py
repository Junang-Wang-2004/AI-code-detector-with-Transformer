from functools import reduce

class C1(object):

    def numberOfWays(self, a1, a2, a3):
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

        def z_function(a1):
            v1 = [0] * len(a1)
            v2, v3 = (0, 0)
            for v4 in range(1, len(v1)):
                if v4 <= v3:
                    v1[v4] = min(v3 - v4 + 1, v1[v4 - v2])
                while v4 + v1[v4] < len(v1) and a1[v1[v4]] == a1[v4 + v1[v4]]:
                    v1[v4] += 1
                if v4 + v1[v4] - 1 > v3:
                    v2, v3 = (v4, v4 + v1[v4] - 1)
            return v1
        v2 = len(a1)
        v3 = [[0, 1], [v2 - 1, v2 - 1 - 1]]
        v4 = [1, 0]
        v4 = matrix_mult([v4], matrix_expo(v3, a3))[0]
        v5 = z_function(a2 + a1 + a1[:-1])
        return reduce(lambda a, b: (a + b) % v1, (v4[int(i != 0)] for v6 in range(v2) if v5[v6 + len(a2)] >= len(a2)), 0)
