class C1(object):

    def __init__(self, a1, a2, a3):
        self.val = a1
        self.left = a2
        self.right = a3

class C2(object):

    def treeToDoublyList(self, a1):
        """
        """
        if not a1:
            return None
        v1, v2, v3, v4 = (a1, a1, a1, a1)
        if a1.left:
            v1 = self.treeToDoublyList(a1.left)
            v2 = v1.left
        if a1.right:
            v3 = self.treeToDoublyList(a1.right)
            v4 = v3.left
        v2.right, v3.left = (a1, a1)
        a1.left, a1.right = (v2, v3)
        v1.left, v4.right = (v4, v1)
        return v1
