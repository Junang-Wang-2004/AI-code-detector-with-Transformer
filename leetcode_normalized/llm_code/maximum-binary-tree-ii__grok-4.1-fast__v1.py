class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def insertIntoMaxTree(self, a1, a2):
        if a1 is None:
            return C1(a2)
        if a1.val < a2:
            v1 = C1(a2)
            v1.left = a1
            return v1
        if a1.right is None or a1.right.val <= a2:
            v1 = C1(a2)
            v1.left = a1.right
            a1.right = v1
            return a1
        a1.right = self.insertIntoMaxTree(a1.right, a2)
        return a1
