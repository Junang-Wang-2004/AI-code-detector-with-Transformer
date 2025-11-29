class C1(object):

    def longestConsecutive(self, a1):
        v1 = [0]

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
            v6 = 1
            if a1.left and a1.left.val == a1.val - 1:
                v6 = max(v6, v2 + 1)
            if a1.right and a1.right.val == a1.val - 1:
                v6 = max(v6, v4 + 1)
            v1[0] = max(v1[0], v5 + v6 - 1)
            return (v5, v6)
        dfs(a1)
        return v1[0]
