import collections
import heapq

class C1(object):

    def canMove(self, a1):
        pass

    def move(self, a1):
        pass

    def isTarget(self):
        pass

class C2(object):

    def findShortestPath(self, a1):
        v1 = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        v2 = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

        def explore(a1, a2, a3, a4, a5):
            if a2[0] is None and a3.isTarget():
                a2[0] = a1
            a4.add(a1)
            for v1, (v2, v3) in v1.items():
                if not a3.canMove(v1):
                    continue
                v4 = (a1[0] + v2, a1[1] + v3)
                if v4 in a5[a1]:
                    continue
                v5 = a3.move(v1)
                a5[a1][v4] = v5
                if v4 not in a4:
                    explore(v4, a2, a3, a4, a5)
                v6 = a3.move(v2[v1])
                a5[v4][a1] = v6

        def min_distance(a1, a2, a3):
            v1 = {a2: 0}
            v2 = [(0, a2)]
            while v2:
                v3, v4 = heapq.heappop(v2)
                if v3 > v1.get(v4, float('inf')):
                    continue
                for v5, v6 in a1[v4].items():
                    v7 = v3 + v6
                    if v7 < v1.get(v5, float('inf')):
                        v1[v5] = v7
                        heapq.heappush(v2, (v7, v5))
            return v1.get(a3, -1)
        v3 = (0, 0)
        v4 = [None]
        v5 = collections.defaultdict(dict)
        v6 = set()
        explore(v3, v4, a1, v6, v5)
        if v4[0] is None:
            return -1
        return min_distance(v5, v3, v4[0])
