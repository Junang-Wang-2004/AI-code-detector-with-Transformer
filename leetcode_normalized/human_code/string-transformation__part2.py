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

        def getPrefix(a1):
            v1 = [-1] * len(a1)
            v2 = -1
            for v3 in range(1, len(a1)):
                while v2 + 1 > 0 and a1[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a1[v2 + 1] == a1[v3]:
                    v2 += 1
                v1[v3] = v2
            return v1

        def KMP(a1, a2):
            v1 = getPrefix(a2)
            v2 = -1
            for v3 in range(len(a1)):
                while v2 + 1 > 0 and a2[v2 + 1] != a1[v3]:
                    v2 = v1[v2]
                if a2[v2 + 1] == a1[v3]:
                    v2 += 1
                if v2 + 1 == len(a2):
                    yield (v3 - v2)
                    v2 = v1[v2]
        v2 = len(a1)
        v3 = [[0, 1], [v2 - 1, v2 - 1 - 1]]
        v4 = [1, 0]
        v4 = matrix_mult([v4], matrix_expo(v3, a3))[0]
        return reduce(lambda a, b: (a + b) % v1, (v4[int(i != 0)] for v5 in KMP(a1 + a1[:-1], a2)), 0)
