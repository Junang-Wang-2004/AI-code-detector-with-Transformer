class C1(object):

    def canReachCorner(self, a1, a2, a3):
        """
        """

        def check(a1, a2, a3, a4, a5, a6):
            return (a1 - a4) ** 2 + (a2 - a5) ** 2 <= (a3 + a6) ** 2

        def bfs(a1, a2):
            v1 = [False] * len(adj)
            v1[a1] = True
            v2 = [a1]
            while v2:
                v3 = []
                for v4 in v2:
                    for v5 in adj[v4]:
                        if v1[v5]:
                            continue
                        v1[v5] = True
                        v3.append(v5)
                v2 = v3
            return v1[a2]
        v1 = [[] for v2 in range(len(a3) + 2)]
        for v3 in range(len(a3)):
            v4, v5, v6 = a3[v3]
            if v4 - v6 <= 0 or v5 + v6 >= a2:
                v1[v3].append(len(a3))
                v1[len(a3)].append(v3)
            if v4 + v6 >= a1 or v5 - v6 <= 0:
                v1[v3].append(len(a3) + 1)
                v1[len(a3) + 1].append(v3)
            for v7 in range(v3):
                v8, v9, v10 = a3[v7]
                if not check(v4, v5, v6, v8, v9, v10):
                    continue
                v1[v3].append(v7)
                v1[v7].append(v3)
        return not bfs(len(a3), len(a3) + 1)
