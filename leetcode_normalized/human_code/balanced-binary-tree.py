class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isBalanced(self, a1):

        def getHeight(a1):
            if a1 is None:
                return 0
            v1, v2 = (getHeight(a1.left), getHeight(a1.right))
            if v1 < 0 or v2 < 0 or abs(v1 - v2) > 1:
                return -1
            return max(v1, v2) + 1
        return getHeight(a1) >= 0
