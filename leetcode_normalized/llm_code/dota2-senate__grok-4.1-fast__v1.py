import heapq

class C1:

    def predictPartyVictory(self, a1):
        v1 = len(a1)
        v2 = []
        v3 = []
        for v4 in range(v1):
            if a1[v4] == 'R':
                heapq.heappush(v2, v4)
            else:
                heapq.heappush(v3, v4)
        while v2 and v3:
            v5 = heapq.heappop(v2)
            v6 = heapq.heappop(v3)
            if v5 < v6:
                heapq.heappush(v2, v5 + v1)
            else:
                heapq.heappush(v3, v6 + v1)
        return 'Radiant' if v2 else 'Dire'
