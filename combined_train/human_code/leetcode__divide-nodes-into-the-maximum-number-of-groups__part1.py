class C1(object):

    def magnificentSets(self, a1, a2):
        """
        """

        def iter_dfs(a1):
            v1 = []
            v2 = [a1]
            lookup[a1] = 0
            while v2:
                a1 = v2.pop()
                v1.append(a1)
                for v4 in adj[a1]:
                    if lookup[v4] != -1:
                        if lookup[v4] == lookup[a1]:
                            return []
                        continue
                    lookup[v4] = lookup[a1] ^ 1
                    v2.append(v4)
            return v1

        def bfs(a1):
            v1 = 0
            v2 = [False] * a1
            v3 = [a1]
            v2[a1] = True
            while v3:
                v4 = []
                for a1 in v3:
                    for v6 in adj[a1]:
                        if v2[v6]:
                            continue
                        v2[v6] = True
                        v4.append(v6)
                v3 = v4
                v1 += 1
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3 - 1].append(v4 - 1)
            v1[v4 - 1].append(v3 - 1)
        v5 = 0
        v6 = [-1] * a1
        for v3 in range(a1):
            if v6[v3] != -1:
                continue
            v7 = iter_dfs(v3)
            if not v7:
                return -1
            v5 += max((bfs(v3) for v3 in v7))
        return v5
