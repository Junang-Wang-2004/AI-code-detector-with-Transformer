class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def maxDepth(self, a1):
        if a1 is None:
            return 0
        else:
            return max(self.maxDepth(a1.left), self.maxDepth(a1.right)) + 1
