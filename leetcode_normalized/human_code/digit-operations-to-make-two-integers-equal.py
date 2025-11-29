import heapq

class C1(object):

    def minOperations(self, a1, a2):
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

        def dijkstra(a1, a2):
            if spf[a1] == a1:
                return -1
            v1 = set()
            v2 = [(a1, a1)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v4 in v1:
                    continue
                v1.add(v4)
                if v4 == a2:
                    return v3
                v5 = 1
                while v5 <= v4:
                    v6 = v4 // v5
                    for v7 in (-1, 1):
                        if (1 if v6 <= 9 else 0) <= v6 % 10 + v7 <= 9 and spf[v4 + v7 * v5] != v4 + v7 * v5 and (v4 + v7 * v5 not in v1):
                            heapq.heappush(v2, (v3 + (v4 + v7 * v5), v4 + v7 * v5))
                    v5 *= 10
            return -1
        v1 = 1
        while v1 < max(a1, a2):
            v1 *= 10
        v2 = linear_sieve_of_eratosthenes(v1)
        return dijkstra(a1, a2)
