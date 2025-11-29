import collections

class C1(object):

    def squareFreeSubsets(self, a1):
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
            return v1
        v1 = max(a1)
        v2 = linear_sieve_of_eratosthenes(v1)
        v3 = [0] * (v1 + 1)
        for v4 in range(v1 + 1):
            v5 = v4
            for v6, v7 in enumerate(v2):
                if v5 % v7:
                    continue
                if v5 % v7 ** 2 == 0:
                    v3[v4] = 0
                    break
                v3[v4] |= 1 << v6
                v5 //= v7
        v8 = 10 ** 9 + 7
        v9 = collections.Counter(a1)
        v10 = [v4 for v4 in v9.keys() if v4 != 1]
        v11 = [1] * (1 << len(v2))
        for v4 in v10:
            if not v3[v4]:
                continue
            for v12 in reversed(range(len(v11))):
                if v3[v4] & v12 == 0:
                    v11[v12 | v3[v4]] = (v11[v12 | v3[v4]] + v9[v4] * v11[v12]) % v8
        return (v11[-1] * pow(2, v9[1], v8) - 1) % v8 if 1 in v9 else (v11[-1] - 1) % v8
