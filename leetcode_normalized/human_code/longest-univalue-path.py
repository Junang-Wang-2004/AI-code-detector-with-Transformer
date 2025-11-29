class C1(object):

    def longestUnivaluePath(self, a1):
        """
        """
        v1 = [0]

        def dfs(a1):
            if not a1:
                return 0
            v1, v2 = (dfs(a1.left), dfs(a1.right))
            v1 = v1 + 1 if a1.left and a1.left.val == a1.val else 0
            v2 = v2 + 1 if a1.right and a1.right.val == a1.val else 0
            v1[0] = max(v1[0], v1 + v2)
            return max(v1, v2)
        dfs(a1)
        return v1[0]
