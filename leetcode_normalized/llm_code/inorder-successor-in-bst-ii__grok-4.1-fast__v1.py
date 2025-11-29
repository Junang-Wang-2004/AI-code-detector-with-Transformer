class C1:

    def __init__(self, a1, a2, a3, a4):
        self.val, self.left, self.right, self.parent = (a1, a2, a3, a4)

class C2:

    def inorderSuccessor(self, a1):
        if a1 is None:
            return None
        if a1.right:
            v1 = a1.right
            while v1.left:
                v1 = v1.left
            return v1
        v2 = a1.parent
        while v2 and v2.right == a1:
            a1 = v2
            v2 = v2.parent
        return v2
