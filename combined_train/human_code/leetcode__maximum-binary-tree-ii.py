class C1(object):

    def __init__(self, a1):
        self.val = a1
        self.left = None
        self.right = None

class C2(object):

    def insertIntoMaxTree(self, a1, a2):
        """
        """
        if not a1:
            return C1(a2)
        if a2 > a1.val:
            v1 = C1(a2)
            v1.left = a1
            return v1
        v2 = a1
        while v2.right and v2.right.val > a2:
            v2 = v2.right
        v1 = C1(a2)
        v2.right, v1.left = (v1, v2.right)
        return a1
