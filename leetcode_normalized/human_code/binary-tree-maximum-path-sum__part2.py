class C1(object):

    def maxPathSum(self, a1):

        def dfs(a1):
            if not a1:
                return (float('-inf'), 0)
            v1, v2 = dfs(a1.left)
            v3, v4 = dfs(a1.right)
            return (max(v1, v3, a1.val + max(v2, 0) + max(v4, 0)), a1.val + max(v2, v4, 0))
        return dfs(a1)[0]
