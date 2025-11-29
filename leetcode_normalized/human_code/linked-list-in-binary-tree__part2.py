class C1(object):

    def isSubPath(self, a1, a2):
        """
        """

        def dfs(a1, a2):
            if not a1:
                return True
            if not a2:
                return False
            return a2.val == a1.val and (dfs(a1.__next__, a2.left) or dfs(a1.__next__, a2.right))
        if not a1:
            return True
        if not a2:
            return False
        return dfs(a1, a2) or self.isSubPath(a1, a2.left) or self.isSubPath(a1, a2.right)
