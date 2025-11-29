class C1(object):

    def printTree(self, a1):
        """
        """

        def getWidth(a1):
            if not a1:
                return 0
            return 2 * max(getWidth(a1.left), getWidth(a1.right)) + 1

        def getHeight(a1):
            if not a1:
                return 0
            return max(getHeight(a1.left), getHeight(a1.right)) + 1

        def preorderTraversal(a1, a2, a3, a4, a5):
            if not a1:
                return
            v1 = a3 + (a4 - a3) / 2
            a5[a2][v1] = str(a1.val)
            preorderTraversal(a1.left, a2 + 1, a3, v1 - 1, a5)
            preorderTraversal(a1.right, a2 + 1, v1 + 1, a4, a5)
        v1, v2 = (getHeight(a1), getWidth(a1))
        v3 = [[''] * v2 for v4 in range(v1)]
        preorderTraversal(a1, 0, 0, v2 - 1, v3)
        return v3
