class C1(object):

    def getAncestors(self, a1, a2):
        """
        """

        def bfs(a1, a2, a3):
            v1 = [False] * len(a1)
            v2 = [a2]
            v1[a2] = True
            while v2:
                v3 = []
                for v4 in v2:
                    for v5 in a1[v4]:
                        if v1[v5]:
                            continue
                        v1[v5] = True
                        v3.append(v5)
                        a3[a2].append(v5)
                v2 = v3
            a3[a2].sort()
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v4].append(v3)
        v5 = [[] for v2 in range(a1)]
        for v3 in range(a1):
            bfs(v1, v3, v5)
        return v5
