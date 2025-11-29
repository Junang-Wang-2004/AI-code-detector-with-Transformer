class C1(object):

    def componentValue(self, a1, a2):
        """
        """

        def iter_dfs(a1):
            v1 = a1[:]
            v2 = [(1, (0, -1))]
            while v2:
                v3, (v4, v5) = v2.pop()
                if v3 == 1:
                    v2.append((2, (v4, v5)))
                    for v6 in adj[v4]:
                        if v6 == v5:
                            continue
                        v2.append((1, (v6, v4)))
                elif v3 == 2:
                    for v6 in adj[v4]:
                        if v6 == v5:
                            continue
                        v1[v4] += v1[v6]
                    if v1[v4] == a1:
                        v1[v4] = 0
            return v1[0]
        v1 = 0
        v2 = [[] for v3 in range(len(a1))]
        for v4, v5 in a2:
            v2[v4].append(v5)
            v2[v5].append(v4)
        v6 = sum(a1)
        for v7 in reversed(range(2, len(a1) + 1)):
            if v6 % v7 == 0 and iter_dfs(v6 // v7) == 0:
                return v7 - 1
        return 0
