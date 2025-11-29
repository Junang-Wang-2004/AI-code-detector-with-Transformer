import collections

class C1(object):

    def idealArrays(self, a1, a2):
        """
        """
        v1 = 10 ** 9 + 7
        v2, v3, v4 = [[1] * 2 for v5 in range(3)]

        def nCr(a1, a2):
            while len(v3) <= a1:
                v2.append(v2[-1] * len(v3) % v1)
                v3.append(v3[v1 % len(v3)] * (v1 - v1 // len(v3)) % v1)
                v4.append(v4[-1] * v3[-1] % v1)
            return v2[a1] * v4[a1 - a2] % v1 * v4[a2] % v1

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

        def prime_factors(a1):
            v1 = collections.Counter()
            for v2 in primes:
                if v2 * v2 > a1:
                    break
                while a1 % v2 == 0:
                    v1[v2] += 1
                    a1 //= v2
            if a1 != 1:
                v1[a1] += 1
            return v1
        v6 = linear_sieve_of_eratosthenes(int(a2 ** 0.5))
        v7 = 0
        for v8 in range(1, a2 + 1):
            v9 = 1
            for v10 in prime_factors(v8).values():
                v9 = v9 * nCr(a1 + v10 - 1, v10) % v1
            v7 = (v7 + v9) % v1
        return v7
