class C1(object):

    def __init__(self, a1, a2):
        self.val = a1
        self.children = a2

class C2(object):

    def maxDepth(self, a1):
        """
        """
        if not a1:
            return 0
        v1 = 0
        for v2 in a1.children:
            v1 = max(v1, self.maxDepth(v2))
        return 1 + v1
