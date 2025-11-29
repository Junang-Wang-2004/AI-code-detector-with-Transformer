import heapq

class C1(object):

    def mostBooked(self, a1, a2):
        """
        """
        a2.sort()
        v1 = [(a2[0][0], i) for v2 in range(a1)]
        v3 = [0] * a1
        for v4, v5 in a2:
            while v1 and v1[0][0] < v4:
                v6, v2 = heapq.heappop(v1)
                heapq.heappush(v1, (v4, v2))
            v7, v2 = heapq.heappop(v1)
            heapq.heappush(v1, (v7 + (v5 - v4), v2))
            v3[v2] += 1
        return max(range(a1), key=lambda x: v3[x])
