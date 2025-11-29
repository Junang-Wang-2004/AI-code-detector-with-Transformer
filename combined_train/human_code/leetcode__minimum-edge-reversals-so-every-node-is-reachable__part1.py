class C1(object):

    def minEdgeReversals(self, a1, a2):
        """
        """

        def iter_dfs1():
            v1 = 0
            v2 = [(0, -1)]
            while v2:
                v3, v4 = v2.pop()
                for v5 in adj[v3].keys():
                    if v5 == v4:
                        continue
                    v1 += adj[v3][v5]
                    v2.append((v5, v3))
            return v1

        def iter_dfs2(a1):
            v1 = [-1] * a1
            v2 = [(0, a1)]
            while v2:
                v3, a1 = v2.pop()
                v1[v3] = a1
                for v5 in adj[v3].keys():
                    if v1[v5] == -1:
                        v2.append((v5, a1 - adj[v3][v5] + adj[v5][v3]))
            return v1
        v1 = collections.defaultdict(dict)
        for v2, v3 in a2:
            v1[v2][v3] = 0
            v1[v3][v2] = 1
        return iter_dfs2(iter_dfs1())
