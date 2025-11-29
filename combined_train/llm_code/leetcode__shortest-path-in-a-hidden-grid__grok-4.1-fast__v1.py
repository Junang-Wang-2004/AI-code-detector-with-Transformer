import collections

class C1(object):

    def findShortestPath(self, a1):
        v1 = [(-1, 0, 'U'), (1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R')]
        v2 = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

        def traverse(a1, a2, a3, a4, a5):
            if a2[0] is None and a3.isTarget():
                a2[0] = a1
            a4.add(a1)
            for v1, v2, v3 in v1:
                v4 = (a1[0] + v1, a1[1] + v2)
                if not a3.canMove(v3):
                    continue
                a5[a1].add(v4)
                a5[v4].add(a1)
                if v4 in a4:
                    continue
                a3.move(v3)
                traverse(v4, a2, a3, a4, a5)
                a3.move(v2[v3])

        def shortest_route(a1, a2, a3):
            from collections import deque
            if a2 == a3:
                return 0
            v1 = set([a2])
            v2 = deque([a2])
            v3 = 0
            while v2:
                v3 += 1
                v4 = len(v2)
                for v5 in range(v4):
                    v6 = v2.popleft()
                    for v7 in a1[v6]:
                        if v7 in v1:
                            continue
                        if v7 == a3:
                            return v3
                        v1.add(v7)
                        v2.append(v7)
            return -1
        v3 = collections.defaultdict(set)
        v4 = [None]
        v5 = (0, 0)
        traverse(v5, v4, a1, set(), v3)
        if v4[0] is None:
            return -1
        return shortest_route(v3, v5, v4[0])
