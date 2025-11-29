import heapq

class C1(object):

    def findCrossingTime(self, a1, a2, a3):
        """
        """
        v1, v2, v3, v4 = ([(-(a3[i][0] + a3[i][2]), -i) for v5 in range(a2)], [], [], [])
        heapq.heapify(v1)
        v6 = 0
        while a1:
            while v4 and v4[0][0] <= v6:
                v7, v5 = heapq.heappop(v4)
                heapq.heappush(v1, (-(a3[v5][0] + a3[v5][2]), -v5))
            while v2 and v2[0][0] <= v6:
                v7, v5 = heapq.heappop(v2)
                heapq.heappush(v3, (-(a3[v5][0] + a3[v5][2]), -v5))
            if v3:
                v7, v5 = heapq.heappop(v3)
                v5 = -v5
                v6 += a3[v5][2]
                heapq.heappush(v4, (v6 + a3[v5][3], v5))
                a1 -= 1
            elif v1 and a1 - len(v2):
                v7, v5 = heapq.heappop(v1)
                v5 = -v5
                v6 += a3[v5][0]
                heapq.heappush(v2, (v6 + a3[v5][1], v5))
            else:
                v6 = min(v4[0][0] if v4 else float('inf'), v2[0][0] if v2 else float('inf'))
        return v6
