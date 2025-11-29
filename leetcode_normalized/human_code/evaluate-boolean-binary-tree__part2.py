class C1(object):

    def evaluateTree(self, a1):
        """
        """
        v1 = float('inf')
        v2 = {2: lambda x, y: x or y, 3: lambda x, y: x and y}

        def dfs(a1):
            if a1.left == a1.right:
                return a1.val
            return v2[a1.val](dfs(a1.left), dfs(a1.right))
        return dfs(a1)
