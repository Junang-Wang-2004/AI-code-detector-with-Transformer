class C1(object):

    def goodNodes(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return 0
            a2 = max(a2, a1.val)
            return int(a2 <= a1.val) + dfs(a1.left, a2) + dfs(a1.right, a2)
        return dfs(a1, a1.val)
