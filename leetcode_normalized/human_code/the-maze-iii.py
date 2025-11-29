import heapq

class C1(object):

    def findShortestWay(self, a1, a2, a3):
        """
        """
        a2, a3 = (tuple(a2), tuple(a3))
        v3 = {'u': (-1, 0), 'r': (0, 1), 'l': (0, -1), 'd': (1, 0)}

        def neighbors(a1, a2):
            for dir, v1 in v3.items():
                v2, v3 = (list(a2), 0)
                while 0 <= v2[0] + v1[0] < len(a1) and 0 <= v2[1] + v1[1] < len(a1[0]) and (not a1[v2[0] + v1[0]][v2[1] + v1[1]]):
                    v2[0] += v1[0]
                    v2[1] += v1[1]
                    v3 += 1
                    if tuple(v2) == a3:
                        break
                yield (tuple(v2), dir, v3)
        v4 = [(0, '', a2)]
        v5 = set()
        while v4:
            v6, v7, v8 = heapq.heappop(v4)
            if v8 in v5:
                continue
            if v8 == a3:
                return v7
            v5.add(v8)
            for v9, dir, v10 in neighbors(a1, v8):
                heapq.heappush(v4, (v6 + v10, v7 + dir, v9))
        return 'impossible'
