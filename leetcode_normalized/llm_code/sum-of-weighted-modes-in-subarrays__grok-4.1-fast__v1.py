import collections
import heapq

class C1:

    def modeWeight(self, a1, a2):
        v1 = collections.Counter()
        v2 = []
        v3 = 0
        v4 = 0
        for v5 in range(len(a1)):
            v6 = a1[v5]
            v1[v6] += 1
            heapq.heappush(v2, (-v1[v6], v6))
            while v5 - v4 + 1 > a2:
                v7 = a1[v4]
                v1[v7] -= 1
                v4 += 1
            if v5 - v4 + 1 == a2:
                while v2 and v1[v2[0][1]] != -v2[0][0]:
                    heapq.heappop(v2)
                v8 = -v2[0][0]
                v9 = v2[0][1]
                v3 += v8 * v9
        return v3
