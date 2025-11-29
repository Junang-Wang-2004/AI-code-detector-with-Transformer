import heapq

class C1(object):

    def shortestDistance(self, a1, a2, a3):
        """
        """
        a2, a3 = (tuple(a2), tuple(a3))

        def neighbors(a1, a2):
            for dir in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                v1, v2 = (list(a2), 0)
                while 0 <= v1[0] + dir[0] < len(a1) and 0 <= v1[1] + dir[1] < len(a1[0]) and (not a1[v1[0] + dir[0]][v1[1] + dir[1]]):
                    v1[0] += dir[0]
                    v1[1] += dir[1]
                    v2 += 1
                yield (v2, tuple(v1))
        v3 = [(0, a2)]
        v4 = set()
        while v3:
            v5, v6 = heapq.heappop(v3)
            if v6 in v4:
                continue
            if v6 == a3:
                return v5
            v4.add(v6)
            for v7, v8 in neighbors(a1, v6):
                heapq.heappush(v3, (v5 + v7, v8))
        return -1
