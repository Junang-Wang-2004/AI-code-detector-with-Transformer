class C1(object):

    def pruneTree(self, a1):
        """
        """
        if not a1:
            return None
        a1.left = self.pruneTree(a1.left)
        a1.right = self.pruneTree(a1.right)
        if not a1.left and (not a1.right) and (a1.val == 0):
            return None
        return a1
