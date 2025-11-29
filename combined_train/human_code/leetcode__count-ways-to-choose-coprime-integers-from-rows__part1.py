import collections
from functools import reduce

class C1(object):

    def countCoprime(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

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

        def mobius(a1):
            v1 = [0] * len(a1)
            for v2 in range(1, len(v1)):
                v1[v2] = 1 if v2 == 1 else 0 if a1[v2 // a1[v2]] == a1[v2] else -v1[v2 // a1[v2]]
            return v1
        v2 = max((max(row) for v3 in a1))
        v4 = mobius(linear_sieve_of_eratosthenes(v2))
        v5 = [1] * (v2 + 1)
        for v3 in a1:
            v6 = collections.defaultdict(int)
            for v7 in v3:
                v6[v7] += 1
            for v8 in range(1, v2 + 1):
                v5[v8] = v5[v8] * reduce(lambda accu, x: (accu + v7) % v1, (v6[j] for v9 in range(v8, v2 + 1, v8)), 0) % v1
        return reduce(lambda accu, x: (accu + v7) % v1, (v5[v8] * v4[v8] for v8 in range(1, v2 + 1)), 0)
