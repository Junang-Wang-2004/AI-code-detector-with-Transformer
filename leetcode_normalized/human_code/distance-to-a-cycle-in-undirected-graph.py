class C1(object):

    def distanceToCycle(self, a1, a2):
        """
        """

        def cycle(a1, a2, a3):
            v1 = [a1[a2], a2]
            while a3 != a1[a2]:
                v1.append(a3)
                a3 = a1[a3]
            return v1

        def iter_dfs(a1):
            v1 = [0]
            v2 = [-2] * len(a1)
            v2[0] = -1
            while v1:
                v3 = v1.pop()
                for v4 in reversed(a1[v3]):
                    if v2[v4] != -2:
                        if v4 == v2[v3]:
                            continue
                        return cycle(v2, v4, v3)
                    v2[v4] = v3
                    v1.append(v4)

        def bfs(a1, a2):
            v1 = [-1] * a1
            for v2 in a2:
                v1[v2] = 0
            v3 = 1
            while a2:
                v4 = []
                for v5 in a2:
                    for v6 in a1[v5]:
                        if v1[v6] != -1:
                            continue
                        v1[v6] = v3
                        v4.append(v6)
                a2 = v4
                v3 += 1
            return v1
        v1 = [[] for v2 in range(a1)]
        for v3, v4 in a2:
            v1[v3].append(v4)
            v1[v4].append(v3)
        return bfs(v1, iter_dfs(v1))
