import heapq

class C1:

    def resultsArray(self, a1, a2):
        v1 = []
        v2 = []
        for v3 in a1:
            v4 = abs(v3[0]) + abs(v3[1])
            if len(v1) < a2:
                heapq.heappush(v1, -v4)
            elif v4 < -v1[0]:
                heapq.heappop(v1)
                heapq.heappush(v1, -v4)
            if len(v1) == a2:
                v2.append(-v1[0])
            else:
                v2.append(-1)
        return v2
