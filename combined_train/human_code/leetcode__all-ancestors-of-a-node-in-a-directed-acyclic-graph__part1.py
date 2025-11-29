class C1(object):

    def getAncestors(self, a1, a2):
        """
        """

        def iter_dfs(a1, a2, a3):
            v1 = [False] * len(a1)
            v2 = [a2]
            while v2:
                v3 = v2.pop()
                for v4 in reversed(a1[v3]):
                    if v1[v4]:
                        continue
                    v1[v4] = True
                    v2.append(v4)
                    a3[v4].append(a2)
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
        v5 = [[] for v2 in range(a1)]
        for v3 in range(a1):
            iter_dfs(v1, v3, v5)
        return v5
