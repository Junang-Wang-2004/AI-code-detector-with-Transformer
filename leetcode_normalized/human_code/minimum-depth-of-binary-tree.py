class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def minDepth(self, a1):
        if a1 is None:
            return 0
        if a1.left and a1.right:
            return min(self.minDepth(a1.left), self.minDepth(a1.right)) + 1
        else:
            return max(self.minDepth(a1.left), self.minDepth(a1.right)) + 1
