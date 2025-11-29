class C1(object):

    def averageOfSubtree(self, a1):
        """
        """

        def dfs(a1):
            if not a1:
                return [0] * 3
            v1 = dfs(a1.left)
            v2 = dfs(a1.right)
            return [v1[0] + v2[0] + a1.val, v1[1] + v2[1] + 1, v1[2] + v2[2] + int((v1[0] + v2[0] + a1.val) // (v1[1] + v2[1] + 1) == a1.val)]
        return dfs(a1)[2]
