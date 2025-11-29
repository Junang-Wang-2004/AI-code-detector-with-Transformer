class C1:

    def __init__(self, a1=0, a2=None, a3=None):
        self.val = a1
        self.left = a2
        self.right = a3

class C2:

    def removeLeafNodes(self, a1, a2):
        if a1 is None:
            return None
        a1.left = self.removeLeafNodes(a1.left, a2)
        a1.right = self.removeLeafNodes(a1.right, a2)
        if a1.val == a2 and a1.left is None and (a1.right is None):
            return None
        return a1
