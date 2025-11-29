class C1(object):

    def numberOfWays(self, a1, a2, a3, a4, a5):
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
        v2 = [[0, a2 - 1, a1 - 1, 0], [1, a2 - 2, 0, a1 - 1], [1, 0, a1 - 2, a2 - 1], [0, 1, 1, a1 - 2 + (a2 - 2)]]
        v3 = [0] * 4
        if a4 == a5:
            v3[0] = 1
        elif a4[0] == a5[0]:
            v3[1] = 1
        elif a4[1] == a5[1]:
            v3[2] = 1
        else:
            v3[3] = 1
        v3 = matrix_mult([v3], matrix_expo(v2, a3))[0]
        return v3[0]
