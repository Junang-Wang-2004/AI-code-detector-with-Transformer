class C1(object):

    def remainingMethods(self, a1, a2, a3):
        """
        """

        def bfs():
            v1 = [False] * a1
            v1[a2] = True
            v2 = [a2]
            while v2:
                v3 = []
                for v4 in v2:
                    for v5 in adj[v4]:
                        if v1[v5]:
                            continue
                        v1[v5] = True
                        v3.append(v5)
                v2 = v3
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a3:
            v1[v3].append(v4)
        v5 = bfs()
        return [v3 for v3 in range(a1) if not v5[v3]] if all((v5[v3] == v5[v4] for v3, v4 in a3)) else list(range(a1))
