import heapq

class C1(object):

    def mostBooked(self, a1, a2):
        """
        """
        a2.sort()
        v1, v2 = (list(range(a1)), [])
        v3 = [0] * a1
        for v4, v5 in a2:
            while v2 and v2[0][0] <= v4:
                v6, v7 = heapq.heappop(v2)
                heapq.heappush(v1, v7)
            if v1:
                v7 = heapq.heappop(v1)
                heapq.heappush(v2, (v5, v7))
            else:
                v8, v7 = heapq.heappop(v2)
                heapq.heappush(v2, (v8 + (v5 - v4), v7))
            v3[v7] += 1
        return max(range(a1), key=lambda x: v3[x])
