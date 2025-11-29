import heapq

class C1(object):

    def maximumMinimumPath(self, a1):
        """
        """
        v1 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v2 = [(-a1[0][0], 0, 0)]
        v3 = set([(0, 0)])
        while v2:
            v4, v5, v6 = heapq.heappop(v2)
            if v5 == len(a1) - 1 and v6 == len(a1[0]) - 1:
                return -v4
            for v7 in v1:
                v8, v9 = (v5 + v7[0], v6 + v7[1])
                if 0 <= v8 < len(a1) and 0 <= v9 < len(a1[0]) and ((v8, v9) not in v3):
                    heapq.heappush(v2, (-min(-v4, a1[v8][v9]), v8, v9))
                    v3.add((v8, v9))
        return -1
