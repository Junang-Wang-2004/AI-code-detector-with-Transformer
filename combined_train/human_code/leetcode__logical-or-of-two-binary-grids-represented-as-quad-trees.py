class C1(object):

    def __init__(self, a1, a2, a3, a4, a5, a6):
        self.val = a1
        self.isLeaf = a2
        self.topLeft = a3
        self.topRight = a4
        self.bottomLeft = a5
        self.bottomRight = a6

class C2(object):

    def intersect(self, a1, a2):
        """
        """
        if a1.isLeaf:
            return a1 if a1.val else a2
        elif a2.isLeaf:
            return a2 if a2.val else a1
        v1 = self.intersect(a1.topLeft, a2.topLeft)
        v2 = self.intersect(a1.topRight, a2.topRight)
        v3 = self.intersect(a1.bottomLeft, a2.bottomLeft)
        v4 = self.intersect(a1.bottomRight, a2.bottomRight)
        if v1.isLeaf and v2.isLeaf and v3.isLeaf and v4.isLeaf and (v1.val == v2.val == v3.val == v4.val):
            return C1(v1.val, True, None, None, None, None)
        return C1(True, False, v1, v2, v3, v4)
