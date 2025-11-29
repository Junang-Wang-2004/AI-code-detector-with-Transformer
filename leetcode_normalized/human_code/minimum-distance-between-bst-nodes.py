class C1(object):

    def minDiffInBST(self, a1):
        """
        """

        def dfs(a1):
            if not a1:
                return
            dfs(a1.left)
            self.result = min(self.result, a1.val - self.prev)
            self.prev = a1.val
            dfs(a1.right)
        self.prev = float('-inf')
        self.result = float('inf')
        dfs(a1)
        return self.result
