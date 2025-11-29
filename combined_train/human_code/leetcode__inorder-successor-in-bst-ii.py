class C1(object):

    def __init__(self, a1, a2, a3, a4):
        self.val = a1
        self.left = a2
        self.right = a3
        self.parent = a4

class C2(object):

    def inorderSuccessor(self, a1):
        """
        """
        if not a1:
            return None
        if a1.right:
            a1 = a1.right
            while a1.left:
                a1 = a1.left
            return a1
        while a1.parent and a1.parent.right is a1:
            a1 = a1.parent
        return a1.parent
