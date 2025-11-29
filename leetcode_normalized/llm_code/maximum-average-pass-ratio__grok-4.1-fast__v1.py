import heapq

class C1:

    def maxAverageRatio(self, a1, a2):
        v1 = len(a1)
        v2 = [list(mem) for v3 in a1]

        def marg(a1, a2):
            return (a1 + 1) / (a2 + 1) - a1 / a2
        v4 = []
        for v5 in range(v1):
            v6, v7 = v2[v5]
            heapq.heappush(v4, (-marg(v6, v7), v5))
        for v8 in range(a2):
            v8, v9 = heapq.heappop(v4)
            v6, v7 = v2[v9]
            v2[v9][0] += 1
            v2[v9][1] += 1
            heapq.heappush(v4, (-marg(v6, v7), v9))
        return sum((v6 / v7 for v6, v7 in v2)) / v1
