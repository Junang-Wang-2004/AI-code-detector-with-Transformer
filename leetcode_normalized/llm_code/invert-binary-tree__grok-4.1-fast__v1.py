class C1:

    def invertTree(self, a1):

        def dfs(a1):
            if a1:
                dfs(a1.left)
                dfs(a1.right)
                a1.left, a1.right = (a1.right, a1.left)
        dfs(a1)
        return a1
