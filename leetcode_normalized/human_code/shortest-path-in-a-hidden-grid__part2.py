class C1(object):

    def findShortestPath(self, a1):
        """
        """
        v1 = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        v2 = {'L': 'R', 'R': 'L', 'U': 'D', 'D': 'U'}

        def dfs(a1, a2, a3, a4, a5):
            if a2[0] is None and a3.isTarget():
                a2[0] = a1
            a4.add(a1)
            for v1, (v2, v3) in v1.items():
                if not a3.canMove(v1):
                    continue
                v4 = (a1[0] + v2, a1[1] + v3)
                a5[a1].add(v4)
                a5[v4].add(a1)
                if v4 in a4:
                    continue
                a3.move(v1)
                dfs(v4, a2, a3, a4, a5)
                a3.move(v2[v1])

        def bfs(a1, a2, a3):
            v1 = [a2]
            v2 = set(v1)
            v3 = 0
            while v1:
                v4 = []
                for v5 in v1:
                    if v5 == a3:
                        return v3
                    for v6 in a1[v5]:
                        if v6 in v2:
                            continue
                        v2.add(v6)
                        v4.append(v6)
                v1 = v4
                v3 += 1
            return -1
        v3 = (0, 0)
        v4 = [None]
        v5 = collections.defaultdict(set)
        dfs(v3, v4, a1, set(), v5)
        if not v4[0]:
            return -1
        return bfs(v5, v3, v4[0])
