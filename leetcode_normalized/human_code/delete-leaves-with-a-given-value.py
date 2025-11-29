class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def removeLeafNodes(self, a1, a2):
        """
        """
        if not a1:
            return None
        a1.left = self.removeLeafNodes(a1.left, a2)
        a1.right = self.removeLeafNodes(a1.right, a2)
        return None if a1.left == a1.right and a1.val == a2 else a1
