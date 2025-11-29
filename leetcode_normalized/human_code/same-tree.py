class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def isSameTree(self, a1, a2):
        if a1 is None and a2 is None:
            return True
        if a1 is not None and a2 is not None:
            return a1.val == a2.val and self.isSameTree(a1.left, a2.left) and self.isSameTree(a1.right, a2.right)
        return False
