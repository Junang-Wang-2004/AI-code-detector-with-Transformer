class C1(object):

    def countOfArrays(self, a1, a2, a3):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3 = (a2 // 2, (a2 + 1) // 2)
        v4 = [[0] * (a3 + 1) for v5 in range(2)]
        v4[0][0], v4[1][0] = (v2, v3)
        for v5 in range(a1 - 1):
            for v6 in reversed(range(a3 + 1)):
                v4[0][v6], v4[1][v6] = (((v4[0][v6 - 1] if v6 - 1 >= 0 else 0) + v4[1][v6]) * v2 % v1, (v4[0][v6] + v4[1][v6]) * v3 % v1)
        return (v4[0][a3] + v4[1][a3]) % v1
