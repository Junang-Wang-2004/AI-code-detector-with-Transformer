class C1(object):

    def boundaryOfBinaryTree(self, a1):
        """
        """

        def leftBoundary(a1, a2):
            if not a1 or (not a1.left and (not a1.right)):
                return
            a2.append(a1.val)
            if not a1.left:
                leftBoundary(a1.right, a2)
            else:
                leftBoundary(a1.left, a2)

        def rightBoundary(a1, a2):
            if not a1 or (not a1.left and (not a1.right)):
                return
            if not a1.right:
                rightBoundary(a1.left, a2)
            else:
                rightBoundary(a1.right, a2)
            a2.append(a1.val)

        def leaves(a1, a2):
            if not a1:
                return
            if not a1.left and (not a1.right):
                a2.append(a1.val)
                return
            leaves(a1.left, a2)
            leaves(a1.right, a2)
        if not a1:
            return []
        v1 = [a1.val]
        leftBoundary(a1.left, v1)
        leaves(a1.left, v1)
        leaves(a1.right, v1)
        rightBoundary(a1.right, v1)
        return v1
