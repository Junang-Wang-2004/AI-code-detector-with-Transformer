class C1(object):

    def diameterOfBinaryTree(self, a1):
        """
        """

        def dfs(a1):
            if not a1:
                return (0, 0)
            v1, v2 = dfs(a1.left)
            v3, v4 = dfs(a1.right)
            return (max(v1, v3, v2 + v4), 1 + max(v2, v4))
        return dfs(a1)[0]
