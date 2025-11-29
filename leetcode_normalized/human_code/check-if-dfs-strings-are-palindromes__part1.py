class C1(object):

    def findAnswer(self, a1, a2):
        """
        """

        def manacher(a1):
            a1 = '^#' + '#'.join(a1) + '#$'
            v2 = [0] * len(a1)
            v3, v4 = (0, 0)
            for v5 in range(1, len(a1) - 1):
                v6 = 2 * v3 - v5
                if v4 > v5:
                    v2[v5] = min(v4 - v5, v2[v6])
                while a1[v5 + 1 + v2[v5]] == a1[v5 - 1 - v2[v5]]:
                    v2[v5] += 1
                if v5 + v2[v5] > v4:
                    v3, v4 = (v5, v5 + v2[v5])
            return v2

        def iter_dfs(a1):
            v1 = 0
            v2 = []
            v3 = [None] * len(adj)
            v4 = [(1, (0,))]
            while v4:
                v5, v6 = v4.pop()
                if v5 == 1:
                    a1 = v6[0]
                    v4.append((2, (a1, v1)))
                    for v8 in reversed(adj[a1]):
                        v4.append((1, (v8,)))
                elif v5 == 2:
                    a1, v9 = v6
                    v2.append(a2[a1])
                    v3[a1] = (v9, v1)
                    v1 += 1
            return (v2, v3)
        v1 = [[] for v2 in range(len(a1))]
        for v3 in range(1, len(a1)):
            v1[a1[v3]].append(v3)
        v4, v5 = iter_dfs(0)
        v6 = manacher(v4)
        return [v6[(2 * (left + 1) + 2 * (right + 1)) // 2] >= right - left + 1 for v7, v8 in v5]
