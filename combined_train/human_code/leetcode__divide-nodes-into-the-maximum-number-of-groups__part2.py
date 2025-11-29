class C1(object):

    def magnificentSets(self, a1, a2):
        """
        """

        def bfs(a1):
            v1 = []
            v2 = [a1]
            lookup[a1] = True
            while v2:
                v3 = []
                for a1 in v2:
                    v1.append(a1)
                    for v5 in adj[a1]:
                        if lookup[v5]:
                            continue
                        lookup[v5] = True
                        v3.append(v5)
                v2 = v3
            return v1

        def bfs2(a1):
            v1 = 0
            v2 = [False] * a1
            v3 = {a1}
            v2[a1] = True
            while v3:
                v4 = set()
                for a1 in v3:
                    for v6 in adj[a1]:
                        if v6 in v3:
                            return 0
                        if v2[v6]:
                            continue
                        v2[v6] = True
                        v4.add(v6)
                v3 = v4
                v1 += 1
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v1[v4 - 1].append(v3 - 1)
        v5 = 0
        v6 = [0] * a1
        for v3 in range(a1):
            if v6[v3]:
                continue
            v7 = bfs(v3)
            v8 = 0
            for v3 in v7:
                v9 = bfs2(v3)
                if v9 == 0:
                    return -1
                v8 = max(v8, v9)
            v5 += v8
        return v5
