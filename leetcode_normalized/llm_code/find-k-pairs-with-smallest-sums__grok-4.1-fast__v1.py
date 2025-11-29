import heapq

class C1(object):

    def kSmallestPairs(self, a1, a2, a3):
        v1 = []
        if a3 <= 0 or not a1 or (not a2):
            return v1
        v2 = []
        v3 = set()
        heapq.heappush(v2, (a1[0] + a2[0], 0, 0))
        v3.add((0, 0))
        while v2 and len(v1) < a3:
            v4, v5, v6 = heapq.heappop(v2)
            v1.append([a1[v5], a2[v6]])
            for v7, v8 in [(1, 0), (0, 1)]:
                v9, v10 = (v5 + v7, v6 + v8)
                if v9 < len(a1) and v10 < len(a2) and ((v9, v10) not in v3):
                    v3.add((v9, v10))
                    heapq.heappush(v2, (a1[v9] + a2[v10], v9, v10))
        return v1
