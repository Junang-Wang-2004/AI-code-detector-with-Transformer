class C1(object):

    def longestConsecutive(self, a1):

        def dfs(a1):
            if not a1:
                return (0, 0)
            v1, v2 = dfs(a1.left)
            v3, v4 = dfs(a1.right)
            v5 = 1
            if a1.left and a1.left.val == a1.val + 1:
                v5 = max(v5, v1 + 1)
            if a1.right and a1.right.val == a1.val + 1:
                v5 = max(v5, v3 + 1)
            v6 = max(v5, v2, v4)
            return (v5, v6)
        if not a1:
            return 0
        v1, v2 = dfs(a1)
        return v2
