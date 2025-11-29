class C1(object):

    def equalToDescendants(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return 0
            v1 = dfs(a1.left, a2) + dfs(a1.right, a2)
            if a1.val == v1:
                a2[0] += 1
            return v1 + a1.val
        v1 = [0]
        dfs(a1, v1)
        return v1[0]
