class C1(object):

    def findBottomLeftValue(self, a1):
        """
        """

        def findBottomLeftValueHelper(a1, a2, a3, a4):
            if not a1:
                return (a3, a4)
            if not a1.left and (not a1.right) and (a2 + 1 > a3):
                return (a2 + 1, a1.val)
            a3, a4 = findBottomLeftValueHelper(a1.left, a2 + 1, a3, a4)
            a3, a4 = findBottomLeftValueHelper(a1.right, a2 + 1, a3, a4)
            return (a3, a4)
        v1, v2 = (0, 0)
        return findBottomLeftValueHelper(a1, 0, v2, v1)[1]
