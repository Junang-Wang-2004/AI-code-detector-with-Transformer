class C1(object):

    def loudAndRich(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3, a4):
            if a4[a3] is None:
                a4[a3] = a3
                for v1 in a1[a3]:
                    v2 = dfs(a1, a2, v1, a4)
                    if a2[v2] < a2[a4[a3]]:
                        a4[a3] = v2
            return a4[a3]
        v1 = [[] for v2 in range(len(a2))]
        for v3, v4 in a1:
            v1[v4].append(v3)
        v5 = [None] * len(a2)
        return [dfs(v1, a2, x, v5) for v6 in range(len(a2))]
