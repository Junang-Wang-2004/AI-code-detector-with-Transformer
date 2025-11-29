class C1(object):

    def findPrimePairs(self, a1):
        """
        """

        def linear_sieve_of_eratosthenes(a1):
            v1 = []
            v2 = [-1] * (a1 + 1)
            for v3 in range(2, a1 + 1):
                if v2[v3] == -1:
                    v2[v3] = v3
                    v1.append(v3)
                for v4 in v1:
                    if v3 * v4 > a1 or v4 > v2[v3]:
                        break
                    v2[v3 * v4] = v4
            return v2
        v1 = linear_sieve_of_eratosthenes(a1)
        return [[i, a1 - i] for v2 in range(2, a1 // 2 + 1) if v1[v2] == v2 and v1[a1 - v2] == a1 - v2]
