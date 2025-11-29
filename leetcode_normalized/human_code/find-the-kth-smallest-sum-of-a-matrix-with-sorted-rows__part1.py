import heapq

class C1(object):

    def kthSmallest(self, a1, a2):
        """
        """

        def kSmallestPairs(a1, a2, a3):
            v1, v2 = ([], [])
            for v3 in range(min(len(a1), a3)):
                heapq.heappush(v2, (a1[v3] + a2[0], 0))
                v3 += 1
            while len(v1) != a3 and v2:
                v4, v3 = heapq.heappop(v2)
                v1.append(v4)
                if v3 + 1 == len(a2):
                    continue
                heapq.heappush(v2, (v4 - a2[v3] + a2[v3 + 1], v3 + 1))
            return v1
        v1 = a1[0]
        for v2 in range(1, len(a1)):
            v1 = kSmallestPairs(v1, a1[v2], a2)
        return v1[a2 - 1]
