import heapq
import bisect

class C1:

    def maxPoints(self, a1, a2):
        if not a1 or not a1[0]:
            return [0] * len(a2)
        v1, v2 = (len(a1), len(a1[0]))
        v3 = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        v4 = []
        heapq.heappush(v4, (a1[0][0], 0, 0))
        v5 = set([(0, 0)])
        v6 = 0
        v7 = []
        while v4:
            v8, v9, v10 = heapq.heappop(v4)
            v6 = max(v6, v8)
            v7.append(v6)
            for v11, v12 in v3:
                v13, v14 = (v9 + v11, v10 + v12)
                if 0 <= v13 < v1 and 0 <= v14 < v2 and ((v13, v14) not in v5):
                    v5.add((v13, v14))
                    heapq.heappush(v4, (a1[v13][v14], v13, v14))
        v7.sort()
        return [bisect.bisect_left(v7, q) for v15 in a2]
