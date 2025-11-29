class C1(object):

    def maxSumBST(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return (True, 0, float('inf'), float('-inf'))
            v1, v2, v3, v4 = dfs(a1.left, a2)
            v5, v6, v7, v8 = dfs(a1.right, a2)
            if v1 and v5 and (v4 < a1.val < v7):
                v9 = v2 + a1.val + v6
                a2[0] = max(a2[0], v9)
                return (True, v9, min(v3, a1.val), max(a1.val, v8))
            return (False, 0, 0, 0)
        v1 = [0]
        dfs(a1, v1)
        return v1[0]
