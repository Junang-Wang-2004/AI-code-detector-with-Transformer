class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def sufficientSubset(self, a1, a2):
        """
        """
        if not a1:
            return None
        if not a1.left and (not a1.right):
            return None if a1.val < a2 else a1
        a1.left = self.sufficientSubset(a1.left, a2 - a1.val)
        a1.right = self.sufficientSubset(a1.right, a2 - a1.val)
        if not a1.left and (not a1.right):
            return None
        return a1
