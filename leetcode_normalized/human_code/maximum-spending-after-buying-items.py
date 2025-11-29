import heapq

class C1(object):

    def maxSpending(self, a1):
        """
        """
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(a1[i].pop(), i) for v4 in range(v1)]
        heapq.heapify(v3)
        v5 = 0
        for v6 in range(1, v1 * v2 + 1):
            v7, v4 = heapq.heappop(v3)
            v5 += v7 * v6
            if a1[v4]:
                heapq.heappush(v3, (a1[v4].pop(), v4))
        return v5
