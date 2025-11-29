class C1(object):

    def convertBST(self, a1):
        """
        """

        def convertBSTHelper(a1, a2):
            if not a1:
                return a2
            if a1.right:
                a2 = convertBSTHelper(a1.right, a2)
            a2 += a1.val
            a1.val = a2
            if a1.left:
                a2 = convertBSTHelper(a1.left, a2)
            return a2
        convertBSTHelper(a1, 0)
        return a1
