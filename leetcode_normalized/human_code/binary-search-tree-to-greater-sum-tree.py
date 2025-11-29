class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def bstToGst(self, a1):
        """
        """

        def bstToGstHelper(a1, a2):
            if not a1:
                return a1
            bstToGstHelper(a1.right, a2)
            a1.val += a2[0]
            a2[0] = a1.val
            bstToGstHelper(a1.left, a2)
            return a1
        v1 = [0]
        return bstToGstHelper(a1, v1)
