class C1:

    def maxPathSum(self, a1):
        v1 = float('-inf')

        def path(a1):
            nonlocal best
            if not a1:
                return 0
            v1 = max(path(a1.left), 0)
            v2 = max(path(a1.right), 0)
            v3 = max(v3, a1.val + v1 + v2)
            return a1.val + max(v1, v2)
        path(a1)
        return v1
