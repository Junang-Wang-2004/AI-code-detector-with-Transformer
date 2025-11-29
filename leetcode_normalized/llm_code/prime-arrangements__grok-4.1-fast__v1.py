class C1(object):

    def numPrimeArrangements(self, a1):
        v1 = 10 ** 9 + 7
        v2 = [1] * (a1 + 1)
        for v3 in range(2, a1 + 1):
            v2[v3] = v2[v3 - 1] * v3 % v1

        def count_primes(a1):
            if a1 < 2:
                return 0
            v1 = [True] * (a1 + 1)
            v1[0] = v1[1] = False
            for v2 in range(2, int(a1 ** 0.5) + 1):
                if v1[v2]:
                    for v3 in range(v2 * v2, a1 + 1, v2):
                        v1[v3] = False
            return sum(v1)
        v4 = count_primes(a1)
        return v2[v4] * v2[a1 - v4] % v1
