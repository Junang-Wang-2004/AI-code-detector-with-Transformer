class C1(object):

    def pseudoPalindromicPaths(self, a1):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return 0
            a2 ^= 1 << a1.val - 1
            return int(a1.left == a1.right and a2 & a2 - 1 == 0) + dfs(a1.left, a2) + dfs(a1.right, a2)
        return dfs(a1, 0)
