class C1(object):

    def trimBST(self, a1, a2, a3):
        """
        """
        if not a1:
            return None
        if a1.val < a2:
            return self.trimBST(a1.right, a2, a3)
        if a1.val > a3:
            return self.trimBST(a1.left, a2, a3)
        a1.left, a1.right = (self.trimBST(a1.left, a2, a3), self.trimBST(a1.right, a2, a3))
        return a1
