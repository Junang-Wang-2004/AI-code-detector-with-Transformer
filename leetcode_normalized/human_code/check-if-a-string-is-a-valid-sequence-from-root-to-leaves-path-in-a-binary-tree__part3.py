class C1(object):

    def isValidSequence(self, a1, a2):
        """
        """

        def dfs(a1, a2, a3):
            if not a1 or a3 == len(a2) or a1.val != a2[a3]:
                return False
            if a3 + 1 == len(a2) and a1.left == a1.right:
                return True
            return dfs(a1.left, a2, a3 + 1) or dfs(a1.right, a2, a3 + 1)
        return dfs(a1, a2, 0)
