v1 = [[-1] * (5 + 1) for v2 in range(5 + 1)]

class C1(object):

    def hasSameDigits(self, a1):
        """
        """

        def nCr(a1, a2):
            if a1 - a2 < a2:
                a2 = a1 - a2
            if v1[a1][a2] == -1:
                v2 = 1
                for v3 in range(1, a2 + 1):
                    v2 *= a1 - v3 + 1
                    v2 //= v3
                v1[a1][a2] = v2
            return v1[a1][a2]

        def nCr_mod(a1, a2, a3):
            v1 = 1
            while a1 > 0 or a2 > 0:
                a1, v3 = divmod(a1, a3)
                a2, v5 = divmod(a2, a3)
                if v3 < v5:
                    return 0
                v1 = v1 * nCr(v3, v5) % a3
            return v1

        def nC10(a1, a2):
            return lookup[nCr_mod(a1, a2, 2)][nCr_mod(a1, a2, 5)]
        v1 = [[0] * 5 for v2 in range(2)]
        for v2 in range(10):
            v1[v2 % 2][v2 % 5] = v2
        v3 = 0
        for v2 in range(len(a1) - 1):
            v3 = (v3 + nC10(len(a1) - 2, v2) * (ord(a1[v2]) - ord(a1[v2 + 1]))) % 10
        return v3 == 0
