class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def sumRootToLeaf(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def sumRootToLeafHelper(a1, a2):
            if not a1:
                return 0
            a2 = (a2 * 2 + a1.val) % v1
            if not a1.left and (not a1.right):
                return a2
            return (sumRootToLeafHelper(a1.left, a2) + sumRootToLeafHelper(a1.right, a2)) % v1
        return sumRootToLeafHelper(a1, 0)
