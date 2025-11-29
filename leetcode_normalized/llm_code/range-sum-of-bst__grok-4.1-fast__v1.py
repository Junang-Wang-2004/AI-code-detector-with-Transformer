class C1(object):

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def rangeSumBST(self, a1, a2, a3):

        def helper(a1):
            if not a1:
                return 0
            v1 = 0
            if a2 <= a1.val <= a3:
                v1 += a1.val
            if a2 < a1.val:
                v1 += helper(a1.left)
            if a1.val < a3:
                v1 += helper(a1.right)
            return v1
        return helper(a1)
