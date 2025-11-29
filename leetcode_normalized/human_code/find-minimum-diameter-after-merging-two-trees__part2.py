class C1(object):

    def minimumDiameterAfterMerge(self, a1, a2):
        """
        """

        def ceil_divide(a1, a2):
            return (a1 + a2 - 1) // 2

        def tree_diameter(a1):

            def dfs(a1, a2):
                v1 = 0
                for v2 in adj[a1]:
                    if v2 == a2:
                        continue
                    v3 = dfs(v2, a1)
                    result[0] = max(result[0], v1 + (v3 + 1))
                    v1 = max(v1, v3 + 1)
                return v1
            v1 = [[] for v2 in range(len(a1) + 1)]
            for v3, v4 in a1:
                v1[v3].append(v4)
                v1[v4].append(v3)
            v5 = [0]
            dfs(0, -1)
            return v5[0]
        v1 = tree_diameter(a1)
        v2 = tree_diameter(a2)
        return max(ceil_divide(v1, 2) + 1 + ceil_divide(v2, 2), v1, v2)
