class C1(object):

    def isUnivalTree(self, a1):
        """
        """
        return (not a1.left or (a1.left.val == a1.val and self.isUnivalTree(a1.left))) and (not a1.right or (a1.right.val == a1.val and self.isUnivalTree(a1.right)))
