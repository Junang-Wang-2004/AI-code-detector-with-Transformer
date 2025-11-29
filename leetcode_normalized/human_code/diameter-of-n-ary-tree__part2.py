class C1(object):

    def diameter(self, a1):
        """
        """

        def dfs(a1):
            v1, v2 = (0, 0)
            for v3 in a1.children:
                v4, v5 = dfs(v3)
                v1 = max(v1, v4, v2 + v5 + 1)
                v2 = max(v2, v5 + 1)
            return (v1, v2)
        return dfs(a1)[0]
