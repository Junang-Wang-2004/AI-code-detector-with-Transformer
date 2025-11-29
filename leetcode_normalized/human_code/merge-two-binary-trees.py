class C1(object):

    def mergeTrees(self, a1, a2):
        """
        """
        if a1 is None:
            return a2
        if a2 is None:
            return a1
        a1.val += a2.val
        a1.left = self.mergeTrees(a1.left, a2.left)
        a1.right = self.mergeTrees(a1.right, a2.right)
        return a1
