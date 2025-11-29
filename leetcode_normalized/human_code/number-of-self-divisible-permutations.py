class C1(object):

    def selfDivisiblePermutationCount(self, a1):
        """
        """

        def popcount(a1):
            return bin(a1).count('1')

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        v1 = [[gcd(i + 1, j + 1) == 1 for v2 in range(a1)] for v3 in range(a1)]
        v4 = [0] * (1 << a1)
        v4[0] = 1
        for v5 in range(1 << a1):
            v3 = popcount(v5)
            for v2 in range(a1):
                if v5 & 1 << v2 == 0 and v1[v3][v2]:
                    v4[v5 | 1 << v2] += v4[v5]
        return v4[-1]
