class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def increasingBST(self, a1):
        """
        """

        def increasingBSTHelper(a1, a2):
            if not a1:
                return a2
            v1 = increasingBSTHelper(a1.left, a1)
            a1.left = None
            a1.right = increasingBSTHelper(a1.right, a2)
            return v1
        return increasingBSTHelper(a1, None)
