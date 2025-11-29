class C1(object):

    def widthOfBinaryTree(self, a1):
        """
        """

        def dfs(a1, a2, a3, a4):
            if not a1:
                return 0
            if a3 >= len(a4):
                a4.append(a2)
            return max(a2 - a4[a3] + 1, dfs(a1.left, a2 * 2, a3 + 1, a4), dfs(a1.right, a2 * 2 + 1, a3 + 1, a4))
        v1 = []
        return dfs(a1, 1, 0, v1)
