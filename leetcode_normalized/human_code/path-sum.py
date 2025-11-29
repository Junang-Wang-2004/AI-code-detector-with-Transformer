class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def hasPathSum(self, a1, a2):
        if a1 is None:
            return False
        if a1.left is None and a1.right is None and (a1.val == a2):
            return True
        return self.hasPathSum(a1.left, a2 - a1.val) or self.hasPathSum(a1.right, a2 - a1.val)
