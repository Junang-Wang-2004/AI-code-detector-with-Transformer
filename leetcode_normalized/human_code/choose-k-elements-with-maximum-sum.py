import heapq

class C1(object):

    def findMaxSum(self, a1, a2, a3):
        """
        """
        v1 = [0] * len(a1)
        v2 = []
        v3 = list(range(len(a1)))
        v3.sort(key=lambda x: a1[x])
        v4 = v5 = 0
        for v6 in range(len(v3)):
            while a1[v3[v5]] < a1[v3[v6]]:
                v4 += a2[v3[v5]]
                heapq.heappush(v2, a2[v3[v5]])
                if len(v2) == a3 + 1:
                    v4 -= heapq.heappop(v2)
                v5 += 1
            v1[v3[v6]] = v4
        return v1
