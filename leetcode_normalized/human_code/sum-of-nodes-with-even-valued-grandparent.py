class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def sumEvenGrandparent(self, a1):
        """
        """

        def sumEvenGrandparentHelper(a1, a2, a3):
            return sumEvenGrandparentHelper(a1.left, a1.val, a2) + sumEvenGrandparentHelper(a1.right, a1.val, a2) + (a1.val if a3 is not None and a3 % 2 == 0 else 0) if a1 else 0
        return sumEvenGrandparentHelper(a1, None, None)
