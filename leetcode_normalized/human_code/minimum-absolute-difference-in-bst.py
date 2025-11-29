class C1(object):

    def getMinimumDifference(self, a1):
        """
        """

        def inorderTraversal(a1, a2, a3):
            if not a1:
                return (a3, a2)
            a3, a2 = inorderTraversal(a1.left, a2, a3)
            if a2:
                a3 = min(a3, a1.val - a2.val)
            return inorderTraversal(a1.right, a1, a3)
        return inorderTraversal(a1, None, float('inf'))[0]
