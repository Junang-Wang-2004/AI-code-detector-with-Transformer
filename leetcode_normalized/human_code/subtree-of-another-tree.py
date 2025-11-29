class C1(object):

    def isSubtree(self, a1, a2):
        """
        """

        def isSame(a1, a2):
            if not a1 and (not a2):
                return True
            if not a1 or not a2:
                return False
            return a1.val == a2.val and isSame(a1.left, a2.left) and isSame(a1.right, a2.right)

        def preOrderTraverse(a1, a2):
            return a1 != None and (isSame(a1, a2) or preOrderTraverse(a1.left, a2) or preOrderTraverse(a1.right, a2))
        return preOrderTraverse(a1, a2)
