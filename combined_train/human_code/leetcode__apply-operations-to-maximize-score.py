import heapq

class C1(object):

    def maximumScore(self, a1, a2):
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
            return v1
        v2 = {}

        def count_of_distinct_prime_factors(a1):
            v1 = a1
            if v1 not in v2:
                v2 = 0
                for v3 in primes:
                    if v3 * v3 > a1:
                        break
                    if a1 % v3 != 0:
                        continue
                    v2 += 1
                    while a1 % v3 == 0:
                        a1 //= v3
                if a1 != 1:
                    v2 += 1
                v2[v1] = v2
            return v2[v1]
        v3 = linear_sieve_of_eratosthenes(int(max(a1) ** 0.5))
        v4 = [count_of_distinct_prime_factors(x) for v5 in a1]
        v6 = [-1] * len(v4)
        v7 = [-1]
        for v8 in range(len(v4)):
            while v7[-1] != -1 and v4[v7[-1]] < v4[v8]:
                v7.pop()
            v6[v8] = v7[-1]
            v7.append(v8)
        v9 = [-1] * len(v4)
        v7 = [len(v4)]
        for v8 in reversed(range(len(v4))):
            while v7[-1] != len(v4) and v4[v7[-1]] <= v4[v8]:
                v7.pop()
            v9[v8] = v7[-1]
            v7.append(v8)
        v10 = 1
        v11 = [(-v5, v8) for v8, v5 in enumerate(a1)]
        heapq.heapify(v11)
        while v11:
            v12, v8 = heapq.heappop(v11)
            v13 = min((v8 - v6[v8]) * (v9[v8] - v8), a2)
            v10 = v10 * pow(a1[v8], v13, v1) % v1
            a2 -= v13
            if not a2:
                break
        return v10
