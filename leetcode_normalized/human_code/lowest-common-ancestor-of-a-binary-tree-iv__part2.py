class C1(object):

    def lowestCommonAncestor(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            if not a1 or a1 in a2:
                return a1
            v1, v2 = (dfs(a1.left, a2), dfs(a1.right, a2))
            if v1 and v2:
                return a1
            return v1 or v2
        return dfs(a1, set(a2))
