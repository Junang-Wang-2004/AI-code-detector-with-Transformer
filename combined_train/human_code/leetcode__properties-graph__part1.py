class C1(object):

    def numberOfComponents(self, a1, a2):
        """
        """

        def bfs(a1):
            v1 = [a1]
            while v1:
                v2 = []
                for a1 in v1:
                    for v4 in adj[a1]:
                        if lookup[v4]:
                            continue
                        lookup[v4] = True
                        v2.append(v4)
                v1 = v2
        v1 = [set(p) for v2 in a1]
        v3 = [[] for v4 in range(len(a1))]
        for v5 in range(len(v1)):
            for v6 in range(v5 + 1, len(v1)):
                if sum((x in v1[v6] for v7 in v1[v5])) >= a2:
                    v3[v5].append(v6)
                    v3[v6].append(v5)
        v8 = [False] * len(a1)
        v9 = 0
        for v5 in range(len(a1)):
            if v8[v5]:
                continue
            bfs(v5)
            v9 += 1
        return v9
